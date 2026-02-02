# Phase 2 Debug Configuration

デバッグ用にPhase 2（技練習フェーズ）から開始するための設定ファイルです。

## 使い方 / Usage

### 通常起動（Phase 1から開始）
```bash
python src/main.py --config-filename config/button_challenge.toml
```

または

```bash
button_challenge.bat
```

### デバッグ起動（Phase 2から開始）
```bash
python src/main.py --config-filename config/button_challenge_debug_phase2.toml
```

## 設定の変更方法 / How to Change Configuration

### config/button_challenge.toml を直接編集
デフォルトの設定ファイルを編集して、いつもPhase 2から開始したい場合：

```toml
challenge_phase = "2_moves"  # "1_buttons" から "2_moves" に変更
```

### 独自の設定ファイルを作成
`button_challenge.toml` をコピーして、独自の設定ファイルを作成することもできます：

```bash
cp config/button_challenge.toml config/my_config.toml
```

そして `my_config.toml` の `challenge_phase` を編集してください。

## Phase の違い / Difference Between Phases

### Phase 1: "1_buttons" (ボタン練習フェーズ)
- ミッションが左右の派生バージョンで増幅されます
- 例: "右上" → "右上", "左上" の2つのミッションが生成される
- ボタンの基本的な練習に適しています

### Phase 2: "2_moves" (技練習フェーズ)  
- ミッションは増幅されません（元のミッション数のまま）
- 向きを意識した練習ができます
- 各サイクルごとに左右が切り替わります
- 方向矢印が表示されます
- 技名が表示されます（moves_toml が設定されている場合）

## トラブルシューティング / Troubleshooting

### エラー: "Invalid challenge_phase"
`challenge_phase` の値が正しくありません。以下のいずれかを使用してください：
- `"1_buttons"` - Phase 1 (ボタン練習)
- `"2_moves"` - Phase 2 (技練習)

### Phase が正しく切り替わらない
1. 設定ファイルのパスが正しいか確認してください
2. TOML ファイルの構文が正しいか確認してください（カンマやクォートなど）
3. アプリケーションを再起動してください
