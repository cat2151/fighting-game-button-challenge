# デバッグ用設定: 決定的なミッション順序

## 概要

このREADMEは、デバッグ用の新しい設定オプション `use_random_mission` について説明します。

## 背景

通常、ボタンチャレンジはランダムにミッションを選択します。これはゲームプレイとしては良いですが、デバッグやテストでは以下の問題があります:

- ミッションの順序が予測できない
- 特定のミッションシーケンスを再現できない
- エッジケースのテストが難しい

## 設定方法

### button_challenge.toml での設定

```toml
use_random_mission = false  # ランダム選択を無効化し、決定的な選択を有効化
```

- `true` (デフォルト): ランダムにミッションを選択（通常の動作）
- `false`: 決定的にミッションを選択（デバッグ用）

### デバッグ設定ファイルの使用

決定的なミッション選択を使用する専用のデバッグ設定ファイルが用意されています:

```bash
python src/main.py --config-filename config/button_challenge_debug_deterministic.toml
```

## 動作

### use_random_mission = true (デフォルト)

- ランダムに次のミッションを選択
- 毎回異なる順序でミッションが表示される

### use_random_mission = false (デバッグモード)

- アルファベット順（ソート順）で最初のミッションを常に選択
- 同じ条件で実行すると、常に同じ順序でミッションが表示される
- テストの再現性が高い

## 使用例

### 通常のゲームプレイ
```bash
python src/main.py --config-filename config/button_challenge.toml
```

### デバッグ（決定的なミッション順序）
```bash
python src/main.py --config-filename config/button_challenge_debug_deterministic.toml
```

## 技術的な詳細

決定的モードでは、`get_new_mission_index()` 関数は:

```python
# use_random=True の場合
mission = random.choice(list(missions_set))

# use_random=False の場合
mission = sorted(list(missions_set))[0]
```

これにより、常にソート順で最初のミッションが選択されます。

## テスト

新しい機能のテストは `tests/test_random_mission_selection.py` に含まれています:

```bash
pytest tests/test_random_mission_selection.py -v
```

## 参照

- Issue: [#30](https://github.com/cat2151/fighting-game-button-challenge/issues/30)
- 設定ファイル: `config/button_challenge_debug_deterministic.toml`
