import PySimpleGUI as sg
import random
import string

BOX_SIZE = 15
znak = "X"
pole = [[0 for _ in range(20)] for _ in range(20)]

layout = [
    [sg.Text('Piškvorky'), sg.Text('', key='-OUTPUT-')],
    [sg.Graph((600, 600), (0, 300), (300, 0), key='-GRAPH-',
              change_submits=True, drag_submits=False, background_color='white')],
    [sg.Button('Exit')]
]

window = sg.Window('Piškvorky', layout, finalize=True)
g = window['-GRAPH-']

for row in range(20):
    for col in range(20):
         g.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black')



while True:           
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    mouse = values['-GRAPH-']
           
    if event == '-GRAPH-':
        if mouse == (None, None):
            continue
        box_x = mouse[0]//BOX_SIZE
        box_y = mouse[1]//BOX_SIZE
        letter_location = (box_x * BOX_SIZE + 8, box_y * BOX_SIZE + 8)
        print(box_x, box_y)
 

    

    if (pole[int(box_x)][int(box_y)] == 0):
        pole[int(box_x)][int(box_y)] = znak
    else:
        continue

    if(znak == "X"):
        znak ="O"
        color ='red'
    else:
        znak ="X"
        color = 'blue'

    g.draw_text('{}'.format(znak),
            letter_location, font='Courier 25', color = color)
    
        

                    
window.close()