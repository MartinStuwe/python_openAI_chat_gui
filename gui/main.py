import PySimpleGUI as sg
from gpt.main import ask_gpt


def start_gui():
    layout = [
                [sg.Text('Hello from PySimpleGUI')],
                [sg.Button('OK'), sg.Button('Close Window')],
                [sg.Multiline(size=(45, 5), key='textbox')],
                [sg.Text("", key='output', size=(45, 5))]]

    window = sg.Window('Text', layout).Finalize()

    while True:
        event, values = window.read()
        if event in (None, 'Close Window'):
            break
        print('You entered ', values['textbox'])
        answer = ask_gpt(values['textbox'])
        print(answer)
        window['output'].update(answer)


if __name__ == '__main__':
    start_gui()