Last updated: 2026-02-01

# Development Status

## 現在のIssues
- GUIのPhase1とPhase2におけるUI表示の不一致([Issue #25](../issue-notes/25.md), [Issue #24](../issue-notes/24.md), [Issue #21](../issue-notes/21.md))に関する複数の課題がオープン中。
- プレイヤーの上達度を可視化するスコアリング改善([Issue #10](../issue-notes/10.md))は進行中で、失敗判定とミッションごとの時間計測は完了、ラップタイム表示が次のステップ。
- 新しい練習モードの検討([Issue #16](../issue-notes/16.md))、コンボ表示([Issue #15](../issue-notes/15.md))、ローカルでのドッグフーディング([Issue #20](../issue-notes/20.md))といった機能改善・運用課題も残る。

## 次の一手候補
1. Phase1とPhase2でのGUI表示の不一致を解消 [Issue #25](../issue-notes/25.md), [Issue #24](../issue-notes/24.md), [Issue #21](../issue-notes/21.md)
   - 最初の小さな一歩: `src/gui.py`の`update_display_with_mission`関数内で`challenge_phase`に応じて`label1`（ボタンガイド）と`label2`（ムーブ行）の表示内容を適切に制御する。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/gui.py`

     実行内容: `src/gui.py`内の`update_display_with_mission`関数を修正してください。
     関数内で`state`から取得される`challenge_phase`の値（`PHASE_1_BUTTONS`または`PHASE_2_MOVES`）に基づいて、`format_dict`に渡す`mission`と`move_name`の値を適切に制御します。
     具体的には：
     1.  現在の`mission`変数を`displayed_mission`という新しい変数に格納します。
     2.  現在の`displayed_move_name`変数を`displayed_move`という新しい変数に格納します。
     3.  `challenge_phase`が`PHASE_1_BUTTONS`の場合：
         -   `displayed_move`を空文字列に設定します。
     4.  `challenge_phase`が`PHASE_2_MOVES`の場合：
         -   `displayed_mission`を空文字列に設定します。
         -   `current_direction`に基づいた方向インジケータ（例: 「（右向き）」）を`displayed_move`の先頭に追加します。
     5.  `format_dict`の`mission`キーには`displayed_mission`を、`move_name`キーには`displayed_move`を設定します。

     確認事項:
     - `PHASE_1_BUTTONS`と`PHASE_2_MOVES`の定数が`missions.py`から正しくインポートされていることを確認してください。
     - `config/button_challenge.toml`の`display_format`で`label1`が`{mission}`を、`label2`が`{move_name}`を使用していることを前提とします。
     - Phase1ではボタンガイド（`label1`）のみが表示され、ムーブ行（`label2`）は表示されないこと。
     - Phase2ではムーブ行（`label2`）のみが表示され、ボタンガイド（`label1`）は表示されないこと。

     期待する出力: `update_display_with_mission`関数が修正された`src/gui.py`の更新内容と、変更点の詳細を説明するMarkdown形式のレポート。
     ```

2. ラップタイムの算出とデバッグ表示 [Issue #10](../issue-notes/10.md)
   - 最初の小さな一歩: `src/main.py`の`main`関数で`state["all_mission_start_time"]`を初期化し、`main_loop`内で全ミッションサイクル開始時に時刻を記録、全ミッション成功時にラップタイムを計算してコンソールにデバッグ出力する。
   - Agent実行プロンプ:
     ```
     対象ファイル: `src/main.py`

     実行内容: `src/main.py`を修正し、全ミッションサイクルにおけるラップタイムを計測・表示する機能を実装してください。
     1.  `main`関数内の`state`オブジェクトの初期化時に、`"all_mission_start_time": None`を追加してください。
     2.  `main_loop`関数内で、`check_and_update_mission`の呼び出し直後に、`on_all_mission_green`が`False`で`mission_index`が`0`であるなど、全ミッションサイクルが開始されることを検出する適切なタイミングで、`state["all_mission_start_time"]`が`None`であれば、現在の時刻（ミリ秒単位）を`state["all_mission_start_time"]`に記録してください。
     3.  `check_and_update_mission`の返り値である`on_all_mission_green`が`True`になったとき（全ミッションが成功したとき）、`state["all_mission_start_time"]`が`None`でなければ、現在の時刻との差分を計算して`lap_time`（ミリ秒単位）を算出し、コンソールに`"Lap Time: [lap_time]ms"`の形式でデバッグ出力してください。その後、`state["all_mission_start_time"]`を`None`にリセットしてください。
     時刻の取得には`time.time() * 1000`を使用するため、`time`モジュールをインポートしてください。

     確認事項:
     - `state`オブジェクト内の`all_mission_start_time`が正しく初期化、記録、リセットされることを確認してください。
     - 全ミッションサイクル開始と終了のタイミングが正確に検出され、ラップタイムが正しく計測されること。
     - `time`モジュールが適切にインポートされていること。

     期待する出力: `main`関数および`main_loop`関数が修正された`src/main.py`の更新内容と、変更点の詳細を説明するMarkdown形式のレポート。
     ```

3. コンボ表示機能の初期実装（データ管理とデバッグ出力） [Issue #15](../issue-notes/15.md)
   - 最初の小さな一歩: `src/main.py`の`state`にコンボ関連のメンバーを追加し、`src/missions.py`の`check_and_update_mission`関数内でミッション成功・失敗時、および全ミッション成功時にコンボ数を更新・リセットし、デバッグ出力を行う。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/missions.py`と`src/main.py`

     実行内容: コンボ表示機能の初期実装として、以下の修正を行ってください。
     1.  `src/main.py`の`main`関数内にある`state`オブジェクトの初期化時に、`"current_combo": 0`, `"max_combo_in_lap": 0`, `"lifetime_max_combo": 0`を追加してください。
     2.  `src/missions.py`内の`check_and_update_mission`関数を修正し、ミッションが成功（green）したときに、`state["current_combo"]`をインクリメントしてください。同時に、`state["max_combo_in_lap"]`と`state["lifetime_max_combo"]`を`state["current_combo"]`と比較して最大値を更新してください。
     3.  ミッションが失敗（red判定）した場合、`state["current_combo"]`を`0`にリセットしてください。
     4.  `on_all_mission_green`（全ミッションが成功し、ラップが終了したとき）の場合、`state["current_combo"]`と`state["max_combo_in_lap"]`を`0`にリセットしてください。
     5.  `check_and_update_mission`関数内で、`current_combo`、`max_combo_in_lap`、`lifetime_max_combo`の現在値をデバッグ目的でコンソールにprintする処理を、ミッション成功時または失敗時に追加してください。

     確認事項:
     - `state`オブジェクトが`main.py`と`missions.py`間で適切に共有・更新されることを確認してください。
     - コンボのインクリメント、リセット、最大値更新のロジックが期待通りに動作すること。
     - デバッグ出力が適切に行われ、コンボ数の変化が確認できること。

     期待する出力: `src/main.py`と`src/missions.py`が修正された更新内容と、変更点の詳細を説明するMarkdown形式のレポート。

---
Generated at: 2026-02-01 07:04:44 JST
