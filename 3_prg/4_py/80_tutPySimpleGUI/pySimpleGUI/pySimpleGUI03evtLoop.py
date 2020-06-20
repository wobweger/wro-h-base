import PySimpleGUI as sg      

sg.change_look_and_feel('DarkAmber')    # Remove line if you want plain gray windows

layout = [[sg.Text('Persistent window')],      
          [sg.Input(key='-IN-')],      
          [sg.Button('Read'), sg.Exit()]]      

window = sg.Window('Window that stays open', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event in (None, 'Exit'):      
        break      

window.close()