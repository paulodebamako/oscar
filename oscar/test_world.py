from tkinter import *

def close_config():
    nb_Ah = Ah.get()
    root_config.destroy()
    print('toto')

    
def launch():
    root = Tk()
    root.title('OSCAR')
    root.geometry('750x750')
    root.minsize(750,750)
    for ligne in range(25):
        for colonne in range(25):
            case = Frame(root, bg='white', bd=1, height=30, width=30, highlightbackground='black', highlightcolor='black', highlightthickness=1)
            case.grid(row=ligne, column=colonne)
    root.mainloop()
    
#launch()
            
