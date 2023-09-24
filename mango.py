from tkinter import *
import tkinter.ttk
from emailsender import *

def mango():
    style = tkinter.ttk.Style()
    style.configure("W.TButton", font=('calibri', 16))
    mango_win = Tk()
    mango_win.title('Mango Tree')
    mango_win.maxsize(3000, 700)
    mango_win.configure(bg='black')

    Label(mango_win, text='Mango Tree', font='calibri 35',fg='OliveDrab1',bg='black').pack(anchor=N)
    Label(mango_win, text='Steps and Measures to Grow Mango tree', font='Calibri 24',fg='OliveDrab1',bg='black').pack(anchor=NW)

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
    CheckVar27 = IntVar()
    CheckVar28 = IntVar()
    CheckVar29 = IntVar()

    C1 = Checkbutton(mango_win, text="1.Temperatures do not usually dip below 4 C", variable=CheckVar1, onvalue=1,
                     offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C2 = Checkbutton(mango_win,
                     text="2.The plant can thrive in almost any soil but requires well-drained soil  in a site with protection from cold.",
                     variable=CheckVar2, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C3 = Checkbutton(mango_win,
                     text="3.Position your tree where it will receive full sun for best fruit production.",
                     variable=CheckVar3, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C4 = Checkbutton(mango_win,
                     text="4.New mango tree planting is done in late winter to early spring when the plant is not actively growing.",
                     variable=CheckVar4, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C5 = Checkbutton(mango_win,
                     text="5.Prepare the site by digging a hole that is twice as wide and deep as the root ball.",
                     variable=CheckVar5, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C6 = Checkbutton(mango_win,
                     text="6.Check the drainage by filling the hole with water and watching how fast it drains.",
                     variable=CheckVar6, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C7 = Checkbutton(mango_win, text="7.Plant the young tree with the graft scar just at the soil surface.",
                     variable=CheckVar7, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C8 = Checkbutton(mango_win, text="8.Get a fresh mango pit and slit the hard husk.", variable=CheckVar8,
                     onvalue=1,
                     offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C9 = Checkbutton(mango_win, text="9.Remove the seed inside and plant it in seed starter mix in a large pot.",
                     variable=CheckVar9, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C10 = Checkbutton(mango_win,
                      text="10.Situate the seed with ¼-inch protruding above the soil surface when growing mango trees.",
                      variable=CheckVar10, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C11 = Checkbutton(mango_win,
                      text="11.Keep the soil evenly moist and place the pot where temperatures remain at least 70 F. (21 C.).",
                      variable=CheckVar11, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C12 = Checkbutton(mango_win, text="12.Water the trees deeply to saturate the long taproot.",
                      variable=CheckVar12,
                      onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C13 = Checkbutton(mango_win,
                      text="13.Withhold irrigation for two months prior to flowering and then resume once fruits begin to produce.",
                      variable=CheckVar13, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C14 = Checkbutton(mango_win,
                      text="14.Fertilize the tree with nitrogen fertilizer three times per year. Space the feedings and apply 1 pound per year of tree growth.",
                      variable=CheckVar14, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C15 = Checkbutton(mango_win,
                      text="15.Prune when the tree is four years old to remove any weak stems and produce a strong scaffold of branches. Thereafter, prune only to remove broken or diseased plant material.",
                      variable=CheckVar15, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    C16 = Checkbutton(mango_win,
                      text="16.Caring for mango trees must also include watching for pests and diseases. Deal with these as they occur with organic pesticides, cultural and biological controls or horticultural oils.",
                      variable=CheckVar16, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

    def nxt_page():
        next_page = Tk()
        next_page.title('mango')
        next_page.maxsize(3000, 700)
        next_page.configure(bg='black')

        Label(next_page, text='Diseases of mangoes', font='calibri 35',fg='OliveDrab1',bg='black').pack(anchor=NW)
        C17 = Checkbutton(next_page,
                          text="1. Anthracnose (Colletotrichum gloeosporioides) :-    Affects mangos most severely. In the case of anthracnose, mango disease symptoms appear as black, sunken, irregularly shaped lesions that grow resulting in blossom blight,\n leaf spotting, fruit staining and eventual rot.The disease is fostered by rainy conditions and heavy dews.",
                          variable=CheckVar17, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C18 = Checkbutton(next_page,
                          text="2.Powdery mildew :-   Affects leaves, flowers and young fruit. Infected areas become covered with a whitish powdery mold. As leaves mature,\n lesions along the midribs or underside of the foliage become dark brown and greasy looking. In severe cases, the infection will destroy flowering panicles resulting in a lack of fruit set and defoliation of the tree.",
                          variable=CheckVar18, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C19 = Checkbutton(next_page,
                          text="3.Mango scab (Elsinoe mangiferae) :-  Attacks leaves, flowers, fruit and twigs. The first signs of infection mimic the symptoms of anthracnose. Fruit lesions will be covered with a corky, brown tissue and leaves become distorted.",
                          variable=CheckVar19, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C20 = Checkbutton(next_page,
                          text="4.Verticillium wilt :-    Attacks the tree’s roots and vascular system, preventing the tree from up-taking water. Leaves begin to wilt, brown, and desiccate; stems and limbs die back; and the vascular tissues turn brown.\n The disease is most damaging to young trees and may even kill them.",
                          variable=CheckVar20, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C21 = Checkbutton(next_page,
                          text="5.Parasitic algal spot is another infection that more rarely afflicts mango trees. \nIn this case, mango disease symptoms present as circular greenish grey spots that turn rust red on the leaves. Infection of stems can lead to bark cankers and stem thickening and death.",
                          variable=CheckVar21, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        f = tkinter.ttk.Button(next_page, text='Mango tree treatments', style='W.TButton', command=tree_nxt)
        f.pack()

    def tree_nxt():
        tree_next = Tk()
        tree_next.title('mango')
        tree_next.maxsize(3000, 700)
        tree_next.configure(bg='black')

        C22 = Checkbutton(tree_next,
                          text='1.   Treating a sick mango for fungal diseases involves using a fungicide. All susceptible parts of the tree should be thoroughly coated with the fungicide before infection occurs.\n If applied when the tree is already infected, the fungicide will have no effect. Fungicide sprays need to be reapplied on new growth.',
                          variable=CheckVar22, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C23 = Checkbutton(tree_next,
                          text='2.    Apply fungicide in the early spring and again 10-21 days later to protect the panicles of blossoms during development and fruit set.',
                          variable=CheckVar23, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C24 = Checkbutton(tree_next,
                          text='3.    If powdery mildew is in evidence, apply sulfur to prevent the spread of the infection to new growth.',
                          variable=CheckVar24, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C25 = Checkbutton(tree_next,
                          text='4.   If the tree becomes infected with verticillium wilt, prune out any infected limbs. Mango scab generally doesn’t need to be treated since an anthracnose spray program also controls scab.\n Algal spot will also usually not be an issue when copper fungicides are periodically applied during the summer.',
                          variable=CheckVar25, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C26 = Checkbutton(tree_next,
                          text='5.   To reduce the risk of fungal infections, grow only anthracnose resistant cultivars of mango. Maintain a consistent and timely program for fungal application and \nthoroughly cover all susceptible parts of the tree. For assistance with treatment of disease, consult your local extension office for recommended control recommendations.',
                          variable=CheckVar26, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        e = tkinter.ttk.Button(tree_next, text='sun burn', style='W.TButton', command=sunburn)
        e.pack()

    def sunburn():
        burn_win = Tk()
        burn_win.title('Sun burn')
        burn_win.maxsize(1500, 700)
        burn_win.configure(bg='black')

        Label(burn_win, text='Sun burn and its prevention', font='calibri 19',fg='OliveDrab1',bg='black').pack()
        C27 = Checkbutton(burn_win,
                          text='1.    The importance of sunscreen in humans is indisputable but can mangoes get sunburnt? Sunburn occurs in many plants, whether fruiting or not. \n Mango trees are affected when grown in areas with temperatures that exceed 100 degrees Fahrenheit (38 C.).\n A combination of moisture and high sun and heat are the culprits of mango sun damage. Preventing mango sunburn occurs with either chemicals or covers. There are several studies on the most effective methods.',
                          variable=CheckVar27, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        C28 = Checkbutton(burn_win,
                          text='2.    Mangoes that have become sunburnt have some portion, usually the dorsal surface,\n that is dry and shrunken. The area appears necrotic, tan to brown, with darker lining the edges and some bleed around the area.\n Essentially, the area has been cooked by the sun, just as if you held a blowtorch to the fruit briefly. \nIt occurs when the sun is scorching and water or other sprays are present on the fruit. It is called the “lens effect” where the sun’s heat is magnified on the skin of the mango.',
                          variable=CheckVar28, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)

        Label(burn_win, text='Preventions', font='calibri 15',fg='OliveDrab1',bg='black').pack()

        C29 = Checkbutton(burn_win,
                          text='1.    use the plastic “mango hats” that are lined with wool. Embedded in the wool lining are beneficial bacteria and a copper compound to help combat any fungal or disease issues.',
                          variable=CheckVar29, onvalue=1, offvalue=0, justify='left',fg='OliveDrab1',bg='black',selectcolor='black').pack(anchor=NW)
        p = tkinter.ttk.Button(burn_win, text='continue', style='W.TButton', command=emailwin)
        p.pack()

    d = tkinter.ttk.Button(mango_win, text='Next page',style='W.TButton', command=nxt_page)
    d.pack()

    mango_win.minsize(1000, 600)
    mango_win.mainloop()