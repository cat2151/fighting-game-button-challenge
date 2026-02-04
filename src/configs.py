from utils import get_args, read_toml, update_args_by_toml, debug_print
from theme import get_theme_colors

def load_game_configuration():
    args = get_args()
    args = update_args_by_toml(args, args.config_filename)
    args = update_args_by_toml(args, args.mission_toml)
    
    # テーマ設定を読み込んで適用
    args = apply_theme_configuration(args)
    
    (names, plus, lever_names, missions, none_word, alias_conf, no_count_names, moves) = load_all_configs(args)
    return args, names, plus, lever_names, missions, none_word, alias_conf, no_count_names, moves

def apply_theme_configuration(args):
    """テーマ設定を読み込んでargsに適用する"""
    # デフォルト値
    theme_mode = "light"
    light_colors = None
    dark_colors = None
    
    # TOML設定からテーマ情報を取得
    if hasattr(args, 'theme'):
        theme_config = args.theme
        theme_mode = theme_config.get('mode', 'light')
        
        # ライトモードとダークモードの色設定を取得
        light_colors = theme_config.get('light', None)
        dark_colors = theme_config.get('dark', None)
    
    # テーマカラーを計算してargsに設定
    args.theme_colors = get_theme_colors(theme_mode, light_colors, dark_colors)
    
    return args

def load_all_configs(args):
    config = read_toml(args.button_names_toml)
    names = config.get("names", [])
    plus = config.get("plus")
    none_word = config.get("none_word")
    debug_print(f"読み込まれた設定: {names}")

    config = read_toml(args.lever_toml)
    lever_names = config.get("names", [])
    no_count_names = config.get("no_count_names", [])
    debug_print(f"読み込まれた設定: {lever_names}")
    debug_print(f"no_count_names: {no_count_names}")

    alias_conf = read_toml(args.alias_toml)

    # Load moves configuration if moves_toml is defined
    moves = []
    if hasattr(args, 'moves_toml') and args.moves_toml:
        moves_config = read_toml(args.moves_toml)
        moves = moves_config.get("moves", [])

    return names, plus, lever_names, args.missions, none_word, alias_conf, no_count_names, moves
