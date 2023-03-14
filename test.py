from tkinter import * 
import random as rd

root = Tk()
root.title('Belote Cortenaise')
root.geometry("900x500")
root.configure(background="Green")

#Fonction de melange
def shuffle():
    #Definition
    couleurs = ["Carreau","Coeur","Trèfle","Pique"]
    #11 = Valet , 12 = Dame , 13 = Roi , 14 = AS
    valeurs = range(7,15)

    global deck
    deck = []

    for couleur in couleurs:
        for valeur in valeurs:
            deck.append(f'{valeur} de {couleur}')
                    
            
            

            
    
    #Creer les JOueurs

    global joueur1 , joueur2 , joueur3 , joueur4
    joueur1 = []
    joueur2 = []
    joueur3 = []
    joueur4 = []


    #Donner une carte aléatoire 
    for i in range(9):

        carte = rd.choice(deck)
        deck.remove(carte)
        joueur1.append(carte)
        player1_label.insert(i,carte)

        carte = rd.choice(deck)
        deck.remove(carte)
        joueur2.append(carte)
        player2_label.insert(i,carte)

        carte = rd.choice(deck)
        deck.remove(carte)
        joueur3.append(carte)
        player3_label.insert(i,carte)

        carte = rd.choice(deck)
        deck.remove(carte)
        joueur4.append(carte)
        player4_label.insert(i,carte)





gros_frame = Frame(root,bg="green")
gros_frame.pack(pady=20)

#Frame pour le cartes
player1_frame = LabelFrame(gros_frame,text="Joueur1",border=0)
player1_frame.grid(row=0,column=0,padx=20,ipadx=20)

player2_frame = LabelFrame(gros_frame,text="Joueur2",border=0)
player2_frame.grid(row=0,column=1,padx=20,ipadx=20)

player3_frame = LabelFrame(gros_frame,text="Joueur3",border=0)
player3_frame.grid(row=0,column=2,padx=20,ipadx=20)

player4_frame = LabelFrame(gros_frame,text="Joueur4",border=0)
player4_frame.grid(row=0,column=3,padx=20,ipadx=20)

#mettre les cartes
player1_label = Listbox(player1_frame)
player1_label.pack(pady=20)

player2_label = Listbox(player2_frame)
player2_label.pack(pady=20)

player3_label = Listbox(player3_frame)
player3_label.pack(pady=20)

player4_label = Listbox(player4_frame)
player4_label.pack(pady=20)

#Creer des bouttons 

shuffle_button = Button(root,text="Mélanger",font=("Helvetica",14),command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root,text="Piocher",font=("Helvetica",14))
card_button.pack(pady=20)


root.mainloop()