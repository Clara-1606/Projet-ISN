#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      clara
#
# Created:     09/03/2019
# Copyright:   (c) clara 2019
# Licence:     <your licence>

#-------------------------------------------------------------------------------
import random
import tkinter #ouvrir une interface graphique
import tkMessageBox #ouvrir les fenetres pour mettre des messages




#FENETRE + DESIGN

fenetre=Tkinter.Tk() #Ouvrir une fenêtre
fenetre.title("Mastermind") #Nommer la fenêtre
fenetre.geometry("450x720") #Définir la taile en pixels

Frame=Tkinter.Frame(fenetre,bg="#610943",width =450, height =720) #Mettre un cadre dans la fenetre pour y placer d'autres widgets (boutons etc)
Frame.pack() #Placer le cadre
Frame.pack_propagate(0) #Normalement le cadre s'adapte à ce qui y a dedans, avec cette fonction on evite cela


photo = Tkinter.PhotoImage(file=".\images\mastermind.gif") #On definit une photo pour mettre le logo du site
logo = Tkinter.Label(Frame, image=photo,highlightthickness=0 ) #Grâce au label on peut mettre la photo dans le cadre
logo.grid(row=0, column=0, columnspan=8) #On le place tout en haut (x=0 et y=0), et qu'il prenne 8 colonnes de larges

ligne = Tkinter.Canvas(Frame, highlightthickness=0, width=450, height=20, background="#610943") #Creer un canevas (toile)
ligne1 = ligne.create_line(0, 10, 450, 10, width=2) #Creer une ligne pour séparer nos choix et les resultats des essais
ligne.grid(row=23, column=0, columnspan=8) #On la place dans la Frame

#DEFINIR LES VARIABLES
A = random.randint(1,5) # On definit chaque chiffre du code
B = random.randint(1,5)
C = random.randint(1,5)
D = random.randint(1,5)

E = 0 #Cela servira pour definir le code qu'on choisi
F = 0
G = 0
H = 0

#Zone de texte qui s'afficheront selon le resultat
Bienvenue = Tkinter.Label(Frame,text="Bienvenue, saisi ton code !")
Bienvenue.grid(row=12, column=5, columnspan=8)

#BOUTONS EXTERIEURS
fin=Tkinter.Button(fenetre, width=10, height=3, text="Quitter le jeu",relief="raised",borderwidth=4, command=fenetre.destroy) #bouton pour quitter le jeu
Rejoue=Tkinter.Button(fenetre, width=10, height=3, text="Rejouer",relief="raised",borderwidth=4) #Creer un bouton pour rejouer
valider=Tkinter.Button(Frame, width=9, height=3,borderwidth=3, foreground="#FF0080", relief="raised", text="Valider", bg="#F6CEEC", command=Bienvenue.destroy) #Bouton pour valider nos choix
reset=Tkinter.Button(Frame, width=9, height=3,borderwidth=3, foreground="#FF0080", relief="raised", text="Reset", bg="#F6CEEC") #bouton reset pour faire un nouveau choix

choix1=Tkinter.Button(Frame, width=9, background="darkgray") #On definit chaque bouton pour mettre une couleur
choix2=Tkinter.Button(Frame, width=9, background="darkgray")
choix3=Tkinter.Button(Frame, width=9, background="darkgray")
choix4=Tkinter.Button(Frame, width=9, background="darkgray")

#La fonction grid ne permet pas de mettre des espaces entres les lignes, alors on créer des labels sans rien juste pour éviter que les boutons soient collés
Lab = Tkinter.Label(Frame, bg="#610943")
Lab1 = Tkinter.Label(Frame, bg="#610943")
Lab2 = Tkinter.Label(Frame, bg="#610943")
Lab3 = Tkinter.Label(Frame, bg="#610943")
Lab4 = Tkinter.Label(Frame, bg="#610943")
Lab5 = Tkinter.Label(Frame, bg="#610943")
Lab6 = Tkinter.Label(Frame, bg="#610943")
Lab7 = Tkinter.Label(Frame, bg="#610943")
Lab8 = Tkinter.Label(Frame, bg="#610943")
Lab9 = Tkinter.Label(Frame, bg="#610943")
Lab10 = Tkinter.Label(Frame, bg="#610943")


#Pour chaque ligne, on cree 4 boutons pour representer chaque essais
A1=Tkinter.Button(Frame, width=9, background="darkgray")
A2=Tkinter.Button(Frame, width=9, background="darkgray")
A3=Tkinter.Button(Frame, width=9, background="darkgray")
A4=Tkinter.Button(Frame, width=9, background="darkgray")

B1=Tkinter.Button(Frame, width=9, background="darkgray")
B2=Tkinter.Button(Frame, width=9, background="darkgray")
B3=Tkinter.Button(Frame, width=9, background="darkgray")
B4=Tkinter.Button(Frame, width=9, background="darkgray")

C1=Tkinter.Button(Frame, width=9, background="darkgray")
C2=Tkinter.Button(Frame, width=9, background="darkgray")
C3=Tkinter.Button(Frame, width=9, background="darkgray")
C4=Tkinter.Button(Frame, width=9, background="darkgray")

D1=Tkinter.Button(Frame, width=9, background="darkgray")
D2=Tkinter.Button(Frame, width=9, background="darkgray")
D3=Tkinter.Button(Frame, width=9, background="darkgray")
D4=Tkinter.Button(Frame, width=9, background="darkgray")

E1=Tkinter.Button(Frame, width=9, background="darkgray")
E2=Tkinter.Button(Frame, width=9, background="darkgray")
E3=Tkinter.Button(Frame, width=9, background="darkgray")
E4=Tkinter.Button(Frame, width=9, background="darkgray")

F1=Tkinter.Button(Frame, width=9, background="darkgray")
F2=Tkinter.Button(Frame, width=9, background="darkgray")
F3=Tkinter.Button(Frame, width=9, background="darkgray")
F4=Tkinter.Button(Frame, width=9, background="darkgray")

G1=Tkinter.Button(Frame, width=9, background="darkgray")
G2=Tkinter.Button(Frame, width=9, background="darkgray")
G3=Tkinter.Button(Frame, width=9, background="darkgray")
G4=Tkinter.Button(Frame, width=9, background="darkgray")

H1=Tkinter.Button(Frame, width=9, background="darkgray")
H2=Tkinter.Button(Frame, width=9, background="darkgray")
H3=Tkinter.Button(Frame, width=9, background="darkgray")
H4=Tkinter.Button(Frame, width=9, background="darkgray")

I1=Tkinter.Button(Frame, width=9, background="darkgray")
I2=Tkinter.Button(Frame, width=9, background="darkgray")
I3=Tkinter.Button(Frame, width=9, background="darkgray")
I4=Tkinter.Button(Frame, width=9, background="darkgray")

J1=Tkinter.Button(Frame, width=9, background="darkgray")
J2=Tkinter.Button(Frame, width=9, background="darkgray")
J3=Tkinter.Button(Frame, width=9, background="darkgray")
J4=Tkinter.Button(Frame, width=9, background="darkgray")

#DEFINITION DE FONCTION POUR CHANGER DE COULEUR SELON LE NOMBRE DE CLIQUES
Clic1 = 0
def QuandClique(event): #Definition de la fonction
    global Clic1, E #Pour les variables Clic1 et E
    Clic1 = Clic1 + 1
    if Clic1 == 1:
        choix1.config(bg="blue")
        E = 1 #On lui donne une valeur pour pouvoir la comparer au code a trouver
    elif Clic1 ==2:
        choix1.config(bg="red")
        E = 2
    elif Clic1 ==3:
        choix1.config(bg="green")
        E = 3
    elif Clic1==4:
        choix1.config(bg="yellow")
        E = 4
    else:
        choix1.config(bg="#FF5900")
        E = 5
        Clic1 = 0 #On remet a 0 pour pouvoir continuer de cliquer

choix1.bind("<ButtonRelease-1>", QuandClique)#Quand on appuie sur le bouton, on applique la fonction QuandClique


Clic2 = 0
def QuandClique(event) :
    global Clic2, F
    Clic2 = Clic2 + 1
    if Clic2 ==1:
        choix2.config(bg="blue")
        F = 1
    elif Clic2 ==2:
        choix2.config(bg="red")
        F = 2
    elif Clic2 ==3:
        choix2.config(bg="green")
        F = 3
    elif Clic2==4:
        choix2.config(bg="yellow")
        F = 4
    else:
        choix2.config(bg="#FF5900")
        F = 5
        Clic2 = 0

choix2.bind("<ButtonRelease-1>", QuandClique)#Quand on appuie sur le bouton, on applique la fonction QuandClique


Clic3 = 0
def QuandClique(event) :
    global Clic3, G
    Clic3 = Clic3 + 1
    if Clic3 ==1:
        choix3.config(bg="blue")
        G = 1
    elif Clic3 ==2:
        choix3.config(bg="red")
        G = 2
    elif Clic3 ==3:
        choix3.config(bg="green")
        G = 3
    elif Clic3==4:
        choix3.config(bg="yellow")
        G = 4
    else:
        choix3.config(bg="#FF5900")
        G = 5
        Clic3 = 0

choix3.bind("<ButtonRelease-1>", QuandClique) #Quand on appuie sur le bouton, on applique la fonction QuandClique


Clic4 = 0
def QuandClique(event) :
    global Clic4, H
    Clic4 = Clic4 + 1
    if Clic4 ==1:
        choix4.config(bg="blue")
        H = 1
    elif Clic4 ==2:
        choix4.config(bg="red")
        H = 2
    elif Clic4 ==3:
        choix4.config(bg="green")
        H = 3
    elif Clic4==4:
        choix4.config(bg="yellow")
        H = 4
    else:
        choix4.config(bg="#FF5900")
        H = 5
        Clic4 = 0

choix4.bind("<ButtonRelease-1>", QuandClique) #Quand on appuie sur le bouton, on applique la fonction QuandClique


#DEFINITION DE FONCTION POUR LE BOUTON RESET, VALIDER ET REJOUER

ClicReset = 0
def Reset (event) :
    global ClicReset
    ClicReset = ClicReset + 1
    if ClicReset >= 1 : #Si on appuies sur Reset, les boutons se reinitialisent
        choix1.config(bg="darkgray")
        choix2.config(bg="darkgray")
        choix3.config(bg="darkgray")
        choix4.config(bg="darkgray")
    else :
        pass

reset.bind("<ButtonRelease-1>", Reset) #Lorque qu'on clique, on applique la fonction Reset
reset.grid(row=24, column=5)


ClicValider = 0 #Valeur de base
def Valider (event) :
    global ClicValider
    ClicValider = ClicValider + 1 #A chaque fois qu'on clique, la valeur augmente de 1
    if ClicValider==1 and A==E==1: #Si on a clique une fois, que la couleur est bonne et qu'elle est bleu, alors le bouton devient bleu
        J1.config(bg="blue")
    elif ClicValider==1 and A==E==2: #Elif --> Sinon si
        J1.config(bg="red")
    elif ClicValider==1 and A==E==3:
        J1.config(bg="green")
    elif ClicValider==1 and A==E==4:
        J1.config(bg="yellow")
    elif ClicValider==1 and A==E==5:
        J1.config(bg="#FF5900")
    else : #Sinon
        pass #Ne rien faire
    if ClicValider==1 and B==F==1:
        J2.config(bg="blue")
    elif ClicValider==1 and B==F==2:
        J2.config(bg="red")
    elif ClicValider==1 and B==F==3:
        J2.config(bg="green")
    elif ClicValider==1 and B==F==4:
        J2.config(bg="yellow")
    elif ClicValider==1 and B==F==5:
        J2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==1 and C==G==1:
        J3.config(bg="blue")
    elif ClicValider==1 and C==G==2:
        J3.config(bg="red")
    elif ClicValider==1 and C==G==3:
        J3.config(bg="green")
    elif ClicValider==1 and C==G==4:
        J3.config(bg="yellow")
    elif ClicValider==1 and C==G==5:
        J3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==1 and D==H==1:
        J4.config(bg="blue")
    elif ClicValider==1 and D==H==2:
        J4.config(bg="red")
    elif ClicValider==1 and D==H==3:
        J4.config(bg="green")
    elif ClicValider==1 and D==H==4:
        J4.config(bg="yellow")
    elif ClicValider==1 and D==H==5:
        J4.config(bg="#FF5900")
    else :
        pass
    if ClicValider==2 and A==E==1:
        I1.config(bg="blue")
    elif ClicValider==2 and A==E==2:
        I1.config(bg="red")
    elif ClicValider==2 and A==E==3:
        I1.config(bg="green")
    elif ClicValider==2 and A==E==4:
        I1.config(bg="yellow")
    elif ClicValider==2 and A==E==5:
        I1.config(bg="#FF5900")
    else :
        pass
    if ClicValider==2 and B==F==1:
        I2.config(bg="blue")
    elif ClicValider==2 and B==F==2:
        I2.config(bg="red")
    elif ClicValider==2 and B==F==3:
        I2.config(bg="green")
    elif ClicValider==2 and B==F==4:
        I2.config(bg="yellow")
    elif ClicValider==2 and B==F==5:
        I2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==2 and C==G==1:
        I3.config(bg="blue")
    elif ClicValider==2 and C==G==2:
        I3.config(bg="red")
    elif ClicValider==2 and C==G==3:
        I3.config(bg="green")
    elif ClicValider==2 and C==G==4:
        I3.config(bg="yellow")
    elif ClicValider==2 and C==G==5:
        I3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==2 and D==H==1:
        I4.config(bg="blue")
    elif ClicValider==2 and D==H==2:
        I4.config(bg="red")
    elif ClicValider==2 and D==H==3:
        I4.config(bg="green")
    elif ClicValider==2 and D==H==4:
        I4.config(bg="yellow")
    elif ClicValider==2 and D==H==5:
        I4.config(bg="#FF5900")
    else :
        pass
    if ClicValider==3 and A==E==1:
        H1.config(bg="blue")
    elif ClicValider==3 and A==E==2:
        H1.config(bg="red")
    elif ClicValider==3 and A==E==3:
        H1.config(bg="green")
    elif ClicValider==3 and A==E==4:
        H1.config(bg="yellow")
    elif ClicValider==3 and A==E==5:
        H1.config(bg="#FF5900")
    else :
        pass
    if ClicValider==3 and B==F==1:
        H2.config(bg="blue")
    elif ClicValider==3 and B==F==2:
        H2.config(bg="red")
    elif ClicValider==3 and B==F==3:
        H2.config(bg="green")
    elif ClicValider==3 and B==F==4:
        H2.config(bg="yellow")
    elif ClicValider==3 and B==F==5:
        H2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==3 and C==G==1:
        H3.config(bg="blue")
    elif ClicValider==3 and C==G==2:
        H3.config(bg="red")
    elif ClicValider==3 and C==G==3:
        H3.config(bg="green")
    elif ClicValider==3 and C==G==4:
        H3.config(bg="yellow")
    elif ClicValider==3 and C==G==5:
        H3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==3 and D==H==1:
        H4.config(bg="blue")
    elif ClicValider==3 and D==H==2:
        H4.config(bg="red")
    elif ClicValider==3 and D==H==3:
        H4.config(bg="green")
    elif ClicValider==3 and D==H==4:
        H4.config(bg="yellow")
    elif ClicValider==3 and D==H==5:
        H4.config(bg="#FF5900")
    else :
        pass
    if ClicValider==4 and A==E==1:
        G1.config(bg="blue")
    elif ClicValider==4 and A==E==2:
        G1.config(bg="red")
    elif ClicValider==4 and A==E==3:
        G1.config(bg="green")
    elif ClicValider==4 and A==E==4:
        G1.config(bg="yellow")
    elif ClicValider==4 and A==E==5:
        G1.config(bg="#FF5900")
    else :
        pass
    if ClicValider==4 and B==F==1:
        G2.config(bg="blue")
    elif ClicValider==4 and B==F==2:
        G2.config(bg="red")
    elif ClicValider==4 and B==F==3:
        G2.config(bg="green")
    elif ClicValider==4 and B==F==4:
        G2.config(bg="yellow")
    elif ClicValider==4 and B==F==5:
        G2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==4 and C==G==1:
        G3.config(bg="blue")
    elif ClicValider==4 and C==G==2:
        G3.config(bg="red")
    elif ClicValider==4 and C==G==3:
        G3.config(bg="green")
    elif ClicValider==4 and C==G==4:
        G3.config(bg="yellow")
    elif ClicValider==4 and C==G==5:
        G3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==4 and D==H==1:
        G4.config(bg="blue")
    elif ClicValider==4 and D==H==2:
        G4.config(bg="red")
    elif ClicValider==4 and D==H==3:
        G4.config(bg="green")
    elif ClicValider==4 and D==H==4:
        G4.config(bg="yellow")
    elif ClicValider==4 and D==H==5:
        G4.config(bg="#FF5900")
    else :
        pass
    if ClicValider==5 and A==E==1:
        F1.config(bg="blue")
    elif ClicValider==5 and A==E==2:
        F1.config(bg="red")
    elif ClicValider==5 and A==E==3:
        F1.config(bg="green")
    elif ClicValider==5 and A==E==4:
        F1.config(bg="yellow")
    elif ClicValider==5 and A==E==5:
        F1.config(bg="#FF5900")
    else :
        pass
    if ClicValider==5 and B==F==1:
        F2.config(bg="blue")
    elif ClicValider==5 and B==F==2:
        F2.config(bg="red")
    elif ClicValider==5 and B==F==3:
        F2.config(bg="green")
    elif ClicValider==5 and B==F==4:
        F2.config(bg="yellow")
    elif ClicValider==5 and B==F==5:
        F2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==5 and C==G==1:
        F3.config(bg="blue")
    elif ClicValider==5 and C==G==2:
        F3.config(bg="red")
    elif ClicValider==5 and C==G==3:
        F3.config(bg="green")
    elif ClicValider==5 and C==G==4:
        F3.config(bg="yellow")
    elif ClicValider==5 and C==G==5:
        F3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==5 and D==H==1:
        F4.config(bg="blue")
    elif ClicValider==5 and D==H==2:
        F4.config(bg="red")
    elif ClicValider==5 and D==H==3:
        F4.config(bg="green")
    elif ClicValider==5 and D==H==4:
        F4.config(bg="yellow")
    elif ClicValider==5 and D==H==5:
        F4.config(bg="#FF5900")
    else :
        pass
    if ClicValider==6 and A==E==1:
        E1.config(bg="blue")
    elif ClicValider==6 and A==E==2:
        E1.config(bg="red")
    elif ClicValider==6 and A==E==3:
        E1.config(bg="green")
    elif ClicValider==6 and A==E==4:
        E1.config(bg="yellow")
    elif ClicValider==6 and A==E==5:
        E1.config(bg="#FF5900")
    else :
        pass
    if ClicValider==6 and B==F==1:
        E2.config(bg="blue")
    elif ClicValider==6 and B==F==2:
        E2.config(bg="red")
    elif ClicValider==6 and B==F==3:
        E2.config(bg="green")
    elif ClicValider==6 and B==F==4:
        E2.config(bg="yellow")
    elif ClicValider==6 and B==F==5:
        E2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==6 and C==G==1:
        E3.config(bg="blue")
    elif ClicValider==6 and C==G==2:
        E3.config(bg="red")
    elif ClicValider==6 and C==G==3:
        E3.config(bg="green")
    elif ClicValider==6 and C==G==4:
        E3.config(bg="yellow")
    elif ClicValider==6 and C==G==5:
        E3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==6 and D==H==1:
        E4.config(bg="blue")
    elif ClicValider==6 and D==H==2:
        E4.config(bg="red")
    elif ClicValider==6 and D==H==3:
        E4.config(bg="green")
    elif ClicValider==6 and D==H==4:
        E4.config(bg="yellow")
    elif ClicValider==6 and D==H==5:
        E4.config(bg="#FF5900")
    else :
        pass
    if ClicValider==7 and A==E==1:
        D1.config(bg="blue")
    elif ClicValider==7 and A==E==2:
        D1.config(bg="red")
    elif ClicValider==7 and A==E==3:
        D1.config(bg="green")
    elif ClicValider==7 and A==E==4:
        D1.config(bg="yellow")
    elif ClicValider==7 and A==E==5:
        D1.config(bg="#FF5900")
    else :
        pass
    if ClicValider==7 and B==F==1:
        D2.config(bg="blue")
    elif ClicValider==7 and B==F==2:
        D2.config(bg="red")
    elif ClicValider==7 and B==F==3:
        D2.config(bg="green")
    elif ClicValider==7 and B==F==4:
        D2.config(bg="yellow")
    elif ClicValider==7 and B==F==5:
        D2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==7 and C==G==1:
        D3.config(bg="blue")
    elif ClicValider==7 and C==G==2:
        D3.config(bg="red")
    elif ClicValider==7 and C==G==3:
        D3.config(bg="green")
    elif ClicValider==7 and C==G==4:
        D3.config(bg="yellow")
    elif ClicValider==7 and C==G==5:
        D3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==7 and D==H==1:
        D4.config(bg="blue")
    elif ClicValider==7 and D==H==2:
        D4.config(bg="red")
    elif ClicValider==7 and D==H==3:
        D4.config(bg="green")
    elif ClicValider==7 and D==H==4:
        D4.config(bg="yellow")
    elif ClicValider==7 and D==H==5:
        D4.config(bg="#FF5900")
    else :
        pass
    if ClicValider==8 and A==E==1:
        C1.config(bg="blue")
    elif ClicValider==8 and A==E==2:
        C1.config(bg="red")
    elif ClicValider==8 and A==E==3:
        C1.config(bg="green")
    elif ClicValider==8 and A==E==4:
        C1.config(bg="yellow")
    elif ClicValider==8 and A==E==5:
        C1.config(bg="#FF5900")
    else :
        pass
    if ClicValider==8 and B==F==1:
        C2.config(bg="blue")
    elif ClicValider==8 and B==F==2:
        C2.config(bg="red")
    elif ClicValider==8 and B==F==3:
        C2.config(bg="green")
    elif ClicValider==8 and B==F==4:
        C2.config(bg="yellow")
    elif ClicValider==8 and B==F==5:
        C2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==8 and C==G==1:
        C3.config(bg="blue")
    elif ClicValider==8 and C==G==2:
        C3.config(bg="red")
    elif ClicValider==8 and C==G==3:
        C3.config(bg="green")
    elif ClicValider==8 and C==G==4:
        C3.config(bg="yellow")
    elif ClicValider==8 and C==G==5:
        C3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==8 and D==H==1:
        C4.config(bg="blue")
    elif ClicValider==8 and D==H==2:
        C4.config(bg="red")
    elif ClicValider==8 and D==H==3:
        C4.config(bg="green")
    elif ClicValider==8 and D==H==4:
        C4.config(bg="yellow")
    elif ClicValider==8 and D==H==5:
        C4.config(bg="#FF5900")
    else :
        pass
    if ClicValider==9 and A==E==1:
        B1.config(bg="blue")
    elif ClicValider==9 and A==E==2:
        B1.config(bg="red")
    elif ClicValider==9 and A==E==3:
        B1.config(bg="green")
    elif ClicValider==9 and A==E==4:
        B1.config(bg="yellow")
    elif ClicValider==9 and A==E==5:
        B1.config(bg="#FF5900")
    else :
        pass
    if ClicValider==9 and B==F==1:
        B2.config(bg="blue")
    elif ClicValider==9 and B==F==2:
        B2.config(bg="red")
    elif ClicValider==9 and B==F==3:
        B2.config(bg="green")
    elif ClicValider==9 and B==F==4:
        B2.config(bg="yellow")
    elif ClicValider==9 and B==F==5:
        B2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==9 and C==G==1:
        B3.config(bg="blue")
    elif ClicValider==9 and C==G==2:
        B3.config(bg="red")
    elif ClicValider==9 and C==G==3:
        B3.config(bg="green")
    elif ClicValider==9 and C==G==4:
        B3.config(bg="yellow")
    elif ClicValider==9 and C==G==5:
        B3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==9 and D==H==1:
        B4.config(bg="blue")
    elif ClicValider==9 and D==H==2:
        B4.config(bg="red")
    elif ClicValider==9 and D==H==3:
        B4.config(bg="green")
    elif ClicValider==9 and D==H==4:
        B4.config(bg="yellow")
    elif ClicValider==9 and D==H==5:
        B4.config(bg="#FF5900")
    else :
        pass
    if ClicValider==10 and A==E==1:
        A1.config(bg="blue")
    elif ClicValider==10 and A==E==2:
        A1.config(bg="red")
    elif ClicValider==10 and A==E==3:
        A1.config(bg="green")
    elif ClicValider==10 and A==E==4:
        A1.config(bg="yellow")
    elif ClicValider==10 and A==E==5:
        A1.config(bg="#FF5900")
    else :
        pass
    if ClicValider==10 and B==F==1:
        A2.config(bg="blue")
    elif ClicValider==10 and B==F==2:
        A2.config(bg="red")
    elif ClicValider==10 and B==F==3:
        A2.config(bg="green")
    elif ClicValider==10 and B==F==4:
        A2.config(bg="yellow")
    elif ClicValider==10 and B==F==5:
        A2.config(bg="#FF5900")
    else :
        pass
    if ClicValider==10 and C==G==1:
        A3.config(bg="blue")
    elif ClicValider==10 and C==G==2:
        A3.config(bg="red")
    elif ClicValider==10 and C==G==3:
        A3.config(bg="green")
    elif ClicValider==10 and C==G==4:
        A3.config(bg="yellow")
    elif ClicValider==10 and C==G==5:
        A3.config(bg="#FF5900")
    else :
        pass
    if ClicValider==10 and D==H==1:
        A4.config(bg="blue")
    elif ClicValider==10 and D==H==2:
        A4.config(bg="red")
    elif ClicValider==10 and D==H==3:
        A4.config(bg="green")
    elif ClicValider==10 and D==H==4:
        A4.config(bg="yellow")
    elif ClicValider==10 and D==H==5:
        A4.config(bg="#FF5900")
    else :
        pass
    if A==E and B==F and C==G and D==H: #Si tout est bon, on affiche le texte pour le signaler, et qu'il peut rejouer
        tkMessageBox.showinfo("Felicitation!"," Bravo tu as gagne, tu peux refaire une partie en cliquant sur rejouer") #Si il gagne, une fenetre s'ouvre pour avertir le joueur
    else :
        pass
    if ClicValider>=10 : #Si on a fait les 10 essais, on affiche qu'il a perdu et qu'il peut rejouer
        tkMessageBox.showinfo("Desole !"," Tu as perdu mais tu peux refaire une partie en cliquant sur rejouer")#Si il perd, une fenetre s'ouvre pour avertir le joueur
        ClicValider=0
    else :
        pass


valider.bind("<ButtonRelease-1>", Valider) #Quand on appuie sur le bouton, cela applique la fonction Valider
valider.grid(row=24, column=7)


ClicRejouer = 0
def Rejouer (event) : #on reinitialise tous les boutons et on définit un nouveau code au hasard
    global ClicRejouer, ClicValider, A, B, C, D, E, F, G, H
    ClicRejouer = ClicRejouer + 1
    if ClicRejouer >= 1 :
     A1.config(bg="darkgray")
     A2.config(bg="darkgray")
     A3.config(bg="darkgray")
     A4.config(bg="darkgray")
     B1.config(bg="darkgray")
     B2.config(bg="darkgray")
     B3.config(bg="darkgray")
     B4.config(bg="darkgray")
     C1.config(bg="darkgray")
     C2.config(bg="darkgray")
     C3.config(bg="darkgray")
     C4.config(bg="darkgray")
     D1.config(bg="darkgray")
     D2.config(bg="darkgray")
     D3.config(bg="darkgray")
     D4.config(bg="darkgray")
     E1.config(bg="darkgray")
     E2.config(bg="darkgray")
     E3.config(bg="darkgray")
     E4.config(bg="darkgray")
     F1.config(bg="darkgray")
     F2.config(bg="darkgray")
     F3.config(bg="darkgray")
     F4.config(bg="darkgray")
     G1.config(bg="darkgray")
     G2.config(bg="darkgray")
     G3.config(bg="darkgray")
     G4.config(bg="darkgray")
     H1.config(bg="darkgray")
     H2.config(bg="darkgray")
     H3.config(bg="darkgray")
     H4.config(bg="darkgray")
     I1.config(bg="darkgray")
     I2.config(bg="darkgray")
     I3.config(bg="darkgray")
     I4.config(bg="darkgray")
     J1.config(bg="darkgray")
     J2.config(bg="darkgray")
     J3.config(bg="darkgray")
     J4.config(bg="darkgray")
     choix1.config(bg="darkgray")
     choix2.config(bg="darkgray")
     choix3.config(bg="darkgray")
     choix4.config(bg="darkgray")
     ClicValider=0
     A = random.randint(1,5) # On definit chaque chiffre du nouveau code
     B = random.randint(1,5)
     C = random.randint(1,5)
     D = random.randint(1,5)
     E = 0
     F = 0
     G = 0
     H = 0

Rejoue.bind("<ButtonRelease-1>", Rejouer)
fin.pack(side="left")
Rejoue.pack(side="right")


#PLACEMENT DES BOUTONS
Lab.grid(row=1, column=0) #les labels sont la pour mettre de l'espace entre les boutons

A1.grid(row=3, column=0)
A2.grid(row=3, column=1)
A3.grid(row=3, column=2)
A4.grid(row=3, column=3)

Lab1.grid(row=4, column=3)

B1.grid(row=5, column=0)
B2.grid(row=5, column=1)
B3.grid(row=5, column=2)
B4.grid(row=5, column=3)

Lab2.grid(row=6, column=0)

C1.grid(row=7, column=0)
C2.grid(row=7, column=1)
C3.grid(row=7, column=2)
C4.grid(row=7, column=3)

Lab3.grid(row=8, column=0)

D1.grid(row=9, column=0)
D2.grid(row=9, column=1)
D3.grid(row=9, column=2)
D4.grid(row=9, column=3)

Lab4.grid(row=10, column=0)

E1.grid(row=11, column=0)
E2.grid(row=11, column=1)
E3.grid(row=11, column=2)
E4.grid(row=11, column=3)

Lab5.grid(row=12, column=0)

F1.grid(row=13, column=0)
F2.grid(row=13, column=1)
F3.grid(row=13, column=2)
F4.grid(row=13, column=3)

Lab6.grid(row=14, column=0)

G1.grid(row=15, column=0)
G2.grid(row=15, column=1)
G3.grid(row=15, column=2)
G4.grid(row=15, column=3)

Lab7.grid(row=16, column=0)

H1.grid(row=17, column=0)
H2.grid(row=17, column=1)
H3.grid(row=17, column=2)
H4.grid(row=17, column=3)

Lab8.grid(row=18, column=0)

I1.grid(row=19, column=0)
I2.grid(row=19, column=1)
I3.grid(row=19, column=2)
I4.grid(row=19, column=3)

Lab9.grid(row=20, column=0)

J1.grid(row=21, column=0)
J2.grid(row=21, column=1)
J3.grid(row=21, column=2)
J4.grid(row=21, column=3)

Lab10.grid(row=22, column=0)

choix1.grid(row=24, column=0)
choix2.grid(row=24, column=1)
choix3.grid(row=24, column=2)
choix4.grid(row=24, column=3)

fenetre.mainloop()
