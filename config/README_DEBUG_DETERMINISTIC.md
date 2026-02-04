# デバッグ用設定: Deterministic Mode

## 概要
決定論的(Deterministic)モードでのデバッグ用設定ファイルです。

## 設定内容
- `challenge_phase = "1_buttons"` - Phase 1 (ボタンモード) でスタート
- `use_random_mission = false` - 決定論的にミッションを選択（常に同じミッション）
- タイトルに "DEBUG Deterministic" と表示

## 使い方
```bash
python src/main.py --config-filename config/button_challenge_debug_deterministic.toml
```

## 用途
- 再現可能なテスト
- 特定のミッションの動作確認
- デバッグ時に毎回同じミッションで確認したい場合
