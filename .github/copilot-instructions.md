# fighting-game-button-challenge 用 Copilot 指針

## 主要アーキテクチャ（全体像）
- エントリポイントは `main()`（[src/main.py](src/main.py)）。設定読込 → Tkinter UI 初期化 → pygame ジョイスティック初期化 → 60fps ループ。
- 設定は TOML 駆動。`get_args()` → `update_args_by_toml()` で複数 TOML を `args` に合成（[src/utils.py](src/utils.py), [src/configs.py](src/configs.py)）。中心は [config/button_challenge.toml](config/button_challenge.toml)。
- ミッション処理は [src/missions.py](src/missions.py)。
  - Phase 1（`PHASE_1_BUTTONS`）は `left_right` + `left_right_temp` により左右派生を自動生成（[config/mission.toml](config/mission.toml)）。
  - Phase 2（`PHASE_2_MOVES`）は向きに応じてミッションを再生成し、1周ごとに左右を切替。
  - 成功時はスコア/フレーム統計更新、失敗時は赤フラッシュ、「全ボタン離し待ち」を次ミッションのゲートにする。
- 入力パイプライン: pygame → `get_buttons_as_bitstring()` / `get_hat_input_as_fighting_game_notation()` → `create_button_states()` で「レバー + ボタン」文字列に統合（[src/joystick.py](src/joystick.py)）。
- UI パイプライン: `update_display_with_mission()` が `args.display_format` で文字列を構築し、[config/alias.toml](config/alias.toml) のエイリアス適用。Phase 2 では `get_move_name_for_input()` で技名表示（[config/moves_sf6lily.toml](config/moves_sf6lily.toml)）。
- Windows 専用の“背面化”挙動: [src/check_playing_game.py](src/check_playing_game.py) がアクティブプロセスを判定（[src/get_window_info.py](src/get_window_info.py)）し、ゲーム起動中はウィンドウを背面へ。Z-order 操作は [src/gui_utils.py](src/gui_utils.py)。

## 開発ワークフロー
- 依存関係の導入: `pip install -r requirements.txt`（Windows 依存: `pywin32`, `psutil`, `pygame`）。
- 起動: [button_challenge.bat](button_challenge.bat)。設定 TOML を読み込み、終了は `CTRL+C`。
- テスト: `pytest`。`tests` は `sys.path` に `src` を注入して実行（例: [tests/test_challenge_phases.py](tests/test_challenge_phases.py)）。リポジトリ直下で実行すること。

## このプロジェクト固有の慣習・パターン
- ミッション/技入力は文字列ベースで、`plus` 区切りトークンをソートして正規化（`format_mission_string()` in [src/missions.py](src/missions.py)）。新規入力を追加する際は [config/button_names.toml](config/button_names.toml) の `plus` に合わせる。
- 左右入替は `left_right_temp` による一時トークン置換を前提とし、ミッション文字列に含まれない安全な値が必須。
- 「ノーカウント」判定は [config/lever_names.toml](config/lever_names.toml) の `no_count_names` を `is_no_count_case()` が参照。
- UI テキストは `args.display_format` の `label1`〜`label4` に完全依存。ラベル数を増やす場合は `gui_label_count` を [src/gui.py](src/gui.py) で調整。
- 技名表示は `moves_toml` が設定されているときのみ有効（[config/button_challenge.toml](config/button_challenge.toml)）。`None` 相当で無効化。

## 外部依存・統合ポイント
- 入力/タイミング: `pygame`、UI: Tkinter。
- アクティブウィンドウ判定: `pywin32` + `psutil`。対象プロセスは [config/button_challenge.toml](config/button_challenge.toml) の `backmost_mode.process_names` を更新。
