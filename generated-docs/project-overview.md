Last updated: 2026-02-02

# Project Overview

## プロジェクト概要
- Windows向けの格闘ゲーム練習用アプリです
- ランダムに表示されるお題に合わせてボタンを入力し、スコアを競います
- 常駐型で、使いたい時にすぐに起動でき、ゲームプレイを邪魔しない設計です

## 技術スタック
- フロントエンド: PythonベースのGUIフレームワークを利用して、ユーザーインターフェースを構築しています。
- 音楽・オーディオ: 特になし（豪華なサウンドはスコープ外とされています）。
- 開発ツール: Pythonのパッケージ管理ツール `pip` を使用し、依存関係は `requirements.txt` で管理されています。設定ファイルにはTOML形式 (`*.toml`) を採用しています。
- テスト: Python向けのテストフレームワークを利用し、`tests/` ディレクトリ配下で各機能のユニットテストや統合テストが記述されています。
- ビルドツール: Pythonプロジェクトの依存関係管理には`pip`が使用されています。
- 言語機能: 主要なアプリケーションロジックはPythonで記述されています。
- 自動化・CI/CD: GitHub Actionsを利用して、ドキュメントの自動生成などを行っています。
- 開発標準: `.editorconfig` でエディタ間のコーディングスタイルを統一し、Pylint (`.pylintrc`) でPythonコードの静的解析を行っています。

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
  📖 26.md
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
  📄 test_gui_phase2_mission_display.py
  📄 test_is_no_count_case.py
  📄 test_phase_transition_integration.py
```

## ファイル詳細説明
- **.editorconfig**: 複数のエディタやIDE間で、インデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。
- **.pylintrc**: Pythonの静的コード解析ツールPylintの設定ファイルで、コード品質の維持に役立ちます。
- **.vscode/settings.json**: Visual Studio Codeエディタのワークスペースに特化した設定を定義するファイルです。
- **LICENSE**: 本ソフトウェアの利用条件を定めるライセンス情報が記述されています。
- **README.ja.md**: プロジェクトの日本語での概要、機能、使い方などが説明された主要なドキュメントです。
- **README.md**: `README.ja.md`を基に自動生成された、プロジェクトの英語での概要ドキュメントです。
- **_config.yml**: GitHub Pagesなどの静的サイトジェネレーターで使用される設定ファイルです。
- **button_challenge.bat**: Windows環境で本アプリケーションを起動するためのバッチスクリプトです。
- **config/**: アプリケーションの様々な設定ファイルを格納するディレクトリです。
    - **alias.toml**: ゲーム内で表示されるボタン名に対する別名（エイリアス）を定義する設定ファイルです。
    - **button_challenge.toml**: アプリケーション全体の動作に関する基本的な設定を定義するファイルです。
    - **button_names.toml**: 各ボタン入力に対応する内部的な名前やゲーム固有のボタン名を定義する設定ファイルです。
    - **lever_names.toml**: レバー入力（方向キーなど）に対応する名前を定義する設定ファイルです。
    - **mission.toml**: ユーザーに提示されるミッションの内容や条件を定義するファイルです。
    - **moves.toml**: 各ボタン入力やレバー入力の組み合わせに対応するゲーム内の「ムーブ」（技）を定義するファイルです。
    - **moves_sf6lily.toml**: 特定のゲーム（例: ストリートファイター6のリリー）に特化したムーブの定義を記述するファイルです。
- **generated-docs/**: 自動生成されたドキュメント（例: 開発状況レポートなど）を格納するディレクトリです。
- **googled947dc864c270e07.html**: Googleのサイト所有権確認などの認証に使用される可能性のあるHTMLファイルです。
- **issue-notes/**: 開発中に発生した課題や検討事項、技術メモなどを記録したMarkdownファイル群を格納するディレクトリです。
- **requirements.txt**: プロジェクトが依存するPythonライブラリとそのバージョンを一覧表示するファイルです。`pip`によるインストールに使用されます。
- **src/**: アプリケーションの主要なPythonソースコードが格納されているディレクトリです。
    - **check_playing_game.py**: 現在PC上で別のゲームが実行されているかを検出し、本アプリの表示状態（最前面/最背面）を制御するロジックが含まれています。
    - **configs.py**: `config/`ディレクトリ内のTOML設定ファイルを読み込み、Pythonオブジェクトとしてアプリケーション全体に提供する役割を担います。
    - **get_window_info.py**: WindowsのAPIを利用して、実行中のウィンドウ情報を取得するユーティリティ関数を提供します。
    - **gui.py**: アプリケーションのグラフィカルユーザーインターフェース（GUI）の主要な構築と表示ロジックを実装しています。
    - **gui_utils.py**: GUI関連で汎用的に利用される補助的な関数やコンポーネントを定義しています。
    - **joystick.py**: XInputなどのジョイスティックやゲームコントローラーからの入力を検出し、処理する機能を提供します。
    - **main.py**: アプリケーションの起動点であり、全体の設定読み込み、GUIの初期化、イベントループの実行など、主要な流れを管理します。
    - **missions.py**: ランダムなミッションの生成、ユーザーの入力判定、スコア計算など、ミッションのロジック全般を扱います。
    - **utils.py**: アプリケーション全体で共通して利用される汎用的なヘルパー関数やユーティリティが含まれています。
- **tests/**: アプリケーションの各機能が正しく動作するかを確認するためのテストコードを格納するディレクトリです。
    - **test_amplify_missions_left_right.py**: ミッションの方向性（左右）の変換・拡張に関するテストです。
    - **test_challenge_phases.py**: チャレンジの進行フェーズ（段階）に関するテストです。
    - **test_format_mission_string.py**: ミッション表示用の文字列が正しくフォーマットされるかのテストです。
    - **test_get_move_name_for_input.py**: 特定の入力に対して正しいムーブ名が取得されるかのテストです。
    - **test_get_pressed_buttons.py**: ユーザーが押したボタンが正確に検出されるかのテストです。
    - **test_gui_phase2_mission_display.py**: GUIにおけるミッション表示のフェーズ2に関するテストです。
    - **test_is_no_count_case.py**: スコアとしてカウントしない特定のケースが正しく判定されるかのテストです。
    - **test_phase_transition_integration.py**: アプリケーションのフェーズ遷移全体の統合テストです。

## 関数詳細説明
提供された情報に基づき、個別の関数詳細は不明です。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-02 07:04:28 JST
