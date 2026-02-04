# デバッグ用設定: Phase 2

## 概要
Phase 2 (必殺技モード) の開発・デバッグ用設定ファイルです。

## 設定内容
- `challenge_phase = "2_moves"` - Phase 2 (必殺技モード) でスタート
- `use_random_mission = true` - ランダムにミッションを選択
- タイトルに "DEBUG Phase2" と表示

## 使い方
```bash
python src/main.py --config-filename config/button_challenge_debug_phase2.toml
```

## 用途
- Phase 2 の動作確認
- 必殺技入力のテスト
- 左右の向き切り替え機能のデバッグ
