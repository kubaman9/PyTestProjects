import PySimpleGUI as sg

layout = [
    [sg.Input(key='Input'), sg.Spin(['km to mile', ' kg to lb'], key='Spin'), sg.Button('Convert')],
    [sg.Text('Output:'), sg.Text('',key='Output')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Convert':
        match values['Spin']:
            case 'km to mile':
                output = str(int(values['Input']) * 0.6214)
                window['Output'].update(output)

            case 'kg to lb':
                output = str(int(values['Input']) * 2.20462)
                window['Output'].update(output)

window.close()