## Ex0

- **概要**
    
    プログラムがユーザーからメッセージを受け取る方法を探る
    
- **要件**
    
    

**Authorized:** import sys, sys.argv, len(), print()

**Example:**

```jsx
$> python3 ft_command_quest.py
=== Command Quest ===
No arguments provided!
Program name: ft_command_quest.py
Total arguments: 1
$> python3 ft_command_quest.py hello world 42
=== Command Quest ===
Program name: ft\_command\_quest.py
Arguments received: 3
Argument 1: hello
Argument 2: world
Argument 3: 42
Total arguments: 4
$> python3 ft_command_quest.py "Data Quest"
=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 1
Argument 1: Data Quest
Total arguments: 2
```

## Ex1

- **概要**
    
    Score Cruncher Moduleの作成。リーダーボードみたいなもの。
    
- **要件**
    
    **Authorized:** sys.argv, len(), sum(), max(), min(), int(), print(), try/except
    
    - コマンドライン引数からプレイヤーのスコアを見る
    - スコアを整理するために list を使用する
    - スコアを計算してなにか指標を作る
    - 数字じゃないスコアに対応する
    - 見た目を整える

**Example:**

```jsx
$> python3 ft_score_analytics.py 1500 2300 1800 2100 1950
=== Player Score Analytics ===
Scores processed: [1500, 2300, 1800, 2100, 1950]
Total players: 5
Total score: 9650
Average score: 1930.0
High score: 2300
Low score: 1500
Score range: 800
$> python3 ft_score_analytics.py
=== Player Score Analytics ===
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
```

## Ex2

- **概要**
    
    三次元座標についての理解。特定の座標にテレポートしたり、異なる２つの座標間の距離を求める。
    
- **要件**
    
    **Authorized:**  import sys, sys.argv, import math, tuple(), int(), float(), print(), split(), try/except, math.sqrt()
    
    tupleを使用して３次元座標システムを作る。
    
    - (x, y, z)を設定
    - sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2) を使用して二点間の距離を求める
    - 座標の文字列を解析して、ユーザーに役立つ情報を示す

**Example:**

```jsx
$> python3 ft_coordinate_system.py
=== Game Coordinate System ===
Position created: (10, 20, 5)
Distance between (0, 0, 0) and (10, 20, 5): 22.91
Parsing coordinates: "3,4,0"
Parsed position: (3, 4, 0)
Distance between (0, 0, 0) and (3, 4, 0): 5.0
Parsing invalid coordinates: "abc,def,ghi"
Error parsing coordinates: invalid literal for int() with base 10: 'abc'
Error details - Type: ValueError, Args: ("invalid literal for int() with base 10: 'abc'",)
Unpacking demonstration:
Player at x=3, y=4, z=0
Coordinates: X=3, Y=4, Z=0
```

## Ex3

- **概要**
    
    アチーブメントシステムを作る。
    
- **要件**
    
    **Authorized:** set(), len(), print(), union(), intersection(), difference()
    
    sets を使用して Achievement Hunter を作成する。
    
    - 特別な実績を記録する（例：First Killは一回のみ）
    - 複数のプレイヤーが共有できる実績を作る
    - 激レア実績を作る
    - 未取得の実績を確認できる
    - 共通の実績に基づいてコミュニティを構築

**Example:**

```jsx
$> python3 ft_achievement_tracker.py
=== Achievement Tracker System ===
Player alice achievements: {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
Player bob achievements: {'first_kill', 'level_10', 'boss_slayer', 'collector'}
Player charlie achievements: {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
=== Achievement Analytics ===
All unique achievements: {'boss_slayer', 'collector', 'first_kill', 'level_10', 'perfectionist', 'speed_demon', 'treasure_hunter'}
Total unique achievements: 7
Common to all players: {'level_10'}
Rare achievements (1 player): {'collector', 'perfectionist'}
Alice vs Bob common: {'first_kill', 'level_10'}
Alice unique: {'speed_demon', 'treasure_hunter'}
Bob unique: {'boss_slayer', 'collector'}
```

## Ex4

- **概要**
    
    インベントリ機能を実装し、所持品を見れるようにする
    
- **要件**
    
    **Authorized:** dict(), len(), print(), keys(), values(), items(), get(), update()
    
    dict を使用して以下の機能を持つインベントリを実装する
    
    - プレイヤーのインベントリーを操作できる
    - アイテムの詳細（量、種類、価値）が見れる
    - Total Inventory Value を計算する
    - カテゴリーによってアイテムを整理する
    - 見やすい Inventory Reportを作成する

**Example:**

```jsx
$> python3 ft_inventory_system.py
=== Player Inventory System ===
=== Alice's Inventory ===
sword (weapon, rare): 1x @ 500 gold each = 500 gold
potion (consumable, common): 5x @ 50 gold each = 250 gold
shield (armor, uncommon): 1x @ 200 gold each = 200 gold
Inventory value: 950 gold
Item count: 7 items
Categories: weapon(1), consumable(5), armor(1)
=== Transaction: Alice gives Bob 2 potions ===
Transaction successful!
=== Updated Inventories ===
Alice potions: 3
Bob potions: 2
=== Inventory Analytics ===
Most valuable player: Alice (850 gold)
Most items: Alice (5 items)
Rarest items: sword, magic_ring
```

## Ex5

- **概要**
    
    PythonのMemory-savingについて学ぶ
    
- **要件**
    
    **Authorized:** yield, next(), iter(), range(), len(), print(), for loops
    
    - データの流れを作成する
    - for - in loops を使用してイベントを一つずつ処理する
    - 面白そうなイベントをフィルター分けする
    - すべてを貯めずにstaticのtrackを保存する
    - store everything と stream everythingの違いを示す

**Example:**

```jsx
$> python3 ft_data_stream.py
=== Game Data Stream Processor ===
Processing 1000 game events...
Event 1: Player alice (level 5) killed monster
Event 2: Player bob (level 12) found treasure
Event 3: Player charlie (level 8) leveled up
...
=== Stream Analytics ===
Total events processed: 1000
High-level players (10+): 342
Treasure events: 89
Level-up events: 156
Memory usage: Constant (streaming)
Processing time: 0.045 seconds
=== Generator Demonstration ===
Fibonacci sequence (first 10): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
Prime numbers (first 5): 2, 3, 5, 7, 11
```

## Ex6

- **概要**
    
    Comprehensions (list, dict, set)を使用した統計ダッシュボードを作成する。
    
- **要件**
    - listを使用してデータのフィルタリングや変更を行う
    - dictを使用してマッピング作成とデータのグルーピングを行う
    - setを使用して特徴のある値を見つける
    - Sample gaming dataを編集する
    - どのComprehensionが実行されているのかを明示する
    
    **Authorized:** List/dict/set comprehensions, len(), print(), sum(), max(), min(), sorted()
    

**Example:**

```jsx
$> python3 ft_analytics_dashboard.py
=== Game Analytics Dashboard ===
=== List Comprehension Examples ===
High scorers (>2000): ['alice', 'charlie', 'diana']
Scores doubled: [4600, 3600, 4300, 4100]
Active players: ['alice', 'bob', 'charlie']
=== Dict Comprehension Examples ===
Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}
Score categories: {'high': 3, 'medium': 2, 'low': 1}
Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}
=== Set Comprehension Examples ===
Unique players: {'alice', 'bob', 'charlie', 'diana'}
Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}
Active regions: {'north', 'east', 'central'}
=== Combined Analysis ===
Total players: 4
Total unique achievements: 12
Average score: 2062.5
Top performer: alice (2300 points, 5 achievements)
```
