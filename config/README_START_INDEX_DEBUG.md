# Start Mission Index Debug Configuration

デバッグ用に特定のミッションから開始するための設定ファイルです。

## 概要 / Overview

この機能を使用すると、特定のミッション番号から開始できます。例えば：
- 1番目のミッションから開始（`start_mission_index = 0`）
- 2番目のミッションから開始（`start_mission_index = 1`）
- 6番目のミッションから開始（`start_mission_index = 5`）

これにより、特定のミッションのデバッグやテストが容易になります。

## 使い方 / Usage

### 通常起動（ランダムなミッション順序）
```bash
python src/main.py --config-filename config/button_challenge.toml
```

または

```bash
button_challenge.bat
```

### デバッグ起動（特定のミッションから開始）
```bash
python src/main.py --config-filename config/button_challenge_debug_start_index.toml
```

## 設定の変更方法 / How to Change Configuration

### config/button_challenge.toml を直接編集

デフォルトの設定ファイルを編集して、特定のミッションから開始したい場合：

```toml
use_random_mission = false     # ランダム選択を無効化
start_mission_index = 5        # 6番目のミッションから開始（0-based index）
```

### 独自の設定ファイルを作成

`button_challenge_debug_start_index.toml` をコピーして、独自の設定ファイルを作成することもできます：

```bash
cp config/button_challenge_debug_start_index.toml config/my_start_index.toml
```

そして `my_start_index.toml` の `start_mission_index` を編集してください。

## 設定パラメータ / Configuration Parameters

### use_random_mission

- `true` (デフォルト): ランダムにミッションを選択
- `false`: 決定的にミッションを選択（デバッグ用）

**重要**: `start_mission_index` を使用する場合は、`use_random_mission = false` に設定する必要があります。

### start_mission_index

- 開始するミッションのインデックス（0-based）
- `0`: 1番目のミッション
- `1`: 2番目のミッション
- `5`: 6番目のミッション
- など

**注意**: `use_random_mission = false` のときのみ有効です。

**重要な動作**: この設定は**最初のミッション**のみに影響します。最初のミッション完了後は、決定的モードの通常の順序（ソート順で0, 1, 2...）に従います。

**範囲外の値**: インデックスが範囲外の場合、自動的にラップアラウンド（modulo）されます。
- 例: ミッションが10個で `start_mission_index = 15` の場合、`15 % 10 = 5` となり、6番目のミッションから開始します。

**無効な値**: 負の数や整数以外の値が設定された場合、警告が表示され、デフォルト値 `0` が使用されます。

## ミッションの順序 / Mission Order

`use_random_mission = false` の場合、ミッションはアルファベット順（ソート順）で並べられます。

例えば、以下のミッションがある場合：
```
- "上"
- "右上"
- "右"
- "下"
```

ソート順は：
```
0: "下"
1: "右"
2: "右上"
3: "上"
```

`start_mission_index = 2` に設定すると、「右上」から開始します。

## 使用例 / Examples

### 例1: 最初のミッションから開始（決定的な順序）

```toml
use_random_mission = false
start_mission_index = 0
```

### 例2: 5番目のミッションから開始

```toml
use_random_mission = false
start_mission_index = 4  # 0-based, so 4 = 5th mission
```

### 例3: Phase 2（技練習）の特定のミッションから開始

```toml
challenge_phase = "2_moves"
use_random_mission = false
start_mission_index = 3
```

## 他のデバッグ機能との組み合わせ / Combining with Other Debug Features

この機能は他のデバッグ機能と組み合わせることができます：

### 決定的なミッション順序 + 特定のミッションから開始

```toml
use_random_mission = false     # 決定的な順序
start_mission_index = 5        # 6番目から開始
```

### Phase 2 + 特定のミッションから開始

```toml
challenge_phase = "2_moves"    # 技練習フェーズ
use_random_mission = false
start_mission_index = 2        # 3番目から開始
```

## トラブルシューティング / Troubleshooting

### start_mission_index が無視される

確認すべきこと：
1. `use_random_mission = false` に設定されているか確認してください
2. 設定ファイルのパスが正しいか確認してください
3. TOML ファイルの構文が正しいか確認してください

### 期待したミッションから開始しない

ミッションの順序はアルファベット順（ソート順）です。どのミッションがどのインデックスに対応するか確認するには、`use_random_mission = false` でアプリケーションを起動し、最初に表示されるミッションを確認してください。

## 技術的な詳細 / Technical Details

`start_mission_index` は、`initialize_mission_sets()` 関数で使用され、初期ミッションの選択時にのみ適用されます。その後のミッション選択は、`get_new_mission_index()` 関数によって行われ、`use_random_mission` の設定に従います。

決定的モード（`use_random_mission = false`）では：
```python
# ミッションをソート
sorted_missions = sorted(list(missions_set))

# インデックスを使用してミッションを選択（ラップアラウンド）
index = start_mission_index % len(sorted_missions)
mission = sorted_missions[index]
```

## 参照 / References

- Issue: [#31](https://github.com/cat2151/fighting-game-button-challenge/issues/31)
- 設定ファイル: `config/button_challenge_debug_start_index.toml`
- 関連機能: `config/README_DEBUG_DETERMINISTIC.md`
- 関連機能: `config/README_PHASE2_DEBUG.md`
