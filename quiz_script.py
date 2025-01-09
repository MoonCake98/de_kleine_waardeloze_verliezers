""""

"""

import tkinter as tk

mainframe = tk.Tk()
mainframe.title("SCIDD Quizzzzz")
mainframe.geometry("500x800")

counter = 0


def global_counter():
    global counter
    counter +=1
    print(counter)
    return

def first_question():
    butten_start.destroy()

    question_label = tk.Label(mainframe, text="very intresting quistion")
    question_label.grid(row=1, column=2 )
    q_1_a_1 = tk.Button(mainframe, text="Wrong awnser", command=second_quistion)
    q_1_a_1.grid(row=3, column=2)
    q_1_a_2 = tk.Button(mainframe, text="Good awnser", command=[second_quistion, global_counter])
    q_1_a_2.grid(row=4, column=2)
    return

def second_quistion():
    #destroy old
    return

butten_start = tk.Button(mainframe, text="start", command=first_question)
butten_start.grid(row=3, column=3, pady=4)

mainframe.mainloop()

