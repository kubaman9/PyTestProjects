import PySimpleGUI as sg

def createWindow(theme):
    sg.theme(theme)
    sg.set_options(font='Calibri 14', button_element_size=(6,3))
    buttonSize = (6,3)
    layout = [
        [sg.Text(
            '0', 
            key='-Output-', 
            font='Franklin 26', 
            justification='right', 
            expand_x=True, 
            pad=(10, 20),
            right_click_menu=themeMenu
            )],
        [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button('1', size = buttonSize), sg.Button('2', size = buttonSize), sg.Button('3', size = buttonSize), sg.Button('+', size = buttonSize)],
        [sg.Button('4', size = buttonSize), sg.Button('5', size = buttonSize), sg.Button('6', size = buttonSize), sg.Button('-', size = buttonSize)],
        [sg.Button('7', size = buttonSize), sg.Button('8', size = buttonSize), sg.Button('9', size = buttonSize), sg.Button('*', size = buttonSize)],
        [sg.Button('0', size = buttonSize, expand_x = True), sg.Button('/', size = buttonSize)],
    ]

    return sg.Window('Calculator', layout)

def updateOutput(text):
    window['-Output-'].update(text)

themeMenu = ['menu', ['LightGray1', 'dark', 'DarkGray8', 'random']]
window = createWindow('LightGray1')

currentNum = '0'
prevNum = ''
operation = ''

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in themeMenu[1]:
        window.close()
        window = createWindow(event)

    if event in ['0','1','2','3','4','5','6','7','8','9']:
        if currentNum == '0':
            currentNum = event
        else:
            currentNum += event
        updateOutput(currentNum)

    if event in ['+','-','*','/']:
        operation = event
        if prevNum != '':
            currentNum = '0'
        else:
            prevNum = currentNum
            currentNum = '0'
        updateOutput(currentNum)



    if event == 'Enter':

        match operation:
            case '+':
                currentNum = str(int(prevNum) + int(currentNum))
            case '-':
                currentNum = str(int(prevNum) - int(currentNum))
            case '*':
                currentNum = str(int(prevNum) * int(currentNum))
            case '/':
                currentNum = str(int(prevNum) / int(currentNum))
        
        updateOutput(currentNum)
        prevNum = ''
        operation = ''

    if event == 'Clear':
        updateOutput(0)
        currentNum = '0'
        prevNum = ''
        operation = ''

window.close()