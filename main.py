# AE, EW, SC, DD Period 7th Build a Game 

import time
#EW Beginning dialouge
print("Welcome to the Adventure of a Lifetime!")
# SC Journey & variables
name = input("What is your hero's name?\n").strip().title()
wizard = input("Give me a name for the Wizard, please!\n").strip().title()
wizitem = input("Give me a noun. Trust\n").strip().lower()
time.sleep(3)
print(f"Your name is {name}, and you walk into a tavern hoping to find a quest and become a hero!")
time.sleep(3)
print("A wizard walks up to you, and says, 'Oy kid, what are you doing in such a place.'")
time.sleep(3)
print(f"{name}: I am {name}, and I wish to go on an adventure and become a hero!")
time.sleep(3)
print(f"{wizard}: Oh I see. Well I am missing something, and I am in desparate for someone to come fetch it for me.")
time.sleep(3)
print(f"{name}: Oh! Well what is it? Maybe I can go get it for you.")
time.sleep(3)
print(f"{wizard}: You'll do it? Well alright! It is a {wizitem}. Go and get it, come back, and you'll be the biggest hero of all!")
time.sleep(3)
print("The old wizard roughly pushes you out the door. You think he just wants you to leave the tavern, but that doesn't matter. You will go find the item and become a hero!")
time.sleep(3)

#Journey:
print(f"{name} is walking down a path, looking for anything that is could be a clue of how the wizard lost his {wizitem} and to see if you can find a way to get the wizard his {wizitem} back")
time.sleep(3)
print(f"After a little bit of walking down the path, you come across a crossroad, which way do you go, Left or right")
crossroad = input("You are walking and come across a crossroad, do you want t go left or right?")
left = input("You continue walking down the path and come across a dead end. Do you want to turn back or walk to the dead end?\n")
if right:
    input("You walk along the stream until you see a cool crystal. Do you pick up the crystal or leave it alone")
    if pick_up:
            print("You pick up the crystal and nothing happens")
else:
		print("You leave the crystal alone and walk away.")
crystal = input("Do you want to put it down or keep it?\n")
if put it down:
		print("You put down the crystal back on the ground and continue walking.")
elif:
		print(“You put the crystal in your satchel for safe keeping, you continue walking.”)
else:
	print(“You turn left and find yourself on another path going towards a forest”)
	continue = input(“Do you want to continue walking towards the forest or turn back?\n”)
	if continue:
		print(“You continue walking towards the forest”)
	else:
		print(“You turn back and walk towards the crossroad.”)

# Journey pt. 2 AE Crossroad

print("Walking along the path you hear a noise from behind, there are two options climb a tree or start walking faster along the path")
choice = input("What do you do?\n")
if choice 


# DD Monster encounters
import sys
import random

goblin = [ # Base goblin
"/|___|\\",
"|o\\ /o|",
"\\__^__/"
]
goblin_hurt = [ # Hurt goblin
"/|___|\\",
"|>\\ /o|",
"\\__^__/"
]
goblin_dead = [ # Dead goblin
"/|___|\\",
"|/x x\\|",
"\\__o__/"
]
bandit = [ # Base bandit
"/*****\\",
"|o\\`/o|",
"\\__w__/"
]
bandit_hurt = [ # Hurt bandit
"/*****\\",
"|>\\`/o|",
"\\__w__/"
]
bandit_dead = [ # Dead bandit
"/*****\\",
"|/x`x\\|",
"\\__o__/"
]
boss = [ # Base boss
"   /\\   ",
" _/ii\\_ ",
" /0``0\\ ",
" | ~~ |",
" ######",
"  #### ",
"   ##  "
]
boss_hurt = [ # Hurt boss
"   /\\   ",
" _/ii\\_ ",
" />``0\\ ",
" | ~~ |",
" ######",
"  #### ",
"   ##  "
]
boss_dead = [ # Dead boss
"   /\\   ",
" _/ii\\_ ",
" /x``x\\ ",
" | ~~ |",
" ######",
"  #### ",
"   ##  "
]
def weapon_use(): # We are gonna use a weapon A LOT, so we can do this to make it easy on future me :D
    while True:
        weapon_choosing = input("What weapon would you like to use? You have a shortsword and shortbow in your inventory. ").strip().capitalize()
        time.sleep(1)
        if weapon_choosing == "Shortbow" or weapon_choosing == "Bow":
            weapon_choice = "shortbow"
            break
        elif weapon_choosing == "Shortsword" or weapon_choosing == "Sword":
            weapon_choice = "sword"
            break
    print(f"You have chosen the {weapon_choice}.")
    time.sleep(1)
    if weapon_choice == "shortbow":
        damage = random.randint(1,6)+1 # Die roll
        print(f"You loosed an arrow from your {weapon_choice}, dealing {damage} damage.")
        time.sleep(1)
        return damage
    elif weapon_choice == "sword":
        damage = random.randint(1,8)+1 # Die roll
        print(f"You advance forward, swinging your sword. Your enemy gets caught in your swing, taking {damage} damage.")
        time.sleep(1)
        return damage
    time.sleep(2)


def goblin_encounter(): # We are gonna make a function so we can call a goblin fight simply anytime
    def goblin_turn():
        time.sleep(2)
        print("The goblin will attack now.")
        time.sleep(2)
        goblin_damage = random.randint(1,6)+2 # Die roll
        print(f"The goblin leaps at you and swings their crude sword down, dealing {goblin_damage} damage.")
        return goblin_damage
    def player_turn():
        time.sleep(3)
        print("It is your turn now.")
        time.sleep(1)
        damage = weapon_use()
        for item in goblin_hurt:
            print(item)
        return damage
    time.sleep(2)
    print("Oh no! A goblin has appeared and is ready to attack!")
    time.sleep(1)
    for item in goblin:
        print(item)
        player_hp = 25
        goblin_hp = 10
    while True:
        goblin_damage = goblin_turn()
        damage = player_turn()
        if goblin_hp <= damage:
            time.sleep(1)
            print("Congratulations, the goblin is slain.")
            time.sleep(1)
            for item in goblin_dead:
                print(item)
            break
        elif player_hp <= goblin_damage:
            print("You have died.")
            break
            sys.exit()
        elif goblin_hp > damage:
            goblin_hp -= damage
        elif player_hp > goblin_damage:
            player_hp -= goblin_damage
heart = [
"/**\\/**\\"
"\\"
]

def bandit_encounter(): # We are gonna make a function so we can call a bandit fight simply anytime
    def bandit_turn():
        time.sleep(2)
        print("The bandit will attack now.")
        time.sleep(2)
        bandit_damage = random.randint(1,6)+2 # Die roll
        print(f"The bandit dashes at you and swings their scimitar horizontally, dealing {bandit_damage} damage.")
        return bandit_damage
    def player_turn():
        time.sleep(3)
        print("It is your turn now.")
        time.sleep(1)
        damage = weapon_use()
        for item in bandit_hurt:
            print(item)
        return damage
    time.sleep(2)
    print("Oh no! A bandit has appeared and is ready to rob you!")
    time.sleep(1)
    for item in bandit:
        print(item)
        player_hp = 30
        bandit_hp = 15
    while True:
        bandit_damage = bandit_turn()
        damage = player_turn()
        if bandit_hp <= damage:
            time.sleep(1)
            print("Congratulations, the bandit is slain.")
            time.sleep(1)
            for item in bandit_dead:
                print(item)
            break
        elif player_hp <= bandit_damage:
            print("You have died.")
            break
            sys.exit()
        elif bandit_hp > damage:
            bandit_hp -= damage
        elif player_hp > bandit_damage:
            player_hp -= bandit_damage

def boss_encounter(): # We are gonna make a function so we can call a boss fight simply anytime
    def boss_turn():
        time.sleep(2)
        print("The boss will attack now.")
        time.sleep(2)
        boss_damage = random.randint(1,8)+2 # Die roll
        print(f"The boss raises their hand and summons a fireball and throws it at you, dealing {boss_damage} damage.")
        return boss_damage
    def player_turn():
        time.sleep(3)
        print("It is your turn now.")
        time.sleep(1)
        damage = weapon_use()
        for item in boss_hurt:
            print(item)
        return damage
    time.sleep(2)
    print("Be ready. The boss is here, ready to fight you. Be on your guard, and don't die.")
    time.sleep(3)
    for item in boss:
        print(item)
        player_hp = 40
        boss_hp = 50
    while True:
        boss_damage = boss_turn()
        damage = player_turn()+5
        damage =+ 5
        if boss_hp <= damage:
            time.sleep(1)
            print("The boss crumples to the ground, defeated.")
            time.sleep(2)
            for item in boss_dead:
                print(item)
            break
        elif player_hp <= boss_damage:
            print("You have died.")
            break
            sys.exit()
        elif boss_hp > damage:
            boss_hp -= damage
        elif player_hp > boss_damage:
            player_hp -= boss_damage