import PySimpleGUI as sg


def show_get_robot():
    chosse_robot = [
        [
            sg.Text("Choose Robot", size=(30, 1),
                    justification='center', font=("Helvetica", 25)),

        ],
        [
            sg.Button('Robot 1', enable_events=True, key='-r1-'),

            sg.Button('Robot 2', enable_events=True, key='-r2-'),
            sg.Button('Robot 3', enable_events=True, key='-r3-')
        ],
        [
            sg.Button('Exit',  key='-x-'),
            sg.Button('Select', key='-x1-')

        ],
    ]

    layout = [
        [
            sg.Column(chosse_robot, size=(500, 400))
        ]
    ]

    window = sg.Window("Robot", layout)

    while True:
        event, values = window.read()
        if event == "-x-" or event == sg.WINDOW_CLOSED:
            r = [-1]
            break
        elif event == "-r1-":
            r = [1]


        elif event == "-r2-":
            r = [2]
        elif event == "-r3-":
            r = [3]
        elif event == "-x1-":
            window.close()
            show_get_sequence(r)
  

def show_get_sequence(robotValueArg):
    list1 = ["White", "Green", "Red", "Yellow"]
    chosse_secquence = [
        [
            sg.Text("Quick", size=(30, 1), justification='center',
                    font=("Helvetica", 25)),

        ],
        [
            sg.Button('Secquence 1', enable_events=True, key='-s1-'),

            sg.Button('Secquence 2', enable_events=True, key='-s2-')
        ]

    ]
    detaled = [
        [
            sg.Text("Detaled", size=(30, 1),
                    justification='center', font=("Helvetica", 25)),
        ],
        [
            sg.Combo(list1, size=(25, 100), readonly=True,
                     enable_events=True, key='-w-')
        ],
        [
            sg.Combo(list1, size=(25, 100), readonly=True,
                     enable_events=True, key='-g-')
        ],
        [
            sg.Combo(list1, size=(25, 100), readonly=True,
                     enable_events=True, key='-r1-')
        ],
        [
            sg.Combo(list1, size=(25, 100), readonly=True,
                     enable_events=True, key='-y-')
        ]
    ]
    button = [
        [
            
            sg.Button('Back',  key='-Back-'),
            sg.Button('Enter',  key='-x1-')


        ]
    ]

    layout = [
        [
            sg.Column(chosse_secquence)
        ],
        [
            sg.Column(detaled)
        ],
        [
            sg.Column(button)
        ]

    ]

    window = sg.Window("Secquence", layout)
    s = []

    while True:
        # s = []
        event, values = window.read()
        if event == "-x-" or event == sg.WINDOW_CLOSED:
            s = [-1]
            break
        elif event == "-Back-":
            window.close()
            show_get_robot()
        elif event == "-s1-":
            test = [1]
            s = test
        elif event == "-s2-":
            test = [2]
            s = test
        elif event == "-w-":
            test = values['-w-']
            s.append(test)
        elif event == "-g-":
            test = values["-g-"]
            s.append(test)
        elif event == "-r1-":
            test = values["-r1-"]
            s.append(test)
        elif event == "-y-":
            test = values["-y-"]
            s.append(test)

        elif event == "-x1-":
            window.close()
            show_get_timings(robotValueArg,s)
            # break


def show_get_timings(a,b):
    list1 = ["300", "400", "500", "600"]
    list2 = ["10", "20", "30", "40", '50', "60"]
    quick_select = [
        [
            sg.Text("Quick Select", size=(30, 1), font=("Helvetica", 25)),

        ],
        [
            sg.Text("Cycles", size=(15, 1), font=("Helvetica", 15))
        ],
        [
            sg.Combo(list1, size=(25, 100), readonly=True,
                     enable_events=True,  key='-c-')
        ],
        [
            sg.Text("Long", size=(15, 1), font=("Helvetica", 15))
        ],
        [
            sg.Combo(list2, size=(25, 100), readonly=True,
                     enable_events=True, key='-l-')
        ]

    ]

    button = [
        [
            sg.Button('Back',  key='-Back-'),
            sg.Button('Enter',  key='-x1-')


        ]
    ]

    layout = [
        [
            sg.Column(quick_select, justification='center')
     
        ],
        [
            sg.Column(button, justification='center')
        ]

    ]

    window = sg.Window("Timings", layout)
    while True:
        event, values = window.read()
        if event == "-x-" or event == sg.WINDOW_CLOSED:
            t = -1
            break
        
        elif event == '-Back-':
            window.close()
            show_get_sequence(a)
        elif event == '-c-':
            t = [values['-c-']]
        elif event == '-l-':
            t1 = [values['-l-']]
        elif event == '-x1-':
            window.close()
            show_get_running_process(a,b,t,t1)

array = []
    
def show_get_running_process(a,b,t,t1):

    array.clear()
    
    array.append(a)
    array.append(b)
    array.append(t)
    array.append(t1)
    
    list1 = ""

    running_process = [
        [
            sg.Text("Active Process", size=(50, 2), font=("Helvetica", 25)),

        ],
        [
            sg.Text(f"Robot:{a},Sequence:{b}, Timing: {t},{t1}", size=(
                50, 3), font=("Helvetica", 15))
        ]

    ]

    exit_button = [
        [
            sg.Button('ok', key='-x-')
        ]

    ]

    button = [
        [
            sg.Button('Home',  key='-Home-')
        ]
    ]
    layout1 = [
        [
            sg.Text("Do you want to Quit", size=(
                30, 1), font=("Helvetica", 25))
        ],
        [
            sg.Column(exit_button, justification='center')
        ]
    ]
    layout = [
        [
            sg.Column(running_process)
        ],
        [
            sg.Column(button, justification='center')
        ]

    ]

    window = sg.Window("Running Process", layout,size=(800, 300))
    while True:
        event, values = window.read()
        if event == "-x-":
            window1 = sg.Window("CLose", layout1)
            event, values = window1.read()
            if event == '-x1-' or event == sg.WIN_CLOSED:
                window.close()
            break
        elif event == '-Home-':
            # print(array)
            window.close()
            show_get_sequence(a)
        else:
            break


while True:
    test = show_get_robot()
    print(array)
    
    if test == -1:

        break
    break
