# デバッグ用設定: Start Index

## 概要
特定のミッションから開始するデバッグ用設定ファイルです。

## 設定内容
- `challenge_phase = "1_buttons"` - Phase 1 (ボタンモード) でスタート
- `use_random_mission = true` - ランダムにミッションを選択
- `start_mission_index = 0` - 最初のミッション（ソート順）から開始
- タイトルに "DEBUG StartIndex" と表示

## 使い方
```bash
python src/main.py --config-filename config/button_challenge_debug_start_index.toml
```

`start_mission_index` の値を変更することで、任意のミッションから開始できます：
- `start_mission_index = 0` - 最初のミッション
- `start_mission_index = 1` - 2番目のミッション
- `start_mission_index = 5` - 6番目のミッション

## 用途
- 特定のミッションから開始したい場合
- ミッションリストの後半をテストしたい場合
- 決定論的モード（`use_random_mission = false`）と組み合わせて特定のミッションのみテスト
