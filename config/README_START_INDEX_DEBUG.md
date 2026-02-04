# デバッグ用設定: Start Index

## 概要
特定のミッションから開始するデバッグ用設定ファイルです。

## 設定内容
- `challenge_phase = "1_buttons"` - Phase 1 (ボタンモード) でスタート
- `use_random_mission = false` - 決定論的にミッションを選択（必須: start_mission_indexを使うため）
- `start_mission_index = 0` - 最初のミッション（ソート順）から開始
- タイトルに "DEBUG StartIndex" と表示

**注意**: `start_mission_index` は `use_random_mission = false` の場合のみ有効です。

## 使い方
```bash
python src/main.py --config-filename config/button_challenge_debug_start_index.toml
```

`start_mission_index` の値を変更することで、任意のミッションから開始できます（決定論的モードのみ有効）：
- `start_mission_index = 0` - 最初のミッション
- `start_mission_index = 1` - 2番目のミッション
- `start_mission_index = 5` - 6番目のミッション

**重要**: ランダムモード（`use_random_mission = true`）では `start_mission_index` は無視されます。

## 用途
- 特定のミッションから開始したい場合（決定論的モードで）
- ミッションリストの後半をテストしたい場合
- 特定のミッションのみを繰り返しテストしたい場合
