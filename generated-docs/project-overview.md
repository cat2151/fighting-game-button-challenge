Last updated: 2026-03-17

# Project Overview

## プロジェクト概要
- Windows用の格闘ゲームボタン練習アプリです。
- ランダムに表示されるお題に合ったボタンを押して、スコアと反応速度を競います。
- 常駐型でゲームの邪魔にならず、設定ファイルを編集することで様々なゲームに対応可能です。

## 技術スタック
- フロントエンド: PythonのGUIライブラリ（具体的なライブラリ名はプロジェクト情報には明記されていませんが、GUIを構築するために使用されています）、Windows API（最前面/最背面化などのウィンドウ操作、特定のゲームの実行状態チェックに使用）。
- 音楽・オーディオ: プロジェクト情報に明記された情報はありません。豪華なサウンドはスコープ外とされています。
- 開発ツール: Pylint（Pythonコードの静的解析と品質維持）、EditorConfig（複数のエディタやIDE間でのコードスタイル統一）、Visual Studio Code（`.vscode/settings.json` により開発環境の標準化）、Git（バージョン管理）、GitHub（コードホスティング）。
- テスト: Pythonのテストフレームワーク（`tests/` ディレクトリに複数のテストファイルがあることから、ユニットテストや結合テストが書かれていると推測されます。例: `unittest` や `pytest`）。
- ビルドツール: Pythonのパッケージ管理（`pip` による依存ライブラリのインストール）、TOMLパーサー（`config/` ディレクトリにある`.toml`形式の設定ファイルを読み込むために使用）。
- 言語機能: Python（アプリケーションの主要なロジックはPythonで記述されています）。
- 自動化・CI/CD: GitHub Actions（`README.md` の自動英訳プロセスに利用されており、継続的インテグレーション/デリバリーの一環として利用）。
- 開発標準: Pylint（コード品質基準の適用）、EditorConfig（コードフォーマットの統一）。

## ファイル階層ツリー
```
.editorconfig
.gitignore
.pylintrc
.vscode/
  settings.json
DARK_MODE.md
DARK_MODE_INTEGRATION.md
IMPLEMENTATION_SUMMARY.md
LICENSE
README.ja.md
README.md
THEME_COMPARISON.md
THEME_EXAMPLES.md
_config.yml
button_challenge.bat
config/
  alias.toml
  button_challenge.toml
  button_names.toml
  lever_names.toml
  mission.toml
  moves.toml
  moves_sf6lily.toml
docs/
  hot_reload.md
generated-docs/
googled947dc864c270e07.html
issue-notes/
  10.md
  11.md
  12.md
  13.md
  14.md
  15.md
  16.md
  18.md
  2.md
  20.md
  21.md
  22.md
  24.md
  26.md
  27.md
  29.md
  30.md
  31.md
  32.md
  39.md
  41.md
  5.md
  8.md
requirements.txt
src/
  check_playing_game.py
  configs.py
  get_window_info.py
  gui.py
  gui_utils.py
  joystick.py
  main.py
  missions.py
  theme.py
  toml_hot_reload.py
  utils.py
tests/
  demo_theme_colors.py
  manual_test_hot_reload.py
  screenshot_demo.py
  test_amplify_missions_left_right.py
  test_challenge_phases.py
  test_config_phase2_start.py
  test_debug_print_config.py
  test_debug_print_integration.py
  test_demo_random_vs_deterministic.py
  test_format_mission_string.py
  test_get_move_name_for_input.py
  test_get_pressed_buttons.py
  test_gui_phase2_mission_display.py
  test_is_no_count_case.py
  test_phase2_initial_mission_not_empty.py
  test_phase_transition_integration.py
  test_random_mission_selection.py
  test_start_mission_index.py
  test_theme.py
  test_theme_config.py
  test_toml_hot_reload.py
  visual_test_theme.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
- **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイル。ビルド生成物や一時ファイルなどが含まれます。
- **.pylintrc**: Pythonの静的コード解析ツールPylintの設定ファイル。コーディング規約や潜在的なバグの検出ルールを定義します。
- **.vscode/settings.json**: Visual Studio Codeエディタのワークスペース固有の設定ファイル。リンターやフォーマッター、デバッグ設定などが含まれます。
- **DARK_MODE.md, DARK_MODE_INTEGRATION.md, THEME_COMPARISON.md, THEME_EXAMPLES.md**: アプリケーションのダークモード機能やテーマに関する説明、統合方法、比較、および具体的なテーマ例を示すドキュメント。
- **IMPLEMENTATION_SUMMARY.md**: プロジェクトの主要な実装内容やアーキテクチャの概要を説明するドキュメント。
- **LICENSE**: プロジェクトのライセンス情報（例: MIT License）を記載したファイル。
- **README.ja.md, README.md**: プロジェクトの目的、機能、使い方、開発状況などを説明する主要なドキュメント（日本語版と英語版）。
- **_config.yml**: GitHub Pagesなどの静的サイトジェネレーターの設定ファイルである可能性があります。
- **button_challenge.bat**: Windows環境でアプリケーションを起動するためのバッチスクリプト。
- **config/alias.toml**: ボタン表示名のエイリアス（別名）を定義するためのTOML形式の設定ファイル。
- **config/button_challenge.toml**: アプリケーションの全体的な動作設定を定義する主要なTOML設定ファイル。
- **config/button_names.toml**: ゲームコントローラーの物理的なボタン名と、アプリケーション内で表示されるボタン名のマッピングを定義するTOML設定ファイル。
- **config/lever_names.toml**: レバー入力（方向キーなど）の定義を記述するTOML設定ファイル。
- **config/mission.toml**: プレイヤーに提示されるミッションの内容や条件を定義するTOML設定ファイル。
- **config/moves.toml**: ゲーム内の技（ムーブ）の定義を記述するTOML設定ファイル。
- **config/moves_sf6lily.toml**: ストリートファイター6のリリーという特定のキャラクターの技を定義したTOML設定ファイルの例。
- **docs/hot_reload.md**: アプリケーションが設定ファイルの変更を自動的に検知して再読み込みする「ホットリロード」機能に関する詳細な説明。
- **generated-docs/**: 自動生成されたドキュメントを格納するためのディレクトリ（例: 開発状況レポートなど）。
- **googled947dc864c270e07.html**: Googleのサイト所有権確認などで使用されるHTMLファイル。アプリケーションの機能とは直接関係ありません。
- **issue-notes/**: 開発中に発生した課題、検討事項、決定事項などを記録したメモを格納するディレクトリ。
- **requirements.txt**: Pythonプロジェクトの依存ライブラリとバージョンをリストアップしたファイル。`pip install -r` で一括インストールに使用します。
- **src/check_playing_game.py**: 現在Windows上で他の格闘ゲームが実行されているかどうかをチェックするロジックが含まれるPythonモジュール。
- **src/configs.py**: TOML形式の設定ファイルを読み込み、アプリケーション全体で利用できるように管理するPythonモジュール。
- **src/get_window_info.py**: Windows APIを利用して、ウィンドウの情報を取得したり、ウィンドウの前面/背面化を制御したりするPythonモジュール。
- **src/gui.py**: アプリケーションのユーザーインターフェース (GUI) の主要な構築と描画ロジックを管理するPythonモジュール。
- **src/gui_utils.py**: GUI関連の汎用的なユーティリティ関数やヘルパークラスを提供するPythonモジュール。
- **src/joystick.py**: XInputなどのAPIを利用して、ゲームコントローラー（ジョイスティック）からの入力を検出し、処理するPythonモジュール。
- **src/main.py**: アプリケーションのエントリーポイントとなるPythonスクリプト。全体の初期化、メインループの実行、各モジュールの連携を管理します。
- **src/missions.py**: ミッションの生成、現在の入力に対するミッションの成否判定、スコア計算などのロジックを管理するPythonモジュール。
- **src/theme.py**: アプリケーションのビジュアルテーマ（色、フォント、スタイルなど）に関する設定と適用を管理するPythonモジュール。
- **src/toml_hot_reload.py**: `config/` ディレクトリ内のTOML設定ファイルの変更を監視し、変更があった場合に自動的に設定を再読み込みする機能を提供するPythonモジュール。
- **src/utils.py**: プロジェクト全体で利用される汎用的なヘルパー関数やユーティリティを集めたPythonモジュール。
- **tests/**: アプリケーションの様々な機能に対するテストコードを格納するディレクトリ。各ファイルは特定の機能のテストケースを含みます。

## 関数詳細説明
提供されたプロジェクト情報には、各関数の詳細なシグネチャ（引数、戻り値）は含まれていません。そのため、各Pythonモジュールの役割に基づき、想定される主要な関数とその機能について説明します。

- **`src/main.py`**
    - `main()`: アプリケーションのエントリーポイント。初期設定の読み込み、GUIの構築、ジョイスティック入力の監視、ミッションの生成と表示、メインループの実行など、アプリケーション全体の流れを管理します。
- **`src/gui.py`**
    - `initialize_gui(root_window)`: GUIウィンドウを初期化し、各種ウィジェット（ミッション表示、スコア表示など）を配置します。
    - `update_mission_display(mission_string)`: 現在のお題ミッション文字列をGUI上に表示します。
    - `update_score_display(current_score)`: 現在のスコアをGUI上に更新表示します。
    - `set_window_visibility(is_visible)`: アプリケーションウィンドウの表示状態（最前面、最背面、非表示など）を制御します。
- **`src/joystick.py`**
    - `init_joystick()`: ジョイスティック（ゲームコントローラー）の初期化処理を行います。
    - `get_pressed_buttons()`: 現在押されているボタンの入力を検出し、その情報を返します。
- **`src/missions.py`**
    - `generate_random_mission(current_phase)`: 現在のゲームフェーズに基づき、ランダムな新しいミッションを生成し、その内容を返します。
    - `check_mission_success(current_mission, pressed_buttons)`: プレイヤーの入力（押されたボタン）が現在のお題ミッションに合致しているか判定し、成功/失敗の結果とタイム情報を返します。
    - `update_score(is_success, time_taken)`: ミッションの成否と所要時間に基づいてスコアを更新します。
- **`src/configs.py`**
    - `load_config_file(file_path)`: 指定されたTOML形式の設定ファイルを読み込み、Pythonの辞書形式で返します。
    - `get_setting(key_path)`: ドット区切りなどで指定されたキーパスに基づいて、読み込まれた設定値を取得します。
- **`src/toml_hot_reload.py`**
    - `start_watcher(config_directory, callback_function)`: 指定された設定ディレクトリ内のTOMLファイルの変更を監視し、変更が検出された場合に指定されたコールバック関数を実行します。
- **`src/check_playing_game.py`**
    - `is_game_running(game_process_names)`: 指定されたゲームのプロセスが現在Windows上で実行中であるかをチェックし、真偽値を返します。
- **`src/get_window_info.py`**
    - `set_foreground_window(window_handle)`: 指定されたウィンドウハンドルを持つウィンドウを最前面に設定します。
    - `set_background_window(window_handle)`: 指定されたウィンドウハンドルを持つウィンドウを最背面に設定します。
- **`src/theme.py`**
    - `apply_theme(gui_elements, theme_config)`: GUI要素にテーマ設定（色、フォントなど）を適用します。
- **`src/utils.py`**
    - `debug_print(message, level)`: デバッグメッセージをコンソールに出力します。
    - `format_time(milliseconds)`: ミリ秒単位の時間を整形された文字列に変換します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-17 07:09:38 JST
