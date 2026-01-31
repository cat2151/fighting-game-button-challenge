Last updated: 2026-02-01

# Project Overview

## プロジェクト概要
- 格ゲーのボタン練習アプリ
- ランダムでお題が表示されます
- お題に合ったボタンを押すとスコアが入って次のお題が表示されます

## 技術スタック
- フロントエンド: PythonのGUIライブラリ（具体的なフレームワークは明示されていませんが、`src/gui.py`および`src/gui_utils.py`が存在するため、PythonのGUI機能を利用していると推測されます。）
- 音楽・オーディオ: (該当する技術情報の提供はありません)
- 開発ツール: Visual Studio Code (開発環境設定ファイル `.vscode/settings.json` が存在), Git (バージョン管理システム)
- テスト: Pythonテストフレームワーク (テストディレクトリ `tests/` が存在しますが、具体的なフレームワークは明示されていません)
- ビルドツール: pip (Pythonパッケージ管理ツール、`requirements.txt` にて依存関係を管理)
- 言語機能: Python (アプリケーション開発に使用されるプログラミング言語)
- 自動化・CI/CD: GitHub Actions (READMEファイルの自動翻訳に使用), Google Gemini (GitHub Actionsによる自動翻訳エンジン)
- 開発標準: Pylint (Pythonコードの品質チェックツール、`.pylintrc` が存在), EditorConfig (異なるエディタ間でのコードスタイル統一設定、`.editorconfig` が存在)
- その他: XInput (Windows環境でのゲームコントローラー入力処理に使用), TOML (設定ファイル形式、`config/*.toml` にて利用)

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
  📄 moves.toml
  📄 moves_sf6lily.toml
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
  📄 test_challenge_phases.py
  📄 test_format_mission_string.py
  📄 test_get_move_name_for_input.py
  📄 test_get_pressed_buttons.py
  📄 test_is_no_count_case.py
  📄 test_phase_transition_integration.py
```

## ファイル詳細説明
-   `.editorconfig`: 異なるテキストエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
-   `.gitignore`: Gitによるバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
-   `.pylintrc`: Pythonコードの静的解析ツールPylintの設定ファイル。コード品質やスタイルに関するルールを定義します。
-   `.vscode/settings.json`: Visual Studio Codeエディタのワークスペース固有の設定を定義するファイル。
-   `LICENSE`: 本プロジェクトのソフトウェアライセンス情報が記述されています。
-   `README.ja.md`: プロジェクトの目的、使い方、機能などを日本語で説明する主要なドキュメント。
-   `README.md`: `README.ja.md` を基に自動生成された、プロジェクトの英語での説明ドキュメント。
-   `_config.yml`: GitHub Pagesなどで使用されるJekyllサイトの設定ファイルである可能性があります。
-   `button_challenge.bat`: Windows環境でアプリケーションを起動するためのババッチスクリプト。
-   `config/alias.toml`: アプリ内で使用されるボタン名の別名（エイリアス）を定義するTOML形式の設定ファイル。
-   `config/button_challenge.toml`: アプリケーションの主要な動作設定やパラメータを定義するTOML形式の設定ファイル。
-   `config/button_names.toml`: 実際のコントローラーボタンとアプリ内で表示される名前のマッピングを定義するTOML形式の設定ファイル。
-   `config/lever_names.toml`: コントローラーのレバー入力方向（例: UP, DOWN）とアプリ内で表示される名前のマッピングを定義するTOML形式の設定ファイル。
-   `config/mission.toml`: ユーザーに提示されるミッション（お題）の内容や条件を定義するTOML形式の設定ファイル。
-   `config/moves.toml`: ゲーム内の一般的なムーブ（技）や入力パターンを定義するTOML形式の設定ファイル。
-   `config/moves_sf6lily.toml`: 特定のゲーム（ストリートファイター6）の特定のキャラクター（リリー）に特化したムーブ定義を記述するTOML形式の設定ファイル。
-   `generated-docs/`: GitHub Actionsなどによって自動生成されたドキュメントやレポートを格納するディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのサイト所有権確認に使用されるHTMLファイル。
-   `issue-notes/`: 開発中の課題、検討事項、メモなどがMarkdown形式で記録されているディレクトリ。
-   `requirements.txt`: このPythonプロジェクトが依存する外部ライブラリとそのバージョンをリストアップしたファイル。`pip install -r` でインストールされます。
-   `src/check_playing_game.py`: 他のゲームアプリケーションが現在実行中であるかを検出し、本アプリの動作を制御するロジックを格納するファイル。
-   `src/configs.py`: TOML形式の設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理する機能を提供するファイル。
-   `src/get_window_info.py`: Windowsのウィンドウ情報（タイトル、アクティブ状態など）を取得し、ウィンドウの最前面化・最背面化などの操作を行うユーティリティ関数を格納するファイル。
-   `src/gui.py`: アプリケーションのグラフィカルユーザーインターフェース（GUI）を構築し、表示を管理する主要なロジックを格納するファイル。
-   `src/gui_utils.py`: GUI関連の汎用的なユーティリティ関数やヘルパークラスを格納するファイル。
-   `src/joystick.py`: XInputなどのAPIを介してゲームコントローラーからの入力（ボタン押下、レバー方向）を検出し、アプリケーションに提供するファイル。
-   `src/main.py`: アプリケーションのエントリーポイントであり、GUI、コントローラー入力、ミッションロジックなどの主要なコンポーネントを統合し、全体の実行フローを制御するファイル。
-   `src/missions.py`: ミッションの生成、現在の入力に対するミッションの成否判定、ミッション文字列のフォーマットなど、ミッション関連のコアロジックを格納するファイル。
-   `src/utils.py`: プロジェクト全体で利用される汎用的なユーティリティ関数（ファイル操作、時間処理、デバウンスなど）を格納するファイル。
-   `tests/test_*.py`: アプリケーションの各コンポーネントや機能が正しく動作するかを確認するためのテストスクリプト群。

## 関数詳細説明
※提供された情報には関数の具体的な実装やシグネチャが含まれていないため、ファイル名とその役割から推定される関数について説明します。引数や戻り値の型は推測に基づいています。

-   **`src/check_playing_game.py`**
    -   `is_game_playing() -> bool`:
        -   **役割**: 現在、設定された特定のゲームがWindows上でアクティブにプレイされているかを判定します。
        -   **引数**: なし。
        -   **戻り値**: ゲームがプレイ中の場合は `True`、そうでない場合は `False`。

-   **`src/configs.py`**
    -   `load_config(config_name: str) -> dict`:
        -   **役割**: 指定された設定ファイル（TOML形式）を読み込み、辞書形式で内容を返します。
        -   **引数**: `config_name` (str) - 読み込む設定ファイルの名前（例: "button_challenge"）。
        -   **戻り値**: 設定ファイルの内容を表す辞書。
    -   `get_button_name_map() -> dict`:
        -   **役割**: `config/button_names.toml` からボタン名マッピングを取得します。
        -   **引数**: なし。
        -   **戻り値**: 実際のボタン入力と表示名を対応付ける辞書。
    -   `get_alias_map() -> dict`:
        -   **役割**: `config/alias.toml` からボタンエイリアスマッピングを取得します。
        -   **引数**: なし。
        -   **戻り値**: エイリアス名と実際のボタン名の対応辞書。

-   **`src/get_window_info.py`**
    -   `get_active_window_title() -> str`:
        -   **役割**: 現在Windowsで最前面にあるウィンドウのタイトルを取得します。
        -   **引数**: なし。
        -   **戻り値**: 最前面ウィンドウのタイトル文字列。
    -   `set_window_foreground(target_title: str) -> None`:
        -   **役割**: 指定されたタイトルを持つウィンドウを最前面に表示します。
        -   **引数**: `target_title` (str) - 最前面にしたいウィンドウのタイトル。
        -   **戻り値**: なし。
    -   `set_window_background(target_title: str) -> None`:
        -   **役割**: 指定されたタイトルを持つウィンドウを最背面に移動させます。
        -   **引数**: `target_title` (str) - 最背面にしたいウィンドウのタイトル。
        -   **戻り値**: なし。

-   **`src/gui.py`**
    -   `create_main_window() -> Any`:
        -   **役割**: アプリケーションのメインGUIウィンドウを生成し、初期設定を行います。
        -   **引数**: なし。
        -   **戻り値**: 作成されたGUIウィンドウオブジェクト。
    -   `update_mission_display(mission_string: str) -> None`:
        -   **役割**: GUI上のミッション表示を更新します。
        -   **引数**: `mission_string` (str) - 表示するミッションのテキスト。
        -   **戻り値**: なし。
    -   `update_score_display(score: int) -> None`:
        -   **役割**: GUI上のスコア表示を更新します。
        -   **引数**: `score` (int) - 表示する現在のスコア。
        -   **戻り値**: なし。

-   **`src/joystick.py`**
    -   `initialize_joystick() -> bool`:
        -   **役割**: XInputコントローラーを初期化し、利用可能にします。
        -   **引数**: なし。
        -   **戻り値**: 初期化に成功した場合は `True`、失敗した場合は `False`。
    -   `get_pressed_buttons() -> list[str]`:
        -   **役割**: 現在コントローラーで押されているボタンのリストを取得します。
        -   **引数**: なし。
        -   **戻り値**: 押されているボタンの名前のリスト。
    -   `get_lever_direction() -> str`:
        -   **役割**: 現在のレバー入力の方向（例: "UP", "DOWN", "LEFT", "RIGHT"）を取得します。
        -   **引数**: なし。
        -   **戻り値**: レバー方向を表す文字列。

-   **`src/main.py`**
    -   `main() -> None`:
        -   **役割**: アプリケーションの主要な実行ロジックを定義し、GUIの起動、ジョイスティックの監視、ミッションの進行などを統合します。
        -   **引数**: なし。
        -   **戻り値**: なし。
    -   `run_challenge_loop() -> None`:
        -   **役割**: ボタンチャレンジのメインゲームループを制御し、ミッションの表示、入力の検出、スコア更新、ウィンドウの状態管理などを行います。
        -   **引数**: なし。
        -   **戻り値**: なし。

-   **`src/missions.py`**
    -   `generate_random_mission() -> dict`:
        -   **役割**: 設定ファイルに基づいてランダムなミッションを生成し、その詳細を返します。
        -   **引数**: なし。
        -   **戻り値**: ミッションの詳細を含む辞書。
    -   `check_mission_success(current_mission: dict, pressed_buttons: list[str], lever_direction: str) -> bool`:
        -   **役割**: 現在のミッションとコントローラーからの入力を比較し、ミッションが成功したかどうかを判定します。
        -   **引数**:
            -   `current_mission` (dict) - 現在のアクティブなミッション情報。
            -   `pressed_buttons` (list[str]) - 現在押されているボタンのリスト。
            -   `lever_direction` (str) - 現在のレバー方向。
        -   **戻り値**: ミッションが成功した場合は `True`、そうでない場合は `False`。
    -   `get_mission_string(mission_data: dict) -> str`:
        -   **役割**: ミッションデータからユーザーに表示するためのフォーマットされた文字列を生成します。
        -   **引数**: `mission_data` (dict) - 表示したいミッションの詳細情報。
        -   **戻り値**: 表示用のミッション文字列。

-   **`src/utils.py`**
    -   `load_toml(filepath: str) -> dict`:
        -   **役割**: 指定されたパスのTOMLファイルを読み込み、その内容を辞書として返します。
        -   **引数**: `filepath` (str) - 読み込むTOMLファイルのパス。
        -   **戻り値**: TOMLファイルの内容を表す辞書。
    -   `get_timestamp_ms() -> int`:
        -   **役割**: 現在のシステム時刻をミリ秒単位のタイムスタンプで取得します。
        -   **引数**: なし。
        -   **戻り値**: 現在のミリ秒タイムスタンプ。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-01 07:04:29 JST
