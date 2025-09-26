# AE, EW, SC, DD Period 7th Build a Game 

import time
#EW Beginning dialouge
print("Welcome to the Adventure of a Lifetime!")
# SC Journey & variables
name = input("What is your hero's name?\n").strip().title()
wizard = input("Give me a name for the Wizard, please!: \n").strip().title()
wizitem = input("Give me a noun. Trust\n").strip().lower()
print(f"{name} is down in a tavern, they are young and want to start their first adventure to become a proper hero! A wizard comes out from behind a corner and they ask {name} if they can help the poor wizard get his {wizitem} back! {name} agrees to help the poor wizard get his {wizitem} back! They start to go on their way...")
print(f"Your name is {name}, and you walk into a tavern hoping to find a quest and become a hero")
print("A wizard walks up to you, and says, 'Oy kid, what are you doing in such a place.'")
print(f"{name}: I am {name}, and I wish to go on an adventure and become a hero!")
print(f"{wizard}: Oh I see. Well I am missing something, and I am in desparate for someone to come fetch it for me.")
print(f"{name}: Oh! Well what is it? Maybe I can go get it for you.")
print(f"{wizard}: You'll do it? Well alright! It is a {wizitem}. Go and get it, come back, and you'll be the biggest hero of all!")
print("The old wizard roughly pushes you out the door. You think he ")

#Journey:
print(f"{name} is walking down a path, looking for anything that is could be a clue of how the wizard lost his {wizitem} and to see if you can find a way to get the wizard his {wizitem} back")

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
        player_hp = 25
        bandit_hp = 10
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
    
boss_encounter()


# AE endings & some pieces of the journey

# Crossroad

print(f"{name} stops on the path hearing something from behind, run along the path or climb a tree :)")
path = input("What are you doing?\n").strip().lower()

tree = input("You see some squirrels: climb higher or go back down\n").strip().lower()
climb = print("You reach the top of the tree, an eagle's nest, unprotected")
down = print("You land safely at the crossroad as something tackles you from behind") # encounter with ememy

run = print("You run along the path as something tackles you") # encounter with enemy

if tree:
    input("You see some squirrels: climb higher or go back down\n").strip().lower()
else:
    print("You run along the path as something tackles you") # encounter with enemy


if climb:
    print("You reach the top of the tree, an eagle's nest, unprotected")
else:
    print("You land safely at the crossroad as something tackles you from behind") # encounter with ememy