# ダークモード機能 (Dark Mode Feature)

## 概要 (Overview)

ボタンチャレンジアプリケーションにダークモード機能を追加しました。
ライトモード、ダークモード、システム設定追従の3つのモードから選択できます。

This application now supports dark mode with three options:
- Light mode (ライトモード)
- Dark mode (ダークモード)  
- System mode (システム設定追従) - automatically follows Windows OS dark mode settings

## 設定方法 (Configuration)

`config/button_challenge.toml` で以下のように設定します:

```toml
[theme]
    mode = "system"  # "light", "dark", or "system"
    
    # Light theme colors (optional - defaults are shown)
    [theme.light]
        bg_color = "SystemButtonFace"
        fg_color = "black"
        success_color = "#00FF00"
        fail_color = "red"
    
    # Dark theme colors (optional - defaults are shown)
    [theme.dark]
        bg_color = "#2b2b2b"
        fg_color = "#ffffff"
        success_color = "#00FF00"
        fail_color = "#ff4444"
```

## モード説明 (Mode Details)

### ライトモード (Light Mode)
```toml
mode = "light"
```
- システムのデフォルト背景色を使用
- 黒い文字色
- 明るい背景で見やすい

### ダークモード (Dark Mode)
```toml
mode = "dark"
```
- ダークグレーの背景色 (#2b2b2b)
- 白い文字色
- 暗い環境での目の疲れを軽減

### システム設定追従 (System Mode)
```toml
mode = "system"
```
- Windows OSのダークモード設定を自動検出
- OSの設定に応じて自動的にライト/ダークモードを切り替え
- **Windows 10/11のみ対応** (他のOSではライトモードにフォールバック)

## カラーのカスタマイズ (Color Customization)

各テーマの色は自由にカスタマイズできます:

```toml
[theme.dark]
    bg_color = "#1e1e1e"      # お好みの背景色
    fg_color = "#d4d4d4"      # お好みの文字色
    success_color = "#4ec9b0" # 成功時のフラッシュ色
    fail_color = "#f48771"    # 失敗時のフラッシュ色
```

## 技術詳細 (Technical Details)

### Windows ダークモード検出 (Windows Dark Mode Detection)

システムモードでは、Windowsレジストリから以下のキーを読み取ります:
```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize
AppsUseLightTheme
```

- 値が `0` = ダークモード
- 値が `1` = ライトモード

### 実装ファイル (Implementation Files)

- `src/theme.py` - テーマ管理とWindows検出
- `src/configs.py` - TOML設定の読み込みと適用
- `src/gui_utils.py` - Tkinterウィンドウの初期化とテーマ適用
- `src/gui.py` - UIの更新とフラッシュ効果
- `src/missions.py` - 成功/失敗時のフラッシュ色設定

## テスト (Tests)

以下のテストが含まれています:

- `tests/test_theme.py` - テーマ機能の単体テスト
- `tests/test_theme_config.py` - TOML設定の読み込みテスト
- `tests/demo_theme_colors.py` - 各モードの色を表示するデモ

テストの実行:
```bash
python -m pytest tests/test_theme.py -v
python tests/demo_theme_colors.py
```

## 動作確認 (Verification)

1. `config/button_challenge.toml` でモードを変更
2. アプリケーションを起動
3. 背景色と文字色が設定に応じて変更されることを確認
4. ミッション成功/失敗時のフラッシュ色を確認

## 既知の制限 (Known Limitations)

- システムモードのWindows検出は Windows 10/11 でのみ動作
- 他のOS (Linux, macOS) ではライトモードにフォールバック
- ホットリロード機能を使用する場合、設定変更は即座に反映されます
