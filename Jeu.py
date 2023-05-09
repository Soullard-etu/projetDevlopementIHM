from tkinter import * 
import random
from turtle import *
from PIL import Image, ImageTk
from tkinter import ttk



root = Tk()



root.geometry("900x500")
root.configure(background="green")

# Fonction qui recadre les cartes
def resize_cards(card):
	# ouvrir l'image
	our_card_img = Image.open(card)

	#Redimensioner 
	our_card_resize_image = our_card_img.resize((75, 125))
	
	#Afficher la carte
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	return our_card_image

# fonction qui recadre la carte à l'horizontale
def resize_cards_horizontal(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((125, 75))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Fonction qui mélange les cartes 
def shuffle():
	# Définition du deck
	suits = ["diamonds", "clubs", "hearts", "spades"]
	values = range(7, 15)
	# 11 = Valet, 12=Dame, 13=Roi, 14 = As

	global deck
	deck =[]

	for suit in suits:
		for value in values:
			deck.append(f'{value}_of_{suit}')

	# Création des joueurs
	global dealer, player,player2,player3
	dealer = []
	player = []
	player2 = []
	player3 = []


	# cartes dealer
	card = random.choice(deck)
	#On enlève la carte piochée
	deck.remove(card)
	# On l'ajoute dans la main du joeur 
	dealer.append(card)
	
	# On l'affiche
	global dealer_image
	dealer_image = resize_cards(f'cartes/cartes/{card}.png')
	dealer_label.config(image=dealer_image)

	card = random.choice(deck)
	deck.remove(card)
	dealer.append(card)
	global dealer_image_2
	dealer_image_2 = resize_cards(f'cartes/cartes/{card}.png')
	dealer_label_2.config(image=dealer_image_2)

	card = random.choice(deck)
	deck.remove(card)
	dealer.append(card)
	global dealer_image_3
	dealer_image_3 = resize_cards(f'cartes/cartes/{card}.png')
	dealer_label_3.config(image=dealer_image_3)

	card = random.choice(deck)
	deck.remove(card)
	dealer.append(card)
	global dealer_image_4
	dealer_image_4 = resize_cards(f'cartes/cartes/{card}.png')
	dealer_label_4.config(image=dealer_image_4)

	card = random.choice(deck)
	deck.remove(card)
	dealer.append(card)
	global dealer_image_5
	dealer_image_5 = resize_cards(f'cartes/cartes/{card}.png')
	dealer_label_5.config(image=dealer_image_5)

	card = random.choice(deck)
	deck.remove(card)
	dealer.append(card)
	global dealer_image_6
	dealer_image_6 = resize_cards(f'cartes/cartes/{card}.png')
	dealer_label_6.config(image=dealer_image_6)

	card = random.choice(deck)
	deck.remove(card)
	dealer.append(card)
	global dealer_image_7
	dealer_image_7 = resize_cards(f'cartes/cartes/{card}.png')
	dealer_label_7.config(image=dealer_image_7)

	card = random.choice(deck)
	deck.remove(card)
	dealer.append(card)
	global dealer_image_8
	dealer_image_8 = resize_cards(f'cartes/cartes/{card}.png')
	dealer_label_8.config(image=dealer_image_8)

	# Pareil pour chaque joueur
	card = random.choice(deck)
	
	deck.remove(card)
	
	player.append(card)
	
	global player_image
	player_image = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player_label.config(image=player_image)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image2
	player_image2 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player_label2.config(image=player_image2)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image3
	player_image3 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player_label3.config(image=player_image3)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image4
	player_image4 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player_label4.config(image=player_image4)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image5
	player_image5 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player_label5.config(image=player_image5)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image6
	player_image6 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player_label6.config(image=player_image6)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image7
	player_image7 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player_label7.config(image=player_image7)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image8
	player_image8 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player_label8.config(image=player_image8)


	
    # Joeur 3
	card = random.choice(deck)
	
	deck.remove(card)
	
	player2.append(card)
	global player2_image
	player2_image = resize_cards(f'cartes/cartes/{card}.png')
	player2_label.config(image=player2_image)


	card = random.choice(deck)
	deck.remove(card)
	player2.append(card)
	global player2_image2
	player2_image2 = resize_cards(f'cartes/cartes/{card}.png')
	player2_label2.config(image=player2_image2)

	card = random.choice(deck)
	deck.remove(card)
	player2.append(card)
	global player2_image3
	player2_image3 = resize_cards(f'cartes/cartes/{card}.png')
	player2_label3.config(image=player2_image3)

	card = random.choice(deck)
	deck.remove(card)
	player2.append(card)
	global player2_image4
	player2_image4 = resize_cards(f'cartes/cartes/{card}.png')
	player2_label4.config(image=player2_image4)

	card = random.choice(deck)
	deck.remove(card)
	player2.append(card)
	global player2_image5
	player2_image5 = resize_cards(f'cartes/cartes/{card}.png')
	player2_label5.config(image=player2_image5)

	card = random.choice(deck)
	deck.remove(card)
	player2.append(card)
	global player2_image6
	player2_image6 = resize_cards(f'cartes/cartes/{card}.png')
	player2_label6.config(image=player2_image6)

	card = random.choice(deck)
	deck.remove(card)
	player2.append(card)
	global player2_image7
	player2_image7 = resize_cards(f'cartes/cartes/{card}.png')
	player2_label7.config(image=player2_image7)

	card = random.choice(deck)
	deck.remove(card)
	player2.append(card)
	global player2_image8
	player2_image8 = resize_cards(f'cartes/cartes/{card}.png')
	player2_label8.config(image=player2_image8)

	
    # Joueur 4
	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image
	player3_image = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player3_label.config(image=player3_image)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image2
	player3_image2 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player3_label2.config(image=player3_image2)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image3
	player3_image3 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player3_label3.config(image=player3_image3)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image4
	player3_image4 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player3_label4.config(image=player3_image4)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image5
	player3_image5 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player3_label5.config(image=player3_image5)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image6
	player3_image6 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player3_label6.config(image=player3_image6)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image7
	player3_image7 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player3_label7.config(image=player3_image7)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image8
	player3_image8 = resize_cards_horizontal(f'cartes/cartes/{"dos_de_carte_horizontal"}.jpg')
	player3_label8.config(image=player3_image8)
	
	



	



#Frame contenant le jeu 
my_frame = Frame(root, bg="green")
my_frame.pack(pady=20,fill=BOTH,expand=True)

# Frames contenant les contenant de cartes 
dealer_frame = LabelFrame(my_frame, text="Joueur1", bd=0)
dealer_frame.pack(side=BOTTOM,anchor=CENTER,padx=5, ipadx=5)

player_frame = LabelFrame(my_frame, text="Joueur2", bd=0)
player_frame.pack(side=RIGHT,anchor=CENTER,ipadx=5,pady=5)

player2_frame = LabelFrame(my_frame, text="Joueur3", bd=0)
player2_frame.pack(side=TOP,anchor=CENTER, ipadx=5,pady=5)

player3_frame = LabelFrame(my_frame, text="Joueur4", bd=0)
player3_frame.pack(side=LEFT,anchor=CENTER, ipadx=5,pady=5)

# Frames contenant les cartes (dealer est le joueur 1)
dealer_label = Label(dealer_frame, text='')
dealer_label.grid(row=0 , column=0, pady=5,padx=5)
dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0,column=1,pady=5,padx=5)
dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0,column=2,pady=5,padx=5)
dealer_label_4 = Label(dealer_frame, text='')
dealer_label_4.grid(row=0,column=3,pady=5,padx=5)
dealer_label_5= Label(dealer_frame, text='')
dealer_label_5.grid(row=0,column=4,pady=5,padx=5)
dealer_label_6 = Label(dealer_frame, text='')
dealer_label_6.grid(row=0,column=5,pady=5,padx=5)
dealer_label_7 = Label(dealer_frame, text='')
dealer_label_7.grid(row=0,column=6,pady=5,padx=5)
dealer_label_8 = Label(dealer_frame, text='')
dealer_label_8.grid(row=0,column=7,pady=5,padx=5)


player_label = Label(player_frame, text='')
player_label.grid(row=0,column=0,pady=0,padx=5,sticky=W)
player_label2 = Label(player_frame, text='')
player_label2.grid(row=1,column=0,pady=5,padx=5,sticky=W)
player_label3 = Label(player_frame, text='')
player_label3.grid(row=2,column=0,pady=5,padx=5,sticky=W)
player_label4 = Label(player_frame, text='')
player_label4.grid(row=3,column=0,pady=5,padx=5,sticky=W)
player_label5 = Label(player_frame, text='')
player_label5.grid(row=4,column=0,pady=5,padx=5,sticky=W)
player_label6 = Label(player_frame, text='')
player_label6.grid(row=5,column=0,pady=5,padx=5,sticky=W)
player_label7 = Label(player_frame, text='')
player_label7.grid(row=6,column=0,pady=5,padx=5,sticky=W)
player_label8 = Label(player_frame, text='')
player_label8.grid(row=7,column=0,pady=5,padx=5,sticky=W)

player2_label = Label(player2_frame, text='')
player2_label.grid(row=0,column=0,pady=5,padx=5)
player2_label2 = Label(player2_frame, text='')
player2_label2.grid(row=0,column=1,pady=5,padx=5)
player2_label3 = Label(player2_frame, text='')
player2_label3.grid(row=0,column=2,pady=5,padx=5)
player2_label4 = Label(player2_frame, text='')
player2_label4.grid(row=0,column=3,pady=5,padx=5)
player2_label5 = Label(player2_frame, text='')
player2_label5.grid(row=0,column=4,pady=5,padx=5)
player2_label6 = Label(player2_frame, text='')
player2_label6.grid(row=0,column=5,pady=5,padx=5)
player2_label7 = Label(player2_frame, text='')
player2_label7.grid(row=0,column=6,pady=5,padx=5)
player2_label8 = Label(player2_frame, text='')
player2_label8.grid(row=0,column=7,pady=5,padx=5)

player3_label = Label(player3_frame, text='')
player3_label.grid(row=0,column=0,pady=5,sticky=E)
player3_label2 = Label(player3_frame, text='')
player3_label2.grid(row=1,column=0,pady=5,sticky=E)
player3_label3 = Label(player3_frame, text='')
player3_label3.grid(row=2,column=0,pady=5,sticky=E)
player3_label4 = Label(player3_frame, text='')
player3_label4.grid(row=3,column=0,pady=5,sticky=E)
player3_label5 = Label(player3_frame, text='')
player3_label5.grid(row=4,column=0,pady=5,sticky=E)
player3_label6 = Label(player3_frame, text='')
player3_label6.grid(row=5,column=0,pady=5,sticky=E)
player3_label7 = Label(player3_frame, text='')
player3_label7.grid(row=6,column=0,pady=5,sticky=E)
player3_label8 = Label(player3_frame, text='')
player3_label8.grid(row=7,column=0,pady=5,sticky=E)



#Fenêtre d'annonce à combiner avec Ange-ma pour les conditions 
class GameSetupWindow(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.title("Configuration du jeu")
        self.geometry("300x200")
        
		
        # Frame pour la sélection de la valeur
        value_frame = ttk.Frame(self)
        value_frame.pack(pady=10)
        
        ttk.Label(value_frame, text="Sélectionnez une valeur : ").pack(side=LEFT, padx=5)
        
        value_options = [i for i in range(80, 170, 10)]
        self.selected_value = StringVar(value=value_options[0])
        
        value_dropdown = ttk.OptionMenu(value_frame, self.selected_value, *value_options)
        value_dropdown.pack(side=LEFT, padx=5)
        
        # Frame pour la sélection de la couleur
        color_frame = ttk.Frame(self)
        color_frame.pack(pady=10)
        
        ttk.Label(color_frame, text="Sélectionnez une couleur : ").pack(side=LEFT, padx=5)
        
        self.selected_color = StringVar(value="Pique")
        
        color_button = OptionMenu(color_frame, self.selected_color, "Pique", "Coeur", "Carreau", "Trèfle")
        color_button.pack(side=LEFT, padx=5)
        
        # Bouton pour enregistrer les options sélectionnées
        save_button = ttk.Button(self, text="Enregistrer", command=self.save_options)
        save_button.pack(pady=10)
    
    
        
    def save_options(self):
        value = int(self.selected_value.get())
        color = self.selected_color.get()
        self.parent.game_options = (value, color)
        self.destroy()
	

#Cartes cliquées 
def card_clicked(event):
    # fonction appelée lorsque l'utilisateur clique sur une carte
    global drop_button
    drop_button = None
    if drop_button:
        return 
    card = event.widget
    # création du bouton déposer
    drop_button = Button(root, text="Déposer", command=lambda: drop_card(card))
    drop_button.pack()

    # placement du boutonau centre
    drop_button.place(x=root.winfo_width() / 2 ,
                     y=root.winfo_height() / 2)
#Destruction du bouton
def drop_card(event):
    global drop_button


    card_image = event.cget("image")

    # suppression du bouton déposer et du label contenant la carte
    drop_button.destroy()
    event.destroy()

    # création d'un nouveau label avec l'image de la carte
    card_label = Label(root, image=card_image)
     

    # placement du label au centre de la fenêtre
    card_label.place(x=root.winfo_width() / 2 ,
                     y=root.winfo_height() / 2 )







# Shuffle Deck On Start
shuffle()


#Binds pour réagir aux events
dealer_label.bind("<Button-1>",card_clicked)
dealer_label_2.bind("<Button-1>",card_clicked)
dealer_label_3.bind("<Button-1>",card_clicked)
dealer_label_4.bind("<Button-1>",card_clicked)
dealer_label_5.bind("<Button-1>",card_clicked)
dealer_label_6.bind("<Button-1>",card_clicked)
dealer_label_7.bind("<Button-1>",card_clicked)
dealer_label_8.bind("<Button-1>",card_clicked)



##Boucle de jeu

game_setup_window = GameSetupWindow(root)
root.wait_window(game_setup_window)

value, color = root.game_options

# Put number of remaining cards in title bar
root.title(f'Annonce :{value} , {color} ')


root.mainloop()


