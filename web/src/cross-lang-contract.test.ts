import fs from 'node:fs';
import path from 'node:path';

import { describe, expect, test } from 'vitest';

import { normalizeUrl } from './enrich';

/**
 * 跨語言契約測試（TS 側）。
 *
 * why 這支存在：`web/src/`（Astro 靜態站）與 `src/web/`（Python Web Monitor）
 * 是「原始資料 box」的兩份平行實作。樣式層刻意不共用，但 URL 正規化與訊號標籤
 * 這兩項**契約**必須逐字一致——對不上的症狀是 box 查不到資料而**整個靜默不渲染**，
 * 沒有 log、沒有 exception。
 *
 * why 讀共用 fixture 而不是在這裡寫期望值：期望值寫兩份等於把重複搬進測試，
 * 兩邊各自漂移一樣抓不到。期望值只存在 `__fixtures__/cross-lang-contract.json`，
 * Python 側 `tests/test_cross_lang_contract.py` 讀同一個檔案。
 */

// happy-dom 環境下 import.meta.url 是 http(s) 的頁面網址而非 file://，
// 故以 cwd（= web/）為基準解析，與 enrich.ts / raw.ts 讀 data/ 的作法一致。
const FIXTURE_PATH = path.resolve(process.cwd(), 'src/__fixtures__/cross-lang-contract.json');
const RAW_TS_PATH = path.resolve(process.cwd(), 'src/raw.ts');

interface Fixture {
  normalizeUrl: {
    shared: { input: string; expected: string; note: string }[];
    divergent: { input: string; ts: string; python: string; note: string }[];
  };
  signalLabels: { entries: { key: string; label: string }[] };
}

const fixture: Fixture = JSON.parse(fs.readFileSync(FIXTURE_PATH, 'utf-8'));

describe('normalizeUrl 對照共用 fixture', () => {
  test('fixture 本身有內容（避免檔案被清空造成「零斷言全綠」）', () => {
    expect(fixture.normalizeUrl.shared.length).toBeGreaterThan(5);
    expect(fixture.normalizeUrl.divergent.length).toBeGreaterThan(0);
    expect(fixture.signalLabels.entries.length).toBeGreaterThan(0);
  });

  test.each(fixture.normalizeUrl.shared)('兩端一致：$note（$input）', ({ input, expected }) => {
    expect(normalizeUrl(input)).toBe(expected);
  });

  // 已知分歧刻意不修，所以這裡釘的是「TS 端目前的行為」。
  // 哪天有人把兩端統一（例如 Python 改成錨定的取代），這一筆會 FAIL 並把人帶回 fixture。
  test.each(fixture.normalizeUrl.divergent)(
    '已知分歧（TS 側預期值）：$input',
    ({ input, ts }) => {
      expect(normalizeUrl(input)).toBe(ts);
    },
  );

  test('undefined 視同空字串（TS 側獨有的簽名，Python 端以空字串涵蓋）', () => {
    expect(normalizeUrl(undefined)).toBe('');
  });
});

/**
 * `SIGNAL_LABELS` 是 raw.ts 的模組私有常數。純為測試而 export 會擴大模組公開介面，
 * 因此這裡改讀原始碼文字把陣列字面值解出來。
 * 代價是對排版格式敏感——解析失敗時會明確 FAIL 並指回 fixture，不會靜默略過。
 */
function parseSignalLabelsFromSource(): { key: string; label: string }[] {
  const source = fs.readFileSync(RAW_TS_PATH, 'utf-8');
  const block = source.match(/const SIGNAL_LABELS[^=]*=\s*\[([\s\S]*?)\];/);
  if (!block) {
    throw new Error(
      'raw.ts 中找不到 SIGNAL_LABELS 的陣列字面值（排版變了？）。' +
        '請確認它仍與 __fixtures__/cross-lang-contract.json 一致，並修正這裡的解析。',
    );
  }
  const out: { key: string; label: string }[] = [];
  const tuple = /\[\s*(['"])(.*?)\1\s*,\s*(['"])(.*?)\3\s*\]/g;
  for (const m of block[1].matchAll(tuple)) out.push({ key: m[2], label: m[4] });
  return out;
}

describe('SIGNAL_LABELS 對照共用 fixture', () => {
  test('key、標籤文字與順序完全相同', () => {
    // 整份比對而非逐筆：少一筆、多一筆、順序調換都要被抓到。
    expect(parseSignalLabelsFromSource()).toEqual(fixture.signalLabels.entries);
  });
});
