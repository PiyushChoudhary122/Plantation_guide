from tkinter import ttk
from mint import *
from mango import *
from grape import *


def choose():
    choice_win = Tk()
    choice_win.title("choice window")
    choice_win.configure(bg='black')

    style = ttk.Style()
    style.configure("W.TButton", font=('calibri', 16), relief='grooved', foreground='orange', background='black')

    # Add a grid
    mainframe = Frame(choice_win)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    # Create a Tkinter variable
    sapling = StringVar(choice_win)

    # Dictionary with options
    choices = {'Select....', 'Mango', 'Mint', 'Grapes'}
    sapling.set('Select....')  # set the default option

    popupmenu = OptionMenu(mainframe, sapling, *choices)
    popupmenu.configure(fg='OliveDrab1', bg='black')
    Label(mainframe, text="Choose a Sapling", fg='OliveDrab1', bg='black').grid(row=1, column=1)
    popupmenu.grid(row=2, column=1)
    global x
    x = ttk.Button(choice_win, style="W.TButton")
    x.pack()

    def label_print(*args):
        global x, val
        val = 0
        x.pack_forget()
        if sapling.get() == 'Mango':
            val = 1
        if sapling.get() == 'Grapes':
            val = 2
        if sapling.get() == 'Mint':
            val = 3

        if val == 1:
            x = ttk.Button(choice_win, text='Mango tree', style="W.TButton", command=mango)
            x.pack()
        if val == 2:
            x = ttk.Button(choice_win, text='Grape Vine', style="W.TButton", command=grape)
            x.pack()
        if val == 3:
            x = ttk.Button(choice_win, text='Mint plant', style="W.TButton", command=mint)
            x.pack()
        else:
            val = 0

    # link function to change dropdown
    sapling.trace('w', label_print)

    choice_win.mainloop()

