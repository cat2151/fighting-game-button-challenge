Last updated: 2025-11-10

# Project Overview

## プロジェクト概要
- 格ゲーのボタン練習に特化したWindows用アプリケーションです。
- ランダムに表示されるお題に合わせ、正しいボタン入力を素早く行うことでスコアを獲得します。
- 常駐型で、ゲームプレイを邪魔せず、いつでも即座に練習を開始できる設計が特徴です。

## 技術スタック
- フロントエンド: PythonベースのGUIライブラリ（詳細は不明だが、Windowsデスクトップアプリケーションを構築）
- 音楽・オーディオ: (情報なし)
- 開発ツール:
    - Visual Studio Code: エディタ設定ファイル（`.vscode/settings.json`）
    - Git: ソースコードのバージョン管理（リポジトリのcloneを前提）
    - TOML: 設定ファイル形式（`config/`ディレクトリ内の各種設定）
    - pip: Pythonパッケージのインストールと管理（`requirements.txt`）
- テスト: Pythonの標準的なテストフレームワーク（`tests/`ディレクトリ内のテストスクリプト）
- ビルドツール:
    - requirements.txt: Pythonの依存関係を管理
    - .bat: Windows環境でのアプリケーション起動スクリプト
- 言語機能: Python: アプリケーションの主要な開発言語
- 自動化・CI/CD:
    - GitHub Actions: `README.ja.md` から `README.md` への自動翻訳ワークフロー
    - Gemini: 翻訳エンジンとして利用
- 開発標準:
    - .editorconfig: 複数のエディタ間でのコーディングスタイルの一貫性を維持
    - Pylint: Pythonコードの品質とスタイルをチェックするための設定（`.pylintrc`）

## ファイル階層ツリー
```
📄 .editorconfig
📄 .gitignore
📄 .pylintrc
📁 .vscode/
  📊 settings.json
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
📁 generated-docs/
📁 issue-notes/
  📖 10.md
  📖 11.md
  📖 12.md
  📖 13.md
  📖 14.md
  📖 15.md
  📖 16.md
  📖 2.md
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
  📄 utils.py
📁 tests/
  📄 test_amplify_missions_left_right.py
  📄 test_format_mission_string.py
  📄 test_get_pressed_buttons.py
  📄 test_is_no_count_case.py
```

## ファイル詳細説明
-   `.editorconfig`: さまざまなエディタやIDEで一貫したコーディングスタイルを適用するための設定を定義します。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定します。
-   `.pylintrc`: Pythonの静的コードアナライザPylintの設定ファイルで、コードの品質とコーディング規約を維持するために使用されます。
-   `.vscode/settings.json`: Visual Studio Codeエディタのワークスペース固有の設定を定義し、開発環境をカスタマイズします。
-   `LICENSE`: プロジェクトの配布および使用条件を定めたライセンス情報が含まれています。
-   `README.ja.md`: プロジェクトの日本語での概要、機能、使い方、設定方法などを詳細に説明する主要なドキュメントです。
-   `README.md`: `README.ja.md`を基に自動生成された英語バージョンのプロジェクト概要ドキュメントです。
-   `_config.yml`: GitHub Pagesなどの静的サイトジェネレータで利用される可能性のある設定ファイルです。
-   `button_challenge.bat`: Windows環境でアプリケーションを起動するためのバッチスクリプトです。
-   `config/`: アプリケーションの各種設定ファイルを格納するディレクトリです。
    -   `alias.toml`: アプリ内で表示されるボタン名に対するエイリアス（別名）を定義し、表示をカスタマイズします。
    -   `button_challenge.toml`: アプリケーション全体の挙動に関する詳細な設定（例: スコアリング、タイマーなど）を定義します。
    -   `button_names.toml`: ゲーム内のボタンアサインと、実際に使用するコントローラーのボタン入力をマッピングするための設定ファイルです。ユーザーがゲームに合わせて編集します。
    -   `lever_names.toml`: レバー入力の名称を定義し、ミッション表示や入力判定に利用します。
    -   `mission.toml`: ユーザーが挑戦するミッション（お題）のリストとその詳細を定義するファイルです。
-   `generated-docs/`: プロジェクトのドキュメントが自動生成されるディレクトリです。（例: 開発状況レポートなど）
-   `issue-notes/`: 開発中の課題、検討事項、メモなどが記述されたドキュメントを格納するディレクトリです。
-   `requirements.txt`: プロジェクトが依存するPythonライブラリとそのバージョンをリストアップしたファイルです。
-   `src/`: アプリケーションの主要なPythonソースコードを格納するディレクトリです。
    -   `check_playing_game.py`: 特定の格闘ゲームが現在実行中であるかを検出し、アプリケーションのウィンドウ挙動（最前面化/最背面化）を制御するためのロジックを提供します。
    -   `configs.py`: `config/`ディレクトリ内のTOML設定ファイルを読み込み、アプリケーション内で利用可能な設定オブジェクトを提供する役割を担います。
    -   `get_window_info.py`: Windows APIを利用して、最前面のウィンドウ情報や、特定のウィンドウを最前面/最背面に設定する機能を提供します。
    -   `gui.py`: アプリケーションのグラフィカルユーザーインターフェース（GUI）の構築と描画、および表示要素（ミッション、スコアなど）の更新ロジックを実装します。
    -   `gui_utils.py`: GUI要素の作成、フォント設定など、GUI関連の汎用的なユーティリティ関数やヘルパーを提供します。
    -   `joystick.py`: XInputなどのAPIを介して、ジョイスティックやゲームパッドからの入力を検出し、ボタンの状態やレバーの入力を取得するロジックを処理します。
    -   `main.py`: アプリケーションのエントリーポイントです。設定の初期化、GUIとジョイスティックのセットアップ、メインループの実行、および終了処理を統括します。
    -   `missions.py`: ミッションの読み込み、ランダムなミッションの生成、ユーザー入力とミッションの成否判定、ミッション文字列のフォーマットなどのロジックを管理します。
    -   `utils.py`: アプリケーション全体で利用される汎用的なヘルパー関数やユーティリティ機能を提供します。
-   `tests/`: プロジェクトのテストスクリプトを格納するディレクトリです。
    -   `test_amplify_missions_left_right.py`: ミッションの左右反転ロジックの正確性を検証するテストです。
    -   `test_format_mission_string.py`: ミッション表示文字列のフォーマット機能が正しく動作するかをテストします。
    -   `test_get_pressed_buttons.py`: ジョイスティックからのボタン入力検出ロジックが期待通りに動作するかを検証します。
    -   `test_is_no_count_case.py`: 特定の条件下でスコアが加算されないケースの判定ロジックをテストします。

## 関数詳細説明
このプロジェクト情報からは具体的な関数名、引数、戻り値の詳細は検出されませんでした。しかし、各ファイルの役割から以下の主要な機能を持つ関数が存在すると推測されます。

-   **`check_playing_game.py`**:
    -   `is_game_active()`: 現在、設定された格闘ゲームがフォアグラウンドで実行されているかを判断します。
-   **`configs.py`**:
    -   `load_config(file_path)`: 指定されたTOML設定ファイルを読み込み、その内容をデータ構造として返します。
    -   `get_all_configs()`: 全ての関連設定ファイルを読み込み、アプリケーション全体の設定オブジェクトを構築して提供します。
-   **`get_window_info.py`**:
    -   `get_foreground_window_title()`: 現在最前面にあるウィンドウのタイトル文字列を取得します。
    -   `set_window_foreground(window_handle)`: 指定されたウィンドウを最前面に表示します。
    -   `set_window_background(window_handle)`: 指定されたウィンドウを最背面に移動させます。
-   **`gui.py`**:
    -   `initialize_gui()`: GUIウィンドウ、表示ラベル、ボタンなどのインターフェース要素を初期設定します。
    -   `update_display(mission_text, score, time_elapsed)`: GUI上のミッションテキスト、スコア、経過時間などの表示を最新の情報に更新します。
    -   `run_gui_loop()`: GUIのイベント処理ループを開始し、ユーザーインターフェースからのイベントに応答します。
-   **`gui_utils.py`**:
    -   `create_text_label(parent, text, style)`: 指定された親要素内にテキストラベルを作成し、設定されたスタイルを適用します。
    -   `apply_font(widget, font_spec)`: GUIウィジェットに対して、指定されたフォント名、サイズ、スタイルを適用します。
-   **`joystick.py`**:
    -   `init_joystick_input()`: XInputライブラリなどを初期化し、コントローラーとの接続を確立します。
    -   `get_current_inputs()`: 現在押されているボタンやレバーの入力状態を検出し、その情報を返します。
-   **`main.py`**:
    -   `main()`: アプリケーションの主処理を開始するエントリーポイントです。設定の読み込み、GUIと入力デバイスの初期化、メインループの開始、終了処理などを管理します。
    -   `application_loop()`: アプリケーションのメインループを構成し、入力の監視、ミッションの更新、GUIの描画、ウィンドウの表示状態制御などを継続的に実行します。
-   **`missions.py`**:
    -   `load_mission_definitions(config_data)`: 設定データからミッションの定義リストを読み込みます。
    -   `generate_random_challenge()`: 定義されたミッションの中からランダムに一つのお題を選択して提供します。
    -   `evaluate_input(current_challenge, user_input)`: 現在のミッションとユーザーの入力が一致するかを判定し、成否を返します。
    -   `format_challenge_string(challenge_data)`: ミッションデータをユーザーに分かりやすい表示用文字列に変換します。
-   **`utils.py`**:
    -   `get_current_timestamp_ms()`: 現在のシステム時刻をミリ秒単位で取得します。
    -   `sleep_for_ms(milliseconds)`: 指定されたミリ秒間、プログラムの実行を一時停止させます。

## 関数呼び出し階層ツリー
```
提供された情報からは、プロジェクトの関数呼び出し階層ツリーを分析できませんでした。

---
Generated at: 2025-11-10 08:01:26 JST
