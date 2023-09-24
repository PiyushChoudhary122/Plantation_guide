import tkinter.ttk
from emailsender import *
def mint():

    style = tkinter.ttk.Style()
    style.configure("W.TButton", font=('calibri', 16), relief='grooved', foreground='orange', background='black')

    mint_win = Tk()
    mint_win.title('Mint Plant')
    mint_win.maxsize(3000, 700)
    mint_win.configure(bg='black')

    Label(mint_win,
          text='Mint plant', font='calibri 30',fg='OliveDrab1',bg='black').pack(anchor=N)
    Label(mint_win,
          text='Steps and Measures to Grow mint plant', font='Calibri 16',fg='OliveDrab1',bg='black').pack(anchor=NW)
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    CheckVar9 = IntVar()
    CheckVar10 = IntVar()
    CheckVar11 = IntVar()
    CheckVar12 = IntVar()
    CheckVar13 = IntVar()
    CheckVar14 = IntVar()
    CheckVar15 = IntVar()
    CheckVar16 = IntVar()
    CheckVar17 = IntVar()
    CheckVar18 = IntVar()
    CheckVar19 = IntVar()
    CheckVar20 = IntVar()
    CheckVar21 = IntVar()
    CheckVar22 = IntVar()
    CheckVar23 = IntVar()
    CheckVar24 = IntVar()
    CheckVar25 = IntVar()
    CheckVar26 = IntVar()

    C1 = Checkbutton(mint_win,
                     text="1.Cut a 4 inch (10 cm) sprig about ½ inch (1 cm) above a junction to allow new branches to grow in its place.",
                     variable=CheckVar1, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C2 = Checkbutton(mint_win,
                     text='2.Place the sprig in a glass of water, and remove any leaves that fall below the water line.',
                     variable=CheckVar2, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C3 = Checkbutton(mint_win,
                     text="3.Purchase a mint seedling or small mint plant.",
                     variable=CheckVar3, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C4 = Checkbutton(mint_win,
                     text="4.Find a runner from a current plant. Runners are long stems that grow away from the current plant and set their own roots in the ground. These can be carefully dug up and transplanted.",
                     variable=CheckVar4, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C5 = Checkbutton(mint_win,
                     text="5.You should plant your mint in the spring, or in the fall if you're in a climate that is free of frost.",
                     variable=CheckVar5, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C6 = Checkbutton(mint_win,
                     text="6. Potting mint is the most popular way to grow it because you can easily keep it in check this way, as well as keeping it close to your kitchen so you can use it frequently. Mint spreads rapidly, and its roots have a tendency to choke out the roots of other plants.",
                     variable=CheckVar6, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C7 = Checkbutton(mint_win,
                     text="7.Plant the rooted sprig or seedling with the roots just below the soil. If planting multiple seedlings, plant them 6 inches (15 cm) apart. This will give each seedling enough room to grow.",
                     variable=CheckVar7, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C8 = Checkbutton(mint_win,
                     text="8. choose an area that receives morning sun and partial afternoon shade.",
                     variable=CheckVar8, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C9 = Checkbutton(mint_win,
                     text="9. During the first year that you have your mint, water it frequently.",
                     variable=CheckVar9, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C10 = Checkbutton(mint_win,
                      text="10.Trim the top of the plant.Horizontally",
                      variable=CheckVar10, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C11 = Checkbutton(mint_win,
                      text="11.Split your plant every two or three years.\n De-pot it and carefully split apart the mint into several plants. Lifting and replanting your mint every two to three or even three to four years will help keep the scent and the flavor of the mint nice and strong.",
                      variable=CheckVar11, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C12 = Checkbutton(mint_win,
                      text="12.Treat your mint with a fungicide spray if it gets infected by rust.",
                      variable=CheckVar12, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C13 = Checkbutton(mint_win,
                      text="13.Just provide good air circulation and soil that is well-drained to keep your plants healthy. If you notice any insects, spray them off with a garden hose..",
                      variable=CheckVar13, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    def harvest():
        harvest_win = Tk()
        harvest_win.title('mango')
        harvest_win.maxsize(3000, 700)
        harvest_win.configure(bg='black')

        Label(harvest_win, text='Harvest your mint ', font='calibri 30',fg='OliveDrab1',bg='black').pack(anchor=NW)

        C14 = Checkbutton(harvest_win,
                          text="1.Harvest fresh green leaves as desired from the late spring through the early autumn, To harvest the leaves, you should pinch off the stems",
                          variable=CheckVar14, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C15 = Checkbutton(harvest_win,
                          text='2.Harvest as much mint as possible before the frost each year.',
                          variable=CheckVar15, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        def precaution():
            precautions = Tk()
            precautions.title('precaution')
            precautions.configure(bg='black')

            Label(precautions, text='Precautions',fg='OliveDrab1',bg='black').pack(anchor=NW)
            Label(precautions,fg='OliveDrab1',bg='black').pack(anchor=NW)

            C16 = Checkbutton(precautions,
                              text="1.Add water to the glass as necessary. Make sure that you change the water every four to five days to prevent rot.",
                              variable=CheckVar16, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            C17 = Checkbutton(precautions,
                              text="2.You should add a water-retaining polymer to the potting soil so that it stays moist and doesn't dry up. You can also use pearlite or vermiculite instead of a polymer.",
                              variable=CheckVar17, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            C18 = Checkbutton(precautions,
                              text="3.Mint grows best in deep, moist soil, so you want to keep it that way. You can even place your mint pot indoors, on a windowsill, as long as it's in a location that will get enough sunlight. ",
                              variable=CheckVar18, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            C19 = Checkbutton(precautions,
                              text="4.growing mint in the ground require a fertile soil with a pH that is between 6.0 and 7.0.",
                              variable=CheckVar19, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            C20 = Checkbutton(precautions,
                              text="5.Make sure that the soil is moist by placing some mulch around the plant's roots to protect them.",
                              variable=CheckVar20, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            C21 = Checkbutton(precautions,
                              text="6.Submerge the container if planting in a flower bed.submerge your mint in a container, such as a pot or a mesh bag that is at least 5 inches (about 13 cm) deep.",
                              variable=CheckVar21, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            C22 = Checkbutton(precautions,
                              text="6.Keep the soil damp, but don't soak it. ",
                              variable=CheckVar22, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)
            C23 = Checkbutton(precautions,
                              text="7.You should trim the buds before they have a chance to open so the plant doesn't grow out of control.",
                              variable=CheckVar23, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            C24 = Checkbutton(precautions,
                              text='8.provide good air circulation and soil that is well-drained to keep your plants healthy.',
                              variable=CheckVar24, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            C25 = Checkbutton(precautions,
                              text='9. wash your leaves with insecticidal soap.',
                              variable=CheckVar25, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            C26 = Checkbutton(precautions,
                              text='10.Make sure to look for pests under the leaves of the plants, too. This is a place where they like to hide.',
                              variable=CheckVar26, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

            p = tkinter.ttk.Button(precautions,text='continue',style='W.TButton',command=emailwin)
            p.pack()

        a = tkinter.ttk.Button(harvest_win, text='Precautions', style='W.TButton', command=precaution)
        a.pack()

    b = tkinter.ttk.Button(mint_win, text='Harvest', style='W.TButton', command=harvest)
    b.pack()
    mint_win.mainloop()
