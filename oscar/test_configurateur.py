from tkinter import *
from test_world import *

def generate_configurateur():    
    root_config = Tk()
    root_config.geometry('450x450')
    root_config.title('OSCAR LAUNCHER')
    root_config.minsize(450,450)

    global Ah 
    global nb_Ac 
    global nb_V 
    global nb_M 

    #generate label and entry for all categories of AGENT
    main_frame = Frame(root_config)
    frame1 = Frame(main_frame)
    label1 = Label(frame1, text="Entrez le nombre d'animaux herbivores", font=("Courrier",10)) 
    label1.pack()
    Ah = Entry(frame1, font=("Courrier",10))
    Ah.pack()
    #nb_Ah = Ah.get()
    frame1.pack()

    frame2 = Frame(main_frame)
    label2 = Label(frame2, text="Entrez le nombre d'animaux carnivores", font=("Courrier",10)) 
    label2.pack()
    nb_Ac = Entry(frame2, font=("Courrier",10))
    nb_Ac.pack()
    frame2.pack()

    frame3 = Frame(main_frame)
    label3 = Label(frame3, text="Entrez le nombre de vegetaux", font=("Courrier",10)) 
    label3.pack()
    nb_V = Entry(frame3, font=("Courrier",10))
    nb_V.pack()
    frame3.pack()

    frame4 = Frame(main_frame)
    label4 = Label(frame4, text="Entrez le nombre de mineraux", font=("Courrier",10)) 
    label4.pack()
    nb_M = Entry(frame4, font=("Courrier",10))
    nb_M.pack()
    frame4.pack()

    bouton = Button(main_frame, text='lancer la simulation', font=("Courrier",10), command=lambda:[launch(),close_config()])
    bouton.pack()
    main_frame.pack()
    root_config.mainloop()
    #print('herbi = ', nb_Ah)

generate_configurateur()
