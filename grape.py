from tkinter import *
import tkinter.ttk
from emailsender import *

def grape():
    grape_win = Tk()
    grape_win.title('Grape vine')
    grape_win.maxsize(3000, 700)
    grape_win.configure(bg='black')

    style = tkinter.ttk.Style()
    style.configure('W.TButton', font=('calibri', 16))

    Label(grape_win,
          text='Grape vine', font='calibri 30',fg='OliveDrab1',bg='black').pack(anchor=N)
    Label(grape_win,
          text='Steps and Measures to Grow Grape Vine', font='Calibri 20',fg='OliveDrab1',bg='black').pack(anchor=NW)
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

    C1 = Checkbutton(grape_win,
                     text="1.Within each general type of grapevine, there are multiple species to choose from which each offer up their own flavor, color, texture, and size. Visit a local nursery to find one that fits your needs and environment.\n Select plants that look healthy and strong, and are 1 year old.\n When possible, get them certified virus-free to ensure that their healthy growth is continued.Look for plants that have an even root distribution, and whose canes are symmetrical.",
                     variable=CheckVar1, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C2 = Checkbutton(grape_win,
                     text='2.make sure that the location you select is a permanent one that will offer up plenty of room for future grapevines.\n plant your grapevines on a downward slope on a south-facing hill, in an area clear of other trees and large plants.',
                     variable=CheckVar2, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C3 = Checkbutton(grape_win,
                     text="3. Use soil that slightly rocky or sandy with a pH just above 7.\n Amend the soil to promote good drainage if necessary, as water-logged roots are not conducive to healthy growing grapevines.",
                     variable=CheckVar3, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C4 = Checkbutton(grape_win,
                     text="4.Prepare a trellis for your grapevines.",
                     variable=CheckVar4, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C5 = Checkbutton(grape_win,
                     text="5.Wait to plant your grapevines until a frost-free day in late winter or early spring. Pruning should happen around this time in upcoming years as well.\n Contact your local agricultural service for exact planting dates.",
                     variable=CheckVar5, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C6 = Checkbutton(grape_win,
                     text="6.Depending on the species of grapes you are planting, spacing will be different for each plant. For American and European grapes, plant each vine 6–10 feet (1.8–3.0 m) apart. Muscadines require much more space, and \n should be planted approximately 16 feet (4.9 m) apart.Plant the cuttings in a trench with the basal and center bud covered. The top bud should be just above the soil surface.\n Press the soil firmly around the newly planted grapevine cuttings.",
                     variable=CheckVar6, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C7 = Checkbutton(grape_win,
                     text="7.Grapevines don’t prefer heavy water or rain, so after the first watering keep the amount of water you give them to a minimum.\n Keep water near the roots so that the majority of it gets absorbed rather than evaporated by the sun.\n If your area doesn’t get much rain, set up a drip system directly at the roots so that the grapevines get small amounts of water on a regular basis.",
                     variable=CheckVar7, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C8 = Checkbutton(grape_win,
                     text="8.The first year, the grapevine should not be allowed to produce any fully matured fruits as these can damage the young vine with their weight.\n Cut back all the fruit, as well as all the vines except for the strongest that branch off the cane.\n In later years prune as needed following established local practices, and prune back 90% of the new growth on older vines each year.",
                     variable=CheckVar8, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C9 = Checkbutton(grape_win,
                     text="9. Always always prune grapevines when they are dormant. They will otherwise bleed their sap - losing vigour.\n This is typically in late winter when it is no longer cold ",
                     variable=CheckVar9, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C10 = Checkbutton(grape_win,
                      text="10. A layer of mulch around your plants will regulate soil temperature, retain water, and reduce weeds.",
                      variable=CheckVar10, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C11 = Checkbutton(grape_win,
                      text="11. Little pest control is needed as grapevines are naturally hardy. Keep weeds at bay by hand-weeding on a regular basis, and cover you grapevines in bird net to keep birds away if necessary. ",
                      variable=CheckVar11, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C12 = Checkbutton(grape_win,
                      text="12.Strong, edible fruit likely won’t appear for anywhere from 1-3 years.When it appears, test its ripeness by \n \t picking a few grapes from different areas and tasting them.If the grapes are sweet, start picking as they ready for harvesting and eating.",
                      variable=CheckVar12, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    def nxt_page():
        next_page = Tk()
        next_page.title('mango')
        next_page.maxsize(3000, 700)
        next_page.configure(bg='black')

        Label(next_page, text='Precautions ', font='calibri 35',fg='OliveDrab1',bg='black').pack(anchor=NW)

        C13 = Checkbutton(next_page,
                          text="1.Cut the sections directly from the vine or from brush that has recently been pruned off. Make sure the cutting is 3 nodes long \n (the nodes will look like bumps). At the bottom of the cutting, make the cut at an angle. This cut should be at 45 degrees and 1/4 to 1-inch above the node.",
                          variable=CheckVar13, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C14 = Checkbutton(next_page,
                          text="2.When taking cuttings, plant as many as possible - in as many locations as possible - to have a higher chance of success. Surplus plants can be given away.",
                          variable=CheckVar14, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C15 = Checkbutton(next_page,
                          text='3.In cold areas be sure to plant the grapevines in a sunny area, preferably facing south. A southern facing location may prevent frost \n nipping the vines. Also avoid "frost pockets" such as low-lying areas or the base of a slope, where cold air can pool and ruin a crop.',
                          variable=CheckVar15, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C16 = Checkbutton(next_page,
                          text="4. Avoid heavily fertilized soil when possible, and follow recommendations from a soil test result",
                          variable=CheckVar16, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C17 = Checkbutton(next_page,
                          text="5.Don’t use a single stake while preparing trellis as this won’t provide enough support for your vines once they start growing. ",
                          variable=CheckVar17, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C18 = Checkbutton(next_page,
                          text="6. Don’t bury the vine cane any higher than the first bud, but make sure the roots are completely covered in soil.",
                          variable=CheckVar18, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C19 = Checkbutton(next_page,
                          text="7.Be sure to plant the grapevines so they receive enough airflow to prevent powdery mildew.",
                          variable=CheckVar19, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)
        C20 = Checkbutton(next_page,
                          text="8.Grapes will not continue to ripen after picking (as is the case with other fruits) so be sure not to pick them prematurely.",
                          variable=CheckVar20, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)
        C21 = Checkbutton(next_page,
                          text="9.Color and size are not necessarily a good indication of ripe fruit. Only pick the fruit after you’ve tasted it and are certain it is ready.",
                          variable=CheckVar21, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        p = tkinter.ttk.Button(next_page, text='continue', style='W.TButton', command=emailwin)
        p.pack()
    c = tkinter.ttk.Button(grape_win, text='Precautions', style='W.TButton', command=nxt_page)
    c.pack()
    grape_win.mainloop()
