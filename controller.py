import pygame

def init_joystick():
    if hasattr(pygame, 'init'):
        pygame.init()  # こうしないとlinterでerror
    pygame.joystick.init()

    joystick = None
    print("接続されているジョイスティック:")
    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print(f"{i}: {joystick.get_name()} - ボタン数: {joystick.get_numbuttons()}")
    return joystick

def detect_controller_input():
    for event in pygame.event.get():  # すべてのイベントを取得
        if event.type == pygame.JOYBUTTONDOWN:
            return f"ボタン {event.button} が押されました！"
        elif event.type == pygame.JOYAXISMOTION:
            # 軸4と5をボタンとして扱う
            if event.axis == 4:  # アナログスティックの軸4
                if event.value == -1:
                    return "ボタン: アナログスティック4 上"
                elif event.value == 1:
                    return "ボタン: アナログスティック4 下"
            elif event.axis == 5:  # アナログスティックの軸5
                if event.value == -1:
                    return "ボタン: アナログスティック5 左"
                elif event.value == 1:
                    return "ボタン: アナログスティック5 右"
        elif event.type == pygame.JOYHATMOTION:
            # ハットスイッチの入力をボタンとして扱う
            x, y = event.value
            if x == -1 and y == 1:
                return "ボタン: ハットスイッチ 左上"
            elif x == -1 and y == -1:
                return "ボタン: ハットスイッチ 左下"
            elif x == 1 and y == -1:
                return "ボタン: ハットスイッチ 右下"
            elif x == 1 and y == 1:
                return "ボタン: ハットスイッチ 右上"
            elif x == -1:
                return "ボタン: ハットスイッチ 左"
            elif x == 1:
                return "ボタン: ハットスイッチ 右"
            elif y == -1:
                return "ボタン: ハットスイッチ 下"
            elif y == 1:
                return "ボタン: ハットスイッチ 上"
            elif x == 0 and y == 0:
                return "ボタン: ハットスイッチ ニュートラル"
        elif event.type == pygame.JOYBUTTONUP:
            # ボタンが離されたイベントは無視
            continue
        else:
            return f"未処理のイベントタイプ: {event.type}"
    return False
