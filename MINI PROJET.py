# ##############################################################
                           # IMPORT #
# ##############################################################

from tkinter import*
from tkinter.filedialog import*
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

# #########################################################
                    # FENETRE 2 / NUAGE #
# #########################################################

def Nuage():
    Fenetre2 = Tk()
    Fenetre2.title("Nuage de mot")
    Fenetre2.geometry("1500x800")
    Fenetre2.resizable(False, False)
    canvas = Canvas(Fenetre2)


    # ################ #
        # Nuage #
    # ################ #
    canvas.create_text(701, 575, anchor=SE, font=("Purisa", 70),fill=Couleur[0],
        text=Final[0])
    canvas.create_text(735, 655, anchor= W, font=("Purisa", 65),fill=Couleur[1],angle=90,
        text=Final[1])
    canvas.create_text(770, 393, anchor= W, font=("Purisa", 60),fill=Couleur[2],
        text=Final[2])
    canvas.create_text(605, 485, anchor=SE, font=("Purisa", 55),fill=Couleur[3],
        text=Final[3])
    canvas.create_text(698, 558, anchor=NE, font=("Purisa", 45),fill=Couleur[4],
        text=Final[4])
    canvas.create_text(770, 458, anchor= W, font=("Purisa", 45),fill=Couleur[5],
        text=Final[5])
    canvas.create_text(810, 301, anchor=NW, font=("Purisa", 40),fill=Couleur[6],
        text=Final[6])
    canvas.create_text(655, 483, anchor=SW, font=("Purisa", 38),fill=Couleur[7],angle=90,
        text=Final[7])
    canvas.create_text(705, 485, anchor=SW, font=("Purisa", 38),fill=Couleur[8],angle=90,
        text=Final[8])
    canvas.create_text(800, 504, anchor= W, font=("Purisa", 37),fill=Couleur[9],
        text=Final[9])
    canvas.create_text(605, 413, anchor=SE, font=("Purisa", 35),fill=Couleur[10],
        text=Final[10])
    canvas.create_text(765, 353, anchor=NW, font=("Purisa", 35),fill=Couleur[11],angle=90,
        text=Final[11])
    canvas.create_text(700, 660, anchor=SE, font=("Purisa", 30),fill=Couleur[12],
        text=Final[12])
    canvas.create_text(768, 650, anchor=NE, font=("Purisa", 30),fill=Couleur[13],
        text=Final[13])
    canvas.create_text(840, 275, anchor=NW, font=("Purisa", 25),fill=Couleur[14],
        text=Final[14])
    canvas.create_text(803, 490, anchor=NW, font=("Purisa", 25),fill=Couleur[15],angle=-90,
        text=Final[15])
    canvas.create_text(820, 523, anchor=NW, font=("Purisa", 21),fill=Couleur[16],
        text=Final[16])
    canvas.create_text(605, 368, anchor=SE, font=("Purisa", 20),fill=Couleur[17],
        text=Final[17])
    canvas.create_text(810, 305, anchor=NW, font=("Purisa", 20),fill=Couleur[18],angle=90,
        text=Final[18])
    canvas.create_text(820, 549, anchor=NW, font=("Purisa", 17),fill=Couleur[19],
        text=Final[19])
    canvas.create_text(820, 525, anchor=NW, font=("Purisa", 15),fill=Couleur[20],angle=-90,
        text=Final[20])
    canvas.create_text(605, 340, anchor=SE, font=("Purisa", 13),fill=Couleur[21],
        text=Final[21])
    canvas.create_text(820, 570, anchor=NW, font=("Purisa", 10),fill=Couleur[22],
        text=Final[22])
    canvas.create_text(840, 280, anchor=NW, font=("Purisa", 10),fill=Couleur[23],angle=90,
        text=Final[23])
    canvas.create_text(870, 267, anchor=NW, font=("Purisa", 9),fill=Couleur[24],
        text=Final[24])
    canvas.create_text(855, 279, anchor=NW, font=("Purisa", 8),fill=Couleur[25],angle=90,
        text=Final[25])
    canvas.create_text(870, 260, anchor=NW, font=("Purisa", 6),fill=Couleur[26],
        text=Final[26])
    canvas.create_text(605, 323, anchor=SE, font=("Purisa", 6),fill=Couleur[27],
        text=Final[27])
    canvas.create_text(870, 253, anchor=NW, font=("Purisa", 5),fill=Couleur[28],
        text=Final[28])

    # ################ #
        # Compteur #
    # ################ #

    canvas.create_text(145, 5, anchor=NW, font=("Purisa", 10),fill="#050439",
        text=NbLettres)
    canvas.create_text(145, 20, anchor=NW, font=("Purisa", 10),fill="#050439",
        text=NbMots)
    canvas.create_text(145, 35, anchor=NW, font=("Purisa", 10),fill="#050439",
        text=NbPhrases)
    canvas.create_text(145, 50, anchor=NW, font=("Purisa", 10),fill="#050439",
        text=Nbcaractere)
    canvas.create_text(110, 65, anchor=NW, font=("Purisa", 10),fill="#050439",
        text=Chemin)
    canvas.create_text(5, 5, anchor=NW, font=("Purisa", 10),fill="#050439",
        text="Nombre de lettres :")
    canvas.create_text(5, 20, anchor=NW, font=("Purisa", 10),fill="#050439",
        text="Nombre de mots :")
    canvas.create_text(5, 35, anchor=NW, font=("Purisa", 10),fill="#050439",
        text="Nombre de phrases :")
    canvas.create_text(5, 50, anchor=NW, font=("Purisa", 10),fill="#050439",
        text="Compteur personalisé :")
    canvas.create_text(5, 65, anchor=NW, font=("Purisa", 10),fill="#050439",
        text="Chemin d'accés :")

    canvas.pack(fill=BOTH, expand=1)
    Fenetre2.mainloop()

# ##############################################################
                      # MECANISME #
# ##############################################################

    # ################ #
        # Couleur #
    # ################ #
def Couleur():
    global Couleur
    Couleur = ["#050439","#0A094E","#0A094E","#07058A","#052594","#052594","#052594","#04459F","#04459F","#04459F","#04459F","#04459F","#04459F","#04459F","#0265A9","#0265A9","#0265A9","#0265A9","#0265A9","#0185B4","#0185B4","#0185B4","#0185B4","#0185B4","#00A5BF","#00A5BF","#00A5BF","#00A5BF","#00A5BF"]

    # ################ #
        # Random #
    # ################ #

def Random():
    global Couleur
    Rand = lambda: random.randint(0,255)
    Couleur = []
    for i in range (0,29):
        Couleur.append('#%02X%02X%02X' % (Rand(),Rand(),Rand()))

    # ################ #
        # Compteur #
    # ################ #

def Count(a):
    global NbLettres,NbMots,NbPhrases,Nbcaractere
    TexteO = text.get(1.0, END)
    TexteO.replace('...','.').replace('?','.').replace('!','.')
    NbLettres = len(TexteO)
    NbMots = len(TexteO.split())
    NbPhrases = TexteO.count(".")
    if a == "0":
        Nbcaractere = "---"
    else:
        Nbcaractere = TexteO.count(a)

    # ############### #
        # Ouvrir #
    # ############### #

def Browse():
    global Chemin
    Tk().withdraw()
    adresse = askopenfilename(title="Ouvrir un fichier Texte",filetypes=[('txt files','.txt'),('all files','.*')])
    TexteFichier = open(adresse,'r')
    TexteOriginal = TexteFichier.read()
    text.delete('1.0', END)
    text.insert(INSERT, TexteOriginal)
    Chemin = adresse

    # ############### #
        # Coller #
    # ############### #

def Paste():
    global Chemin
    root = tk.Tk()
    root.withdraw()
    Clipboard = root.clipboard_get().replace('...','.')
    text.delete('1.0', END)
    text.insert(INSERT, Clipboard)
    Chemin = "Presse-Papier"

    # ############### #
       # Mecanisme #
    # ############### #

def Executer():
    Texte = text.get(1.0, END)
    Texte = Texte.replace('\n','').replace('\t','').replace('.','').replace('--','-')
    Texte = Texte.replace(',','').replace("l'",'').replace("d'",'').replace('é','e').replace('è','e').upper()
    List = dict()
    Mots = Texte.split()
    for Mot in Mots:
        if Mot in List:
            List[Mot] += 1
        else:
            List[Mot] = 1
    Texte = List
    Texte = sorted(Texte.items(), key=lambda t: t[1])
    global Final
    Final = []
    for i in range(1,len(Texte)):
        if len(Texte[-i][0]) > 5:
            Final.append(Texte[-i][0])
    Fenetre1.destroy()
    Nuage()

    # ############### #
         # Check #
    # ############### #

def Check():
    Texte = text.get(1.0, END)
    if len(Texte) < 35:
        messagebox.showinfo("Erreur", "Aucun texte detecté ou texte trop court")
    else:
        answer = simpledialog.askstring("Lettre", "Quelle(s) lettre(s) / mot(s) souhaitez vous compter ?")
        if answer is not None:
            Count(answer)
            Executer()
        else:
            answer = "0"
            Count(answer)
            Executer()

# ##############################################################
                      # FENETRE1 / LAUNCHER #
# ##############################################################

def Start():
    global text,Fenetre1,boxe_prise
    Couleur()
    Fenetre1 = Tk()
    Fenetre1.title("Nuage de mot")
    CadreH = Frame(Fenetre1)
    CadreB = Frame(Fenetre1)
    CadreG = Frame(CadreB)
    CadreD = Frame(CadreB)
    text = Text(CadreH)
    Bouton1 = Button(CadreG, text="Ouvrir",command=Browse)
    Bouton2 = Button(CadreG, text="Coller",command=Paste)
    Bouton3 = Button(CadreD, text="Executer",command=Check)
    Bouton4 = Button(CadreD, text="Couleur aléatoire",command=Random)
    CadreH.pack(side=TOP, fill=BOTH, expand=1)
    CadreB.pack(side=BOTTOM, fill=BOTH, expand=1)
    CadreG.pack(side=LEFT, fill=BOTH, expand=1)
    CadreD.pack(side=RIGHT, fill=BOTH, expand=1)
    text.pack(side=TOP, fill=BOTH, padx=2, pady=2, expand=0)
    Bouton1.pack(side=TOP, fill=BOTH, padx=50, pady=5, expand=1)
    Bouton2.pack(side=BOTTOM, fill=BOTH, padx=50, pady=5, expand=1)
    Bouton3.pack(side=TOP, fill=BOTH, padx=50, pady=5, expand=1)
    Bouton4.pack(side=TOP, fill=BOTH, padx=50, pady=5, expand=1)
    Fenetre1.mainloop()

# ##############################################################
                      # DEMARRAGE #
# ##############################################################

Start()