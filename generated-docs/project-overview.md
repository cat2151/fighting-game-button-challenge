Last updated: 2026-01-04

# Project Overview

## プロジェクト概要
- 格ゲーのボタン練習に特化したWindows用アプリケーションです。
- ランダムに表示されるお題に対し、正しいボタン入力でスコアを獲得します。
- 常駐型でゲームの邪魔にならず、素早い反応と正確な入力の反復練習をサポートします。

## 技術スタック
- フロントエンド: PythonでGUIを直接実装し、ユーザーインターフェースを提供しています。
- 音楽・オーディオ: (情報なし)
- 開発ツール:
    - Git: ソースコードのバージョン管理に使用されています。
    - Visual Studio Code: `.vscode/settings.json`から、開発エディタとして利用されていることが推測されます。
- テスト: `tests/`ディレクトリ内の複数のファイルから、Pytestなどのテストフレームワークを利用して機能テストが実施されていると推測されます。
- ビルドツール:
    - pip: Pythonパッケージの依存関係管理に使用されます。
    - TOML: 設定ファイルの記述形式として、柔軟な設定管理を実現しています。
- 言語機能:
    - Python: アプリケーションの主要な開発言語です。
    - XInput: Windows環境下でのゲームコントローラー（XInput互換デバイス）からの入力処理に使用されます。
- 自動化・CI/CD:
    - GitHub Actions: `README.md`の自動英訳など、継続的インテグレーション/デプロイメントの自動化に利用されています。
- 開発標準:
    - pylint: `.pylintrc`から、Pythonコードの品質とコーディング規約の遵守のために利用されています。
    - EditorConfig: `.editorconfig`から、異なるエディタ間でのコーディングスタイルの統一に利用されています。

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
```

## ファイル詳細説明
-   **.editorconfig**: プロジェクト全体のコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
-   **.gitignore**: Gitバージョン管理システムにおいて、リポジトリに含めないファイルやディレクトリを指定します。
-   **.pylintrc**: Pythonコードの静的解析ツールPylintの設定ファイルで、コード品質の維持に貢献します。
-   **.vscode/settings.json**: Visual Studio Codeエディタのワークスペース固有の設定を定義し、開発環境の統一を図ります。
-   **LICENSE**: 本ソフトウェアの利用条件を定めるライセンス情報です。
-   **README.ja.md**: プロジェクトの目的、機能、使い方などを日本語で説明する主要なドキュメントです。
-   **README.md**: `README.ja.md`を基に自動生成された、プロジェクトの英語説明ドキュメントです。
-   **_config.yml**: Jekyllなどの静的サイトジェネレーターでドキュメントサイトを生成する際に使用される設定ファイルです。
-   **button_challenge.bat**: Windows環境でアプリケーションを簡単に起動するためのバッチファイルです。
-   **config/**: アプリケーションの設定ファイル群を格納するディレクトリです。
    -   **alias.toml**: ゲームのボタン名表示に関するエイリアス（別名）を定義します。
    -   **button_challenge.toml**: ボタンチャレンジの主要な動作設定を定義します。
    -   **button_names.toml**: 物理的なボタン名とゲーム内での表示名をマッピングします。
    -   **lever_names.toml**: レバー（方向入力）の物理名と表示名をマッピングします。
    -   **mission.toml**: ユーザーに提示されるミッションの内容を定義します。
    -   **moves.toml**: ゲーム内の特定の「ムーブ」（技）に関する情報を定義します。
-   **generated-docs/**: 自動生成されたドキュメントやレポートを格納するディレクトリです。
-   **googled947dc864c270e07.html**: Googleサービスのサイト認証などに使用される検証ファイルです。
-   **issue-notes/**: 開発中に発生した課題やその解決策、その他開発メモなどを記録したドキュメントを格納します。
-   **requirements.txt**: プロジェクトが依存するPythonライブラリの一覧が記述されており、環境構築時に使用されます。
-   **src/**: アプリケーションのPythonソースコードが格納されている主要なディレクトリです。
    -   **check_playing_game.py**: 現在ユーザーが格闘ゲームをプレイ中であるかを検出し、アプリの挙動（最前面化/最背面化など）を制御します。
    -   **configs.py**: TOML形式の設定ファイルを読み込み、アプリケーション全体で設定値にアクセスするための機能を提供します。
    -   **get_window_info.py**: Windowsのウィンドウ情報を取得し、アプリケーションの最前面/最背面制御などの機能に利用されます。
    -   **gui.py**: アプリケーションのグラフィカルユーザーインターフェース（GUI）を構築し、ユーザーへの情報表示や操作を受け付けます。
    -   **gui_utils.py**: GUI関連の共通処理やユーティリティ関数をまとめたモジュールです。
    -   **joystick.py**: XInput対応のジョイスティック（コントローラー）からの入力を検出し、アプリケーションに伝えます。
    -   **main.py**: アプリケーションのエントリーポイントであり、初期設定、GUIの起動、メインループ処理など、全体の流れを制御します。
    -   **missions.py**: ミッションの生成、現在のミッションの状態管理、ユーザー入力との比較判定などのロジックを提供します。
    -   **utils.py**: アプリケーション全体で汎用的に利用されるヘルパー関数や共通処理をまとめたモジュールです。
-   **tests/**: アプリケーションの各機能が意図通りに動作するか検証するためのテストコードを格納するディレクトリです。
    -   **test_amplify_missions_left_right.py**: ミッションの方向（左右）を反転させるロジックのテストケースです。
    -   **test_challenge_phases.py**: チャレンジ（お題）の各フェーズ（表示、入力待ち、判定など）が正しく遷移するかをテストします。
    -   **test_format_mission_string.py**: ミッション文字列の表示形式が正しくフォーマットされるかをテストします。
    -   **test_get_move_name_for_input.py**: 特定の入力に対して対応するムーブ名が正しく取得されるかをテストします。
    -   **test_get_pressed_buttons.py**: 現在押されているボタンを正確に検出するロジックのテストケースです。
    -   **test_is_no_count_case.py**: 特定の条件下でスコアが加算されないケースが正しく判定されるかをテストします。

## 関数詳細説明
提供された情報では、各Pythonファイル内の具体的な関数名、引数、戻り値、機能に関する詳細な説明が不足しているため、このセクションで個別の関数の詳細を記述することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-04 07:04:07 JST
