Last updated: 2026-02-06

# Development Status

## 現在のIssues
- プレイヤーの上達をスコアで可視化する [Issue #10](../issue-notes/10.md) の実装が進行中で、失敗判定の厳格化は完了しました。
- ミッションごとのタイマー計測が実装され、現在は全ミッションを1周するラップタイムの算出と表示に向けた検討を進めています。
- その他、2択モードの検討 [Issue #16](../issue-notes/16.md) やコンボ表示の検討 [Issue #15](../issue-notes/15.md) がオープン状態です。

## 次の一手候補
1. [Issue #10](../issue-notes/10.md) ラップタイムの算出と表示（全ミッション1周のタイム計測）
   - 最初の小さな一歩: 全てのミッションが開始されるタイミングを特定し、その開始時刻を記録する `on_all_mission_start` 関数とそのロジックを実装する。
   - Agent実行プロンプ:
     ```
     対象ファイル: `src/main.py`, `src/missions.py`

     実行内容: 全てのミッションが始まる前に一度だけ実行される `on_all_mission_start` 関数を新設し、その中で全ミッション周回の開始時刻を記録する `all_mission_start_time` (state変数) を初期化・設定してください。`main_loop` の適切な箇所からこの関数を呼び出すように変更してください。

     確認事項: `on_all_mission_start` がゲーム開始時または全ミッション完了後の次の周回開始時に一度だけ呼ばれることを確認してください。既存の `mission_start_time` と `all_mission_start_time` が混同しないように注意してください。

     期待する出力: `src/main.py` または関連ファイルに `on_all_mission_start` 関数と `all_mission_start_time` の追加、および `main_loop` からの呼び出しの変更。
     ```

2. [Issue #15](../issue-notes/15.md) コンボ数の可視化（ミッション成功時にコンボ数をprint）
   - 最初の小さな一歩: ミッション成功時 (`on_green` 処理内) に、現在のコンボ数をカウントするロジックを導入し、コンソールに `print` する。コンボは成功で増加、失敗でリセットと定義する。
   - Agent実行プロンプ:
     ```
     対象ファイル: `src/main.py`, `src/gui.py`, `src/missions.py`

     実行内容: ミッション成功時 (`on_green` 処理内) に、現在のコンボ数を管理する変数 (例: `current_combo`) を導入し、成功するとインクリメント、ミッション失敗時に0にリセットするロジックを追加してください。そして、`on_green` の最後に `f"Combo: {current_combo}"` の形式でコンボ数をコンソールに `print` してください。

     確認事項: `on_green` が呼ばれるタイミングと、コンボカウントの増減が適切に行われることを確認してください。失敗時のリセットロジックが正しく機能することを確認してください。

     期待する出力: `src/main.py` または関連ファイルに `current_combo` 変数の導入と管理ロジック、`on_green` 内でのコンボ数 `print` 処理の追加。
     ```

3. [Issue #16](../issue-notes/16.md) 2択モードの導入準備
   - 最初の小さな一歩: `config/button_challenge.toml` に2択モードを有効にする設定項目を追加し、`src/configs.py` でその設定を読み込めるようにする。
   - Agent実行プロンプ:
     ```
     対象ファイル: `config/button_challenge.toml`, `src/configs.py`, `src/main.py`

     実行内容: `config/button_challenge.toml` に `enable_two_choice_mode = false` という設定項目を追加してください。次に、`src/configs.py` の `load_game_configuration` 関数内でこの `enable_two_choice_mode` の値を読み込み、その値を `src/main.py` の `main` および `main_loop` 関数に渡せるように変更してください。

     確認事項: `toml` から設定が正しく読み込まれ、`main_loop` で `enable_two_choice_mode` の値が利用可能になることを確認してください。既存のゲームロジックに影響を与えないことを確認してください。

     期待する出力: `config/button_challenge.toml` への設定項目追加、`src/configs.py` での読み込みロジック追加、`src/main.py` の `main` および `main_loop` の引数または状態管理に当該設定値が渡される変更。
     ```

---
Generated at: 2026-02-06 07:06:00 JST
