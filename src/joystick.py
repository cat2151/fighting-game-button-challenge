import pygame

def setup_pygame_and_joystick():
    if hasattr(pygame, 'init'):  # こうしないとlinterエラー
        pygame.init()
    joystick = initialize_joystick()
    if joystick is None:
        raise RuntimeError("ジョイスティックが接続されていません。プログラムを終了します。")
    return joystick

def initialize_joystick():
    """ジョイスティックを初期化し、接続されていない場合はNoneを返す"""
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("ジョイスティックが接続されていません。")
        return None

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"使用するジョイスティック: {joystick.get_name()}")
    return joystick

def get_buttons_as_bitstring(joystick):
    # ボタン入力を取得（0または1）
    buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]

    # アナログ入力を2ビット表現に変換（軸4と軸5を対象とする）
    axes = []
    for i in range(joystick.get_numaxes()):
        axis_value = joystick.get_axis(i)

        if i in [4, 5]:  # 軸4と軸5の場合
            if axis_value == -1:
                axes.extend([0, 0])  # ニュートラル位置を0とする
            elif axis_value > -1:  # 正方向
                axes.extend([1, 0])
            elif axis_value < -1:  # 負方向（理論的には発生しないが念のため）
                axes.extend([0, 1])

    # ビット列を構成
    bitstring = ''.join(map(str, buttons))  # ボタンのビット列
    bitstring += ''.join(map(str, axes))   # アナログ入力の2ビット列

    return bitstring

def create_button_states(names, plus, lever_names, joystick, bitstring):
    lever = get_hat_input_as_fighting_game_notation(joystick, lever_names)
    if lever == lever_names[4]: # ニュートラルの場合は表示なし。なぜなら「ニュートラル+A+B」はわかりづらいと感じた。今後見直す可能性あり。
        lever = None
    pressed = get_pressed_buttons(names, bitstring, plus)
    lever_plus_pressed = "なし"
    if lever and pressed:
        lever_plus_pressed = f"{lever}{plus}{pressed}"
    elif lever:
        lever_plus_pressed = f"{lever}"
    elif pressed:
        lever_plus_pressed = f"{pressed}"
    return lever_plus_pressed

def get_hat_input_as_fighting_game_notation(joystick, lever_names):
    # ハットスイッチを格ゲー表記に変換
    for i in range(joystick.get_numhats()):
        hat = joystick.get_hat(i)
        # 格ゲー表記の変換
        if hat == (-1, -1):  # 左下
            return lever_names[0]
        elif hat == (0, -1):  # 下
            return lever_names[1]
        elif hat == (1, -1):  # 右下
            return lever_names[2]
        elif hat == (-1, 0):  # 左
            return lever_names[3]
        elif hat == (0, 0):  # ニュートラル
            return lever_names[4]
        elif hat == (1, 0):  # 右
            return lever_names[5]
        elif hat == (-1, 1):  # 左上
            return lever_names[6]
        elif hat == (0, 1):  # 上
            return lever_names[7]
        elif hat == (1, 1):  # 右上
            return lever_names[8]
    return None  # 入力がない場合

def get_pressed_buttons(names, bitstring, plus):
    """現在押されているボタンを 'A + B' の形式で返す"""
    pressed_buttons = [name for name, state in zip(names, bitstring[:len(names)]) if name and state == '1']
    return plus.join(pressed_buttons)

def shutdown_pygame():
    if hasattr(pygame, 'quit'): # こうしないとlinterエラー
        pygame.quit()

def should_skip_input_processing(buttons_bits, initial_bitstring, input_activated):
    # 課題、起動直後の入力誤爆がある、対策、起動直後はボタンを押して離すまでは入力なしとみなす、この関数を利用する
    is_all_released = buttons_bits == initial_bitstring
    if not is_all_released:
        input_activated = True
    return not input_activated, input_activated
