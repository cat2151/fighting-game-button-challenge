from utils import get_args, read_toml, update_args_by_toml

def load_game_configuration():
    args = get_args()
    args = update_args_by_toml(args, args.config_filename)
    (names, plus, lever_names, missions, none_word, alias_conf) = load_all_configs(args)
    return args, names, plus, lever_names, missions, none_word, alias_conf

def load_all_configs(args):
    config = read_toml(args.button_names_toml)
    names = config.get("names", [])
    plus = config.get("plus")
    none_word = config.get("none_word")
    print(f"読み込まれた設定: {names}")

    config = read_toml(args.lever_toml)
    lever_names = config.get("names", [])
    print(f"読み込まれた設定: {lever_names}")

    alias_conf = read_toml(args.alias_toml)

    return names, plus, lever_names, args.missions, none_word, alias_conf
