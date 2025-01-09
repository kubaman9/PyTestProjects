import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests
import time as tm

def get_weather_data(location):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    url = f'https://www.google.com/search?q=weather+{location.replace(" ","")}'
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    html = session.get(url)
    
    soup = bs(html.text, "html.parser")
    time = soup.find("div", attrs={'id': 'wob_dts'}).text
    weather = soup.find("span", attrs={'id': 'wob_dc'}).text
    temp = soup.find("span", attrs={'id': 'wob_tm'}).text
    return time, weather, temp

sg.theme('dark')
image_col = sg.Column([[sg.Image(key='-Image-', background_color='#FFFFFF')]])
info_col = sg.Column([
    [sg.Text('', key='-Location-', font='Calibri 30', pad=0, visible=False)],
    [sg.Text('', key='-Temp-', font='Calibri 16', text_color='#FFFFFF', pad=0, visible=False)],
    [sg.Text('', key='-Time-', font='Calibri 16', text_color='#FFFFFF', pad=(0,10), visible=False, justification='center')]          
])

layout = [
    [sg.Text('Enter City', expand_x=True)],
    [sg.Input(key='-Input-', expand_x=True), sg.Button('Enter', border_width=0)],
    [image_col, info_col]
]

window = sg.Window('Weather', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Enter':
        time, weather, temp = get_weather_data(values['-Input-'])
        window['-Location-'].update(values['-Input-'],visible=True)
        window['-Time-'].update(time,visible=True)
        window['-Temp-'].update(temp + " degrees",visible=True)

        if weather in ('Partly cloudy','Mostly cloudy','Cloudy','Overcast'):
                window['-Image-'].update(filename='symbols/cloudy.png')
        if weather in ('Partly sunny', 'Mostly Sunny'):
                window['-Image-'].update(filename='symbols/partsun.png')
        if weather in ('Rain','Chance of Rain','Light Rain','Showers','Scattered Showers','Rain and Snow','Hail'):
                window['-Image-'].update(filename='symbols/rain.png')
        if weather in ('Freezing Drizzle','Chance of Snow','Sleet','Snow','Icy','Snow Showers'):
                window['-Image-'].update(filename='symbols/snow.png')
        if weather in ('Scattered Thunderstorms','Chance of Storm','Storm','Thunderstorm','Chance of TStorm'):
                window['-Image-'].update(filename='symbols/thunder.png')
        if weather in ('Sun','Sunny','Clear','Clear with periodic clouds', 'Mostly sunny'):
                window['-Image-'].update(filename='symbols/sun.png')

window.close()