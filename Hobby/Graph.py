import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def UpdateFig(data):
    axes = fig.axes
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    axes[0].plot(x,y,'g-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

sg.theme('dark')
tableContent = []
layout = [
    [sg.Table(headings=['Observations', 'Results'], values=tableContent, expand_x=True, expand_y=True, hide_vertical_scroll=True, key='-Table-', font='Calibri 20')],
    [sg.Input(key='-Input-', expand_x=True, font='20'), sg.Button('Submit')],
    [sg.Canvas(key='-Canvas-', expand_x=True, expand_y=True)]
]

window = sg.Window('Graphing App', layout, finalize=True, resizable=True)

tableVals = []

fig = plt.figure(figsize = (5,4))
fig.add_subplot(111).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(fig, window['-Canvas-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        nv = values['-Input-']
        if nv.isnumeric():
            tableVals += [[len(tableVals) + 1, float(nv)]]
            window['-Table-'].update(tableVals)
            window['-Input-'].update('')
            UpdateFig(tableVals)


window.close()