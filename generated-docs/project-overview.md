Last updated: 2026-02-06

# Project Overview

## プロジェクト概要
- 格ゲーのボタン練習に特化したWindows用アプリケーションです。
- ランダムに表示されるお題に合わせてボタンを入力し、スコアを競うことで瞬発的な反応力を鍛えます。
- 常駐型で、ゲーム起動中でも邪魔にならず、設定ファイルを編集することで様々な格闘ゲームに対応可能です。

## 技術スタック
- フロントエンド: PythonベースのGUIライブラリ（PySimpleGUIなどの利用が推測されますが、具体的な記述はありません）、XInput (ジョイスティック/ゲームコントローラーからの入力検出API)。
- 音楽・オーディオ: 特になし。
- 開発ツール: Git (バージョン管理システム)、GitHub (ソースコードホスティングおよびCI/CD連携)、Visual Studio Code (.vscodeディレクトリの設定ファイルより)、Pylint (Pythonコードの静的解析ツール、.pylintrcより)。
- テスト: Pythonのテストフレームワーク（`tests/`ディレクトリに複数のテストスクリプトが存在するため）。
- ビルドツール: pip (Pythonパッケージインストーラ)、TOML (設定ファイル形式)。
- 言語機能: Python (アプリケーションの主要なプログラミング言語)。
- 自動化・CI/CD: GitHub Actions (READMEの自動翻訳など、CI/CDワークフローに利用)。
- 開発標準: EditorConfig (.editorconfigファイルにより、異なるエディタ間でのコードスタイル統一を支援)、Pylint (Pythonコードの品質とコーディング規約のチェック)。

## ファイル階層ツリー
```
📄 .editorconfig
📄 .gitignore
📄 .pylintrc
📁 .vscode/
  📊 settings.json
📖 DARK_MODE.md
📖 DARK_MODE_INTEGRATION.md
📖 IMPLEMENTATION_SUMMARY.md
📄 LICENSE
📖 README.ja.md
📖 README.md
📖 THEME_COMPARISON.md
📖 THEME_EXAMPLES.md
📄 _config.yml
📄 button_challenge.bat
📁 config/
  📄 alias.toml
  📄 button_challenge.toml
  📄 button_names.toml
  📄 lever_names.toml
  📄 mission.toml
  📄 moves.toml
  📄 moves_sf6lily.toml
📁 docs/
  📖 hot_reload.md
📁 generated-docs/
🌐 googled947dc864c270e07.html
📁 issue-notes/
  📖 10.md
  📖 11.md
  📖 12.md
  📖 13.md
  📖 14.md
  📖 15.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 20.md
  📖 21.md
  📖 22.md
  📖 24.md
  📖 26.md
  📖 27.md
  📖 29.md
  📖 30.md
  📖 31.md
  📖 32.md
  📖 39.md
  📖 41.md
  📖 5.md
  📖 8.md
📄 requirements.txt
📁 src/
  📄 check_playing_game.py
  📄 configs.py
  📄 get_window_info.py
  📄 gui.py
  📄 gui_utils.py
  📄 joystick.py
  📄 main.py
  📄 missions.py
  📄 theme.py
  📄 toml_hot_reload.py
  📄 utils.py
📁 tests/
  📄 demo_theme_colors.py
  📄 manual_test_hot_reload.py
  📄 screenshot_demo.py
  📄 test_amplify_missions_left_right.py
  📄 test_challenge_phases.py
  📄 test_config_phase2_start.py
  📄 test_debug_print_config.py
  📄 test_debug_print_integration.py
  📄 test_demo_random_vs_deterministic.py
  📄 test_format_mission_string.py
  📄 test_get_move_name_for_input.py
  📄 test_get_pressed_buttons.py
  📄 test_gui_phase2_mission_display.py
  📄 test_is_no_count_case.py
  📄 test_phase2_initial_mission_not_empty.py
  📄 test_phase_transition_integration.py
  📄 test_random_mission_selection.py
  📄 test_start_mission_index.py
  📄 test_theme.py
  📄 test_theme_config.py
  📄 test_toml_hot_reload.py
  📄 visual_test_theme.py
```

## ファイル詳細説明
-   `.editorconfig`: 異なるエディタ間でインデントスタイルや文字コードなどのコードフォーマットを統一するための設定ファイル。
-   `.gitignore`: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
-   `.pylintrc`: Pythonコードの静的解析ツールPylintの設定ファイル。コード品質やコーディング規約のチェックルールを定義します。
-   `.vscode/settings.json`: Visual Studio Codeエディタのワークスペース固有の設定を定義するファイル。
-   `DARK_MODE.md`: ダークモードに関する説明ドキュメント。
-   `DARK_MODE_INTEGRATION.md`: ダークモードの実装統合に関する詳細ドキュメント。
-   `IMPLEMENTATION_SUMMARY.md`: プロジェクトの実装概要をまとめたドキュメント。
-   `LICENSE`: プロジェクトのソフトウェアライセンス情報。
-   `README.ja.md`: プロジェクトの日本語版概要と使用方法を説明するメインドキュメント。
-   `README.md`: プロジェクトの英語版概要と使用方法を説明するメインドキュメント。
-   `THEME_COMPARISON.md`: 異なるテーマ間の比較を示すドキュメント。
-   `THEME_EXAMPLES.md`: テーマの具体例を示すドキュメント。
-   `_config.yml`: Jekyllなどの静的サイトジェネレータでGitHub Pagesを使用する際の一般的な設定ファイル。
-   `button_challenge.bat`: Windows環境でアプリケーションを起動するためのバッチスクリプト。
-   `config/alias.toml`: ボタン名のエイリアス（別名）を定義するTOML形式の設定ファイル。
-   `config/button_challenge.toml`: アプリケーション全体の挙動に関する主要な設定を定義するTOML形式の設定ファイル。
-   `config/button_names.toml`: 各コントローラーボタンに割り当てる名前を定義するTOML形式の設定ファイル。
-   `config/lever_names.toml`: レバー（方向入力）に割り当てる名前を定義するTOML形式の設定ファイル。
-   `config/mission.toml`: アプリケーションで出題されるミッションの内容を定義するTOML形式の設定ファイル。
-   `config/moves.toml`: ゲーム内の具体的な技の定義を記述するTOML形式の設定ファイル。
-   `config/moves_sf6lily.toml`: 特定のキャラクター（ストリートファイター6のリリー）の技定義を記述するTOML形式の設定ファイル。
-   `docs/hot_reload.md`: 設定ファイルのホットリロード機能に関する詳細な説明ドキュメント。
-   `generated-docs/`: 自動生成されたドキュメントを格納するためのディレクトリ（例: 開発状況レポートなど）。
-   `googled947dc864c270e07.html`: Googleサイト認証のために使用されるHTMLファイル。
-   `issue-notes/`: 開発中の課題、検討事項、メモなどが記録されたドキュメントを格納するディレクトリ。
-   `requirements.txt`: プロジェクトが依存するPythonライブラリの一覧とバージョンを記述したファイル。`pip install`で依存関係をインストールする際に使用されます。
-   `src/check_playing_game.py`: 他の格闘ゲームが現在実行中であるかを検知するためのロジックを実装したPythonスクリプト。
-   `src/configs.py`: TOML形式の設定ファイルを読み込み、アプリケーション全体で利用可能な設定オブジェクトを提供するPythonスクリプト。
-   `src/get_window_info.py`: 現在アクティブなウィンドウのタイトルなど、ウィンドウに関する情報を取得するためのPythonスクリプト。
-   `src/gui.py`: アプリケーションのグラフィカルユーザーインターフェース (GUI) の構築、表示、およびイベント処理の主要なロジックを実装したPythonスクリプト。
-   `src/gui_utils.py`: GUI関連の共通ユーティリティ関数やヘルパークラスを提供するPythonスクリプト。
-   `src/joystick.py`: XInputライブラリを介してジョイスティックやゲームコントローラーからの入力を検出し、処理するPythonスクリプト。
-   `src/main.py`: アプリケーションのエントリポイント。初期化処理、メインループの制御、各モジュールの連携を調整します。
-   `src/missions.py`: ランダムミッションの生成、ユーザー入力との比較、ミッションの成否判定など、ミッションに関するロジックを実装したPythonスクリプト。
-   `src/theme.py`: アプリケーションのGUIテーマ（色、フォントなど）を管理し、適用するためのPythonスクリプト。
-   `src/toml_hot_reload.py`: TOML設定ファイルの変更を監視し、ファイルが変更された際にアプリケーションに通知して設定をホットリロードする機能を提供するPythonスクリプト。
-   `src/utils.py`: アプリケーション全体で汎用的に利用されるユーティリティ関数（例: 時間フォーマット、値のクランプなど）を提供するPythonスクリプト。
-   `tests/`: プロジェクトの各種機能に対するテストスクリプトを格納するディレクトリ。
    -   `demo_theme_colors.py`: テーマ色のデモンストレーションを行うテストスクリプト。
    -   `manual_test_hot_reload.py`: ホットリロード機能の手動テストシナリオ。
    -   `screenshot_demo.py`: スクリーンショットのデモを生成するスクリプト。
    -   `test_*.py`: アプリケーションの各機能（ミッション生成、設定読み込み、GUI表示など）の単体テストや結合テスト。
    -   `visual_test_theme.py`: テーマの表示が意図通りか視覚的に確認するためのテストスクリプト。

## 関数詳細説明
このプロジェクト情報では個々の関数の詳細なシグネチャ（引数や戻り値）までは提供されていませんが、各ファイルの役割に基づいて主要な機能を提供する関数群を以下に説明します。

-   `main.py`:
    -   `main()`: アプリケーションのメインエントリポイント。初期設定の読み込み、GUIの起動、ジョイスティック入力の監視、ミッションの進行管理といったアプリケーションのコアロジックをオーケストレートします。
-   `src/joystick.py`:
    -   `init_joystick()`: XInputコントローラーを初期化し、入力デバイスとの接続を確立します。
    -   `get_pressed_buttons()`: 現在押されているジョイスティック/コントローラーのボタンとレバーの情報を取得して返します。
-   `src/gui.py`:
    -   `create_window()`: アプリケーションのメインGUIウィンドウを作成し、初期表示を設定します。
    -   `update_display()`: ミッションテキスト、スコア、タイマー、デバッグ情報など、GUIの表示内容を更新します。
    -   `handle_event()`: GUIウィンドウからのイベント（ボタンクリック、ウィンドウ閉じなど）を処理します。
-   `src/missions.py`:
    -   `generate_mission()`: 定義されたミッションリストからランダムに新しいミッションを選択し、出題します。
    -   `check_mission_success()`: ユーザーの入力と現在のミッションのお題を比較し、ミッションが成功したかどうかを判定します。
    -   `get_current_mission_string()`: 現在表示されているミッションの文字列を生成して返します。
-   `src/configs.py`:
    -   `load_configs()`: `config/`ディレクトリ内のTOML設定ファイルを読み込み、アプリケーション全体でアクセス可能な設定オブジェクトを構築します。
    -   `get_setting()`: 指定されたキーに対応する設定値を取得します。
-   `src/toml_hot_reload.py`:
    -   `start_watcher()`: 指定されたTOMLファイル群の変更をバックグラウンドで監視するプロセスを開始します。
    -   `check_for_changes()`: ファイル変更が検出された場合に、設定をリロードするためのトリガーを発生させます。
-   `src/check_playing_game.py`:
    -   `is_game_running()`: 特定のプロセス名を持つゲーム（例: ストリートファイター6）が実行中であるかを判定し、ブール値を返します。
-   `src/get_window_info.py`:
    -   `get_active_window_title()`: 現在アクティブな（最前面にある）ウィンドウのタイトルバーの文字列を取得します。
-   `src/theme.py`:
    -   `apply_theme()`: 設定に基づいてGUIのカラーテーマやフォントを適用します。
    -   `get_color_scheme()`: 現在適用されているテーマの色情報を取得します。
-   `src/utils.py`, `src/gui_utils.py`:
    -   `format_time()`: 時間の数値を読みやすい文字列形式にフォーマットします。
    -   `clamp_value()`: ある値を指定された最小値と最大値の範囲内に制限します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は分析できませんでした。

---
Generated at: 2026-02-06 07:06:08 JST
