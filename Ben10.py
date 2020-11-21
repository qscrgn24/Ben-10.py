#!/usr/bin/python3

import random


def randomize(cards):
	shuffled = cards[:]
	random.shuffle(shuffled)
	return shuffled


def card_distribution(shuffled,player1_cards,player2_cards):
	c=0
	t=len(shuffled)
	for card in shuffled:
		if c%2==0:
			player1_cards.append(card)
		else:
			player2_cards.append(card)
		c+=1

	return player1_cards, player2_cards


def show(player_cards):
	for key, value in player_cards[0].items():
		print(key + " : " + str(value))


def choose_option():
	print("\nChoose a trait of your character to PLAY")
	# print("\n")
	print("[1] Attack")
	print("[2] Cost")
	print("[3] Power")
	print("[4] Transform")
	print("[5] Damage")
	try:
		option = int(input("Enter the no. of the chosen trait: "))
		# print(option)
		if not (option>0 and option<6):
			print("Wrong option.. choose again")
			option = choose_option()
		return(option)

	except:
		print("Please Enter a no. between 1-5")
		option = choose_option()


def option_select(i):
    switcher={
            1:'Attack',
            2:'Cost',
            3:'Power',
            4:'Transform',
            5:'Damage'
         }
    return switcher.get(i,"Wrong option.. choose again")
	

def compare(player1_cards,player2_cards,chosen_trait):
	if chosen_trait=="Cost":
		if player1_cards[0][chosen_trait]<player2_cards[0][chosen_trait]:
			return player1
		elif player1_cards[0][chosen_trait]>player2_cards[0][chosen_trait]:
			return player2
		else:
			print("SAME ---> Advantage given to opponent")
			return player2
	else:
		if player1_cards[0][chosen_trait]>player2_cards[0][chosen_trait]:
			return player1
		elif player1_cards[0][chosen_trait]<player2_cards[0][chosen_trait]:
			return player2
		else:
			print("SAME ---> Advantage given to opponent")
			return player2


def deck_update(player1_cards,player2_cards,winner):
	temp1 = player1_cards.pop(0)
	temp2 = player2_cards.pop(0)
	if winner==player1:
		player1_cards.append(temp1)
		player1_cards.append(temp2)
	elif winner==player2:
		player2_cards.append(temp1)
		player2_cards.append(temp2)



player1 = input("Enter Name of Player1: ")
player2 = input("Enter Name of Player2: ")
player1_cards = []
player2_cards = []
current = player1
no_of_cards_p1 = 100
no_of_cards_p2 = 100
flag = 0
cards = ([
	{"Name":"Princess","Description":"Human Character who performs magic tricks as tool of weapon", "Attack":500, "Cost":2, "Power":3000, "Transform":30000, "Damage":35},
	{"Name":"KevinLevin","Description":"Human Character & friend of ben, Ability to convert body into Steel", "Attack":700, "Cost":6, "Power":4000, "Transform":40000, "Damage":50},
	{"Name":"Spitter","Description":"Alien Character spits damge on opponent", "Attack":700, "Cost":6, "Power":5000, "Transform":30000, "Damage":35},
	{"Name":"Dr. Fourarms","Description":"Alien Character combination of victor & Fourarms", "Attack":880, "Cost":6, "Power":6000, "Transform":40000, "Damage":65},
	{"Name":"Dr. Animo","Description":"Human Character who can revive anything dead.", "Attack":640, "Cost":3, "Power":5000, "Transform":40000, "Damage":48},
	{"Name":"HeatBlast","Description":"Alien Character who can live and breathe fire", "Attack":800, "Cost":7, "Power":3000, "Transform":50000, "Damage":60},
        {"Name":"Eyeguy","Description":"Alien character of Ben who has eyes on his whole body & ear on head. He throws destructive laser through each of its eye","Attack":1000,"Cost":9,"Power":8000,"Transform":75000,"Damage":72},
        {"Name":"Upchuk","Description":"Alien character of Ben who has the power to eat anything & convert it to destructible fire shots","Attack":600,"Cost":5,"Power":3000,"Transform":40000,"Damage":49},
        {"Name":"Spider Monkey","Description":"Alien character of Ben who looks like a monkey & spider and has the ability to stick to walls and shoot web. It also has super human ability","Attack":1000,"Cost":9,"Power":10000,"Transform":90000,"Damage":93},
        {"Name":"Grey Matter","Description":"The smallest alien character of Ben and also the maker of the omnitrix. He has very sharp brain","Attack":500,"Cost":5,"Power":1000,"Transform":20000,"Damage":20},
        {"Name":"Humongosor","Description":"Half human and rest dinosaur and has the ability to change size and power increase with increase in size","Attack":1200,"Cost":10,"Power":12000,"Transform":80000,"Damage":95},
        {"Name":"Clancy","Description":"Human character who has the ability to control insects and use them to betray others","Attack":600,"Cost":3,"Power":1000,"Transform":50000,"Damage":10},
        {"Name":"Benvictor","Description":"Alien character of Ben who is gained during encounter with Dr. Victor and evil ghostfreak","Attack":1000,"Cost":9,"Power":9000,"Transform":70000,"Damage":90},
        {"Name":"Benwolf","Description":"Alien character of Ben who looks like a werewolf and has super strength and the ability of blowing sonic waves","Attack":900,"Cost":8,"Power":8000,"Transform":80000,"Damage":90},
        {"Name":"XLR8","Description":"Alien character of Ben who has lightning quick reflexes and has the ability to reach above 300mph. He appose friction to run on any surface","Attack":330,"Cost":3,"Power":3000,"Transform":40000,"Damage":70},
        {"Name":"DNAliens","Description":"This villain alien is part human and part alien drones who serve the highbred. They use special identity masks.","Attack":900,"Cost":10,"Power":6000,"Transform":90000,"Damage":55},
        {"Name":"Enoch","Description":"Member of a secret organisation who deals in illegal alien spyware and technology. He is also behind omnitrix","Attack":650,"Cost":3,"Power":2000,"Transform":20000,"Damage":30},
        {"Name":"Coldblast","Description":"character of Ben who is just the opposite of heat blast. It can freeze things","Attack":200,"Cost":2,"Power":2000,"Transform":50000,"Damage":40},
        {"Name":"Forever Knights","Description":"Part of a secret organisation originally formed in middle ages and deals in illegal alien technology","Attack":450,"Cost":4,"Power":1500,"Transform":25000,"Damage":19},
        {"Name":"Echo","Description":"Alien character of Ben who is a living amplifier and packs some serious power. He can produce steel shattering waves and can duplicate indefinitely","Attack":900,"Cost":9,"Power":7000,"Transform":90000,"Damage":96},
        {"Name":"Gwen Tennyson","Description":"Cousin of Ben and can also perform some magic trick and actions as well","Attack":650,"Cost":6,"Power":1000,"Transform":15000,"Damage":10},
        {"Name":"Kevin Evil Form","Description":"Human character turned into alien by absorbing the power of the omnitrix","Attack":400,"Cost":4,"Power":3000,"Transform":20000,"Damage":70},
        {"Name":"Hex","Description":"Human character with the power of performing evil magic tricks. He is the uncle of princess","Attack":740,"Cost":6,"Power":3000,"Transform":40000,"Damage":27},
        {"Name":"Chromastone","Description":"Nearly indestructible alien of Ben who can absorb energy and rechannel it to destructive laser blast","Attack":1000,"Cost":9,"Power":7500,"Transform":40000,"Damage":100},
        {"Name":"Stinkfly","Description":"Winged alien character of Ben and expert flyer. It defends itself using pincers and has sharp tails and can do amazing acrobatic moves midair","Attack":800,"Cost":7,"Power":6000,"Transform":50000,"Damage":69},
        {"Name":"Ben Tennyson","Description":"The leading hero of this game and has the ability to become different alien character with all his power and capabilities through his omnitrix","Attack":1500,"Cost":15,"Power":1000,"Transform":100000,"Damage":99},
        {"Name":"Goop","Description":"Alien character of Ben who can change the shape of its body and can stretch is body","Attack":900,"Cost":9,"Power":8000,"Transform":89000,"Damage":88},
        {"Name":"Ditto","Description":"Alien character of Ben who can duplicate infinitely","Attack":400,"Cost":3,"Power":1200,"Transform":23000,"Damage":18},
        {"Name":"Max Tennyson","Description":"Grandfather of Ben who is also a semi retired member of a secret investigating organisation called plumbers","Attack":325,"Cost":8,"Power":3000,"Transform":20000,"Damage":10},
        {"Name":"Cannonbolt","Description":"Alien character of Ben who has the ability to roll and attack like a cannon and also has a reflective surface on his body to reflect light","Attack":920,"Cost":7,"Power":8000,"Transform":70000,"Damage":77},
        {"Name":"Ghost Freak","Description":"Shadowy alien character of Ben with ghost like power. He can pass through walls and become invisible","Attack":200,"Cost":5,"Power":3000,"Transform":20000,"Damage":51},
        {"Name":"Acid Breath","Description":"Human villain who belongs to the group of jokers and has the power to blow out acid and acid smoke through breath","Attack":250,"Cost":1,"Power":150,"Transform":9000,"Damage":5},
        {"Name":"Megawatt","Description":"Alien character of Ben who is very small in size but have the power to produce and flow electricity and can also multiply in numbers","Attack":600,"Cost":7,"Power":3500,"Transform":50000,"Damage":47},
        {"Name":"Phil","Description":"Human character who is also a part of secret organisation known as plumber. Later on, he misuses secret gadgets","Attack":750,"Cost":5,"Power":2000,"Transform":30000,"Damage":70},
        {"Name":"Alien Interpreter","Description":"Alien who has come to destroy earth through his master tick who absorb energy of earth","Attack":543,"Cost":5,"Power":2000,"Transform":40000,"Damage":10},
        {"Name":"Articguna","Description":"Alien character of Ben with the ability to freez water through its breath","Attack":500,"Cost":4,"Power":4000,"Transform":40000,"Damage":33},
        {"Name":"Jetray","Description":"Alien character of Ben who can move several times faster than the spped of sound in air. It can also give neuroshock blast","Attack":1000,"Cost":9,"Power":9000,"Transform":88000,"Damage":91},
        {"Name":"Ripjaws","Description":"Water alien character of Ben who works efficiently in water and can change legs into large fins and has powerful jaws to deliver devastating bite","Attack":800,"Cost":7,"Power":2000,"Transform":50000,"Damage":62},
        {"Name":"Leader","Description":"This character battles the alien interpreter","Attack":600,"Cost":5,"Power":2000,"Transform":40000,"Damage":27},
        {"Name":"Kelvin","Description":"Human character with the ability to absorb energy from anything and use it for his use","Attack":570,"Cost":4,"Power":2000,"Transform":15000,"Damage":23},
        {"Name":"Rojo","Description":"Human character who looks like alien after coming in contact with an alien machine. She is ordered to take back omnitrix by vilgax","Attack":750,"Cost":5,"Power":2000,"Transform":30000,"Damage":70},
        {"Name":"Highbreed","Description":"Alien character who believe that DNA is prusit of all alien spicies and seek to cleanse lower life forms","Attack":700,"Cost":7,"Power":7000,"Transform":60000,"Damage":76},
        {"Name":"Wildwine","Description":"Alien character of Ben which can grow and interact with plant and has the ability to throw green bomb for defence","Attack":650,"Cost":5,"Power":2500,"Transform":45000,"Damage":30},
        {"Name":"Diana","Description":"This character also battles the alien interpreter","Attack":600,"Cost":5,"Power":2000,"Transform":40000,"Damage":27},
        {"Name":"Way Big","Description":"Alien character of Ben who is over 500ft long and is rare","Attack":1000,"Cost":12,"Power":10000,"Transform":99000,"Damage":98},
        {"Name":"Upgrade","Description":"Biochemical alien character of Ben which is a living machine with a liquid metal skin. It can covert any device into a hightech technology","Attack":400,"Cost":5,"Power":3000,"Transform":50000,"Damage":30},
        {"Name":"Frightwig","Description":"Human character who has the ability to attack with her wig. This viallain belongs to the group of jokers","Attack":800,"Cost":5,"Power":2000,"Transform":40000,"Damage":25},
        {"Name":"Fourarms","Description":"Alien character of Ben who is 12ft long with four arms and armored skin to protect from harm","Attack":460,"Cost":5,"Power":3000,"Transform":50000,"Damage":88},
        {"Name":"Diamondhead","Description":"Alien character of Ben who has a crystalline body harder than diamond which makes it invulnerable to most physical and light-based attacks","Attack":800,"Cost":7,"Power":3000,"Transform":25000,"Damage":60},
        {"Name":"Swampfire","Description":"Alien character of Ben that looks like heap and has the ability to regenerate, control plant life and shoot fire","Attack":1200,"Cost":10,"Power":10000,"Transform":90000,"Damage":105},
        {"Name":"Big Chill","Description":"Flying alien character of Ben who has the ability to pass through any matter and becime invisible and can drop the temperature to absolute zero","Attack":1100,"Cost":11,"Power":11000,"Transform":95000,"Damage":96},
        {"Name":"Benmummy","Description":"Alien character of Ben which looks like a mummy. It is gained by Ben during encounter with evil mummy","Attack":700,"Cost":7,"Power":4000,"Transform":40000,"Damage":35},
	])

'''
for card in cards:
	print(card)
print("\n")


for card in shuffled:
	print(card)
print("\n")
'''

shuffled = randomize(cards)
player1_cards,player2_cards = card_distribution(shuffled,player1_cards,player2_cards)

while ((no_of_cards_p1 and no_of_cards_p2) > 0):
	try:
		no_of_cards_p1 = len(player1_cards)
		no_of_cards_p2 = len(player2_cards)
		print("\nno_of_cards_p1: ", no_of_cards_p1)
		print("no_of_cards_p2: ", no_of_cards_p2)
		turn = current
		print("\n" + turn + "'s CHANCE")
		if turn==player1:
			show(player1_cards)
			print("\n" + player1_cards[0]['Name'] + " VS " + player2_cards[0]['Name'])
			option = choose_option()
			chosen_trait = option_select(option)
			print(chosen_trait + " : " + str(player1_cards[0][chosen_trait]) + " VS " + chosen_trait + " : " + str(player2_cards[0][chosen_trait]))
		elif turn==player2:
			show(player2_cards)
			print("\n" + player2_cards[0]['Name'] + " VS " + player1_cards[0]['Name'])
			option = choose_option()
			chosen_trait = option_select(option)
			print(chosen_trait + " : " + str(player2_cards[0][chosen_trait]) + " VS " + chosen_trait + " : " + str(player1_cards[0][chosen_trait]))
		else:
			print("Problem in turn")

		# option = choose_option()
		# print(option)
		# chosen_trait = option_select(option)
		# print("You have chosen: " + chosen_trait + " : " + player1_cards[0][chosen_trait])
		winner = compare(player1_cards,player2_cards,chosen_trait)
		print("Winner for this round is: ",winner)
		deck_update(player1_cards,player2_cards,winner)

		current = winner	
		print("################## END OF TURN ##################")

	except:
		print("\n -------X------ GAME OVER ------X-------")
