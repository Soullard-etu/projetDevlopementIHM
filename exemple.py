from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()

root.geometry("900x500")
root.configure(background="green")

# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((50, 100))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Resize Cards
def resize_cards_horizontal(card):
	# Open the image
	our_card_img = Image.open(card)
	our_card_rotate_image = our_card_img.rotate(90)

	# Resize The Image
	our_card_resize_image = our_card_rotate_image.resize((50, 100))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Shuffle The Cards
def shuffle():
	# Define Our Deck
	suits = ["diamonds", "clubs", "hearts", "spades"]
	values = range(7, 15)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

	global deck
	deck =[]

	for suit in suits:
		for value in values:
			deck.append(f'{value}_of_{suit}')

	# Create our players
	global dealer, player,player2,player3
	dealer = []
	player = []
	player2 = []
	player3 = []


	# cartes dealer
	card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(card)
	# Append Card To Dealer List
	dealer.append(card)
	
	# Output Card To Screen
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

	# Grab a random Card For Player
	card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(card)
	# Append Card To Dealer List
	player.append(card)
	# Output Card To Screen
	global player_image
	player_image = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player_label.config(image=player_image)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image2
	player_image2 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player_label2.config(image=player_image2)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image3
	player_image3 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player_label3.config(image=player_image3)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image4
	player_image4 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player_label4.config(image=player_image4)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image5
	player_image5 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player_label5.config(image=player_image5)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image6
	player_image6 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player_label6.config(image=player_image6)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image7
	player_image7 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player_label7.config(image=player_image7)

	card = random.choice(deck)
	deck.remove(card)
	player.append(card)
	global player_image8
	player_image8 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player_label8.config(image=player_image8)


	
    # Grab a random Card For Player
	card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(card)
	# Append Card To Dealer List
	player2.append(card)
	# Output Card To Screen
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

	
    # Grab a random Card For Player
	card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(card)
	# Append Card To Dealer List
	player3.append(card)
	# Output Card To Screen
	global player3_image
	player3_image = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player3_label.config(image=player3_image)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image2
	player3_image2 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player3_label2.config(image=player3_image2)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image3
	player3_image3 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player3_label3.config(image=player3_image3)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image4
	player3_image4 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player3_label4.config(image=player3_image4)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image5
	player3_image5 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player3_label5.config(image=player3_image5)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image6
	player3_image6 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player3_label6.config(image=player3_image6)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image7
	player3_image7 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player3_label7.config(image=player3_image7)

	card = random.choice(deck)
	deck.remove(card)
	player3.append(card)
	global player3_image8
	player3_image8 = resize_cards_horizontal(f'cartes/cartes/{card}.png')
	player3_label8.config(image=player3_image8)
	
	



	# Put number of remaining cards in title bar
	root.title(f'{len(deck)} Cartes restanted')




my_frame = Frame(root, bg="green")
my_frame.pack(pady=20,fill=BOTH,expand=True)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Joueur1", bd=0)
dealer_frame.pack(side=BOTTOM,padx=5, ipadx=5)

player_frame = LabelFrame(my_frame, text="Joueur2", bd=0)
player_frame.pack(side=RIGHT,ipadx=5,pady=5)

player2_frame = LabelFrame(my_frame, text="Joueur3", bd=0)
player2_frame.pack(side=TOP, ipadx=5,pady=5)

player3_frame = LabelFrame(my_frame, text="Joueur4", bd=0)
player3_frame.pack(side=LEFT, ipadx=5,pady=5)

# Put cards in frames
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
player_label.grid(row=0,column=0,pady=5,padx=5,sticky=W)
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









# Shuffle Deck On Start
shuffle()


root.mainloop()