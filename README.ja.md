# fighting-game-button-challenge（格ゲーボタンチャレンジ）
Windows用の格ゲー練習用アプリ。ボタン練習ができます。スト6モダン用に作りました。他のゲームの練習にも使えるかもしれません。

[English README](README.md)

# どんなアプリか3行で説明
- 格ゲーのボタン練習アプリ
- ランダムでお題が表示されます
- お題に合ったボタンを押すとスコアが入って次のお題が表示されます

# 少し詳しく
- 特徴
    - 常駐
        - 常駐型なので、練習したくなってレバーやボタンを入力した瞬間から使えます、1フレで使えます
        - レバーやボタンの入力があったときだけ最前面化します
        - 入力がなくなってから1秒で最背面化するので、邪魔になりません
        - 格ゲーをプレイ中は自動で最背面化するので、邪魔になりません
    - ランダム
        - mission成功ごとに、次のmissionがランダムで降ってきます
        - 予想外の局面にも即応できる柔軟さを鍛えよう
    - タイム
        - 何フレで入力できたか競えます
        - ※30フレなら速い方だと思います。なぜなら日本語を読む時間と、30択を絞れないぶんの遅れで、15フレくらい取られそうなので
        - ※例えばドライブインパクトだけに意識配分を集中すると24フレくらいまですぐ縮められますが、そのぶんドライブインパクト以外への反応が遅くなります。試してみよう
    - スコア
        - 10点獲得するまで練習しよう、など目安に利用できます
    - 設定
        - モダンでなくクラシックも、おそらく設定すればできます
        - スト6以外の格ゲー、あるいは格ゲー以外のゲームも、おそらく設定すればできます
        - スト6モダン以外の設定ファイルはありません。自分で作ってみよう
- 動作確認した環境
    - Windows
    - XInput
    - アーケードコントローラー
        - レバーレスコントローラー（4ボタン + 10ボタン = 14ボタン）

# 使い方
## install
- リポジトリをcloneしてください
- `pip install -r requirements.txt` してください
## 設定
- `config/button_names.toml` を、ゲームのボタンアサインにあわせて編集してください
- ※ほかいくつか設定ファイルがあります。表示ボタン名のaliasやフォントを変更できます
## 起動
- `button_challenge.bat` を実行してください
- 終了は、terminalで`CTRL+C`

# このアプリが解決すること
- ※この欄は、このアプリが何か？を説明する用、マイルストーンの目安にする用、ほかいろいろな用途に使うつもり
- これまでの課題
    - 起動時間
        - たいていの格ゲーは起動してからトレモまでに1分くらいかかる
        - ほしいのは、0秒で、コントローラーのボタンを押したら即座にボタン表示が出るもの
            - このアプリはそれができる。常駐型。邪魔にならない。ボタンを押して1秒で最背面に戻る。
    - 格ゲーごとの操作に慣れる
        - たいていの格ゲーの操作チュートリアルは、
            - 説明パート（キャラを動かせない）と、操作パート（どの操作を学ぶかを素早く選べない）に分かれていたりする。あるいは操作パートがない。
            - クリアすると数秒間、操作できない時間帯が生じて、時間のロスになる。時間がかかりすぎる、テンポがよくない。
                - 入門時、手早く一通りのムーブを把握する用に使うには不足。
                - 入門時、1つずつのムーブをしっかり身につけるように使うには不足。
                - 日々のトレーニング時、素早くウォーミングアップする用には不足。
            - 日々のトレーニング用の素早くウォーミングアップするレシピがゲーム内に存在せず、自動で表示されず、自分でノートに書いてそれを目で見てトレモで自主練するという手作業が必要になる。
        - ほしいのは、どのボタンを押したらどうなるか、を、
            - mission形式で、成功失敗を判定できて、
            - 1秒で1つのmissionを素早く遊べて、
            - そのゲームで必要なボタンの組み合わせを網羅して、
            - 反復練習して身につけることができるモード
            - ランダムmission、どんな局面でも素早くそれに応じた操作ができる、を目指すモード
            - shareすれば、自分でmissionを作らずとも、先人のmission定義でスムーズに学べる
            - このアプリはそれを目指す。
                - ただし実現可能な範囲に割り切る。仕様を絞る。万能ではない。大前提として、実戦もトレモも活用する。

# 考え方
- ※アプリの方針に関係する
- 楽器
    - 楽器の練習と似ている
    - 反復練習することで、無意識にボタンを押せるようになっていく
        - 案、アプリを使っていてだんだんアプリのscoreがupしていくことで実感できるとよさげ
            - 案、scoreをより実力計測に向くタイプのものを用意
            - 案、継続するだけでupしてモチベになるscore（クッキークリッカー的な）も並列で用意するのがよさげ、現状のscoreはこの方針でつけている
- 意識配分
    - ※以下それぞれ経験則
    - ボタンに慣れないうちは、ボタンを押すだけで意識配分の大部分を取られてしまい、状況把握ができないとか判断ができないとかが多発する
    - 例えば、どんなムーブを選び、その結果はどうだったか。あるいは相手の手をなぜくらって対策は何か。などの把握とその場での即応は、ボタンに意識配分が取られているうちは把握できず即応できない、ということが多い
    - ボタンを意識せず押せるようになっていくことで、ボタンにとられていた意識配分を、試合にまわせるようになり、試合展開が有利になっていく

# 実戦 & トレモ との使い分け例
- ※あくまで一例です
- どのボタンがどのムーブか？すぐにわからない！という段階なら
    - このアプリでボタンに慣れる
- ボタンに慣れてきたら
    - トレモをやる
    - 実戦をやる
- 今スキマ時間でゲーム本体を起動できないが、せめてボタン練習だけでもやりたい！
    - このアプリでボタン練習する

# スコープ外
- このアプリを動かすために必要なPythonとmoduleのimport手順の説明：[issue-notes/12.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/12.md)
- スト6モダン以外の設定ファイル
- 設定GUI
- シーケンス入力（例、`DI` > `ア + 強`） → 別Projectで担当します：[コマンドチャレンジ](https://github.com/cat2151/command-challenge)
- 非常に高度なmission
- 豪華なグラフィック
- 豪華なサウンド（例、mission success ファンファーレ）
- 広範囲なコントローラー認識
- マルチプラットフォーム
- ブラウザアプリ化
- ブラウザアプリのタイピングアプリができること全て
