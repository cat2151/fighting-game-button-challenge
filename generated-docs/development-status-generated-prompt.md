Last updated: 2025-12-02

# 開発状況生成プロンプト（開発者向け）

## 生成するもの：
- 現在openされているissuesを3行で要約する
- 次の一手の候補を3つlistする
- 次の一手の候補3つそれぞれについて、極力小さく分解して、その最初の小さな一歩を書く

## 生成しないもの：
- 「今日のissue目標」などuserに提案するもの
  - ハルシネーションの温床なので生成しない
- ハルシネーションしそうなものは生成しない（例、無価値なtaskや新issueを勝手に妄想してそれをuserに提案する等）
- プロジェクト構造情報（来訪者向け情報のため、別ファイルで管理）

## 「Agent実行プロンプト」生成ガイドライン：
「Agent実行プロンプト」作成時は以下の要素を必ず含めてください：

### 必須要素
1. **対象ファイル**: 分析/編集する具体的なファイルパス
2. **実行内容**: 具体的な分析や変更内容（「分析してください」ではなく「XXXファイルのYYY機能を分析し、ZZZの観点でmarkdown形式で出力してください」）
3. **確認事項**: 変更前に確認すべき依存関係や制約
4. **期待する出力**: markdown形式での結果や、具体的なファイル変更

### Agent実行プロンプト例

**良い例（上記「必須要素」4項目を含む具体的なプロンプト形式）**:
```
対象ファイル: `.github/workflows/translate-readme.yml`と`.github/workflows/call-translate-readme.yml`

実行内容: 対象ファイルについて、外部プロジェクトから利用する際に必要な設定項目を洗い出し、以下の観点から分析してください：
1) 必須入力パラメータ（target-branch等）
2) 必須シークレット（GEMINI_API_KEY）
3) ファイル配置の前提条件（README.ja.mdの存在）
4) 外部プロジェクトでの利用時に必要な追加設定

確認事項: 作業前に既存のworkflowファイルとの依存関係、および他のREADME関連ファイルとの整合性を確認してください。

期待する出力: 外部プロジェクトがこの`call-translate-readme.yml`を導入する際の手順書をmarkdown形式で生成してください。具体的には：必須パラメータの設定方法、シークレットの登録手順、前提条件の確認項目を含めてください。
```

**避けるべき例**:
- callgraphについて調べてください
- ワークフローを分析してください
- issue-noteの処理フローを確認してください

## 出力フォーマット：
以下のMarkdown形式で出力してください：

```markdown
# Development Status

## 現在のIssues
[以下の形式で3行でオープン中のissuesを要約。issue番号を必ず書く]
- [1行目の説明]
- [2行目の説明]
- [3行目の説明]

## 次の一手候補
1. [候補1のタイトル。issue番号を必ず書く]
   - 最初の小さな一歩: [具体的で実行可能な最初のアクション]
   - Agent実行プロンプト:
     ```
     対象ファイル: [分析/編集する具体的なファイルパス]

     実行内容: [具体的な分析や変更内容を記述]

     確認事項: [変更前に確認すべき依存関係や制約]

     期待する出力: [markdown形式での結果や、具体的なファイル変更の説明]
     ```

2. [候補2のタイトル。issue番号を必ず書く]
   - 最初の小さな一歩: [具体的で実行可能な最初のアクション]
   - Agent実行プロンプト:
     ```
     対象ファイル: [分析/編集する具体的なファイルパス]

     実行内容: [具体的な分析や変更内容を記述]

     確認事項: [変更前に確認すべき依存関係や制約]

     期待する出力: [markdown形式での結果や、具体的なファイル変更の説明]
     ```

3. [候補3のタイトル。issue番号を必ず書く]
   - 最初の小さな一歩: [具体的で実行可能な最初のアクション]
   - Agent実行プロンプト:
     ```
     対象ファイル: [分析/編集する具体的なファイルパス]

     実行内容: [具体的な分析や変更内容を記述]

     確認事項: [変更前に確認すべき依存関係や制約]

     期待する出力: [markdown形式での結果や、具体的なファイル変更の説明]
     ```
```


# 開発状況情報
- 以下の開発状況情報を参考にしてください。
- Issue番号を記載する際は、必ず [Issue #番号](../issue-notes/番号.md) の形式でMarkdownリンクとして記載してください。

## プロジェクトのファイル一覧
- .editorconfig
- .github/actions-tmp/.github/workflows/call-callgraph.yml
- .github/actions-tmp/.github/workflows/call-daily-project-summary.yml
- .github/actions-tmp/.github/workflows/call-issue-note.yml
- .github/actions-tmp/.github/workflows/call-translate-readme.yml
- .github/actions-tmp/.github/workflows/callgraph.yml
- .github/actions-tmp/.github/workflows/check-recent-human-commit.yml
- .github/actions-tmp/.github/workflows/daily-project-summary.yml
- .github/actions-tmp/.github/workflows/issue-note.yml
- .github/actions-tmp/.github/workflows/translate-readme.yml
- .github/actions-tmp/.github_automation/callgraph/codeql-queries/callgraph.ql
- .github/actions-tmp/.github_automation/callgraph/codeql-queries/codeql-pack.lock.yml
- .github/actions-tmp/.github_automation/callgraph/codeql-queries/qlpack.yml
- .github/actions-tmp/.github_automation/callgraph/config/example.json
- .github/actions-tmp/.github_automation/callgraph/docs/callgraph.md
- .github/actions-tmp/.github_automation/callgraph/presets/callgraph.js
- .github/actions-tmp/.github_automation/callgraph/presets/style.css
- .github/actions-tmp/.github_automation/callgraph/scripts/analyze-codeql.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/callgraph-utils.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/check-codeql-exists.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/check-node-version.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/common-utils.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/copy-commit-results.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/extract-sarif-info.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/find-process-results.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/generate-html-graph.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/generateHTML.cjs
- .github/actions-tmp/.github_automation/check_recent_human_commit/scripts/check-recent-human-commit.cjs
- .github/actions-tmp/.github_automation/project_summary/docs/daily-summary-setup.md
- .github/actions-tmp/.github_automation/project_summary/prompts/development-status-prompt.md
- .github/actions-tmp/.github_automation/project_summary/prompts/project-overview-prompt.md
- .github/actions-tmp/.github_automation/project_summary/scripts/ProjectSummaryCoordinator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/development/DevelopmentStatusGenerator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/development/GitUtils.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/development/IssueTracker.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/generate-project-summary.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/CodeAnalyzer.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectAnalysisOrchestrator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectDataCollector.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectDataFormatter.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectOverviewGenerator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/shared/BaseGenerator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/shared/FileSystemUtils.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/shared/ProjectFileUtils.cjs
- .github/actions-tmp/.github_automation/translate/docs/TRANSLATION_SETUP.md
- .github/actions-tmp/.github_automation/translate/scripts/translate-readme.cjs
- .github/actions-tmp/.gitignore
- .github/actions-tmp/.vscode/settings.json
- .github/actions-tmp/LICENSE
- .github/actions-tmp/README.ja.md
- .github/actions-tmp/README.md
- .github/actions-tmp/_config.yml
- .github/actions-tmp/generated-docs/callgraph.html
- .github/actions-tmp/generated-docs/callgraph.js
- .github/actions-tmp/generated-docs/development-status-generated-prompt.md
- .github/actions-tmp/generated-docs/development-status.md
- .github/actions-tmp/generated-docs/project-overview-generated-prompt.md
- .github/actions-tmp/generated-docs/project-overview.md
- .github/actions-tmp/generated-docs/style.css
- .github/actions-tmp/googled947dc864c270e07.html
- .github/actions-tmp/issue-notes/10.md
- .github/actions-tmp/issue-notes/11.md
- .github/actions-tmp/issue-notes/12.md
- .github/actions-tmp/issue-notes/13.md
- .github/actions-tmp/issue-notes/14.md
- .github/actions-tmp/issue-notes/15.md
- .github/actions-tmp/issue-notes/16.md
- .github/actions-tmp/issue-notes/17.md
- .github/actions-tmp/issue-notes/18.md
- .github/actions-tmp/issue-notes/19.md
- .github/actions-tmp/issue-notes/2.md
- .github/actions-tmp/issue-notes/20.md
- .github/actions-tmp/issue-notes/21.md
- .github/actions-tmp/issue-notes/22.md
- .github/actions-tmp/issue-notes/23.md
- .github/actions-tmp/issue-notes/24.md
- .github/actions-tmp/issue-notes/25.md
- .github/actions-tmp/issue-notes/26.md
- .github/actions-tmp/issue-notes/27.md
- .github/actions-tmp/issue-notes/28.md
- .github/actions-tmp/issue-notes/29.md
- .github/actions-tmp/issue-notes/3.md
- .github/actions-tmp/issue-notes/30.md
- .github/actions-tmp/issue-notes/4.md
- .github/actions-tmp/issue-notes/7.md
- .github/actions-tmp/issue-notes/8.md
- .github/actions-tmp/issue-notes/9.md
- .github/actions-tmp/package-lock.json
- .github/actions-tmp/package.json
- .github/actions-tmp/src/main.js
- .github/workflows/call-daily-project-summary.yml
- .github/workflows/call-issue-note.yml
- .github/workflows/call-translate-readme.yml
- .gitignore
- .pylintrc
- .vscode/settings.json
- LICENSE
- README.ja.md
- README.md
- _config.yml
- button_challenge.bat
- config/alias.toml
- config/button_challenge.toml
- config/button_names.toml
- config/lever_names.toml
- config/mission.toml
- generated-docs/project-overview-generated-prompt.md
- googled947dc864c270e07.html
- issue-notes/10.md
- issue-notes/11.md
- issue-notes/12.md
- issue-notes/13.md
- issue-notes/14.md
- issue-notes/15.md
- issue-notes/16.md
- issue-notes/2.md
- issue-notes/5.md
- issue-notes/8.md
- requirements.txt
- src/check_playing_game.py
- src/configs.py
- src/get_window_info.py
- src/gui.py
- src/gui_utils.py
- src/joystick.py
- src/main.py
- src/missions.py
- src/utils.py
- tests/test_amplify_missions_left_right.py
- tests/test_format_mission_string.py
- tests/test_get_pressed_buttons.py
- tests/test_is_no_count_case.py

## 現在のオープンIssues
## [Issue #16](../issue-notes/16.md): 2択モードを試すか、整理して検討する
[issue-notes/16.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/16.md)

...
ラベル: 
--- issue-notes/16.md の内容 ---

```markdown
# issue 2択モードを試すか、整理して検討する #16
[issues #16](https://github.com/cat2151/fighting-game-button-challenge/issues/16)

# これまでの課題
- 現状自己ベストが29フレ、ヒストグラム中心が40フレ
    - 「猶予26フレのドライブインパクト返しが絶対成功しない」ということ
    - トレモの簡易練習インパクト返しで安定して成功しているので、一見すると矛盾がある
- 分析
    - 30択だから
    - 「日本語を読む時間」のフレーム数が長いから
    - 「インパクト漏れを待ち構えていたら、実際漏れたのが見えた。インパクト返しする」は、日本語を読まずに一瞬で反応できるから
    - 実戦は2択付近に狭まるときは26フレ反応もできる
    - なので26フレ反応成功を体験できるモードができるか？を検証データ取るとよさげ

# 対策案
- 2択モードを試す
    - メリット
        - ドライブインパクト返し成功26フレ等のわかりやすい数字が出せそう
    - 仕様イメージ、1秒で2択が表示され、
        - 次の1秒～2秒のランダム時間の待ちのあと、2択のどっちかがランダムで光って、それを何フレで入力できたかを記録し、26フレ以内安定を目指す
    - 実装方式、ひとまず、tomlで指定したときのみ特殊mode、で試すつもり
- 注意
    - ランダム秒数がマスト、1秒かっきりにはできない
        - 理由
            - 1秒かっきりだと、50%で、1フレなどのありえない数字が出せてしまう
- 課題、ランダム待ち時間でも、投機的に押してしまえば、30択より高い確率で、10フレなどの練習として意味ない（練習モチベの悪影響になる）数字は出せてしまう、と考える
    - 対策、なので最速フレーム表示はせず、ヒストグラム中央を集計して表示すべし
        - ほしいのは、そこで、25フレなど、普段の40フレよりも短いデータが取れることで、
        - より普段の40フレの根拠を得て、説明（30択だから時間かかる）
        - がしやすくなることなので

```

## [Issue #15](../issue-notes/15.md): コンボ表示を試す
[issue-notes/15.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/15.md)

...
ラベル: 
--- issue-notes/15.md の内容 ---

```markdown
# issue コンボ表示を試す #15
[issues #15](https://github.com/cat2151/fighting-game-button-challenge/issues/15)

# これまでの課題
- redが頻発しても、redなしで（コンボで）playできても、報酬が変わらない

# 対策案
- コンボを可視化し、達成感upとし、報酬とする
    - コンボとは、redで0hitに戻り、greenで増えて、1周ごとに0 resetされる
    - max hit とは、1周のなかでのmaxで、1周ごとに0 resetされる
    - 歴代max hitとは、resetされないmax
- playerの心理想定、「よしmission 1周でmax 10hit combo出た、次はmax 11hit comboを目指そう」
- コンボとmax hitは、on greenでひとまずprintする
- 歴代max hitは、1周ごとにひとまずprintする
- 1周ごとに、その周のコンボ数をlistにaddし、ヒストグラムの中心を出す
    - 既存のヒストグラムと揃えて楽をする
        - fncに切り分けて流用がよさげ

↑あとでやる

```

## [Issue #12](../issue-notes/12.md): 訪れたuserがGitHub慣れしていない場合の補助ドキュメントを用意するか、案を洗い出して整理する
[issue-notes/12.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/12.md)...
ラベル: 
--- issue-notes/12.md の内容 ---

```markdown
# issue 訪れたuserがGitHub慣れしていない場合の補助ドキュメントを用意するか、案を洗い出して整理する #12
[issues #12](https://github.com/cat2151/fighting-game-button-challenge/issues/12)

# 起こり得ることをざっくり列挙する
- cloneの概念を知らない（userはアプリをdownloadしたい）
- cloneのかわりにzip downloadがあるのを知らない
- batを実行するのを知らない → OK、README記載済み
- bat実行しエラー。pythonを知らない、installしていない
- pythonのinstall方法が多数あり混乱する → 例えば公式のinstallerの方法を提示する、例えば「AIにきいてね」を誘導する
- pythonにpathが通っていない → 例えば公式installerのinstall設定でpathを通すをonにすることを提示する、例えば「AIにきいてね」を誘導する
- 応急で手でpathを通すとき、cmd前提の「set PATH=～」をChatGPTが提案したが、起動したのがPowerShellで、エラーになり混乱する
- modulesのinstallをしていない → requirements.txt を書く

# コンセプト
- 開発者の作業コストを最小化する
- userの導入コストは青天井でもあまり気にしないことに
- これだと「今のままでいい。対応不要」がひとまず結論にはなる

# コンセプトを元に検討中
- releaseを用意は、後回し。日々commitしているのでその度にtagとかreleaseとかは手間。GitHub Actionsで全自動にできるなら考慮してもいい。知識不足。一度学べばよい。ひとまず保留。
- agentに上記とcodeを元に生成させると、開発者の作業コストを下げつつ、userの導入コストも下げられる可能性がある。試すかも。ひとまず保留。
- 今すぐREADMEを充実させるか？いいえ。ほかの優先タスクをやる

```

## [Issue #10](../issue-notes/10.md): scoreで上達をわかるようにしたい
[issue-notes/10.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/10.md)...
ラベル: 優先
--- issue-notes/10.md の内容 ---

```markdown
# issue scoreで上達をわかるようにしたい #10
[issues #10](https://github.com/cat2151/fighting-game-button-challenge/issues/10)

# これまでの課題
- 1つsuccessごとに1pts.獲得
- いくら失敗しても1pts.獲得は同じ
- いくら入力が遅くても1pts.獲得は同じ
- 上達したのかがわからない

# ブレインストーミング
- 失敗が少ないほうが上達。
    - 楽器の練習と同じで、「最初は丁寧にミスなく」「だんだん素早く」
    - 失敗の判定は厳密にやると開発コストが大きいので、シンプルなルールにする
        - `右上` なら、`右上`が「success」、`右`と`上`は「ノーカン」、それ以外は「失敗」
            - `右`と`上`を分解して扱う新定義がtomlに必要な想定
        - `右 + 弱 + 中` なら、`右`と`弱`と`中`とそれらの組み合わせは「ノーカン」、それ以外は「失敗にする」
    - ノーカンや失敗時は、successするまで同じmissionを続ける。楽器の練習と同じ。これは今までどおりなので実装に影響しない。
    - ノーカンは成績に影響しない。失敗は成績に影響する。成績は後述する。
- 入力が素早いほうが上達。
    - 「かかった時間」を、新規mission開始から、successまでのミリ秒、と定義する。
    - 失敗と関連し、失敗ごとに1000ミリ秒、「かかった時間」を増やす。
        - これで、スコアは「かかった時間」で一元管理をして、わかりやすくする。
- 成績の表示
    - 成績の表示タイミング。
        - 最初の1周が終わるまでは「ラップタイム計測中」と表示する。
        - missionを全問successした瞬間を1周の区切りとする。
        - 次の1周をする間、さきほどの1周のラップタイムを表示する。
    - 成績の表現。
        - 「かかった時間」の「全missionを1周」の「平均フレーム数」で表現する。10のmissionがあり、「かかった時間」の合計が1000フレームなら、平均は100フレームで、それが表示される成績「あなたの素早さは平均100フレです」となる。
- ラップタイム
    - ラップタイムは伝わりやすいので、目標になりやすい。
- リセット
    - Windowが背面になってから1分経過すると、mission状況とラップタイムはリセットされる。
- 累積score
    - これまでのscoreは累積scoreとして残しておく。クッキークリッカーのように、入力だけで増えるスコアがあるのも楽しい。
- 進め方
    - シンプル優先。漸進的な開発。まず上記を切り分けて実現してゆく。一歩一歩を可視化しながら進めてゆく。
- 実装方式
    - ラップタイムの影響範囲は、mission関連に閉じるとよさげ。例えば、`on_green`で開始時刻を保存、`check_mission_success`で終了時刻を保存して「かかった時間」を算出して保存（かかった時間list にappendすればよいだろう）、`on_all_mission_green`でそれらを総合してラップタイム算出、ができるか検討する。timerは使わずシンプルに実現する。
    - 累積scoreは追加実装不要。既存のscoreの実装をそのまま累積scoreとして扱う。
    - 影響範囲の狭いもの、ミスっても戻しやすいものから、一歩ずつ漸進的に変更してゆく。

# LLMに可視化させる
- プロンプト「上記のブレインストーミング欄について、レビューし、listしてください」
    - → 結果、要約しただけの同じ内容がでてきた → OK。「LLM出力が下振れしたときに検知できる安全装置」として今後もしばらく試すとよさげ

# LLMに可視化させる
- プロンプト「上記のブレインストーミング欄について、一歩ずつ漸進的に実装する場合、どのように進めるか検討し、listしてください」
## 結果
- 1.がおかしい
    - 指示曖昧なことが可視化された
    - → ブレインストーミング欄をなおした
- 登場人物（関数名）がないため、妥当性が可視化されていない
    - プロンプト不足なことが可視化された
    - → プロンプトをなおす
- 壁打ちする
    - 壁打ちとみなす。LLMの生成をみて、ブレインストーミングの不足を修正、のサイクルをまわす
- 次のプロンプトを投げる
    - プロンプト「上記のブレインストーミング欄について、一歩ずつ漸進的に実装する場合、どのように進めるか検討し、listしてください。listには、既存のコードを参照の上、新規関数名、既存関数名を含めてください」
    - 結果、低品質。
        - 「既存のコードを参照の上」を指定しないとハルシネーション。
        - 既存関数へのlinkはついたりつかなかったり。プロンプトで明示してもつかない。
        - 内容が低品質。理解不足で「そこは変更しないやろ」という部分をさわり、ムダに影響範囲を広げることが、毎回あちこちで発生。
    - 試しに「ブレインストーミング欄」の「実装方式」欄を追記してみたが、あまり改善されず。
        - 仮説、contextあふれで、ハルシネーション。
    - どうする？
        - 今のLLMの低性能ぶりにあわせる。
        - まず狭いcontextにしぼり、「ブレインストーミング欄の実装を実現するための一般的な進め方」のlistを生成させる。
            - コードベースとの乖離が大きすぎると根本的にどうしようもないので、それを防止するためコードベースは参照させる。
                - だがそれでも乖離はする。そこは低品質と割り切って、一旦そのままとする。
    - プロンプト「上記のブレインストーミング欄について、一歩ずつ漸進的に実装する場合、どのように進めるか検討し、listしてください。listには、既存のコードを参照の上、新規関数名、既存関数名を含めてください。実際にはその実装では間違いである（ハルシネーションを含む）ため、あとでuser側がlistと違う修正を入れることは、織り込み済みとします。listをmd末尾に追記してください。」
    - md末尾の「あとでやる」欄が消されてしまうので、退避しておく（追記しろ、消すな、などを指示しても消される）
        - 仮説、contextあふれで、LLMの品質が下がっている状態
    - contextあふれが目に付く。
        - 対策、品質の下振れを織り込み済みとし、ある程度userがフォローする。
        - LLMのうまみが減るのは割り切る
        - LLMの用途を「認知負荷を下げること」に割り切り、その方向で使う
        - 認知負荷が下がればよいので、userが認知負荷の低いとこでちょくちょく手をいれるのはOK
            - もし認知負荷の高い「大量の単純チェック作業」等をuserがやる羽目になった場合は、
                - 全体の進め方を見直す

---

## LLM出力 : 実装ステップlist

1. **失敗判定の厳格化**
    - `check_mission_success`（既存）を修正し、「ノーカン」「失敗」「成功」の3値を返すようにする
    - 必要に応じて新規関数 `is_no_count_case` を追加

2. **失敗時の成績反映**
    - `check_and_update_mission`（既存）で「失敗」時に失敗回数をカウントする変数（例: `fail_count`）を追加
    - 失敗時はscoreを増やさず、fail_countのみ加算

3. **missionごとのタイマー計測**
    - `on_green`（既存）でmission開始時刻を記録する（例: 新規変数 `mission_start_time`）
    - `check_mission_success`（既存）で成功時に現在時刻との差分を計算し、「かかった時間list」（例: `mission_times`）にappend

4. **失敗ごとに「かかった時間」を加算**
    - 失敗時、`mission_times`の最新要素に1000msを加算する処理を追加

5. **ラップタイムの算出と表示**
    - `on_all_mission_green`（既存）で`mission_times`の合計・平均を計算し、成績として保存
    - 新規関数 `show_lap_time` でラップタイムをUIに表示

6. **成績表示タイミングの制御**
    - `main_loop`（既存）で「1周目終了時」「次の1周開始前」に成績表示を制御
    - 新規変数 `is_first_lap` で状態管理

7. **リセット処理**
    - `main_loop`または`check_playing_game_and_do_backmost`（既存）で、ウィンドウが背面になってから1分経過したら`mission_times`や成績をリセットする処理を追加

8. **累積scoreの維持**
    - 既存のscore変数を「累積score」としてそのまま残す

# 一歩ずつやる
- プロンプト「1. **失敗判定の厳格化** について、外部設計、内部設計、変更する関数名のlist、引数追加のある関数のlist、新規関数名のlist、を書いてください。tomlの仕様変更もあるはずです。対象tomlの名称と、どう変更するかを書いてください。そこからuserが仕様変更する可能性も織り込み済みとします」

## LLM出力 : 1. 失敗判定の厳格化：設計まとめ

### 外部設計
- missionごとに「成功」「ノーカン」「失敗」を厳密に判定する。
- 例：
  - 指定された入力以外は「失敗」
  - missionによっては「ノーカン」パターンも許容（例：方向キーの一部のみ押下など）

### 内部設計
- 判定ロジックを`check_mission_success`で拡張し、3値（成功/ノーカン/失敗）を返す。
- ノーカン判定用の新規関数`is_no_count_case`を追加。
- 失敗判定の条件をmission定義（toml）で柔軟に指定できるようにする。

### 変更する関数名のリスト
- check_mission_success
- check_and_update_mission（失敗時の処理追加）

### 引数追加のある関数のリスト
- check_mission_success（判定結果の3値化に伴い返り値型や引数の見直しが必要）

### 新規関数名のリスト
- is_no_count_case

### tomlの仕様変更
- 対象toml：missions.toml（またはbutton_challenge.toml等、mission定義ファイル）
- 変更内容例：
  - 各missionに「ノーカン」条件や「失敗」条件を明示的に記述できるフィールドを追加
  - 例：
    ```toml
    [[missions]]
    name = "右上"
    success = ["右上"]
    no_count = ["右", "上"]
    fail = ["左", "下", "左上", ...]
    ```
  - 既存のmission定義に「no_count」「fail」などの新フィールドを追加

---

# 所感
- mission単位は複雑すぎる。そうでなく、`lever_names.toml`に、`[[no_count_names]]`として書いた。
- プロンプト「`lever_names.toml`に、`[[no_count_names]]`として書きました。configs.pyでreadする処理を書いてください」
- readする処理を書かせて、いくつか会話して、`no_count_names`がいくつか伝播するところまで書いた
- 状況がわかりづらいぞ
- 可視化させられるか試す
- プロンプト「1.失敗判定の厳格化 はどこまで進捗しましたか？可視化してください」

## LLM出力 : 進捗可視化 : 1. 失敗判定の厳格化

### 現状まとめ（2025-06-06時点）

- 設計・仕様
    - 3値判定（成功/ノーカン/失敗）導入方針は決定済み。
    - mission単位のtoml拡張案は複雑すぎるため、lever_names.tomlの[[no_count_names]]方式に仕様変更。
- 実装
    - lever_names.tomlに[[no_count_names]]を記述済み。
    - configs.pyでno_count_namesをreadする処理は実装済み。
    - no_count_namesが一部ロジックに伝播し始めている。
    - check_mission_successの3値化やis_no_count_caseの本格実装は未着手または進行中。

| 項目                      | 状態         | 備考                                               |
|---------------------------|--------------|----------------------------------------------------|
| 3値判定の設計             | 完了         | 仕様・設計方針は明確                               |
| toml仕様の決定            | 完了         | mission単位→lever_names.tomlのno_count_namesに変更 |
| toml記述                  | 完了         | lever_names.tomlに[[no_count_names]]記述済み        |
| configs.pyでのread実装    | 完了         | no_count_namesの読み込み処理あり                   |
| no_count_namesの伝播      | 一部完了     | いくつかの箇所で利用開始                           |
| 判定ロジックの本実装      | 未着手/途中  | check_mission_successの3値化/is_no_count_case等     |

---

次のアクション例：
- check_mission_successの3値化実装
- is_no_count_caseの新規実装
- 既存ロジックの「ノーカン」対応への修正

（この進捗可視化はmd末尾に自動追記されたものです）

---

# 所感
- 可視化できてると思う。userの認知負荷を下げることができてる。素晴らしい。この手は今後も利用しよう。

# is_no_count_case のアルゴリズムを類推させる
- プロンプトは、以下のブロックを投げる

## is_no_count_case のアルゴリズム検討
- greenでない場合に、is_no_count_case を実行して判定します
- is_no_count_case 内部の処理
    - missionを元に、all_no_count_names を生成します
        - さらに、all_no_count_names を加工します
            - all_no_count_names をforでまわして
                - no_count_names をforでまわして
                    - 例、no_count_names.success に一致したら
                        - no_count_names.no_count をappendします
- かなり省略して書きましたが類推してみてください

# 結果
- キャッチボールを数回繰り返して、以下を生成させた
```
def is_no_count_case(mission_success, input_name, no_count_names_list):
略（バグってたので）
```

# 所感
- 上記関数のレビューは認知負荷が高い
- ためしに判定例をlistさせた
- ハルシネーションとcontextあふれが発生した
- 今のproject方針から考えると、別の手を試そう
- TDDが使えるケースだ
- TDDさせよう
- test～pyを生成させた
- TDDさせた
- is_no_count_case のtest red、LLM提案の案はミスっていたので、userが正しい案を指摘して修正させた
- is_no_count_case のtest green
- よってno_count_namesの伝播は完了したと判断する
- いくつか実装した。よって、以下も完了したと判断する
    - check_mission_successの3値化実装
    - 既存ロジックの「ノーカン」対応への修正
- プロンプト「1.失敗判定の厳格化 はどこまで進捗しましたか？可視化してください。もし完了であれば改善の提案として重要度の高い上位2つを書いてください、それをみてそこまでやるかを判断します」

---

## LLM出力 : 1. 失敗判定の厳格化：進捗可視化（2025-06-07時点）

| 項目                      | 状態         | 備考                                               |
|---------------------------|--------------|----------------------------------------------------|
| 3値判定の設計             | 完了         | 仕様・設計方針は明確                               |
| toml仕様の決定            | 完了         | mission単位→lever_names.tomlのno_count_namesに変更 |
| toml記述                  | 完了         | lever_names.tomlに[[no_count_names]]記述済み        |
| configs.pyでのread実装    | 完了         | no_count_namesの読み込み処理あり                   |
| no_count_namesの伝播      | 完了         | 主要ロジックに伝播済み                             |
| 判定ロジックの本実装      | 完了         | check_mission_successの3値化/is_no_count_case等     |
| テスト                    | 完了         | TDDでtest_is_no_count_case.py作成・green           |

### 総評
- 「失敗判定の厳格化」は設計・実装・テストまで完了しています。
- 仕様変更（mission単位→lever_names.toml）も反映済み。
- 既存ロジックの「ノーカン」対応も完了。

### 改善提案（重要度上位2つ）
1. ノーカン・失敗パターンの柔軟性向上
    - 現状はlever_names.tomlベースで一括管理だが、missionごとに細かく例外や特殊パターンを指定できる仕組みを検討。
    - 例：特定missionのみ独自のno_countやfail条件を持たせる。
2. 判定理由の可視化・デバッグ支援
    - 判定結果（成功/ノーカン/失敗）だけでなく、「なぜその判定になったか」をログやUIで確認できるようにする。
    - テストや運用時の認知負荷をさらに下げる。

---

# 所感
- その2つはprojectの方向性からみて不要。
- 2. **失敗時の成績反映** に進もう
- プロンプト「2. **失敗時の成績反映** について、外部設計、内部設計、変更する関数名のlist、引数追加のある関数のlist、新規関数名のlist、を書いてください」
- 結果、ハルシネーションだらけで使い物にならなかった。仮説、contextあふれ。対策、プロンプトを見直して、以下とした。
- プロンプト：
    - 2. **失敗時の成績反映** について、外部設計、内部設計、変更する関数名のlist、引数追加のある関数のlist、新規関数名のlist、を書いてください。
    - 観点は以下としてください。そして、結果を10.mdの末尾に追記してください。
        - 2. **失敗時の成績反映**
            - `check_and_update_mission`（既存）で「失敗」時に失敗回数をカウントする変数（例: `fail_count`）を追加
            - 失敗時はscoreを増やさず、fail_countのみ加算

---

## LLM出力： 2. **失敗時の成績反映** 外部設計・内部設計

### 外部設計
- ミッション失敗時に成績へ「失敗回数」を反映する。
- 失敗時はscore（成功回数）は増やさず、fail_count（失敗回数）のみ加算する。

### 内部設計
- `check_and_update_mission` 関数にて、失敗時に `fail_count` を加算する処理を追加。
- 成績管理用のデータ構造（例: dictやクラス）に `fail_count` を追加。
- 失敗時の判定ロジックを明確化し、score加算処理と分離。

### 変更する関数名のリスト
- `check_and_update_mission`

### 引数追加のある関数のリスト
- 必要に応じて、成績管理用データ構造を受け渡す関数（例: `check_and_update_mission` など）

### 新規関数名のリスト
- 失敗回数の初期化や取得用の関数（例: `reset_fail_count`, `get_fail_count` など、必要に応じて追加）

# 上記をagent実装させた
- agent実装はスムーズにできていた記憶
- userミス。以降を、うっかり、一歩ずつでなく、まとめて雑にやってしまった
- 指示が雑 → agent実装が雑 → userがagentに指示してリファクタリングさせた → 成功
- 途中で挙動に不満（mission成功時に、次のmissionが表示されてほしいが、そうなってない。以前そうなっていたかは失念） → その場でagentに修正させた
- それも、指示が雑 → agent実装が雑 → userがagentに指示してリファクタリングさせた → 成功
- 「2. **失敗時の成績反映**」は完了した。
- 「3. **missionごとのタイマー計測**」に進む
- と思ったが先に、今回のfail回数可視化の感触が予想よりよかったので、それを踏まえ、以下を先に実現する：
    - 現mission開始からのフレーム数を、fail回数の右に表示。場所などはあとで揉み
- できた、agentに実装させ、レビューして修正させた
- さらにminをやりましょう
- できた、agentに実装させ、レビューして修正させた
- さらに最頻値までやりましょう
- ヒストグラムの最頻ビンの中心について、agentに実装させ、レビューして修正させた
- ヒストグラムの最頻ビンの中心について、過去何回を集計対象にするかtomlで設定できるよう、agentに実装させ、レビューして修正させた
- さて「3. **missionごとのタイマー計測**」に進むか？
    - 先に今のをドッグフーディングしたほうがいいかも
- ドッグフーディング結果
    - mission1周（すべて成功）のラップタイムがほしい
- 「3. **missionごとのタイマー計測**」に進もう

# プロンプト案
- missionごとにかかった時間を計測したいです。コードベースを元に、以下の設計を検討し、変更対象関数名と内容をlistしてください
- 3. **missionごとのタイマー計測**
    - mission開始時刻を記録する
        - stateに新規メンバ `mission_start_time` を追加実装する
            - main_loop で初期化する
        - mission開始時、`mission_start_time` を記録する
            - main_loopと、on_greenそれぞれから、新規関数 `on_mission_start` を呼び出し、そこで記録する
    - かかった時間を記録する
        - 現在時刻と `mission_start_time` の差分を計算し、かかった時間、とする
        - かかった時間listに、それをappendする
        - かかった時間listとは、stateの`mission_times` である
            - mission_timesは、main_loopで初期化する
    - DEBUG用に、かかった時間listを、on_greenにてprintする

# 結果
- agentに設計をlistさせ、レビューして修正させ、実装させ、レビューして修正させた
    - 途中、横断的にpyをみるのが漏れることがあり、「コードベースから自分で探してください」など明示的に指示した
- DEBUG printはできた、想定通り、60フレ以内なら0.9などの表示になっている、多少見づらいのはひとまずOKとする
- 課題、今回追加した`mission_times` は、これまでフレーム数で計測していた `prev_success_frame_counts` と内容が丸かぶりなことに気づいた
    - 分析
        - メリット
            - フレーム数より正確な時間計測ができる
            - 今回追加した `on_mission_start`は全体の構造改善に寄与している
        - デメリット
            - DRYでない、ムダ、重複、複雑
        - 分析
            - 削って消すのはいつでもできる、それほど大きな問題はない
            - むしろ `mission_times`側に統合するのもアリな可能性がある
    - 対策、もう少し実装を進めてトータルの運用データをとるまで様子見

# 次の、4. の要否を検討する
- 4. **失敗ごとに「かかった時間」を加算**
    - 失敗時、`mission_times`の最新要素に1000msを加算する処理を追加
- これ省略、後回し、がよいと判断する
    - なぜなら、1000msという数字が恣意的である
    - そもそもガチャプレイしても、このプレイのルールだと、いい成績は出ないので、
        - 1000msのペナルティの効果が相対的に低い、と考える
        - ペナルティの効果が相対的に高いのは、例えば2択にしてバクチで片方を入力して100msec(6フレ)などウデマエと違う不適切なタイムを出せるようなルール
            - 現在もいわばカウンティングすれば可能だが、30個カウンティングは対象プレイヤー層はできない想定（少なくとも自分はできない）なので、スコープ外とする

# 次の、5. を検討して整理する
## これまで
- 5. **ラップタイムの算出と表示**
    - `on_all_mission_green`（既存）で`mission_times`の合計・平均を計算し、成績として保存
    - 新規関数 `show_lap_time` でラップタイムをUIに表示
## これからの案
- 5. **ラップタイムの算出と表示**
    - `on_all_mission_green`（既存）で`mission_times`の合計・平均を計算し、`lap_time`と`average`として保存
    - DEBUG用に 新規関数 `show_lap_time` でラップタイムをprint
## 検討
- 2.で仕様追加、実装、検証、の結果、状況が変化している
- それを受けて、`on_all_mission_start`を用意して、そこで`all_mission_start_time`を記録し、
    - `on_all_mission_green`で、`lap_time`をprint、がよさげ
    - 想定は、30問で30秒前後、想定プレイヤー心理は「よし30秒を切った、あと1秒縮めよう」など
    - そのほうがシンプルそう
    - そのあと運用データとって、lap_timeをlistし、averageやヒストグラムをDEBUG printするのもよさげ
- その方向でagentに実装させて運用データとろう

↑あとでやる

```

## [Issue #9](../issue-notes/9.md): 破壊的変更時、エンドユーザ作業負荷が高い
# どういうこと？
- tomlの仕様変更があったとき、
    - 開発者は仕様変更時に書き直してるからいいけど、
        - それをcloneして使ってるエンドユーザは、
            - 手で書き直す羽目になって、手間だと思う
# どうする？
- 塩漬け。理由は #1 ...
ラベル: 
--- issue-notes/9.md の内容 ---

```markdown

```

## [Issue #7](../issue-notes/7.md): dark modeがほしい
# これまでの課題
- 自分がdark modeで各種アプリを使っているのに、これが白なので、「dark modeがほしい」となった
# 案
- toml設定。dark modeを、on / off / デフォ（systemに追従して自動on/off） の3択
- まずsystemに追従だけで十分そう、自分の他repositoryでやってたはず（コマンドパレットアプリで）、参考にするつもり...
ラベル: 
--- issue-notes/7.md の内容 ---

```markdown

```

## [Issue #6](../issue-notes/6.md): 「右 + 強 + 必」だけでなくその上に「SA2」という表示がほしい
# これまでの課題
- 「右 + 強 + 必」という文言を見てボタンを押すのは、見る認知負荷が高い
- そこで、「SA2」 という表示があれば、それを見てボタンを押せてよさげ
# 案
- moveとbuttonを両方表示、つまり `SA2`と`右 + 強 + 必`を両方表示
    - 表示行数を増やす
    - 用途は、`SA2`を見ただけで`右 + 強 + 必`ボタンを押す練習用
        - `右 + 強 + 必`を表示するのはあくまでヒント用
            - 場合によっては`右 + 強 + 必`はdelayで表示するのもよさげ、そのほうが練習になるかも、tomlでo...
ラベル: 
--- issue-notes/6.md の内容 ---

```markdown

```

## [Issue #4](../issue-notes/4.md): mission successしたかどうかがわかりづらいし、手応えが薄いため達成感が薄く、再playのモチベが低い
# 言い換えると
- mission successしたかどうか？わかりやすくすれば、以下のメリットが期待できる
    - 手応えup、達成感up、再playのモチベup
# ブレインストーミング
- green
    - テスト駆動開発を基準に、success時にgreen iconを1秒表示
- 効果音
    - 適切な音は手応えupになる、ただしmuteで使う用途が多い（自分は）、なので優先度は低い
- ご褒美画像
    - display image 1sec py （別アプリ）とeasyに連動できるつもりなので実装して検証するとよさげ
        - 例、successご...
ラベル: 
--- issue-notes/4.md の内容 ---

```markdown

```

## [Issue #3](../issue-notes/3.md): もっと実戦に近く「SA3が溜まってる自分に、相手が飛び込んできたので、ワンボタンSA3」などが映像でわかると嬉しい
# 補足
- mission提示画像 : SA3が溜まってる自分に、相手が飛び込んできた
- mission成功画像 : SA3が相手にhitした
# 実現可能性
- ほぼゼロ
- なぜ？
- 画像を現実的な時間で用意する方法がない
- testや検証ができないのなら実装はできない
# どうする？
- 塩漬け
...
ラベル: 
--- issue-notes/3.md の内容 ---

```markdown

```

## [Issue #1](../issue-notes/1.md): 使える時間が限られておりメンテの時間が取れない
# 対策
- 都度トリアージする
- 自分のやりたいissueを優先する
...
ラベル: 
--- issue-notes/1.md の内容 ---

```markdown

```

## ドキュメントで言及されているファイルの内容
### .github/actions-tmp/issue-notes/10.md
```md
# issue callgraph を他projectから使いやすくする #10
[issues #10](https://github.com/cat2151/github-actions/issues/10)

# ブレインストーミング
- 洗い出し
    - 他projectから使う場合の問題を洗い出す、今見えている範囲で、手早く、このnoteに可視化する
    - 洗い出したものは、一部は別issueに切り分ける
- close条件
    - [x] まずは4つそれぞれを個別のdirに切り分けてtest greenとなること、とするつもり
        - 別issueに切り分けるつもり
- 切り分け
    - 別dirに切り分ける
        - [x] 課題、`codeql-queries/` が `.github/` 配下にある。対策、`.github_automation/callgraph/codeql-queries/` とする
        - [x] 課題、scriptも、`.github/`配下にある。対策、移動する
        - 方法、agentを試し、ハルシネーションで時間が取られるなら人力に切り替える
- test
    - local WSL + act でtestする
- 名前
    - [x] 課題、名前 enhanced が不要。対策、名前から enhanced を削除してymlなどもそれぞれ同期して修正すべし
- docs
    - [x] call導入手順を書く

# 状況
- 実際に他project tonejs-mml-to-json リポジトリにて使うことができている
    - その際に発生した運用ミスは、
        - call導入手順のメンテを行ったので、改善された、と判断する

# closeとする

```

### issue-notes/10.md
```md
# issue scoreで上達をわかるようにしたい #10
[issues #10](https://github.com/cat2151/fighting-game-button-challenge/issues/10)

# これまでの課題
- 1つsuccessごとに1pts.獲得
- いくら失敗しても1pts.獲得は同じ
- いくら入力が遅くても1pts.獲得は同じ
- 上達したのかがわからない

# ブレインストーミング
- 失敗が少ないほうが上達。
    - 楽器の練習と同じで、「最初は丁寧にミスなく」「だんだん素早く」
    - 失敗の判定は厳密にやると開発コストが大きいので、シンプルなルールにする
        - `右上` なら、`右上`が「success」、`右`と`上`は「ノーカン」、それ以外は「失敗」
            - `右`と`上`を分解して扱う新定義がtomlに必要な想定
        - `右 + 弱 + 中` なら、`右`と`弱`と`中`とそれらの組み合わせは「ノーカン」、それ以外は「失敗にする」
    - ノーカンや失敗時は、successするまで同じmissionを続ける。楽器の練習と同じ。これは今までどおりなので実装に影響しない。
    - ノーカンは成績に影響しない。失敗は成績に影響する。成績は後述する。
- 入力が素早いほうが上達。
    - 「かかった時間」を、新規mission開始から、successまでのミリ秒、と定義する。
    - 失敗と関連し、失敗ごとに1000ミリ秒、「かかった時間」を増やす。
        - これで、スコアは「かかった時間」で一元管理をして、わかりやすくする。
- 成績の表示
    - 成績の表示タイミング。
        - 最初の1周が終わるまでは「ラップタイム計測中」と表示する。
        - missionを全問successした瞬間を1周の区切りとする。
        - 次の1周をする間、さきほどの1周のラップタイムを表示する。
    - 成績の表現。
        - 「かかった時間」の「全missionを1周」の「平均フレーム数」で表現する。10のmissionがあり、「かかった時間」の合計が1000フレームなら、平均は100フレームで、それが表示される成績「あなたの素早さは平均100フレです」となる。
- ラップタイム
    - ラップタイムは伝わりやすいので、目標になりやすい。
- リセット
    - Windowが背面になってから1分経過すると、mission状況とラップタイムはリセットされる。
- 累積score
    - これまでのscoreは累積scoreとして残しておく。クッキークリッカーのように、入力だけで増えるスコアがあるのも楽しい。
- 進め方
    - シンプル優先。漸進的な開発。まず上記を切り分けて実現してゆく。一歩一歩を可視化しながら進めてゆく。
- 実装方式
    - ラップタイムの影響範囲は、mission関連に閉じるとよさげ。例えば、`on_green`で開始時刻を保存、`check_mission_success`で終了時刻を保存して「かかった時間」を算出して保存（かかった時間list にappendすればよいだろう）、`on_all_mission_green`でそれらを総合してラップタイム算出、ができるか検討する。timerは使わずシンプルに実現する。
    - 累積scoreは追加実装不要。既存のscoreの実装をそのまま累積scoreとして扱う。
    - 影響範囲の狭いもの、ミスっても戻しやすいものから、一歩ずつ漸進的に変更してゆく。

# LLMに可視化させる
- プロンプト「上記のブレインストーミング欄について、レビューし、listしてください」
    - → 結果、要約しただけの同じ内容がでてきた → OK。「LLM出力が下振れしたときに検知できる安全装置」として今後もしばらく試すとよさげ

# LLMに可視化させる
- プロンプト「上記のブレインストーミング欄について、一歩ずつ漸進的に実装する場合、どのように進めるか検討し、listしてください」
## 結果
- 1.がおかしい
    - 指示曖昧なことが可視化された
    - → ブレインストーミング欄をなおした
- 登場人物（関数名）がないため、妥当性が可視化されていない
    - プロンプト不足なことが可視化された
    - → プロンプトをなおす
- 壁打ちする
    - 壁打ちとみなす。LLMの生成をみて、ブレインストーミングの不足を修正、のサイクルをまわす
- 次のプロンプトを投げる
    - プロンプト「上記のブレインストーミング欄について、一歩ずつ漸進的に実装する場合、どのように進めるか検討し、listしてください。listには、既存のコードを参照の上、新規関数名、既存関数名を含めてください」
    - 結果、低品質。
        - 「既存のコードを参照の上」を指定しないとハルシネーション。
        - 既存関数へのlinkはついたりつかなかったり。プロンプトで明示してもつかない。
        - 内容が低品質。理解不足で「そこは変更しないやろ」という部分をさわり、ムダに影響範囲を広げることが、毎回あちこちで発生。
    - 試しに「ブレインストーミング欄」の「実装方式」欄を追記してみたが、あまり改善されず。
        - 仮説、contextあふれで、ハルシネーション。
    - どうする？
        - 今のLLMの低性能ぶりにあわせる。
        - まず狭いcontextにしぼり、「ブレインストーミング欄の実装を実現するための一般的な進め方」のlistを生成させる。
            - コードベースとの乖離が大きすぎると根本的にどうしようもないので、それを防止するためコードベースは参照させる。
                - だがそれでも乖離はする。そこは低品質と割り切って、一旦そのままとする。
    - プロンプト「上記のブレインストーミング欄について、一歩ずつ漸進的に実装する場合、どのように進めるか検討し、listしてください。listには、既存のコードを参照の上、新規関数名、既存関数名を含めてください。実際にはその実装では間違いである（ハルシネーションを含む）ため、あとでuser側がlistと違う修正を入れることは、織り込み済みとします。listをmd末尾に追記してください。」
    - md末尾の「あとでやる」欄が消されてしまうので、退避しておく（追記しろ、消すな、などを指示しても消される）
        - 仮説、contextあふれで、LLMの品質が下がっている状態
    - contextあふれが目に付く。
        - 対策、品質の下振れを織り込み済みとし、ある程度userがフォローする。
        - LLMのうまみが減るのは割り切る
        - LLMの用途を「認知負荷を下げること」に割り切り、その方向で使う
        - 認知負荷が下がればよいので、userが認知負荷の低いとこでちょくちょく手をいれるのはOK
            - もし認知負荷の高い「大量の単純チェック作業」等をuserがやる羽目になった場合は、
                - 全体の進め方を見直す

---

## LLM出力 : 実装ステップlist

1. **失敗判定の厳格化**
    - `check_mission_success`（既存）を修正し、「ノーカン」「失敗」「成功」の3値を返すようにする
    - 必要に応じて新規関数 `is_no_count_case` を追加

2. **失敗時の成績反映**
    - `check_and_update_mission`（既存）で「失敗」時に失敗回数をカウントする変数（例: `fail_count`）を追加
    - 失敗時はscoreを増やさず、fail_countのみ加算

3. **missionごとのタイマー計測**
    - `on_green`（既存）でmission開始時刻を記録する（例: 新規変数 `mission_start_time`）
    - `check_mission_success`（既存）で成功時に現在時刻との差分を計算し、「かかった時間list」（例: `mission_times`）にappend

4. **失敗ごとに「かかった時間」を加算**
    - 失敗時、`mission_times`の最新要素に1000msを加算する処理を追加

5. **ラップタイムの算出と表示**
    - `on_all_mission_green`（既存）で`mission_times`の合計・平均を計算し、成績として保存
    - 新規関数 `show_lap_time` でラップタイムをUIに表示

6. **成績表示タイミングの制御**
    - `main_loop`（既存）で「1周目終了時」「次の1周開始前」に成績表示を制御
    - 新規変数 `is_first_lap` で状態管理

7. **リセット処理**
    - `main_loop`または`check_playing_game_and_do_backmost`（既存）で、ウィンドウが背面になってから1分経過したら`mission_times`や成績をリセットする処理を追加

8. **累積scoreの維持**
    - 既存のscore変数を「累積score」としてそのまま残す

# 一歩ずつやる
- プロンプト「1. **失敗判定の厳格化** について、外部設計、内部設計、変更する関数名のlist、引数追加のある関数のlist、新規関数名のlist、を書いてください。tomlの仕様変更もあるはずです。対象tomlの名称と、どう変更するかを書いてください。そこからuserが仕様変更する可能性も織り込み済みとします」

## LLM出力 : 1. 失敗判定の厳格化：設計まとめ

### 外部設計
- missionごとに「成功」「ノーカン」「失敗」を厳密に判定する。
- 例：
  - 指定された入力以外は「失敗」
  - missionによっては「ノーカン」パターンも許容（例：方向キーの一部のみ押下など）

### 内部設計
- 判定ロジックを`check_mission_success`で拡張し、3値（成功/ノーカン/失敗）を返す。
- ノーカン判定用の新規関数`is_no_count_case`を追加。
- 失敗判定の条件をmission定義（toml）で柔軟に指定できるようにする。

### 変更する関数名のリスト
- check_mission_success
- check_and_update_mission（失敗時の処理追加）

### 引数追加のある関数のリスト
- check_mission_success（判定結果の3値化に伴い返り値型や引数の見直しが必要）

### 新規関数名のリスト
- is_no_count_case

### tomlの仕様変更
- 対象toml：missions.toml（またはbutton_challenge.toml等、mission定義ファイル）
- 変更内容例：
  - 各missionに「ノーカン」条件や「失敗」条件を明示的に記述できるフィールドを追加
  - 例：
    ```toml
    [[missions]]
    name = "右上"
    success = ["右上"]
    no_count = ["右", "上"]
    fail = ["左", "下", "左上", ...]
    ```
  - 既存のmission定義に「no_count」「fail」などの新フィールドを追加

---

# 所感
- mission単位は複雑すぎる。そうでなく、`lever_names.toml`に、`[[no_count_names]]`として書いた。
- プロンプト「`lever_names.toml`に、`[[no_count_names]]`として書きました。configs.pyでreadする処理を書いてください」
- readする処理を書かせて、いくつか会話して、`no_count_names`がいくつか伝播するところまで書いた
- 状況がわかりづらいぞ
- 可視化させられるか試す
- プロンプト「1.失敗判定の厳格化 はどこまで進捗しましたか？可視化してください」

## LLM出力 : 進捗可視化 : 1. 失敗判定の厳格化

### 現状まとめ（2025-06-06時点）

- 設計・仕様
    - 3値判定（成功/ノーカン/失敗）導入方針は決定済み。
    - mission単位のtoml拡張案は複雑すぎるため、lever_names.tomlの[[no_count_names]]方式に仕様変更。
- 実装
    - lever_names.tomlに[[no_count_names]]を記述済み。
    - configs.pyでno_count_namesをreadする処理は実装済み。
    - no_count_namesが一部ロジックに伝播し始めている。
    - check_mission_successの3値化やis_no_count_caseの本格実装は未着手または進行中。

| 項目                      | 状態         | 備考                                               |
|---------------------------|--------------|----------------------------------------------------|
| 3値判定の設計             | 完了         | 仕様・設計方針は明確                               |
| toml仕様の決定            | 完了         | mission単位→lever_names.tomlのno_count_namesに変更 |
| toml記述                  | 完了         | lever_names.tomlに[[no_count_names]]記述済み        |
| configs.pyでのread実装    | 完了         | no_count_namesの読み込み処理あり                   |
| no_count_namesの伝播      | 一部完了     | いくつかの箇所で利用開始                           |
| 判定ロジックの本実装      | 未着手/途中  | check_mission_successの3値化/is_no_count_case等     |

---

次のアクション例：
- check_mission_successの3値化実装
- is_no_count_caseの新規実装
- 既存ロジックの「ノーカン」対応への修正

（この進捗可視化はmd末尾に自動追記されたものです）

---

# 所感
- 可視化できてると思う。userの認知負荷を下げることができてる。素晴らしい。この手は今後も利用しよう。

# is_no_count_case のアルゴリズムを類推させる
- プロンプトは、以下のブロックを投げる

## is_no_count_case のアルゴリズム検討
- greenでない場合に、is_no_count_case を実行して判定します
- is_no_count_case 内部の処理
    - missionを元に、all_no_count_names を生成します
        - さらに、all_no_count_names を加工します
            - all_no_count_names をforでまわして
                - no_count_names をforでまわして
                    - 例、no_count_names.success に一致したら
                        - no_count_names.no_count をappendします
- かなり省略して書きましたが類推してみてください

# 結果
- キャッチボールを数回繰り返して、以下を生成させた
```
def is_no_count_case(mission_success, input_name, no_count_names_list):
略（バグってたので）
```

# 所感
- 上記関数のレビューは認知負荷が高い
- ためしに判定例をlistさせた
- ハルシネーションとcontextあふれが発生した
- 今のproject方針から考えると、別の手を試そう
- TDDが使えるケースだ
- TDDさせよう
- test～pyを生成させた
- TDDさせた
- is_no_count_case のtest red、LLM提案の案はミスっていたので、userが正しい案を指摘して修正させた
- is_no_count_case のtest green
- よってno_count_namesの伝播は完了したと判断する
- いくつか実装した。よって、以下も完了したと判断する
    - check_mission_successの3値化実装
    - 既存ロジックの「ノーカン」対応への修正
- プロンプト「1.失敗判定の厳格化 はどこまで進捗しましたか？可視化してください。もし完了であれば改善の提案として重要度の高い上位2つを書いてください、それをみてそこまでやるかを判断します」

---

## LLM出力 : 1. 失敗判定の厳格化：進捗可視化（2025-06-07時点）

| 項目                      | 状態         | 備考                                               |
|---------------------------|--------------|----------------------------------------------------|
| 3値判定の設計             | 完了         | 仕様・設計方針は明確                               |
| toml仕様の決定            | 完了         | mission単位→lever_names.tomlのno_count_namesに変更 |
| toml記述                  | 完了         | lever_names.tomlに[[no_count_names]]記述済み        |
| configs.pyでのread実装    | 完了         | no_count_namesの読み込み処理あり                   |
| no_count_namesの伝播      | 完了         | 主要ロジックに伝播済み                             |
| 判定ロジックの本実装      | 完了         | check_mission_successの3値化/is_no_count_case等     |
| テスト                    | 完了         | TDDでtest_is_no_count_case.py作成・green           |

### 総評
- 「失敗判定の厳格化」は設計・実装・テストまで完了しています。
- 仕様変更（mission単位→lever_names.toml）も反映済み。
- 既存ロジックの「ノーカン」対応も完了。

### 改善提案（重要度上位2つ）
1. ノーカン・失敗パターンの柔軟性向上
    - 現状はlever_names.tomlベースで一括管理だが、missionごとに細かく例外や特殊パターンを指定できる仕組みを検討。
    - 例：特定missionのみ独自のno_countやfail条件を持たせる。
2. 判定理由の可視化・デバッグ支援
    - 判定結果（成功/ノーカン/失敗）だけでなく、「なぜその判定になったか」をログやUIで確認できるようにする。
    - テストや運用時の認知負荷をさらに下げる。

---

# 所感
- その2つはprojectの方向性からみて不要。
- 2. **失敗時の成績反映** に進もう
- プロンプト「2. **失敗時の成績反映** について、外部設計、内部設計、変更する関数名のlist、引数追加のある関数のlist、新規関数名のlist、を書いてください」
- 結果、ハルシネーションだらけで使い物にならなかった。仮説、contextあふれ。対策、プロンプトを見直して、以下とした。
- プロンプト：
    - 2. **失敗時の成績反映** について、外部設計、内部設計、変更する関数名のlist、引数追加のある関数のlist、新規関数名のlist、を書いてください。
    - 観点は以下としてください。そして、結果を10.mdの末尾に追記してください。
        - 2. **失敗時の成績反映**
            - `check_and_update_mission`（既存）で「失敗」時に失敗回数をカウントする変数（例: `fail_count`）を追加
            - 失敗時はscoreを増やさず、fail_countのみ加算

---

## LLM出力： 2. **失敗時の成績反映** 外部設計・内部設計

### 外部設計
- ミッション失敗時に成績へ「失敗回数」を反映する。
- 失敗時はscore（成功回数）は増やさず、fail_count（失敗回数）のみ加算する。

### 内部設計
- `check_and_update_mission` 関数にて、失敗時に `fail_count` を加算する処理を追加。
- 成績管理用のデータ構造（例: dictやクラス）に `fail_count` を追加。
- 失敗時の判定ロジックを明確化し、score加算処理と分離。

### 変更する関数名のリスト
- `check_and_update_mission`

### 引数追加のある関数のリスト
- 必要に応じて、成績管理用データ構造を受け渡す関数（例: `check_and_update_mission` など）

### 新規関数名のリスト
- 失敗回数の初期化や取得用の関数（例: `reset_fail_count`, `get_fail_count` など、必要に応じて追加）

# 上記をagent実装させた
- agent実装はスムーズにできていた記憶
- userミス。以降を、うっかり、一歩ずつでなく、まとめて雑にやってしまった
- 指示が雑 → agent実装が雑 → userがagentに指示してリファクタリングさせた → 成功
- 途中で挙動に不満（mission成功時に、次のmissionが表示されてほしいが、そうなってない。以前そうなっていたかは失念） → その場でagentに修正させた
- それも、指示が雑 → agent実装が雑 → userがagentに指示してリファクタリングさせた → 成功
- 「2. **失敗時の成績反映**」は完了した。
- 「3. **missionごとのタイマー計測**」に進む
- と思ったが先に、今回のfail回数可視化の感触が予想よりよかったので、それを踏まえ、以下を先に実現する：
    - 現mission開始からのフレーム数を、fail回数の右に表示。場所などはあとで揉み
- できた、agentに実装させ、レビューして修正させた
- さらにminをやりましょう
- できた、agentに実装させ、レビューして修正させた
- さらに最頻値までやりましょう
- ヒストグラムの最頻ビンの中心について、agentに実装させ、レビューして修正させた
- ヒストグラムの最頻ビンの中心について、過去何回を集計対象にするかtomlで設定できるよう、agentに実装させ、レビューして修正させた
- さて「3. **missionごとのタイマー計測**」に進むか？
    - 先に今のをドッグフーディングしたほうがいいかも
- ドッグフーディング結果
    - mission1周（すべて成功）のラップタイムがほしい
- 「3. **missionごとのタイマー計測**」に進もう

# プロンプト案
- missionごとにかかった時間を計測したいです。コードベースを元に、以下の設計を検討し、変更対象関数名と内容をlistしてください
- 3. **missionごとのタイマー計測**
    - mission開始時刻を記録する
        - stateに新規メンバ `mission_start_time` を追加実装する
            - main_loop で初期化する
        - mission開始時、`mission_start_time` を記録する
            - main_loopと、on_greenそれぞれから、新規関数 `on_mission_start` を呼び出し、そこで記録する
    - かかった時間を記録する
        - 現在時刻と `mission_start_time` の差分を計算し、かかった時間、とする
        - かかった時間listに、それをappendする
        - かかった時間listとは、stateの`mission_times` である
            - mission_timesは、main_loopで初期化する
    - DEBUG用に、かかった時間listを、on_greenにてprintする

# 結果
- agentに設計をlistさせ、レビューして修正させ、実装させ、レビューして修正させた
    - 途中、横断的にpyをみるのが漏れることがあり、「コードベースから自分で探してください」など明示的に指示した
- DEBUG printはできた、想定通り、60フレ以内なら0.9などの表示になっている、多少見づらいのはひとまずOKとする
- 課題、今回追加した`mission_times` は、これまでフレーム数で計測していた `prev_success_frame_counts` と内容が丸かぶりなことに気づいた
    - 分析
        - メリット
            - フレーム数より正確な時間計測ができる
            - 今回追加した `on_mission_start`は全体の構造改善に寄与している
        - デメリット
            - DRYでない、ムダ、重複、複雑
        - 分析
            - 削って消すのはいつでもできる、それほど大きな問題はない
            - むしろ `mission_times`側に統合するのもアリな可能性がある
    - 対策、もう少し実装を進めてトータルの運用データをとるまで様子見

# 次の、4. の要否を検討する
- 4. **失敗ごとに「かかった時間」を加算**
    - 失敗時、`mission_times`の最新要素に1000msを加算する処理を追加
- これ省略、後回し、がよいと判断する
    - なぜなら、1000msという数字が恣意的である
    - そもそもガチャプレイしても、このプレイのルールだと、いい成績は出ないので、
        - 1000msのペナルティの効果が相対的に低い、と考える
        - ペナルティの効果が相対的に高いのは、例えば2択にしてバクチで片方を入力して100msec(6フレ)などウデマエと違う不適切なタイムを出せるようなルール
            - 現在もいわばカウンティングすれば可能だが、30個カウンティングは対象プレイヤー層はできない想定（少なくとも自分はできない）なので、スコープ外とする

# 次の、5. を検討して整理する
## これまで
- 5. **ラップタイムの算出と表示**
    - `on_all_mission_green`（既存）で`mission_times`の合計・平均を計算し、成績として保存
    - 新規関数 `show_lap_time` でラップタイムをUIに表示
## これからの案
- 5. **ラップタイムの算出と表示**
    - `on_all_mission_green`（既存）で`mission_times`の合計・平均を計算し、`lap_time`と`average`として保存
    - DEBUG用に 新規関数 `show_lap_time` でラップタイムをprint
## 検討
- 2.で仕様追加、実装、検証、の結果、状況が変化している
- それを受けて、`on_all_mission_start`を用意して、そこで`all_mission_start_time`を記録し、
    - `on_all_mission_green`で、`lap_time`をprint、がよさげ
    - 想定は、30問で30秒前後、想定プレイヤー心理は「よし30秒を切った、あと1秒縮めよう」など
    - そのほうがシンプルそう
    - そのあと運用データとって、lap_timeをlistし、averageやヒストグラムをDEBUG printするのもよさげ
- その方向でagentに実装させて運用データとろう

↑あとでやる

```

### .github/actions-tmp/issue-notes/12.md
```md
# issue project-summary を他projectから使いやすくする #12
[issues #12](https://github.com/cat2151/github-actions/issues/12)

# 保留、別projectでの検証待ちのもの
- promptsをcall側ymlで指定可能にする
  - 保留の理由
    - YAGNI原則
      - 現状の共通workflow側のpromptsで問題ないうちは、保留とする
        - そのままで使える可能性が高い見込み
      - 検証が必要
      - 別promptsを実際に書く必要が出たときに、追加実装をする
# 課題、 docs/ をメンテする
- 対象は、 daily-summary-setup.md
- call-daily-project-summary.yml の導入手順を書く
- どうする？
  - 次の日次バッチでagent用promptを生成させる
- 結果
  - 生成させた
  - 導入手順をメンテさせた
  - 人力でさらにメンテした
  - これでOKと判断する。
  - あとは必要に応じてissue起票すればよい、今すぐのissue起票は不要（YAGNI原則）、と判断する

# closeとする

```

### issue-notes/12.md
```md
# issue 訪れたuserがGitHub慣れしていない場合の補助ドキュメントを用意するか、案を洗い出して整理する #12
[issues #12](https://github.com/cat2151/fighting-game-button-challenge/issues/12)

# 起こり得ることをざっくり列挙する
- cloneの概念を知らない（userはアプリをdownloadしたい）
- cloneのかわりにzip downloadがあるのを知らない
- batを実行するのを知らない → OK、README記載済み
- bat実行しエラー。pythonを知らない、installしていない
- pythonのinstall方法が多数あり混乱する → 例えば公式のinstallerの方法を提示する、例えば「AIにきいてね」を誘導する
- pythonにpathが通っていない → 例えば公式installerのinstall設定でpathを通すをonにすることを提示する、例えば「AIにきいてね」を誘導する
- 応急で手でpathを通すとき、cmd前提の「set PATH=～」をChatGPTが提案したが、起動したのがPowerShellで、エラーになり混乱する
- modulesのinstallをしていない → requirements.txt を書く

# コンセプト
- 開発者の作業コストを最小化する
- userの導入コストは青天井でもあまり気にしないことに
- これだと「今のままでいい。対応不要」がひとまず結論にはなる

# コンセプトを元に検討中
- releaseを用意は、後回し。日々commitしているのでその度にtagとかreleaseとかは手間。GitHub Actionsで全自動にできるなら考慮してもいい。知識不足。一度学べばよい。ひとまず保留。
- agentに上記とcodeを元に生成させると、開発者の作業コストを下げつつ、userの導入コストも下げられる可能性がある。試すかも。ひとまず保留。
- 今すぐREADMEを充実させるか？いいえ。ほかの優先タスクをやる

```

### .github/actions-tmp/issue-notes/15.md
```md
# issue project_summary scripts cjs を分解し、できるだけ1ファイル200行未満にし、agentによるメンテをしやすくする #15
[issues #15](https://github.com/cat2151/github-actions/issues/15)

# 状況
- agentに、最初の小さな一歩のAgent実行プロンプトを実行させた
- 結果、以下を得た：
    - project_summary_cjs_analysis.md
- どうする？
    - 次の一手をagentに生成させてみる（翌日の日次バッチで自動生成させる）
- 結果
    - 生成させたpromptをレビューした
    - promptを修正した
    - agentに投げた
    - 結果、GitUtils.cjsを切り出しできた
    - それをリファクタリングミスがないかチェックさせた
    - agentによるチェック結果は合格だった
- どうする？
    - 次の一手をagentに生成させてみる（翌日の日次バッチで自動生成させる）
- 結果
    - 生成させたpromptをレビューした
        - promptの対象ファイルから project_summary_cjs_analysis.md が漏れていることがわかったので修正した
    - promptを修正した
    - agentに投げた
    - 結果、FileSystemUtils.cjsを切り出しできた
    - それをリファクタリングミスがないかチェックさせた
    - agentによるチェック結果は合格だった
- どうする？
    - 次の一手をagentに生成させてみる（翌日の日次バッチで自動生成させる）
- 結果
    - 生成させたpromptをレビューした
    - 今回は低品質、NG、と判断した
    - 判断基準は、project_summary_cjs_analysis.md と乖離してしまっている点。今回はハルシネーションを含んだplanである、と判断した
    - 人力でpromptを書き、planさせ、plan結果をレビューし、agentに投げた
    - 結果、CodeAnalyzer.cjsとProjectAnalyzer.cjsを切り出しできた
- どうする？
    - 次の一手をagentに生成させてみる（翌日の日次バッチで自動生成させる）
    - 備考、課題、Geminiに生成させているdocumentは2つある。かなり位置づけが違うものである。
        - projectのソースファイル分析。
        - projectのissues分析。
        - この2つについて、class, cjs, yml まで分割をするかを、あとで検討する。
        - おそらく、class分割どまりとし、ソースファイル分析結果をissues分析の参考資料としてGeminiのcontextに与える改善をする、がよい、と想定しておく。
- 課題、エラーで落ちた。昨日は落ちてない。
    - 原因、昨日のagentのリファクタリング時に、ハルシネーションで、
        - codeが破壊されていた
        - run メソッドが削除されていた
        - 一つ前のrevisionにはrun メソッドがあった
        - ほかにもcode破壊があったのかは不明、調査省略、明日の日次バッチをtestと調査として利用するつもり
- どうする？
    - 単純に一つ前のrevisionからrun メソッドを復活させ、明日の日次バッチをtestと調査として利用する
- 再発防止策は？
    - ノーアイデア。昨日それなりにagentにチェックをさせたはずだが根本的な大きなミスが発生していた。
    - 構文チェックは通っていたが、問題を検知できなかった。
    - チェックが機能していない、あるいは機能として不足している。
    - 分析。変更量が大きかったぶんミスのリスクが増えていた。
    - 対策案。もっと小さく一歩ずつ変更させる。
    - 対策案。リファクタリング時、いきなりメソッド削除をさせない。
        - まず全cjsの全メソッドのlistをさせる。
        - のち、削除対象の重複メソッドのlistをさせる。
        - そして削除planをさせる。
        - のち、削除させる。
        - さらに削除後のメソッドlistをさせる。
        - そして削除しすぎていないかを削除前後のlist比較でチェックさせる。
        - これでrunまで削除してしまうのを防止できるかもしれない。
        - これは人力からみると、おかしな話である。人力なら1つずつ移動をするだけであり、ミスのしようがない。
        - LLMの典型的なハルシネーション問題の一つである、と認識する
- 結果は？
    - test green
    - run メソッドの人力復活は成功した
    - 日次バッチで生成した次の一手のpromptを投げた
    - リファクタリング成功した。ProjectSummaryGenerator を切り出した
- どうする？
    - 次の一手をagentに生成させてみる（agentに投げるpromptを、翌日の日次バッチで自動生成させる）
- 結果
    - 先に、2つのdocument生成を、1つずつ生成できるよう疎結合にリファクタリング、をしたほうがよさそう
    - agentにそれを投げた
    - 成功した、と判断する
    - 課題、`BaseSummaryGenerator.cjs` は、baseの機能と、`ProjectOverviewGenerator.cjs`専用の機能とが混ざっている。
        - baseに集約すべきは、`ProjectSummaryCoordinator.cjs`と`ProjectOverviewGenerator.cjs`とが必ずどちらも使う機能、である、と考える。
        - 対策、明日以降それをagentに投げる
    - `project_summary_cjs_analysis.md` は削除とする。役目が完了した、と判断する。リファクタリング前のソース構造の分析documentであり、今は存在しているとわかりづらくなる。シンプル優先のため削除とする。
- どうする？
    - 次の一手をagentに生成させてみる（agentに投げるpromptを、翌日の日次バッチで自動生成させる）
- 結果
    - test green
    - `BaseSummaryGenerator.cjs` を切り出したのは成功した、と判断する
    - `BaseSummaryGenerator.cjs` を2分割するため、agentにplanさせた
    - レビューした
    - agentに2分割させた
    - レビューした。OKと判断する
- どうする？
    - 次の一手をagentに生成させてみる（agentに投げるpromptを、翌日の日次バッチで自動生成させる）
- 結果
    - test green
    - `BaseSummaryGenerator.cjs` を2分割は成功した、と判断する
    - issue track機能構造をリファクタリングし、以下にする
        - development status generator : baseを継承する
        - issue tracker : 汎用関数群
    - agentに実施させた
    - レビューした。OKと判断する
- どうする？
    - 次の一手をagentに生成させてみる（agentに投げるpromptを、翌日の日次バッチで自動生成させる）
- 結果
    - test green
    - DevelopmentStatusGeneratorとissue trackerのリファクタリングは成功した、と判断する
    - ProjectOverview生成機能のリファクタリングをする
    - agentに実施させた
    - レビューした。OKと判断する
- どうする？
    - 次の一手をagentに生成させてみる（agentに投げるpromptを、翌日の日次バッチで自動生成させる）
- 結果
    - test green
    - ProjectOverview生成機能のリファクタリングは成功した、と判断する
    - 課題、overviewと、developmentStatusとが混在し、dirが読みづらい。
    - 対策、shared/、overview/、development/、の3つのdirに切り分ける
    - agentに分析、planさせ、レビューし、planさせ、実施させた
    - レビューした。OKと判断する
- どうする？
    - 次の一手をagentに生成させてみる（agentに投げるpromptを、翌日の日次バッチで自動生成させる）
- 結果
    - test green
    - shared/、overview/、development/、の3つのdirに切り分けるリファクタリングは成功した、と判断する
    - agentに、agentがメンテしやすいか？の観点からレビューさせた
    - 詳細は割愛
        - `> 最優先で取り組むべきは 設定管理の一元化 と エラーハンドリングの統一 です。これにより、Agentにとって予測可能で理解しやすいコードベースになります。`
        - それは別issueで、設定変更をマストでやるので、OKと判断する
- これでagentによるメンテは十分しやすくなった、と判断する
- closeとする

```

### issue-notes/15.md
```md
# issue コンボ表示を試す #15
[issues #15](https://github.com/cat2151/fighting-game-button-challenge/issues/15)

# これまでの課題
- redが頻発しても、redなしで（コンボで）playできても、報酬が変わらない

# 対策案
- コンボを可視化し、達成感upとし、報酬とする
    - コンボとは、redで0hitに戻り、greenで増えて、1周ごとに0 resetされる
    - max hit とは、1周のなかでのmaxで、1周ごとに0 resetされる
    - 歴代max hitとは、resetされないmax
- playerの心理想定、「よしmission 1周でmax 10hit combo出た、次はmax 11hit comboを目指そう」
- コンボとmax hitは、on greenでひとまずprintする
- 歴代max hitは、1周ごとにひとまずprintする
- 1周ごとに、その周のコンボ数をlistにaddし、ヒストグラムの中心を出す
    - 既存のヒストグラムと揃えて楽をする
        - fncに切り分けて流用がよさげ

↑あとでやる

```

### .github/actions-tmp/issue-notes/16.md
```md
# issue issue-note / project-summary / translate / callgraph をtonejs-mml-to-jsonから呼び出す #16
[issues #16](https://github.com/cat2151/github-actions/issues/16)

# これまでの課題
- issue-note / project-summary / translate / callgraph は、github-actions リポジトリ上ではtest greenである。
- だが他のリポジトリにおいて動作するか？が可視化不足である。

# 対策
- issue-note / project-summary / translate / callgraph をtonejs-mml-to-jsonから呼び出す
- 詳しく
    - まず、現状、tonejs-mml-to-json でその4つのworkflowがどうなっているか、このmdに可視化する
    - 例えば、既に呼び出している、呼び出していない、tonejs-mml-to-jsonにある古いworkflowを呼び出している

# 調査結果
- まず、現状、tonejs-mml-to-json でその4つのworkflowがどうなっているか、このmdに可視化する
    - 結果：
        - issue-note
            - tonejs-mml-to-jsonにある古いworkflowを呼び出している
        - project-summary
            - tonejs-mml-to-jsonにある古いworkflowを呼び出している
        - translate
            - tonejs-mml-to-jsonにある古いworkflowを呼び出している
        - callgraph
            - tonejs-mml-to-jsonにある古いworkflowを呼び出している

# どうする？
- issue-note
    - github-actions リポジトリにある、call-issue-note.yml をcpして使うようにする、まず単純cpして動くかを確認する
- project-summary
    - github-actions リポジトリにある、call-daily-project-summary.yml をcpして使うようにする、まず単純cpして動くかを確認する
- translate
    - github-actions リポジトリにある、call-translate-readme.yml をcpして使うようにする、まず単純cpして動くかを確認する
- callgraph
    - github-actions リポジトリにある、call-callgraph.yml をcpして使うようにする、まず単純cpして動くかを確認する

# 状況
- issue-note
    - tonejs-mml-to-jsonリポジトリにて、test green
    - issue-noteについては当issueのタスクは完了した、と判断する
- project-summary
    - tonejs-mml-to-jsonリポジトリにて、test green
    - project-summaryについては当issueのタスクは完了した、と判断する

# 状況
- translate
    - github-actions リポジトリにある、call-translate-readme.yml をcpして使うようにする、まず単純cpして動くかを確認する
        - 状況
            - 単純cpした
            - ソース机上レビューした。OK
            - トリガーはREADME.ja.mdのcommit
            - testは省略とする
            - もし今後README.ja.mdのcommit時にうまく動作しないとしても、そのとき対処すればOK、と判断する
    - translateについては当issueのタスクは完了した、と判断する

# どうする？
- callgraph
    - github-actions リポジトリにある、call-callgraph.yml をcpして使うようにする、まず単純cpして動くかを確認する

# 結果
- callgraph
    - tonejs-mml-to-jsonリポジトリにて、test red
    - logをみても情報不足なため、まずloggerを修正する
    - 結果、わかった、運用ミス、対象srcの指定の考慮漏れ
    - どうする？
        - 対象srcを指定する。tonejs-mml-to-jsonリポジトリにて進める
    - 結果
        - test green
    - callgraphについては当issueのタスクは完了した、と判断する

# 状況
- github-actions以外のリポジトリとして、
    - tonejs-mml-to-jsonリポジトリにおいて、
        - issue-note / project-summary / translate / callgraph がtest greenとなった。
        - closeできる、と判断する。

# closeとする

```

### issue-notes/16.md
```md
# issue 2択モードを試すか、整理して検討する #16
[issues #16](https://github.com/cat2151/fighting-game-button-challenge/issues/16)

# これまでの課題
- 現状自己ベストが29フレ、ヒストグラム中心が40フレ
    - 「猶予26フレのドライブインパクト返しが絶対成功しない」ということ
    - トレモの簡易練習インパクト返しで安定して成功しているので、一見すると矛盾がある
- 分析
    - 30択だから
    - 「日本語を読む時間」のフレーム数が長いから
    - 「インパクト漏れを待ち構えていたら、実際漏れたのが見えた。インパクト返しする」は、日本語を読まずに一瞬で反応できるから
    - 実戦は2択付近に狭まるときは26フレ反応もできる
    - なので26フレ反応成功を体験できるモードができるか？を検証データ取るとよさげ

# 対策案
- 2択モードを試す
    - メリット
        - ドライブインパクト返し成功26フレ等のわかりやすい数字が出せそう
    - 仕様イメージ、1秒で2択が表示され、
        - 次の1秒～2秒のランダム時間の待ちのあと、2択のどっちかがランダムで光って、それを何フレで入力できたかを記録し、26フレ以内安定を目指す
    - 実装方式、ひとまず、tomlで指定したときのみ特殊mode、で試すつもり
- 注意
    - ランダム秒数がマスト、1秒かっきりにはできない
        - 理由
            - 1秒かっきりだと、50%で、1フレなどのありえない数字が出せてしまう
- 課題、ランダム待ち時間でも、投機的に押してしまえば、30択より高い確率で、10フレなどの練習として意味ない（練習モチベの悪影響になる）数字は出せてしまう、と考える
    - 対策、なので最速フレーム表示はせず、ヒストグラム中央を集計して表示すべし
        - ほしいのは、そこで、25フレなど、普段の40フレよりも短いデータが取れることで、
        - より普段の40フレの根拠を得て、説明（30択だから時間かかる）
        - がしやすくなることなので

```

### .github/actions-tmp/issue-notes/2.md
```md
# issue GitHub Actions「関数コールグラフhtmlビジュアライズ生成」を共通ワークフロー化する #2
[issues #2](https://github.com/cat2151/github-actions/issues/2)


# prompt
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
このymlファイルを、以下の2つのファイルに分割してください。
1. 共通ワークフロー       cat2151/github-actions/.github/workflows/callgraph_enhanced.yml
2. 呼び出し元ワークフロー cat2151/github-actions/.github/workflows/call-callgraph_enhanced.yml
まずplanしてください
```

# 結果
- indent
    - linter？がindentのエラーを出しているがyml内容は見た感じOK
    - テキストエディタとagentの相性問題と判断する
    - 別のテキストエディタでsaveしなおし、テキストエディタをreload
    - indentのエラーは解消した
- LLMレビュー
    - agent以外の複数のLLMにレビューさせる
    - prompt
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
以下の2つのファイルをレビューしてください。最優先で、エラーが発生するかどうかだけレビューしてください。エラー以外の改善事項のチェックをするかわりに、エラー発生有無チェックに最大限注力してください。

--- 共通ワークフロー

# GitHub Actions Reusable Workflow for Call Graph Generation
name: Generate Call Graph

# TODO Windowsネイティブでのtestをしていた名残が残っているので、今後整理していく。今はWSL act でtestしており、Windowsネイティブ環境依存問題が解決した
#  ChatGPTにレビューさせるとそこそこ有用そうな提案が得られたので、今後それをやる予定
#  agentに自己チェックさせる手も、セカンドオピニオンとして選択肢に入れておく

on:
  workflow_call:

jobs:
  check-commits:
    runs-on: ubuntu-latest
    outputs:
      should-run: ${{ steps.check.outputs.should-run }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 50 # 過去のコミットを取得

      - name: Check for user commits in last 24 hours
        id: check
        run: |
          node .github/scripts/callgraph_enhanced/check-commits.cjs

  generate-callgraph:
    needs: check-commits
    if: needs.check-commits.outputs.should-run == 'true'
    runs-on: ubuntu-latest
    permissions:
      contents: write
      security-events: write
      actions: read

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set Git identity
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

      - name: Remove old CodeQL packages cache
        run: rm -rf ~/.codeql/packages

      - name: Check Node.js version
        run: |
          node .github/scripts/callgraph_enhanced/check-node-version.cjs

      - name: Install CodeQL CLI
        run: |
          wget https://github.com/github/codeql-cli-binaries/releases/download/v2.22.1/codeql-linux64.zip
          unzip codeql-linux64.zip
          sudo mv codeql /opt/codeql
          echo "/opt/codeql" >> $GITHUB_PATH

      - name: Install CodeQL query packs
        run: |
          /opt/codeql/codeql pack install .github/codeql-queries

      - name: Check CodeQL exists
        run: |
          node .github/scripts/callgraph_enhanced/check-codeql-exists.cjs

      - name: Verify CodeQL Configuration
        run: |
          node .github/scripts/callgraph_enhanced/analyze-codeql.cjs verify-config

      - name: Remove existing CodeQL DB (if any)
        run: |
          rm -rf codeql-db

      - name: Perform CodeQL Analysis
        run: |
          node .github/scripts/callgraph_enhanced/analyze-codeql.cjs analyze

      - name: Check CodeQL Analysis Results
        run: |
          node .github/scripts/callgraph_enhanced/analyze-codeql.cjs check-results

      - name: Debug CodeQL execution
        run: |
          node .github/scripts/callgraph_enhanced/analyze-codeql.cjs debug

      - name: Wait for CodeQL results
        run: |
          node -e "setTimeout(()=>{}, 10000)"

      - name: Find and process CodeQL results
        run: |
          node .github/scripts/callgraph_enhanced/find-process-results.cjs

      - name: Generate HTML graph
        run: |
          node .github/scripts/callgraph_enhanced/generate-html-graph.cjs

      - name: Copy files to generated-docs and commit results
        run: |
          node .github/scripts/callgraph_enhanced/copy-commit-results.cjs

--- 呼び出し元
# 呼び出し元ワークフロー: call-callgraph_enhanced.yml
name: Call Call Graph Enhanced

on:
  schedule:
    # 毎日午前5時(JST) = UTC 20:00前日
    - cron: '0 20 * * *'
  workflow_dispatch:

jobs:
  call-callgraph-enhanced:
    # uses: cat2151/github-actions/.github/workflows/callgraph_enhanced.yml
    uses: ./.github/workflows/callgraph_enhanced.yml # ローカルでのテスト用
```

# レビュー結果OKと判断する
- レビュー結果を人力でレビューした形になった

# test
- #4 同様にローカル WSL + act でtestする
- エラー。userのtest設計ミス。
  - scriptの挙動 : src/ がある前提
  - 今回の共通ワークフローのリポジトリ : src/ がない
  - 今回testで実現したいこと
    - 仮のソースでよいので、関数コールグラフを生成させる
  - 対策
    - src/ にダミーを配置する
- test green
  - ただしcommit pushはしてないので、html内容が0件NG、といったケースの検知はできない
  - もしそうなったら別issueとしよう

# test green

# commit用に、yml 呼び出し元 uses をlocal用から本番用に書き換える

# closeとする
- もしhtml内容が0件NG、などになったら、別issueとするつもり

```

### issue-notes/2.md
```md
# issue #2 入力で「左 + ア + 必」 のとき左か右かがパッと見てわかりづらい #2
[issues #2](https://github.com/cat2151/fighting-game-button-challenge/issues/2)

# なにが問題？
- playerが混乱する
- 練習不足になる。この例だと本質的に練習したいのは、「脳が認識してから」「ボタンを押すまで」の「時間を最小化」という練習である。
  - つまり「左右の見間違いを防止する練習」はまったく不要であり、トータルの練習の邪魔である。
    - 視認性が悪いので視認性をよくするべき、とも言える。

# ブレインストーミング
## 分析
- 視認性が悪いのは「左下」「右下」「左」「右」「左上」「右上」という表示のせい
- よって、それらを、まったく別の視認性の良い文字列「1」「3」「4」「6」「7」「9」に置換表示するとよさげ
## alias機能
- 左 右 を 4 6 に置換して表示する
- alias.toml を用意し、そこで、左 右 を 4 6 に置換とする
- 置換する処理は、displayの処理において、とする
- mission.tomlと関連処理は影響なし、とする
## font
- aliasを、tomlによるfont指定（現在できる）と組み合わせる
- これにより、見て反応しやすいグラフィカルな方向指定やボタン指定ができるか、を検証するとよさげ
- fontは、別issueに切り分けたほうがよいだろう。つまり issue #2 においては、aliasのみを扱おう

# LLMに可視化させる、認知負荷を下げる
- プロンプト「外部仕様の案、内部仕様の案、変更のある関数のlist、を箇条書きでまとめ、md末尾に追記してください」

---

## 外部仕様の案
- 入力表示で「左」「右」などの方向を、数字（例:「4」「6」）に置換して表示できる
- 置換ルールは alias.toml でユーザーが編集可能
- 置換表示は設定でON/OFF切り替え可能

## 内部仕様の案
- alias.toml を読み込み、方向やボタン名の置換マップを生成
- 入力表示処理（display処理）で、表示前に置換マップを適用
- mission.toml等、他の設定ファイルやロジックには影響を与えない
- 設定で置換表示の有効/無効を切り替えられるようにする

## 変更のある関数のlist
- 入力表示用の display 関数
- alias.toml 読み込み処理
- 設定管理（config）関連の関数
- （必要に応じて）初期化処理や設定反映処理

# 上記をレビューした所感
- 補足。on/offもtomlで1行で制御する。on固定よりも、testがしやすい、使いやすい。
- あとはOK

# agentに実装させてみよう
- プロンプト「実装してみてください」
- 結果、alias.tomlの生成の途中で指示待ちになった
    - その内容自体はちょっと追加指示すればなおりそう
- 対策、切り分ける。alias.tomlだけ書かせて、指示して仕上げるところまで一歩ずつやらせる
    - プロンプト「alias.tomlを書いてみてください。イメージは、1つの変換につき、変換元ボタン名、変換後ボタン名、の2要素配列です。そして、それが10個～20個の配列として並びます。tomlの配列（list）の書き方の「[[～]]」を利用してください。」
- 結果、alias.tomlはできた。

# agentに実装させてみよう
- プロンプト「実装してみてください」
- 結果、破綻。仮説、contextあふれ。対策、具体的なソース名と関数名をlistさせる。プロンプト「変更するソース名と関数名をlistしてください」
- 結果、utils.pyが突然登場。想定はconfigs.pyなので混乱。実際、前述でconfigは登場している。対策、button_challege.tomlにalias.tomlとの紐付けを記述。これはほかのtomlを参考にしたもの。ついでにconfigs.pyに、TODOコメントとして指示を記載した。
    - 結局人間が考えている
- プロンプト「実装してみてください。configs.pyのTODOコメントを参照してください。readしたaliasは、update_display_with_missionにわたしてください。update_display_with_missionの内部で、alias関数を呼び出してください。alias関数は最初はガワだけでいいです。」
- 結果、いくつか手直しはさせたが、できている、test green
- プロンプト「#2 の作業の流れ、つまりこのmdの内容を、箇条書きでまとめてください。用途は、今後よりよい進め方をするためのヒント用です」
- 結果、まとめは出たが長いし、いらない（とっくにわかりきっている）ものが多い。userが削る

# 今後のための振り返り
- 課題、破綻。
    - 対策、実装プロンプトを段階的に分割
        - まず alias.toml のみを作成させる
        - その後、実装を進めさせる
- 課題、破綻。
    - 対策、具体的なソース名・関数名をリストアップさせる
- 課題、想定外のファイルや関数が登場。
    - 対策、userがソースのおおまかな調査をして、TODOコメントで補足し、プロンプトをより具体的に記述

```

### .github/actions-tmp/issue-notes/3.md
```md
# issue GitHub Actions「issue note生成」を共通ワークフロー化する #3
[issues #3](https://github.com/cat2151/github-actions/issues/3)

- 前提
  - userは、translateのworkflowを共通ワークフロー化し、動くようにしたので、共通ワークフロー化の知識がある
  - よって、今回は、promptでplanさせ、そのplanをuserがレビューし、planの改善を指示できるので、ハルシネーションのリスクを下げることができる

- prompt
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
このymlはまだ共通ワークフロー化されず、
呼び出し元からコピーされたままの状態です。
このymlファイル名のまま、
中身を共通ワークフロー化してください。
呼び出し元ymlは別途書きますので気にしないでください。
まずplanしてください
```

- plan 生成結果
```
共通ワークフロー化のためのplanは以下の通りです。

1. 目的
現在の issue-note.yml を「共通ワークフロー」として再設計し、他リポジトリや他ワークフローから workflow_call で呼び出せるようにする。
2. 主な変更点
on: トリガーを workflow_call に変更（直接イベントで起動しない）。
必要な入力（inputs）やシークレット（secrets）を workflow_call セクションで定義。
github.event.issue などのイベント依存部分を、inputs経由で受け取る形に修正。
既存の処理（issueノート生成、コミット、issue body更新）はそのまま活かすが、パラメータ化する。
3. 具体的な修正内容
on: issues: → on: workflow_call: に変更。
inputs で必要な値（例: issue_title, issue_number, issue_body, issue_url など）を受け取る。
スクリプト内の ${{ github.event.issue.xxx }} を ${{ inputs.xxx }} に置換。
github-script ステップも同様にinputsを参照。
必要に応じて secrets も workflow_call で受け取れるようにする。
4. ファイル名・配置
ファイル名はそのまま issue-note.yml。
配置場所は workflows でOK（共通ワークフローとしてもこの場所で良い）。
5. 呼び出し元への影響
呼び出し元ワークフローで uses: <repo>/.github/workflows/issue-note.yml@main のように参照し、inputsを渡す形になる。
このplanで進めます。次に、実際の共通ワークフロー化のためのyml修正案を作成しますか？
```

- userがplanレビューし、OKを出した
- agentに生成結果ymlをレビューさせた、OKとなった
  - userはこのレビューは認知負荷が高いのでskipとする（単純な細かい間違い探し作業になるので、それはagentに任せた）
-  エラー。呼び出し元ymlのエラーがあり修正。共通ワークフローのエラー指摘があり、共通ワークフロー側の修正が必要となった
```
原因の分析：

呼び出し元（tonejs-mml-to-jsonのissue-note.yml）は、reusable workflow（cat2151/github-actions/.github/workflows/issue-note.yml@main）をusesで呼び出し、inputsをwithで渡しています。
共通ワークフロー（reusable workflow）は inputs を workflow_call で受け取り、各ステップで ${{ inputs.xxx }} で参照しています。
しかし、エラーが発生したのは actions/github-script@v7 の script 内です。
エラーの本質的な原因：

actions/github-script の script: で ${{ inputs.issue_number }} のような式を直接 JavaScript テンプレートリテラル内で使っていますが、これはサポートされていません。
script: の中は JavaScript であり、YAMLの ${{ ... }} は展開されません（または意図通りに展開されません）。
そのため、inputs 変数は script 内の JavaScript で未定義となり、ReferenceError になります。
正しい書き方：

actions/github-script の script: でワークフローの inputs を使いたい場合は、with: で input を environment 変数や script の引数として渡し、JavaScript で process.env から取得するか、github-script の input 機能を使う必要があります。
例（修正版）：

このように、inputs の値を env で渡し、script 内では process.env で参照してください。

まとめ：

actions/github-script の script 内で ${{ inputs.xxx }} を直接使うと ReferenceError になる
env: で値を渡し、process.env で参照するのが正しい
修正が必要です。修正版のワークフローが必要な場合はお知らせください。
```

- test green
- closeとする

```

### .github/actions-tmp/issue-notes/4.md
```md
# issue GitHub Actions「project概要生成」を共通ワークフロー化する #4
[issues #4](https://github.com/cat2151/github-actions/issues/4)

# prompt
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
このymlファイルを、以下の2つのファイルに分割してください。
1. 共通ワークフロー       cat2151/github-actions/.github/workflows/daily-project-summary.yml
2. 呼び出し元ワークフロー cat2151/github-actions/.github/workflows/call-daily-project-summary.yml
まずplanしてください
```

# 結果、あちこちハルシネーションのあるymlが生成された
- agentの挙動があからさまにハルシネーション
    - インデントが修正できない、「失敗した」という
    - 構文誤りを認識できない
- 人力で修正した

# このagentによるセルフレビューが信頼できないため、別のLLMによるセカンドオピニオンを試す
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
以下の2つのファイルをレビューしてください。最優先で、エラーが発生するかどうかだけレビューてください。エラー以外の改善事項のチェックをするかわりに、エラー発生有無チェックに最大限注力してください。

--- 呼び出し元

name: Call Daily Project Summary

on:
  schedule:
    # 日本時間 07:00 (UTC 22:00 前日)
    - cron: '0 22 * * *'
  workflow_dispatch:

jobs:
  call-daily-project-summary:
    uses: cat2151/github-actions/.github/workflows/daily-project-summary.yml
    secrets:
      GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}

--- 共通ワークフロー
name: Daily Project Summary
on:
  workflow_call:

jobs:
  generate-summary:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      issues: read
      pull-requests: read

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0  # 履歴を取得するため

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: |
          # 一時的なディレクトリで依存関係をインストール
          mkdir -p /tmp/summary-deps
          cd /tmp/summary-deps
          npm init -y
          npm install @google/generative-ai @octokit/rest
          # generated-docsディレクトリを作成
          mkdir -p $GITHUB_WORKSPACE/generated-docs

      - name: Generate project summary
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITHUB_REPOSITORY: ${{ github.repository }}
          NODE_PATH: /tmp/summary-deps/node_modules
        run: |
          node .github/scripts/generate-project-summary.cjs

      - name: Check for generated summaries
        id: check_summaries
        run: |
          if [ -f "generated-docs/project-overview.md" ] && [ -f "generated-docs/development-status.md" ]; then
            echo "summaries_generated=true" >> $GITHUB_OUTPUT
          else
            echo "summaries_generated=false" >> $GITHUB_OUTPUT
          fi

      - name: Commit and push summaries
        if: steps.check_summaries.outputs.summaries_generated == 'true'
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          # package.jsonの変更のみリセット（generated-docsは保持）
          git restore package.json 2>/dev/null || true
          # サマリーファイルのみを追加
          git add generated-docs/project-overview.md
          git add generated-docs/development-status.md
          git commit -m "Update project summaries (overview & development status)"
          git push

      - name: Summary generation result
        run: |
          if [ "${{ steps.check_summaries.outputs.summaries_generated }}" == "true" ]; then
            echo "✅ Project summaries updated successfully"
            echo "📊 Generated: project-overview.md & development-status.md"
          else
            echo "ℹ️ No summaries generated (likely no user commits in the last 24 hours)"
          fi
```

# 上記promptで、2つのLLMにレビューさせ、合格した

# 細部を、先行する2つのymlを参照に手直しした

# ローカルtestをしてからcommitできるとよい。方法を検討する
- ローカルtestのメリット
    - 素早く修正のサイクルをまわせる
    - ムダにgit historyを汚さない
        - これまでの事例：「実装したつもり」「エラー。修正したつもり」「エラー。修正したつもり」...（以降エラー多数）
- 方法
    - ※検討、WSL + act を環境構築済みである。test可能であると判断する
    - 呼び出し元のURLをコメントアウトし、相対パス記述にする
    - ※備考、テスト成功すると結果がcommit pushされる。それでよしとする
- 結果
    - OK
    - secretsを簡略化できるか試した、できなかった、現状のsecrets記述が今わかっている範囲でベストと判断する
    - OK

# test green

# commit用に、yml 呼び出し元 uses をlocal用から本番用に書き換える

# closeとする

```

### .github/actions-tmp/issue-notes/7.md
```md
# issue issue note生成できるかのtest用 #7
[issues #7](https://github.com/cat2151/github-actions/issues/7)

- 生成できた
- closeとする

```

### .github/actions-tmp/issue-notes/9.md
```md
# issue 関数コールグラフhtmlビジュアライズが0件なので、原因を可視化する #9
[issues #9](https://github.com/cat2151/github-actions/issues/9)

# agentに修正させたり、人力で修正したりした
- agentがハルシネーションし、いろいろ根の深いバグにつながる、エラー隠蔽などを仕込んでいたため、検知が遅れた
- 詳しくはcommit logを参照のこと
- WSL + actの環境を少し変更、act起動時のコマンドライン引数を変更し、generated-docsをmountする（ほかはデフォルト挙動であるcpだけにする）ことで、デバッグ情報をコンテナ外に出力できるようにし、デバッグを効率化した

# test green

# closeとする

```

### config/button_challenge.toml
```toml
lever_toml        = "config/lever_names.toml"
button_names_toml = "config/button_names.toml"
alias_toml        = "config/alias.toml"
mission_toml      = "config/mission.toml"

title = "ボタンチャレンジ 終了はterminalでCTRL+C"
geometry = "700x120+256+256"
font_name = "Arial"
font_size = 20

histogram_mode_sample_count = 50 # hist中心の表示用

[display_format]
    label1 = "mission : {mission}"
    label2 = "{lever_plus_pressed}"
    label3 = "score:{score} fail:{fail_count} 前回:{last_mission_frame_count} 最速:{prev_success_min_frame_count} hist中心:{prev_success_hist_center} now:{current_mission_frame_count}"

[backmost_mode]
    check_interval_sec = 10
    process_names = ['StreetFighter6.exe', 'CapcomFightingCollection.exe']

```

### config/lever_names.toml
```toml
# missionで使う用のレバー名称定義

names = [
    "左下",
    "下",
    "右下",
    "左",
    "ニュートラル",
    "右",
    "左上",
    "上",
    "右上",
]

# 斜め上入力をチェックするとき、真上入力したら失敗とみなし、横入力は「成功ではないが、成功まであと一歩なので、失敗ではなくノーカン扱い」とする用
[[no_count_names]]
success  = "右上"
no_count = ["右"] # 上だけの場合はNG。斜めジャンプしようとして垂直ジャンプしたということなので。

[[no_count_names]]
success  = "左上"
no_count = ["左"] # 上だけの場合はNG。斜めジャンプしようとして垂直ジャンプしたということなので。

[[no_count_names]]
success  = "右下"
no_count = ["右", "下"] # 下は許容する。垂直ジャンプと違って取り返しがつくので。

[[no_count_names]]
success  = "左下"
no_count = ["左", "下"] # 下は許容する。垂直ジャンプと違って取り返しがつくので。

```

### issue-notes/5.md
```md
# issue tomlに左右どちらも記述するのは、tomlメンテコストが高い #5
[issues #5](https://github.com/cat2151/fighting-game-button-challenge/issues/5)

# 対策案
- 左右ランダム、tomlの簡素化
    - button_challenge.toml に「左」or「右」で記載されているものは、ひとまず「右」で記載し、「左」を削除
    - button_challenge.toml left_right = ['左', '右']
    - play中は、left_right を使って、ランダム50%で左右反転
    - （alias実装後）左右のかわりに前後や123456789を記載可能に

# LLMに対策案を書かせる
- プロンプト「どうやって実装するか可視化して、開発者の認知負荷を下げてください。具体的には、修正対象ソース、関数、pythonの実際の追加codeや変更code を、このmdに追記してください。このプロンプトと、ここから上は、維持してください。」

# ---

## 修正対象ソース・関数

- [`missions.py`](../missions.py)
  - ミッション表示時に左右反転をランダムで行う処理を追加
  - 反転用の関数を新規追加
- [`configs.py`](../configs.py)
  - `left_right`・`left_right_temp`の値をtomlから読み込む
- [`main.py`](../main.py)
  - ミッション表示前に反転処理を挟む
- [`button_challenge.toml`](../button_challenge.toml)
  - ミッションは「右」だけ記載し、「左」は削除（既に案通りになっている）

---

## 追加・変更するPythonコード例

### 1. [`configs.py`](../configs.py)
`load_game_configuration`で`left_right`と`left_right_temp`も返すように修正

```python
# ...existing code...
def load_game_configuration():
    args = get_args()
    args = update_args_by_toml(args, args.config_filename)
    (names, plus, lever_names, missions) = load_all_configs(args)
    config = read_toml(args.config_filename)
    left_right = config.get("left_right", ["左", "右"])
    left_right_temp = config.get("left_right_temp", ["ひだり", "みぎ"])
    return args, names, plus, lever_names, missions, left_right, left_right_temp
# ...existing code...
```

### 2. [`missions.py`](../missions.py)
ミッション文字列を左右ランダムで反転する関数を追加

```python
import random
# ...existing code...

def maybe_reverse_left_right(mission, left_right, left_right_temp):
    # 50%の確率で左右反転
    if random.random() < 0.5:
        return mission
    # 一時的に置換
    mission_tmp = mission
    for orig, temp in zip(left_right, left_right_temp):
        mission_tmp = mission_tmp.replace(orig, temp)
    # 左右入れ替え
    for orig, temp in zip(left_right, reversed(left_right_temp)):
        mission_tmp = mission_tmp.replace(temp, orig)
    return mission_tmp

# ...existing code...
```

### 3. [`main.py`](../main.py)
`main`や`main_loop`でミッション表示前に反転処理を挟む

```python
# ...existing code...
from missions import check_and_update_mission, initialize_mission_sets, maybe_reverse_left_right
# ...existing code...
def main():
    (args, names, plus, lever_names, missions, left_right, left_right_temp) = load_game_configuration()
    # ...existing code...
    main_loop(tkinter_root, args, check_interval_msec, last_check_msec, joystick, names, plus, lever_names, missions, mission_index, missions_set, success_missions, labels, timer_id_dict, clock, left_right, left_right_temp)
# ...existing code...
def main_loop(..., left_right, left_right_temp):
    # ...existing code...
    while True:
        # ...existing code...
        (mission, mission_index, missions_set, success_missions, score) = check_and_update_mission(...)
        # ここで左右ランダム反転
        mission_display = maybe_reverse_left_right(mission, left_right, left_right_temp)
        old_texts = update_display_with_mission(..., mission_display)
        # ...existing code...
# ...existing code...
```

---

このように修正すれば、tomlの記述を「右」だけにしつつ、実行時に50%で左右反転表示が可能です。
この案を`issue-notes/5.md`の下部に追記します。

---

# レビュー結果
- 手早くレビューしました。
  - まず、5.mdに追記されたものはsourceへのlink形式になっておらず手で開く羽目になり不便でした。linkがほしい。
    - → プロンプト「5.mdを整形してください。具体的には、sourceのlinkは、すべてmarkdown linkの形式にしてください。」で対処しました。
    - → LLMが生成をミスってたので、さらに修正させました。
    - → link踏んでみたもののわかりづらい。普通にagentに直接code修正させるいつものやり方のほうが速い。
  - 次に、maybe～を書く場所が不適切に思えます。
    - そこではview層が変更されるだけに見えます。
    - そうではなく、check_and_update_mission にてmissionを取得後にmaybe～を適用するのでは？
  - → これをLLMに食わせたら破綻したので中断
- 実際は、先頭で「なおして」とagentに書いて直接なおさせるほうが速い認識。今回はあくまで実験として残した。
- まとめ
  - #5 に限った話で、
    - この手法は、現在のLLM性能では失敗した。
        - 普通にagentに直接codeなおさせるほうが速そう。
    - 今後も、LLMに可視化させ、開発者の認知負荷を下げる観点で進める実験は継続するとして、
      - 次は、もっとシンプルで小さい一歩を試そう。

# Blueskyに投稿してから気づいた
- 左右反転のタイミング、まだおかしいんじゃね
- そもそもindexでmissionを指定してるやつで、毎フレmissionをgetしてるんだとしたら、反転が毎フレになったらヤバくね
- まず今やってるmission string自体は、一度mission get時に左右反転したあとは、固定、という構造にリファクタリングが先じゃね
- sourceうろ覚えだけどそんな気がする
- 詳しくはあとで見よう

# さらに気付いた
- コンセプト「左右を網羅して練習する」が暗黙にあった
- なのでランダムはNG、左右いずれも1周のmission setで出現がマスト
- 結果的に、左右網羅したTOML、の出力が正で、それをランダムで散らすのはNG
- なので必要なのは、TOMLでは左右どちらかのみ記述してメンテを楽にしつつ、TOMLをreadした直後に左右増幅、である
- 入力定義は #5 先頭と変わらない。出力定義が変わる。ランダムではなく、#5の前と同じ出力となる。
- code影響範囲はシンプルに狭まり、TOMLをreadした直後にfnc呼ぶだけになる。

# プロンプト
- 「mdの「さらに気付いた」を元に、変更規模（変更や追加のあるソース数と関数の数）を可視化し、開発者の認知負荷を下げたドキュメントを生成し、md末尾に追記してください。」

# 変更規模の可視化（「さらに気付いた」に基づく）

## 概要
- 「左右を網羅して練習する」ため、TOML読込直後に左右両方のミッションを生成する方式に変更。
- ランダム反転は廃止し、ミッションセット自体に左右両方を含める。
- これにより、出力定義が「左右網羅」型となり、ランダム性は排除される。

## 変更・追加のあるソース
- [`missions.py`](../missions.py)
  - TOML読込直後に左右増幅する関数を新規追加、または既存読込処理を修正。
- [`configs.py`](../configs.py)
  - ミッションリスト取得部分で、左右増幅関数を呼び出すよう修正。
- [`main.py`](../main.py)
  - ミッションセットの扱いが変わる場合、呼び出し箇所の引数やロジックを微調整。

## 変更・追加される関数数（目安）
- 新規追加：1関数（左右増幅用）
- 既存修正：2関数（TOML読込・ミッションセット取得）

## 認知負荷のポイント
- 影響範囲はTOML→ミッションセット生成の部分に限定。
- ランダム反転や毎フレ反転の複雑さが消え、構造がシンプルになる。
- 既存の「ミッション表示」や「進行」ロジックにはほぼ影響しない。

---

# 上記仕様どおりにagentに実装させてみた
- それを軽く見たところバグってた
- agentにコードレビューさせ、レビュー結果をもとに指示して修正させた
- レビュー結果が問題なくなるまでそれを繰り返させた。5回くらい繰り返させた記憶

# さらにバグが発覚
- 手で修正した

# 実装を一段落した
- test green

# LLMにまとめさせる
- プロンプト「このmdは、issues #5 の対応をlog的に羅列したものです。要約し、このmdの末尾に追記してください。読みやすく1行は短く、箇条書きで。」

# 対応ログ要約（issues #5）
- tomlの左右記述コスト削減案を検討。
- LLMで実装方針を可視化し、修正対象やコード例を記載。
- agentに実装させたがバグが発生し、レビュー・修正を繰り返した。
- さらに手動でバグ修正し、テストが通る状態に。
- ランダム反転から「左右網羅」型へ仕様変更。
- 影響範囲はTOML読込直後のミッションセット生成に限定。
- LLMによる可視化・認知負荷低減の実験を継続予定。

```

### requirements.txt
```txt
pygame
toml
numpy
psutil
pywin32

```

### src/configs.py
```py
from utils import get_args, read_toml, update_args_by_toml

def load_game_configuration():
    args = get_args()
    args = update_args_by_toml(args, args.config_filename)
    args = update_args_by_toml(args, args.mission_toml)
    (names, plus, lever_names, missions, none_word, alias_conf, no_count_names) = load_all_configs(args)
    return args, names, plus, lever_names, missions, none_word, alias_conf, no_count_names

def load_all_configs(args):
    config = read_toml(args.button_names_toml)
    names = config.get("names", [])
    plus = config.get("plus")
    none_word = config.get("none_word")
    print(f"読み込まれた設定: {names}")

    config = read_toml(args.lever_toml)
    lever_names = config.get("names", [])
    no_count_names = config.get("no_count_names", [])
    print(f"読み込まれた設定: {lever_names}")
    print(f"no_count_names: {no_count_names}")

    alias_conf = read_toml(args.alias_toml)

    return names, plus, lever_names, args.missions, none_word, alias_conf, no_count_names

```

### tests/test_is_no_count_case.py
```py
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import is_no_count_case

no_count_names_list = [
    {"success": "右上", "no_count": ["右"]},
]

@pytest.mark.parametrize("mission_success, input_name, no_count_names_param, expect_exception, expected", [
    ("右上", "右上", no_count_names_list, False, True),
    ("右上", "右", no_count_names_list, False, True),
    ("右上", "上", no_count_names_list, False, False),
    ("右上", "右 + DP", no_count_names_list, False, False),
    ("右上", "右 + 必", no_count_names_list, False, False),
    ("右上", "ア + 必", no_count_names_list, False, False),
    ("右上", "左上", no_count_names_list, False, False),

    ("右", "右", no_count_names_list, False, True),
    ("右", "右上", no_count_names_list, False, False),
    ("右", "上", no_count_names_list, False, False),
    ("右", "右 + DP", no_count_names_list, False, False),
    ("右", "右 + 必", no_count_names_list, False, False),
    ("右", "ア + 必", no_count_names_list, False, False),
    ("右", "左上", no_count_names_list, False, False),

    ("上", "上", no_count_names_list, False, True),
    ("上", "右上", no_count_names_list, False, False),
    ("上", "上 + 弱", no_count_names_list, False, False),

    ("右 + 強 + 必", "右 + 強 + 必", no_count_names_list, False, True),
    ("右 + 強 + 必", "右", no_count_names_list, False, True),
    ("右 + 強 + 必", "強", no_count_names_list, False, True),
    ("右 + 強 + 必", "必", no_count_names_list, False, True),
    ("右 + 強 + 必", "強 + 必", no_count_names_list, False, True),
    ("右 + 強 + 必", "右 + 強", no_count_names_list, False, True),
    ("右 + 強 + 必", "右 + 必", no_count_names_list, False, True),
    ("右 + 強 + 必", "右 + 強 + 必 + DP", no_count_names_list, False, False),
    ("右 + 強 + 必", "なし", no_count_names_list, False, False),

    # no_count_names_list が空のケースはExceptionを期待する
    ("上", "上", [], True, None),
    ("上", "右上", [], True, None),
])
def test_is_no_count_case(mission_success, input_name, no_count_names_param, expect_exception, expected):
    plus = " + "
    if expect_exception:
        with pytest.raises(ValueError):
            is_no_count_case(mission_success, input_name, no_count_names_param, plus)
    else:
        assert is_no_count_case(mission_success, input_name, no_count_names_param, plus) == expected

```

## 最近の変更（過去7日間）
### コミット履歴:
1f4799f Google検索にindexさせる用
76bc6dd Google検索にindexさせる用

### 変更されたファイル:
README.ja.md
README.md
_config.yml
generated-docs/development-status-generated-prompt.md
generated-docs/development-status.md
generated-docs/project-overview-generated-prompt.md
generated-docs/project-overview.md
googled947dc864c270e07.html


---
Generated at: 2025-12-02 07:03:37 JST
