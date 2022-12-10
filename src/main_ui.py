import asyncio

import PySimpleGUI as sg

from main import Main


class Main_ui:

    def __init__(self):
        sg.theme('DarkAmber')  # デザインテーマの設定
        self.main = Main()
        # ウィンドウに配置するコンポーネント
        layout = [[sg.Text('ここは1行目')],
                  [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
                  [sg.Button('起動'), sg.Button('停止')]]

        # ウィンドウの生成
        self.window = sg.Window('サンプルプログラム', layout)

    # イベントループ
    async def ui(self, loop):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == '起動':
                devices = await self.main.scan()
                print(devices)
                await self.main.connect(devices, b'\x01', loop)
                print("ok")
            elif event == '停止':
                devices = await self.main.scan()
                print(devices)
                await self.main.connect(devices, b'\x00', loop)

                print('あなたが入力した値： ', values[0])

        self.window.close()


if __name__ == '__main__':
    main_ui = Main_ui()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_ui.ui(loop))
