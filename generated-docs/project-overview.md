Last updated: 2026-02-05

# Project Overview

## プロジェクト概要
- 格闘ゲームのボタン練習に特化したWindows用アプリケーションです。
- ランダムに表示されるお題に合わせボタンを入力し、スコアを競いながら反応速度と正確性を鍛えます。
- 常駐型で、ゲームプレイ中でも邪魔にならないよう設計されており、プレイヤーのスキルアップをサポートします。

## 技術スタック
- フロントエンド: PythonのGUIフレームワーク（例: Tkinter）とWindows API連携による、ウィンドウの常駐、最前面化、最背面化などの制御。
- 音楽・オーディオ: （該当する技術は見つかりませんでした）
- 開発ツール:
    - Python: アプリケーションの主要開発言語。
    - pip: Pythonパッケージの管理に使用。
    - Git: ソースコードのバージョン管理に使用。
    - VS Code: 開発用エディタ/IDEとして推奨される設定が提供されています。
- テスト: Python標準のテストフレームワーク（例: unittestやpytest）を用いた単体・結合テストにより、各機能の品質を保証。
- ビルドツール:
    - TOML: アプリケーションの設定ファイル形式として使用され、設定の構造化と読み込みに利用されます。
- 言語機能:
    - Python: アプリケーション全体のロジックと機能実装に使用されています。
- 自動化・CI/CD:
    - GitHub Actions: READMEファイルの自動英訳など、継続的インテグレーション・デリバリープロセスの一部として利用。
- 開発標準:
    - EditorConfig: 異なるエディタ間でのコードスタイルの統一を支援します。
    - Pylint: Pythonコードの品質とコーディング規約遵守をチェックする静的解析ツールです。

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
  📄 test_is_no_count_case.py
  📄 test_phase_transition_integration.py
  📄 test_random_mission_selection.py
  📄 test_start_mission_index.py
  📄 test_toml_hot_reload.py
```

## ファイル詳細説明
-   **`.editorconfig`**: 異なるエディタ間でのコードスタイルの統一を定義する設定ファイルです。
-   **`.gitignore`**: Gitによるバージョン管理から除外するファイルやディレクトリを指定するファイルです。
-   **`.pylintrc`**: Pythonコードの静的解析ツールPylintの設定ファイルです。
-   **`.vscode/`**: Visual Studio Codeエディタのワークスペース固有の設定を格納するディレクトリです。
    -   **`settings.json`**: VS Codeのワークスペース設定を定義するファイルです。
-   **`IMPLEMENTATION_SUMMARY.md`**: プロジェクトの実装概要や設計に関するドキュメントです。
-   **`LICENSE`**: プロジェクトのライセンス情報が記載されています。
-   **`README.ja.md`**: プロジェクトの日本語版説明書（README）です。
-   **`README.md`**: プロジェクトの英語版説明書（README）で、`README.ja.md`から自動生成されています。
-   **`_config.yml`**: GitHub Pagesなどで利用されるJekyllなどの静的サイトジェネレータの設定ファイルです。
-   **`button_challenge.bat`**: Windows環境でアプリケーションを起動するためのバッチスクリプトです。
-   **`config/`**: アプリケーションの設定ファイルを格納するディレクトリです。
    -   **`alias.toml`**: ボタン名のエイリアス（別名）を定義するための設定ファイルです。
    -   **`button_challenge.toml`**: アプリケーションの基本的な動作やゲームモードに関する設定を定義します。
    -   **`button_names.toml`**: ゲームコントローラーのボタン名をアプリケーション内で使用する名前にマッピングする設定ファイルです。
    -   **`lever_names.toml`**: ジョイスティックのレバー入力をアプリケーション内で使用する名前にマッピングする設定ファイルです。
    -   **`mission.toml`**: プレイヤーに提示される練習ミッションの内容と種類を定義する設定ファイルです。
    -   **`moves.toml`**: 格闘ゲームの特定のムーブ（技）に関する情報を定義する設定ファイルです。
    -   **`moves_sf6lily.toml`**: ストリートファイター6のリリーキャラクターに特化したムーブに関する設定ファイルです。
-   **`docs/`**: アプリケーションに関する追加ドキュメントを格納するディレクトリです。
    -   **`hot_reload.md`**: 設定ファイルのホットリロード機能について詳細に説明するドキュメントです。
-   **`generated-docs/`**: 自動生成されたドキュメントやレポートを格納するディレクトリです。
-   **`googled947dc864c270e07.html`**: Googleサービスによるサイト所有権確認のためのファイルです。
-   **`issue-notes/`**: 開発中の課題や検討事項を記録したノートを格納するディレクトリです。
-   **`requirements.txt`**: プロジェクトが依存するPythonパッケージとそのバージョンをリストアップしたファイルです。`pip install`コマンドでこれらのパッケージをインストールできます。
-   **`src/`**: アプリケーションの主要なPythonソースコードを格納するディレクトリです。
    -   **`check_playing_game.py`**: 現在実行中のゲームプロセスを検出し、アプリケーションの動作を調整する機能を提供します。
    -   **`configs.py`**: TOML形式の設定ファイルを読み込み、アプリケーション全体でアクセスできるように管理するモジュールです。
    -   **`get_window_info.py`**: Windowsのウィンドウ情報を取得し、アプリケーションのウィンドウを制御（最前面化、最背面化など）するための機能を提供します。
    -   **`gui.py`**: アプリケーションのグラフィカルユーザーインターフェース（GUI）を構築し、画面表示を制御するメインモジュールです。
    -   **`gui_utils.py`**: GUI関連の汎用的なユーティリティ関数やヘルパークラスを定義するモジュールです。
    -   **`joystick.py`**: XInput対応ジョイスティック（ゲームコントローラー）からの入力を検出し、処理する機能を提供します。
    -   **`main.py`**: アプリケーションの起動点となるメインスクリプトで、各モジュールを統合してアプリケーションを実行します。
    -   **`missions.py`**: 練習ミッションの生成、進行状況の管理、プレイヤーの入力に対する正誤判定などのロジックを実装しています。
    -   **`toml_hot_reload.py`**: TOML設定ファイルの変更を監視し、アプリケーションを再起動せずに設定を即座に反映させるホットリロード機能を提供します。
    -   **`utils.py`**: アプリケーション全体で利用される汎用的なヘルパー関数や共通処理をまとめたモジュールです。
-   **`tests/`**: アプリケーションの各種テストコードを格納するディレクトリです。
    -   **`manual_test_hot_reload.py`**: ホットリロード機能を手動でテストするためのスクリプトです。
    -   **`test_amplify_missions_left_right.py`**: ミッションの左右反転機能に関するテストです。
    -   **`test_challenge_phases.py`**: チャレンジモードのフェーズ遷移に関するテストです。
    -   **`test_config_phase2_start.py`**: フェーズ2の開始設定に関するテストです。
    -   **`test_debug_print_config.py`**: デバッグ表示設定に関するテストです。
    -   **`test_debug_print_integration.py`**: デバッグ表示の統合に関するテストです。
    -   **`test_demo_random_vs_deterministic.py`**: ランダムミッションと決定論的ミッションの比較デモテストです。
    -   **`test_format_mission_string.py`**: ミッション表示文字列の整形に関するテストです。
    -   **`test_get_move_name_for_input.py`**: 入力に対応するムーブ名の取得に関するテストです。
    -   **`test_get_pressed_buttons.py`**: 押されたボタンの検出に関するテストです。
    -   **`test_gui_phase2_mission_display.py`**: フェーズ2のGUIミッション表示に関するテストです。
    -   **`test_is_no_count_case.py`**: カウントされないケースの判定に関するテストです。
    -   **`test_phase_transition_integration.py`**: フェーズ遷移の統合テストです。
    -   **`test_random_mission_selection.py`**: ランダムミッションの選択ロジックに関するテストです。
    -   **`test_start_mission_index.py`**: ミッション開始インデックスに関するテストです。
    -   **`test_toml_hot_reload.py`**: TOML設定のホットリロード機能に関するテストです。

## 関数詳細説明
プロジェクト情報から関数の詳細な役割、引数、戻り値、機能を特定できませんでした。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-05 07:04:50 JST
