Last updated: 2026-01-04

# Development Status

## 現在のIssues
- [Issue #10](../issue-notes/10.md) では、失敗判定の厳格化と失敗時の成績反映が完了し、現在はミッションごとのタイマー計測とラップタイム算出・表示機能の実装を進めている。
- [Issue #16](../issue-notes/16.md) では30択の反応速度課題に対し2択モードの導入を検討しており、[Issue #15](../issue-notes/15.md) ではコンボ表示で達成感向上を目指している。
- [Issue #20](../issue-notes/20.md) はローカルでのドッグフーディングに着手しており、その他 ([#12](../issue-notes/12.md), [#9](../issue-notes/9.md), [#7](../issue-notes/7.md), [#3](../issue-notes/3.md), [#1](../issue-notes/1.md)) は検討中または塩漬けとなっている。

## 次の一手候補
1. [Issue #10](../issue-notes/10.md) ラップタイムの算出と表示
   - 最初の小さな一歩: `main.py`の`main_loop`内で、全ミッション成功時 (`on_all_mission_green`相当のタイミング) に、`state.mission_times`から合計時間と平均時間を計算し、その結果をGUIのラベルに表示する。ラップタイム計測の開始を示す`all_mission_start_time`を`main_loop`の開始時と全ミッションクリア時にリセットする処理も追加する。
   - Agent実行プロンプ:
     ```
     対象ファイル: `src/main.py`, `src/gui.py`

     実行内容:
     1. `src/main.py`の`main_loop`関数内で、状態管理を行う`state`オブジェクト（またはそれに相当する変数）に`all_mission_start_time`という新しいメンバを追加し、これを初期化（例えば`time.time()`）する処理を、`main_loop`の開始時と全ミッションクリア時（`on_all_mission_green`相当のロジックが実行される箇所）にそれぞれ追加してください。
     2. 全ミッションクリア時に、`state.mission_times`（ミッションごとの経過時間が格納されているリスト）から合計時間と平均時間をミリ秒単位で計算してください。
     3. 計算した合計時間と平均時間を、`src/gui.py`の`update_display_with_mission`関数内で表示されるラベル（例: label4の`current_mission_frame_count`の右側）に「Lap:{合計時間:.2f}s Avg:{平均時間:.2f}s」のような形式で追加表示するように修正してください。既存のフレーム数表示との兼ね合いも考慮し、見やすい位置を検討してください。

     確認事項:
     - `state`オブジェクトがどのように管理されているか、その構造とライフサイクルを確認してください。
     - `state.mission_times`がどのタイミングでリセット・更新されるかを確認してください。
     - `src/gui.py`の`update_display_with_mission`関数がどのように引数を受け取り、UIを更新しているかを確認し、新しい表示要素を追加しても既存のレイアウトが崩れないように配慮してください。
     - 時間計測には`time.time()`を使用していることを前提とします。

     期待する出力:
     `src/main.py`と`src/gui.py`の変更箇所を示すコードブロック。
     変更後のコードが、ラップタイムと平均時間をUIに表示できるようになっていること。
     ```

2. [Issue #16](../issue-notes/16.md) 2択モードの実装検討
   - 最初の小さな一歩: `config/button_challenge.toml`に`challenge_mode = "default"`という設定を追加し、`src/configs.py`でこの設定を読み込めるようにする。デフォルトは"default"だが、将来的に"2_choices"などが指定できるよう、文字列として読み込む。
   - Agent実行プロンプト:
     ```
     対象ファイル: `config/button_challenge.toml`, `src/configs.py`

     実行内容:
     1. `config/button_challenge.toml`の`[display_format]`セクションの下、または既存の`challenge_phase`設定の近くに、`challenge_mode = "default"`という新しいキーバリューペアを追加してください。
     2. `src/configs.py`の`load_game_configuration`関数および`load_all_configs`関数を修正し、`challenge_mode`の値を読み込み、その値を`load_game_configuration`の戻り値に追加してください。`challenge_mode`は文字列として扱われ、デフォルト値は"default"とします。

     確認事項:
     - `config/button_challenge.toml`の既存の構造を崩さないように新しい設定を追加してください。
     - `src/configs.py`内で既存のtoml読み込みロジックとの整合性を保ち、新しい設定が正しくパースされることを確認してください。
     - `load_game_configuration`の戻り値の順番が変わる場合、呼び出し元への影響を最小限にするように注意してください。

     期待する出力:
     `config/button_challenge.toml`と`src/configs.py`の変更箇所を示すコードブロック。
     変更後のコードが`challenge_mode`設定を正しく読み込めるようになっていること。
     ```

3. [Issue #15](../issue-notes/15.md) コンボ表示を試す
   - 最初の小さな一歩: `src/main.py`内の`main_loop`関数で、ミッション成功時(`on_green`相当のタイミング)に、現在のコンボ数をカウントし、それをデバッグ用にコンソールにprintする処理を追加する。コンボは「REDが発生せずに連続でGREENになった回数」とし、REDが発生したら0にリセットされるシンプルなロジックとする。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/main.py`

     実行内容:
     1. `src/main.py`の`main_loop`関数内で、現在のコンボ数を保持するための変数（例: `current_combo_count`）を初期化（0）してください。この変数は`main_loop`のローカル変数または`state`オブジェクトのメンバとして管理することを検討してください。
     2. `check_and_update_mission`関数からの戻り値（またはその後の処理）でミッションが「GREEN」（成功）と判定された場合、`current_combo_count`をインクリメントしてください。
     3. `check_and_update_mission`関数からの戻り値（またはその後の処理）でミッションが「RED」（失敗、ノーカンではない）と判定された場合、`current_combo_count`を0にリセットしてください。
     4. `current_combo_count`が更新されるたびに、その値をデバッグ用にコンソールにprintするようにしてください。

     確認事項:
     - `check_and_update_mission`関数がどのようにミッションの結果（GREEN/RED/ノーカン）を返しているか、またはその結果をどのように判断できるかを確認してください。
     - `current_combo_count`変数のスコープとライフサイクルが適切であることを確認してください。
     - 既存のロジックに影響を与えないように注意してください。

     期待する出力:
     `src/main.py`の変更箇所を示すコードブロック。
     変更後のコードが、ミッション成功時にコンボ数をカウントし、失敗時にリセットし、その値をコンソールにprintできるようになっていること。
     ```

---
Generated at: 2026-01-04 07:04:13 JST
