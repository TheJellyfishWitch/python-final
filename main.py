# AE, EW, SC, DD Period 7th Build a Game 

import time
import sys
import random
def die(): #Dan made this
    died = [
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|             You died.             |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
    ]
    for item in died:
        print(item)
    sys.exit()
inv = ["Shortsword", "Shortbow"] #Dan made this
def inventory():
    print("These are the items in your inventory.")
    for item in inv:
        print(item)
        time.sleep(1)
    while True:
        drop = input("Do you want to drop anything? ").strip().capitalize()
        if "Yes" in drop:
            time.sleep(1)
            dropping_item = input("What item do you want to drop? ").strip().capitalize()
            time.sleep(2)
            if dropping_item == "Sword" or dropping_item == "Shortsword":
                print("You cannot drop your sword.")
                break
            elif dropping_item == "Bow" or dropping_item == "Shortbow":
                print("You cannot drop your bow")
                break
            else:
                try:
                    inv.remove(dropping_item)
                except ValueError:
                    print("That is not in your inventory")
                    break
                else:
                    print(f"{dropping_item} has been dropped.")
                    break
        else:
            break

#EW Beginning dialouge
print("Welcome to the Adventure of a Lifetime!")
time.sleep(2)
print("Anytime you can type, you can type 'Inventory' to open your inventory.")
time.sleep(2)
# SC Journey & variables
name = input("What is your hero's name?\n").strip().title()
wizard = input("Give me a name for the Wizard, please!\n").strip().title()
wizitem = input("Give me a noun. Trust\n").strip().lower()
print(f"Your name is {name}, and you walk into a tavern hoping to find a quest and become a hero!")
time.sleep(2)
print("A wizard walks up to you, and says, 'Oy kid, what are you doing in such a place.'")
time.sleep(3)
print(f"{name}: I am {name}, and I wish to go on an adventure and become a hero!")
time.sleep(3)
print(f"{wizard}: Oh I see. Well I am missing something, and I am in desparate need for someone to come fetch it for me.")
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
    print(f"After a little bit of walking down the path, you come across a crossroad, which way do you go?")
    crossroad = input("You are walking and come across a crossroad, do you want to go left or right?\n").strip().capitalize()

    if crossroad == "Inventory":
        inventory()
    elif crossroad == "Right":
        print("You turn right and find a stream, you walk along it\n")
    else:
        dead_end = input("You continue walking down the path and come across a dead end. Do you want to turn back or walk to the dead end?\n").strip().capitalize()

    if dead_end == "Walk":
        print("You walk along the stream until you see a cool crystal. Do you pick up the crystal or leave it alone")

    cool = input("Do you pick up the crystal?\n")
    elif dead_end == "Inventory":
        inventory()

    if cool == "Pickup":
        print("You pick up the crystal and nothing happens")
    inv.append("Crystal")
    elif cool == "Inventory":
        inventory()
    else:
        print("You leave the crystal alone and walk away.")

    crystal = input("Do you want to put it down or keep it?\n").strip().capitalize()

    if crystal == "Putitdown":
        print("You put down the crystal back on the ground and continue walking.")
        inv.remove("Crystal")
    elif crystal == "Inventory":
        inventory()
    else:
        print("You put the crystal in your satchel for safe keeping, you continue walking.")

    resume = input("Do you want to walk towards the forest or turn back?\n").strip().capitalize()

if resume == "Walk":
    print("You continue walking towards the forest")
    time.sleep(2)
    print("You come up on a crossroad. Left smells vaguely like strawberries and right looks perfectly normal.")
    time.sleep(2)
    lefty = input("Do you go left or right?").strip().lower()
    if lefty == "left":
        print("You continue going until you see a cave, which you go in, because caves are cool.")
        time.sleep(2)
        print("It smells EXTREMElY strawberry like in here. Weird.")
        time.sleep(2)
        chest == input("You see a chest, do")
    else:
        print("You go to the right and continue walking down the path")
    elif resume == "Inventory":
        inventory()
        else:
        die()

    # AE Questions
    print("Strawberry Cult Leader: In order to enter our cult you must pass this trial,")
    question_one = input("How many seeds does the average strawberry have?\n").strip().capitalize()
    if question_one == "200":
        print("Correct!")
    else:
        print("You made the Cultists mad")
        die()
    question_two = input("How many petals does the average strawberry flower have?\n").strip().capitalize()
    if question_two == "5-7":
        print("Correct!")
    else:
        print("You made the Strawberry Cultists mad.")
        die()
    question_three = input("Which fruit is the first to ripen in the spring?\n").strip().capitalize()
    if question_three == "Strawberries":
        print("Correct!")
    else:
        print("You made the Strawberry Cultists mad.")
        die()
    question_four = input("How many pounds of frest strawberries do Americans eat?\n")
    if question_four == "3.4":
        print("Correct!")
    else:
        print("You made the Strawberry Cultists mad.")
        die()
    question_five = input("One acre of land can grow how many strawberries?\n").strip().capitalize()
    if question_five == "50,000":
        print("Correct!")
    else:
        print("You made the Strawberry Cultists mad.")
        die()
    question_six = input("True or False: Ancient Romans used strawberries to treat everything from depression to fever and sore throats\n").strip().capitalize()
    if question_six == "True":
        print("Correct!")
    else:
        print("You made the Strawberry Cultists mad.")
        die()
    question_seven = input("True or False: Every strawberry is hand-picked about every three days\n").strip().capitalize()
    if question_seven == "True":
     print("Correct!")
    else:
    print("You made the Strawberry Cultists mad.")
        die()
    question_eight = input("What temperature is perfect for strawberries?\n").strip().capitalize()
    if question_eight == "55-78":
        print("Correct!")
    else: 
        print("You made the Strawberry Cultists mad.")
        die()
print("Strawberry Cult Leader: Good job! You passed all of our questions and now an official cult member!")
print("Another member of the Strawberry Cult walks up to you holding a strawberry cloke reverently")
accept = input("Do you accept?\n").strip().capitalize()
if accept == "Yes":
    print("The member hands you the cloak you put it on, you gain 10 hearts")
else:
    print("Strawberry Cult Leader: You don't accept the cloak. Well then, by the power of the strawberry gods we give you this!...")
    time.sleep(1)
    print("Pink lightning rains from the sky, all you see is the cult leader standing before you")
    die()


# DD Monster encounters

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
def weapon_use(): # We are gonna use a weapon A LOT, so we can do this to make it easy on future me :D #Dan made this
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

def goblin_encounter(): # We are gonna make a function so we can call a goblin fight simply anytime #Dan made this
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
        goblin_hp = 15
    if accept == "Yes":
        player_hp = 35
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
            die()
            break
        elif goblin_hp > damage:
            goblin_hp -= damage
        elif player_hp > goblin_damage:
            player_hp -= goblin_damage

def boss_encounter(): # We are gonna make a function so we can call a boss fight simply anytime #Dan made this
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
    if accept == "Yes":
        player_hp = 50
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
            reward = "cool"
            break
        elif player_hp <= boss_damage:
            die()
            sys.exit()
            break
        elif boss_hp > damage:
            boss_hp -= damage
        elif player_hp > boss_damage:
            player_hp -= boss_damage
    return reward
    
# Journey peice AE Crossroad

print("Walking along the path you hear a noise from behind, there are two options climb a tree or start walking faster along the path")
choice = input("What do you do? Climb or Walk?\n").strip().capitalize()
if choice == "Climb":
    print("You begin to climb the tree, reaching the top you see a eagle's nest, would you like to climb higher or go back down?")
    tree_choice = input("Will you choose to go higher or go down?").strip().capitalize()
if tree_choice == "Gohigher":
    print("You reach the top of the tree, the view is beautiful, a forest of trees and a setting sun. As your admiring the scene a gigantic eagle comes and grabs you by the shoulders and carries you off. You scream.")
    die()
else:
    print("You climb back down the tree when you land safely on the path as something tackles you from behind") # encounter
    goblin_encounter
else:
    print("You begin to walk faster until you start to run, something tackles you") # encounter
    goblin_encounter



if boss_encounter() == "cool":
    print("You look at the item, exilerated yet exhausted. You know it is time to go home.")
    time.sleep(2)
    print("The journey back is easier than the one before, and you are able to make it back within a day despite the item you are dragging behind you.")
    time.sleep(3)
    print("Once you get out, you burst into the tavern and everyone looks up at you with shock on their faces")
    time.sleep(3)
    print(f"{name}: {wizard}!")
    time.sleep(1)
    print(f"{wizard}: What? *very clearly annoyed at you*")
    time.sleep(2)
    print(f"{name}: I have your {wizitem}! I battled a wizard to do it!")
    time.sleep(2)
    print(f"{wizard}: Oh... Thank you. You actually did it.")
    time.sleep(2)
    print("The wizard yells to everyone")
    time.sleep(2)
    print(f"Look here everyone! This young hero brought back my {wizitem}! Praise him!")
    time.sleep(2)
    print("Everyone gives you a halfhearted applause and quickly turns around to what they were doing. You beam and jollily skip out of the room.")
    time.sleep(2)
    print("The end!")

