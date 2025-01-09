import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events = True, key='-Text-'), sg.Spin(['Item 1', 'Item 2'])],
    [sg.Button('Button', key = 'Button1')],
    [sg.Input(key='-Input-')],
    [sg.Text('Test'), sg.Button('Test Button', key = 'Button2')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Button1':
        window['-Text-'].update()

    if event == 'Button2':
        print('test')

    if event == '-Text-':
        print('test')

window.close()