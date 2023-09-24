import os
import turtle


def tree(branchLen, t):
    if branchLen > 10:
        t.speed(0)
        t.forward(branchLen)
        t.right(40)
        tree(branchLen - 30, t)
        t.left(80)
        tree(branchLen - 30, t)
        t.right(40)
        t.backward(branchLen)


def main():
    mywindow = turtle.Screen()
    mywindow.title(' tree')
    mywindow.bgcolor("black")
    t = turtle.Turtle()
    t.width(10)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("silver")
    tree(150, t)
    t.hideturtle()
    t.penup()
    t.goto(0, -240)
    t.pendown()
    t.write('ElectroTree', align='center', font='Acropolis 40')
    mywindow.exitonclick()


main()

# main window screen

root = Tk()
root.title('Project')
root.configure(bg='black')

h = Label(root, text='Welcome to project tree ', font='clibryl 40', fg='OliveDrab1', bg='black')
h.pack()


l = Label(root,text="Forests are the lungs of our land, purifying the air and giving freshstrength to our people. ” Trees are indispensable for life. Man can’t live without trees.However,the present condition of forests in the world,especially developing countries is pathetic and miserable. Forests are thesource of life. They are the giving angels. They give man oxygen, rains, wood,fruit, make the world look so beautiful, yet the sinister man kills them! Who will be more inhumane than man himself? Cutting of forests ultimately endangers man’s own existence. \n \n Most of the world oxygen that the animal species including man inhale is produced in the forests and tropical rainforests.Forests and rainforests house millions of species of plants, animals and insects. Even more importantly, they are home to many unique plants and animals that do not exist anywhere else in the world. If the tropical rainforests were to be destroyed, so would the homes of all these species.Without a home, many of these species could become extinct.Trees are important to the environment;  they recycle water and process carbon dioxide in the atmosphere through photosynthesis. They are the world's full-time purifiers of air and water. Their cutting will disturb the natural water cycles which will lead to the shortage of fresh-water in the water reserves of the world.Cutting of trees will have a negative effect on the environment. It will result in an increase in the amount of carbon and other greenhouse gases in the environment. Burning of these forests will result in the emission of a large amount of carbon dioxide into the air. Carbon dioxide and other greenhouse gases like the oxides of nitrogen and methane are known to trap atmospheric heat, thus increasing the average temperature of the Earth's surface. This increase in the temperature near the Earth's surface and oceans is termed as global warming. \n \n Extreme weather conditions, changing agricultural production, and increase in the disease carrying viruses are some of the other effects of global warming. Deforestation is the primary reason behind global warming; we need to show greater concern towards the cutting of trees on a large scale. We need to take quick measures for preventing deforestation of the tropical forests so that we can hope for an environment that is healthy to live in.\n \n So, we see how crucial trees are for evolution and the smooth running of all the life forms on the planet. They are indeed the power-house of evolution. It is our bounden duty to plant and preserve trees and forests as without them we can’t exist.\n\n SO I HOPE EVERYONE SHOULD TAKE A SMALL STEP AND PLANT A TREE!!!",anchor='center', justify='left', wraplength=900, font='Calibri', fg='OliveDrab1', bg='black')
l.pack()

style = tkinter.ttk.Style()
style.configure("W.TButton", font=('calibri', 10), relief='grooved', foreground='orange', background='black')


def choose_win():
    choose()


def registration():
    creds = 'tempfile.temp'

    def Signup():
        global pwordE  # These globals just make the variables global to the entire script, meaning any definition can use them
        global nameE
        global roots

        roots = Tk()
        roots.title('Signup')
        root.configure(bg='black')

        style = tkinter.ttk.Style()
        style.configure("W.TButton", font=('algerian', 16), relief='grooved', foreground='orange', background='black')

        intruction = Label(roots,text='Please Enter new Credidentials\n', fg='OliveDrab1', bg='black')
        intruction.grid(row=0, column=0, sticky=E)

        nameL = Label(roots, text='New Username: ', fg='OliveDrab1', bg='black')
        pwordL = Label(roots, text='New Password: ', fg='OliveDrab1', bg='black')
        nameL.grid(row=1, column=0,sticky=W)  # Same thing as the instruction var just on different rows. :) Tkinter is like that.
        pwordL.grid(row=2, column=0, sticky=W)

        nameE = Entry(roots)  # This now puts a text box waiting for input.
        pwordE = Entry(roots,show='*')  # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
        nameE.grid(row=1, column=1)
        pwordE.grid(row=2, column=1)
        signupButton = tkinter.ttk.Button(roots, text='Signup', style="W.TButton", command=FSSignup)
        signupButton.grid(columnspan=2, sticky=W)
        roots.mainloop()

    def FSSignup():
        with open(creds, 'w') as f:  # Creates a document using the variable we made at the top.
            f.write(
                nameE.get())
            f.write('\n')  # Splits the line so both variables are on different lines.
            f.write(pwordE.get())  # Same as nameE just with pword var
            f.close()

        roots.destroy()  # This will destroy the signup window.
        Login()

    def Login():
        global nameEL
        global pwordEL
        global rootA

        rootA = Tk()
        rootA.title('Login')
        rootA.configure(bg='black')

        style = tkinter.ttk.Style()
        style.configure("W.TButton", font=('calibri', 16), relief='grooved', foreground='red', background='black')

        intruction = Label(rootA, text='Please Login\n', fg='OliveDrab1', bg='black')
        intruction.grid(sticky=E)

        nameL = Label(rootA, text='Username: ', fg='OliveDrab1', bg='black')
        pwordL = Label(rootA, text='Password: ', fg='OliveDrab1', bg='black')
        nameL.grid(row=1, sticky=W)
        pwordL.grid(row=2, sticky=W)

        nameEL = Entry(rootA, fg='OliveDrab1', bg='black')
        pwordEL = Entry(rootA, show='*', fg='OliveDrab1', bg='black')
        nameEL.grid(row=1, column=1)
        pwordEL.grid(row=2, column=1)

        loginB = tkinter.ttk.Button(rootA, text='Login', style="W.TButton", command=CheckLogin)
        loginB.grid(columnspan=2, sticky=W)

        rmuser = tkinter.ttk.Button(rootA, text='Delete User', style="W.TButton", command=DelUser)
        rmuser.grid(columnspan=2, sticky=W)
        rootA.mainloop()

    def CheckLogin():
        with open(creds) as f:
            data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
            uname = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
            pword = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it

        if nameEL.get() == uname and pwordEL.get() == pword:  # Checks to see if you entered the correct data.
            r = Tk()
            r.title(':D')
            r.geometry('150x50')
            r.configure(bg='black')

            style = tkinter.ttk.Style()
            style.configure("W.TButton", font=('calibri', 16), relief='grooved', foreground='orange',
                            background='black')

            rlbl = Label(r, text=' Logged In', fg='OliveDrab1', bg='black')
            rlbl.pack()
            z = tkinter.ttk.Button(r, text='Continue', style="W.TButton", command=choose_win)
            z.pack()
            r.mainloop()
        else:
            r = Tk()
            r.title('D:')
            r.geometry('150x50')
            r.configure(bg='black')

            style = tkinter.ttk.Style()
            style.configure("W.TButton", font=('calibri', 16), relief='grooved', foreground='orange',
                            background='black')

            rlbl = Label(r, text='\n[!] Invalid Login', fg='OliveDrab1', bg='black')
            rlbl.pack()
            r.mainloop()

    def DelUser():
        os.remove(creds)
        rootA.destroy()
        Signup()

    if os.path.isfile(creds):
        Login()
    else:
        Signup()


start = ttk.Button(root, text="Let's Plant", style='W.TButton', command=registration)
start.place(x=550, y=650)

root.resizable(TRUE, TRUE)

root.mainloop()
