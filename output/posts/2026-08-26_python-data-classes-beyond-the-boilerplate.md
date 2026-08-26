---
title: Python Data Classes Beyond the Boilerplate
source: KDnuggets
url: https://www.kdnuggets.com/python-dataclasses-beyond-the-boilerplate
model: claude-code/sonnet
generated_at: '2026-08-26T06:29:50.845706'
score: 69
---

📌 Python Dataclass 不只是少寫幾行 __init__

TL;DR：dataclass 除了省去樣板程式碼，還能透過 field() 與 __post_init__() 做欄位驗證與衍生計算，讓資料模型更貼近真實業務邏輯。

多數開發者對 Python dataclass 的認知，停留在「幫我省下 __init__ 和 __repr__ 這些樣板方法」。但如果只把它當成少打幾行字的工具，其實低估了它的能耐。

🤔 **從 30 行樣板程式碼開始**

先看一個沒有使用 dataclass 的貨運追蹤範例：

```python
class Shipment:
    def __init__(self, tracking_id, origin, destination, weight_kg, priority):
        self.tracking_id = tracking_id
        self.origin = origin
        self.destination = destination
        self.weight_kg = weight_kg
        self.priority = priority

    def __repr__(self):
        return (
            f"Shipment(tracking_id={self.tracking_id!r}, origin={self.origin!r}, "
            f"destination={self.destination!r}, weight_kg={self.weight_kg!r}, "
            f"priority={self.priority!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, Shipment):
            return NotImplemented
        return (
            self.tracking_id == other.tracking_id
            and self.origin == other.origin
            and self.destination == other.destination
            and self.weight_kg == other.weight_kg
            and self.priority == other.priority
        )
```

這段程式碼超過 30 行，卻沒有任何業務邏輯，每個方法的存在只是為了支援物件建構、比較與呈現。換成 @dataclass 裝飾器後：

```python
from dataclasses import dataclass

@dataclass
class Shipment:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str
```

@dataclass 裝飾器會讀取每個帶有型別註記（type annotation）的屬性，在類別定義時自動生成 __init__、__repr__、__eq__ 等方法。這些型別註記本身只是型別提示，Python 並不會在執行期強制檢查，但裝飾器會用它們來判斷哪些屬性屬於這個類別、以及順序為何。結果是同樣的行為，只用了短短幾行程式碼完成。而真正有價值的地方，在於 dataclass 提供的能力遠不止於減少樣板程式碼。

🧩 **用 field() 精細控制每個欄位**

field() 函式是跳脫簡單註記語法的逃生門，讓你能為每個欄位單獨設定，包括預設值、是否納入比較、是否隱藏於物件呈現等。

一個常見的 Python 陷阱是可變預設值：list 或 dict 絕不能直接當作預設值使用，因為每個實例都會共享同一個物件。dataclass 透過強制要求可變預設值必須經由 default_factory 建立來避免這個問題：

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Shipment:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str = "standard"
    route_stops: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
```

default_factory 參數接受任何零參數的可呼叫物件，每個新建立的 Shipment 實例都會拿到自己獨立的 list，消除了物件之間共享可變狀態的風險。

有些欄位純粹是操作用途，不該影響相等性判斷，也不該讓除錯輸出變得雜亂，這時可以用 repr=False 與 compare=False 來控制：

```python
@dataclass
class Shipment:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str = "standard"
    route_stops: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    _internal_notes: str = field(default="", repr=False, compare=False)
```

如此一來，兩筆物流資料完全相同的貨運即使內部備註不同，比較結果仍為相等；_internal_notes 也不會出現在自動生成的 __repr__ 中，讓 log 輸出聚焦在真正重要的資訊上。這種細緻的控制能力，正是 dataclass 適合用於真實世界的領域模型，而不只是簡單資料容器的原因之一。

🧩 **用 __post_init__() 做驗證與衍生欄位**

自動生成的 __init__() 方法會初始化所有欄位，但真實世界的類別往往需要驗證，或是需要根據其他欄位計算出的值。這正是 __post_init__() 的用途——它會在 __init__() 完成所有欄位賦值後立即被呼叫，是驗證與計算衍生屬性的理想位置。

假設每筆貨運的重量必須為正數，且優先等級必須屬於預先定義的集合：

```python
from dataclasses import dataclass, field

VALID_PRIORITIES = {"economy", "standard", "express", "critical"}

@dataclass
class Shipment:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str = "standard"
    route_stops: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.weight_kg <= 0:
            raise ValueError(
                f"weight_kg must be positive, got {self.weight_kg}"
            )
        if self.priority not in VALID_PRIORITIES:
            raise ValueError(
                f"priority must be one of {VALID_PRIORITIES}, got {self.priority!r}"
            )
```

一旦驗證失敗，物件建構會立即中止，無效的實例永遠不會被回傳給呼叫者，錯誤在物件建構期就會被拋出，而不是在應用程式執行到後面才浮現。

除了驗證，__post_init__() 也適合用來計算依賴其他欄位的屬性，關鍵在於用 field(init=False) 宣告這些屬性，讓自動生成的建構子不會把它們當成必要輸入：

```python
from dataclasses import dataclass, field

FREIGHT_RATE_PER_KG = {
    "economy": 1.20,
    "standard": 1.85,
    "express": 3.40,
    "critical": 6.00
}

@dataclass
class Shipment:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str = "standard"
    route_stops: list[str] = field(default_factory=list)
    freight_cost: float = field(init=False)

    def __post_init__(self):
        if self.weight_kg <= 0:
            raise ValueError(f"weight_kg must be positive, got {self.weight_kg}")
        if self.priority not in FREIGHT_RATE_PER_KG:
            raise ValueError(f"Invalid priority: {self.priority!r}")
        self.freight_cost = (
            self.weight_kg * FREIGHT_RATE_PER_KG[self.priority]
        )
```

freight_cost 因為標記了 init=False，不會出現在自動生成的建構子參數中，而是在 weight_kg 與 priority 都完成初始化後，於 __post_init__() 內計算出來。

💡 **值得留意的延伸方向**

原文也提到 dataclass 還能透過 frozen=True 建立不可變物件，並用 slots=True 做記憶體最佳化，這兩項技巧分別對應「防止意外修改欄位」與「降低每個實例的記憶體開銷」，值得在需要不可變資料模型或大量實例化場景時進一步查閱官方文件與原文範例。

🎯 **實務啟示**

如果你的專案裡有大量「只是裝資料」的類別，先檢查它們是否適合改寫成 dataclass；接著問自己兩個問題：這個類別有沒有需要驗證的不變條件（invariant）？有沒有欄位是根據其他欄位算出來的？如果有，__post_init__() 搭配 field(init=False) 會比在呼叫端手動驗證更可靠，因為無效物件從一開始就不會存在。

🔗 **來源**
- 標題：Python Data Classes Beyond the Boilerplate
- 作者／機構：Bala Priya C，KDnuggets
- 連結：https://www.kdnuggets.com/python-dataclasses-beyond-the-boilerplate

#Python #Dataclasses #SoftwareEngineering #CleanCode #PythonTips #DataModeling #Validation #ProgrammingBestPractices #BackendDevelopment #PythonTutorial
