Last updated: 2026-02-04

# Project Overview

## プロジェクト概要
- 格闘ゲームのボタン操作練習に特化したWindows用アプリです。
- ランダムに表示されるお題に合わせてボタンを入力し、反射神経と正確性を鍛えます。
- 常駐型で、ゲーム起動中でも邪魔にならず、素早いウォームアップや反復練習を支援します。

## 技術スタック
- フロントエンド: PythonのGUIフレームワークを利用して、シンプルなボタン表示やスコア表示を実現しています。具体的なライブラリ名はプロジェクト情報に明記されていませんが、ユーザーインターフェースを提供します。
- 音楽・オーディオ: プロジェクト情報に音楽・オーディオ関連技術の記載はありません。
- 開発ツール:
    - VS Code: 開発環境としてVisual Studio Codeが使用されており、`.vscode/settings.json` で設定が管理されています。
- テスト: `tests/` ディレクトリが存在し、Pythonの標準的なテストフレームワーク（例: `unittest` または `pytest`）を利用して、各機能の単体テストや結合テストが実施されています。
- ビルドツール: Pythonスクリプトとして直接実行されるため、特定のビルドツールは使用されていません。依存関係は `requirements.txt` で管理されます。
- 言語機能:
    - Python: アプリケーション本体はPythonで記述されており、様々なモジュールやライブラリを活用しています。
    - TOML: 設定ファイル形式としてTOMLが採用されており、設定の柔軟なカスタマイズとホットリロードに対応しています。
- 自動化・CI/CD:
    - GitHub Actions: READMEの自動英訳に利用されていることが明記されており、継続的インテグレーションやデプロイに活用されています。
- 開発標準:
    - Pylint: Pythonコードの品質チェックツールであるPylintが使用されており、`.pylintrc` でコーディング規約が設定されています。
    - EditorConfig: `.editorconfig` ファイルにより、複数のエディタやIDE間でコーディングスタイルを統一しています。

## ファイル階層ツリー
```
📄 .editorconfig
📄 .gitignore
📄 .pylintrc
📁 .vscode/
  📊 settings.json
📖 IMPLEMENTATION_SUMMARY.md
📄 LICENSE
📖 README.ja.md
📖 README.md
📄 _config.yml
📄 button_challenge.bat
📁 config/
  📖 README_DEBUG_DETERMINISTIC.md
  📖 README_PHASE2_DEBUG.md
  📖 README_START_INDEX_DEBUG.md
  📄 alias.toml
  📄 button_challenge.toml
  📄 button_challenge_debug_deterministic.toml
  📄 button_challenge_debug_phase2.toml
  📄 button_challenge_debug_start_index.toml
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
  📄 toml_hot_reload.py
  📄 utils.py
📁 tests/
  📄 manual_test_hot_reload.py
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
  📄 test_integration_phase2_debug_config.py
  📄 test_is_no_count_case.py
  📄 test_phase_transition_integration.py
  📄 test_random_mission_selection.py
  📄 test_start_mission_index.py
  📄 test_toml_hot_reload.py
```

## ファイル詳細説明
- **`.editorconfig`**: コーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定します。
- **`.pylintrc`**: Pythonコードの静的解析ツールPylintの設定ファイルで、コード品質基準を定義します。
- **`.vscode/settings.json`**: Visual Studio Codeのワークスペース固有の設定を定義するファイルです。
- **`IMPLEMENTATION_SUMMARY.md`**: 実装に関する重要な情報や設計の概要をまとめたドキュメントです。
- **`LICENSE`**: プロジェクトのソフトウェアライセンス情報が記述されています。
- **`README.ja.md`**: プロジェクトの日本語版説明書です。概要、機能、使い方などが記載されています。
- **`README.md`**: プロジェクトの英語版説明書です。`README.ja.md` から自動生成されます。
- **`_config.yml`**: GitHub Pagesの設定ファイルなど、静的サイトジェネレータに関連する可能性があります。
- **`button_challenge.bat`**: Windows環境でアプリケーションを起動するためのバッチスクリプトです。
- **`config/`**: アプリケーションの各種設定ファイルを格納するディレクトリです。
    - **`config/README_DEBUG_*.md`**: デバッグモードに関する特別な設定や情報が記載されたREADMEファイルです。
    - **`config/alias.toml`**: ボタン名やレバー名の別名を定義し、表示をカスタマイズするための設定ファイルです。
    - **`config/button_challenge.toml`**: アプリケーションの基本的な動作設定（UI表示、タイムリミットなど）を定義する主要な設定ファイルです。
    - **`config/button_challenge_debug_*.toml`**: デバッグ時専用の特別なアプリケーション動作設定ファイルです。
    - **`config/button_names.toml`**: 格闘ゲームのボタンに対応する名前や入力を定義するファイルです。
    - **`config/lever_names.toml`**: 格闘ゲームのレバー入力に対応する名前を定義するファイルです。
    - **`config/mission.toml`**: アプリケーションで出題されるミッションの内容（例: 特定のボタンを押す）を定義するファイルです。
    - **`config/moves.toml`**: キャラクターの基本的な技（ムーブ）の入力と名称を定義するファイルです。
    - **`config/moves_sf6lily.toml`**: ストリートファイター6のリリーなど、特定のキャラクターに特化した技の定義ファイルです。
- **`docs/hot_reload.md`**: 設定ファイルのホットリロード機能の詳細な説明ドキュメントです。
- **`generated-docs/`**: 自動生成されたドキュメントやレポートを格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Googleサイト認証用のファイルであり、プロジェクトのウェブ関連設定に使用されます。
- **`issue-notes/`**: 開発中の課題、検討事項、メモなどを記録したMarkdownファイル群を格納するディレクトリです。
- **`requirements.txt`**: プロジェクトが依存するPythonライブラリの一覧が記述されており、`pip install` で必要なライブラリをインストールするために使用されます。
- **`src/`**: アプリケーションの主要なソースコードを格納するディレクトリです。
    - **`src/check_playing_game.py`**: ユーザーが現在他の格闘ゲームをプレイ中かどうかを検知するロジックが含まれます。
    - **`src/configs.py`**: TOML形式の設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するモジュールです。
    - **`src/get_window_info.py`**: Windowsのウィンドウ情報（アクティブウィンドウ、タイトルなど）を取得するユーティリティ機能を提供します。
    - **`src/gui.py`**: アプリケーションのグラフィカルユーザーインターフェース（GUI）の構築と表示ロジックを実装しています。
    - **`src/gui_utils.py`**: GUI関連の汎用的なヘルパー関数やユーティリティを提供します。
    - **`src/joystick.py`**: XInputなどを利用してジョイスティック（ゲームコントローラー）からの入力を検出し、処理するモジュールです。
    - **`src/main.py`**: アプリケーションのエントリーポイントであり、全体のフローを制御するメインスクリプトです。
    - **`src/missions.py`**: ミッションの生成、表示、ユーザー入力との比較、成功判定などのロジックを管理するモジュールです。
    - **`src/toml_hot_reload.py`**: TOML設定ファイルの変更を監視し、変更があった場合に自動的にアプリケーションに反映させるホットリロード機能を提供します。
    - **`src/utils.py`**: アプリケーション全体で利用される汎用的なヘルパー関数（例: 時間計算、文字列フォーマットなど）を集めたモジュールです。
- **`tests/`**: アプリケーションのテストコードを格納するディレクトリです。
    - **`tests/manual_test_hot_reload.py`**: ホットリロード機能の手動テストシナリオを記述したスクリプトです。
    - **`tests/test_*.py`**: 各機能（ミッション生成、設定読み込み、入力処理など）に対する自動テストスクリプト群です。

## 関数詳細説明
- **`main()` (src/main.py)**:
    - 役割: アプリケーションのエントリーポイントであり、全体の実行フローを制御します。
    - 引数: なし。
    - 戻り値: なし。
    - 機能: 設定の初期化、GUIの起動、コントローラー入力の監視、ミッションの生成と表示、スコア計算、ホットリロードの処理、ウィンドウの最前面化/最背面化の制御などを統合します。
- **`load_config()` (src/configs.py)**:
    - 役割: TOML形式の設定ファイルを読み込み、設定値をアプリケーション全体で利用可能な形式で提供します。
    - 引数: `file_path` (str) - 読み込むTOMLファイルのパス。
    - 戻り値: dict - 読み込んだ設定データを辞書形式で返します。
    - 機能: 指定されたパスからTOMLファイルをパースし、設定値へのアクセスを抽象化します。
- **`get_pressed_buttons()` (src/joystick.py)**:
    - 役割: 接続されているゲームコントローラーから、現在押されているボタンの情報を取得します。
    - 引数: なし。
    - 戻り値: list[str] - 現在押されているボタンの名称リスト。
    - 機能: XInputなどのAPIを通じてコントローラーの状態をポーリングし、物理的な入力に対応する論理ボタン名を返します。
- **`generate_mission()` (src/missions.py)**:
    - 役割: 次にユーザーに提示する新しいミッション（お題）を生成します。
    - 引数: `current_phase` (int) - 現在のミッションフェーズ。
    - 戻り値: str - 生成されたミッションのテキスト。
    - 機能: 設定ファイル（`mission.toml`, `moves.toml`など）に基づいて、ランダムまたは特定ルールに従ってミッションを構築します。
- **`check_mission_success()` (src/missions.py)**:
    - 役割: ユーザーの入力が現在のミッションの条件を満たしているか判定します。
    - 引数: `current_mission` (str) - 現在のミッション、`user_input` (list[str]) - ユーザーが入力したボタン。
    - 戻り値: bool - ミッションが成功した場合はTrue、それ以外はFalse。
    - 機能: ユーザー入力とミッション定義を照合し、成功・失敗を判定します。
- **`update_display()` (src/gui.py)**:
    - 役割: GUI画面上のミッション、スコア、タイムなどの表示を更新します。
    - 引数: `mission_text` (str), `score` (int), `time_elapsed` (float) など表示に必要な情報。
    - 戻り値: なし。
    - 機能: GUI要素のテキストや色を変更し、アプリケーションの現在の状態を視覚的にユーザーに伝えます。
- **`watch_config_files()` (src/toml_hot_reload.py)**:
    - 役割: 特定のTOML設定ファイルの変更を監視し、変更が検出された場合にイベントをトリガーします。
    - 引数: `config_paths` (list[str]) - 監視対象のファイルパスリスト、`callback_func` (function) - 変更時に呼び出す関数。
    - 戻り値: なし。
    - 機能: ファイルシステムイベントをリッスンし、設定ファイルのリアルタイム更新を可能にします。
- **`is_game_running()` (src/check_playing_game.py)**:
    - 役割: 現在、特定の格闘ゲームがWindows上で実行中であるかを判定します。
    - 引数: なし。
    - 戻り値: bool - ゲームが実行中の場合はTrue、それ以外はFalse。
    - 機能: 実行中のプロセスやウィンドウタイトルをチェックし、格闘ゲームのプレイ状況を判断します。
- **`get_active_window_title()` (src/get_window_info.py)**:
    - 役割: 現在アクティブな（最前面にある）ウィンドウのタイトルを取得します。
    - 引数: なし。
    - 戻り値: str - アクティブなウィンドウのタイトル。
    - 機能: Windows APIを利用して、現在のフォーカスを持つウィンドウの情報を取得します。
- **`calculate_score()` (src/utils.py)**:
    - 役割: ミッションの成功に基づいてスコアを計算します。
    - 引数: `time_taken` (float) - 入力にかかった時間、`difficulty` (int) - ミッションの難易度。
    - 戻り値: int - 加算されるスコア。
    - 機能: 入力速度やミッションの難易度に応じてスコアを算出し、ユーザーのモチベーション維持に貢献します。

## 関数呼び出し階層ツリー
```
main.py::main()
  ├── configs.py::load_config() (初期設定読み込み)
  ├── toml_hot_reload.py::watch_config_files() (設定ファイルの変更監視)
  │     └── configs.py::load_config() (変更検出時の再読み込み)
  ├── joystick.py::get_pressed_buttons() (コントローラー入力取得)
  ├── missions.py::generate_mission() (ミッション生成)
  ├── missions.py::check_mission_success() (ミッション成功判定)
  ├── gui.py::update_display() (GUI表示更新)
  ├── check_playing_game.py::is_game_running() (ゲームプレイ状況チェック)
  ├── get_window_info.py::get_active_window_title() (アクティブウィンドウタイトル取得)
  └── utils.py::calculate_score() (スコア計算)

---
Generated at: 2026-02-04 07:08:03 JST
