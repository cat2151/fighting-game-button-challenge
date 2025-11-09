Last updated: 2025-11-10

# Development Status

## 現在のIssues
- [Issue #10](../issue-notes/10.md)では、失敗判定の厳格化とミッションごとのタイマー計測の基礎が実装され、現在のフレーム数や最速、ヒストグラムの中心値などが表示可能になり、上達を可視化する基盤が整いました。
- [Issue #16](../issue-notes/16.md)では、30択のミッションにおける反応時間と実戦での2択状況とのギャップを埋めるため、ランダム待ち時間のある2択モードの導入が検討されており、具体的な仕様イメージがブレインストーミングされています。
- [Issue #15](../issue-notes/15.md)では、ミッションの連続成功（コンボ）を可視化し、プレイヤーの達成感を向上させることを目的としており、コンボ数、最大ヒット数、歴代最大ヒット数の表示方法が検討されています。

## 次の一手候補
1. [Issue #10](../issue-notes/10.md) ラップタイムの算出と表示の実現
   - 最初の小さな一歩: `on_all_mission_start` 関数を新規作成し、`main_loop`内でミッションが全てリセットされ次の周が始まるタイミングで呼び出し、`all_mission_start_time`を記録する処理を実装する。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/main.py`, `src/gui.py`

     実行内容:
     1. `src/main.py` 内に `on_all_mission_start` 関数を新規作成する。この関数は引数として `state` オブジェクトを受け取り、`state.all_mission_start_time` に現在の時刻（`time.time()`）を記録する。
     2. `src/main.py` の `main_loop` 関数内で、全てのミッションが成功し、次のミッションサイクルが始まる（またはリセットされる）直前に `on_all_mission_start(state)` を呼び出す箇所を探す。これは `initialize_mission_sets` の後や `on_all_mission_green` と関連するロジック周辺になるはず。
     3. `src/gui.py` 内の `GuiState` クラスに `all_mission_start_time = None` を追加し、`initialize_state` 関数で初期化する。

     確認事項:
     *   `state` オブジェクトが `main_loop` 内で適切に管理・更新されていることを確認する。
     *   `on_all_mission_start` が、ユーザーが1周のミッションを完了し、次の周が始まるまさにそのタイミングで1度だけ呼び出されることを保証する。
     *   既存のミッション進行ロジックや表示ロジックに影響を与えないことを確認する。

     期待する出力: `src/main.py` と `src/gui.py` が上記の変更内容で更新された差分。
     ```

2. [Issue #15](../issue-notes/15.md) コンボ表示の最初の実装
   - 最初の小さな一歩: `on_green` 関数内で、現在のコンボヒット数を`combo_hit_count`として管理し、mission success時に`combo_hit_count`をインクリメントし、GUIに表示する。Red判定時に`combo_hit_count`をリセットする。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/main.py`, `src/gui.py`, `config/button_challenge.toml`

     実行内容:
     1. `src/gui.py` の `GuiState` クラスに `combo_hit_count = 0` を追加し、`initialize_state` で初期化する。
     2. `src/main.py` の `on_green` 関数内で、ミッション成功時に `state.combo_hit_count` を1増やす。
     3. `src/main.py` の `on_red` 関数内で、ミッション失敗時に `state.combo_hit_count` を0にリセットする。
     4. `config/button_challenge.toml` の `[display_format]` セクションに `label_combo = "combo:{combo_hit_count}"` のような新しい表示フォーマットを追加し、`src/main.py` の `update_display_with_mission` 関数でこれをGUIに表示できるようにする。

     確認事項:
     *   `on_green` と `on_red` がそれぞれ正しいタイミングで呼び出されていることを確認する。
     *   GUIへの表示が既存の表示と競合しないようにレイアウトを考慮する。
     *   `combo_hit_count` の初期化とリセットが正しく機能することを確認する。

     期待する出力: `src/main.py`, `src/gui.py`, `config/button_challenge.toml` が上記の変更内容で更新された差分。
     ```

3. [Issue #16](../issue-notes/16.md) 2択モードの基本ロジック検討
   - 最初の小さな一歩: `config/button_challenge.toml` に「2択モード」を有効にする設定（例: `two_choice_mode = false`）を追加し、`src/configs.py` でその設定を読み込めるようにする。
   - Agent実行プロンプト:
     ```
     対象ファイル: `config/button_challenge.toml`, `src/configs.py`, `src/main.py`

     実行内容:
     1. `config/button_challenge.toml` に `two_choice_mode = false` を追加する。
     2. `src/configs.py` の `load_game_configuration` 関数と `load_all_configs` 関数で `two_choice_mode` の設定を読み込み、戻り値に含めるように変更する。デフォルト値は `false` とする。
     3. `src/main.py` の `main` 関数と `main_loop` 関数で、この `two_choice_mode` の値を受け取れるように引数を追加する。

     確認事項:
     *   `two_choice_mode` の値がアプリケーション全体で正しく伝搬されることを確認する。
     *   既存のミッション読み込みロジックや表示ロジックに影響を与えないことを確認する。
     *   `toml` の読み込み処理が既存の他の設定（`lever_toml` など）と競合しないことを確認する。

     期待する出力: `config/button_challenge.toml`, `src/configs.py`, `src/main.py` が上記の変更内容で更新された差分。

---
Generated at: 2025-11-10 08:01:25 JST
