import PySimpleGUI as sg      

layout = [ [sg.Txt('Enter values to calculate')],      
            [sg.In(size=(8,1), key='numerator')],      
            [sg.Txt('_'  * 10)],      
            [sg.In(size=(8,1), key='denominator')],      
            [sg.Txt('', size=(8,1), key='output')  ],      
            [sg.Button('Calculate', bind_return_key=True)]]      

window = sg.Window('Math', layout)      

while True:      
    event, values = window.read()      

    if event is not None:      
        try:      
            numerator = float(values['numerator'])      
            denominator = float(values['denominator'])      
            calc = numerator / denominator      
        except:      
            calc = 'Invalid'      

        window['output'].update(calc)      
    else:      
        break 
