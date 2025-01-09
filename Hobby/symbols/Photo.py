import PySimpleGUI as sg

control_col = sg.Column([
    [sg.Checkbox('Flip x', key='-FlipX-')],
    [sg.Button('Save Image', key='-Save-')]
])
image_col = sg.Column([[sg.Image('test.jpg')]])

layout = [
    [control_col, image_col]
]

window = sg.Window('Image Editor', layout)

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