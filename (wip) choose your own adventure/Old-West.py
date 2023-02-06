import os
import sys
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer

import tkinter as tk
from tkinter import ttk
import random
import time


poss_actions = []
curr_action = ''
poss_loc = ['the dusty road', 'the time machine']
curr_loc = 'the time machine'
town_first_time = True
fought = False
inventory = []
items = ['Gun','Money','Water','Tools','Lucky hat', 'Tobacco', 'Knife']
chose = ''
def TravelToPast():
    global poss_actions
    global curr_action
    global poss_loc
    global curr_loc
    global town_first_time
    global fought
    global inventory
    global items
    global chose
    #check for an item
    def checkitem(item):
        global inventory
        for items in inventory:
            if items['name'] == item:
                return True
            else:
                pass
        return False

    #check for money
    def checkmoney(needed):
        global inventory
        for item_index in range(len(inventory)):
            if inventory[item_index]['name'] == 'money':
                if inventory[item_index]['money'] >= needed:
                    return True
                else: 
                    return False
            else: 
                pass

    def moneyamt():
        global inventory
        for item_index in range(len(inventory)):
            if inventory[item_index]['name'] == 'money':
                return inventory[item_index]['money']
            else:
                pass

    #change money
    def changemoney(change):
        for item_index in range(len(inventory)):
            if inventory[item_index]['name'] == 'money':
                inventory[item_index]['money'] += change
            else:
                pass

    #gun data
    def checkbullets(needed):
        global inventory
        for item_index in range(len(inventory)):
            if inventory[item_index]['name'] == 'gun':
                if inventory[item_index]['bullets'] >= needed:
                    return True
                else: 
                    return False
            else: 
                pass

    def changebullets(change):
        for item_index in range(len(inventory)):
            if inventory[item_index]['name'] == 'gun':
                inventory[item_index]['bullets'] += change
            else:
                pass


    #the places you can go
    
    def place_pick():
        global curr_loc
        loc = [
            inquirer.List('location',
                        message="Where do you want to go?",
                        choices=poss_loc)
        ]
        loc = inquirer.prompt(loc)
        if curr_loc == loc['location']:
            print("\nYou are already here, choose again")
            time.sleep(1)
            place_pick()
        else:
            print("\nYou head off to " + loc['location'])
            curr_loc = loc['location']
            time.sleep(3)
            location_choices()

    def action_pick():
        global curr_action
        global poss_actions
        act = [
            inquirer.List('action',
                        message = "What do you want to do?",
                        choices = poss_actions)   
        ]
        act = inquirer.prompt(act)
        curr_action = act['action']
        time.sleep(3)
        action_choices()

    def action_choices():
        global curr_action
        global poss_actions
        global poss_loc
        global curr_loc
        global fought
        if curr_action == 'Ask to buy tools':
            if checkitem('tools') == True:
                print("\nYou already have tools and dont need to buy them")
                time.sleep(2)
                action_pick()
            else:
                print("\nYou ask the man if he would sell you a few specific tools, and although he is reluctant, he says hes willing to hand them over for 10 dollars")
                poss_actions = ["buy the tools", "go back to the workshop"]
                time.sleep(2)
                action_pick()
        if curr_action == 'go back to the workshop':
            time.sleep(2)
            workshop()
        if curr_action == 'buy the tools':
            if checkmoney(10) == True:
                print("\n The man gives you the tools and you give him 10 dollars")
                changemoney(-10)
                inventory.append({'name': 'tools'})
                time.sleep(2)
                action_pick()
            elif checkmoney(10) == False:
                print("\nYou don't have enough money for that, you may want to find a place to make some")
                time.sleep(2)
                action_pick()
        if curr_action == "Ask to buy Glass":
            print("\nYou ask the man if he'd sell you some glass, and he tells you that the wares aren't cheap. You tell him you only need a small piece and he says he can make it for you for 12 dollars")
            poss_actions = ["buy the glass", "go back to the workshop"]
            time.sleep(2)
            action_pick()
        if curr_action == 'buy the glass':
            if checkmoney(12) == True:
                print("\n The man gives you the glass and you give him 12 dollars")
                changemoney(-12)
                inventory.append({'name': 'glass'})
                time.sleep(2)
                action_pick()
            elif checkmoney(12) == False:
                print("\nYou don't have enough money for that, you may want to find a place to make some")
                time.sleep(2)
                action_pick()
        if curr_action == 'leave':
            print("\nYou head back out to the town and look around for where to go next")
            poss_loc = ["the dusty road", "the workshop", "the saloon"]
            curr_loc = 'gold rush town'
            gold_rush_town()
        if curr_action == 'play':
            broke()
            time.sleep(1)
            print("\nyou have " + str(moneyamt()) + " dollars")
            print("\nYou decide to play blackjack.")
            if checkitem('hat') == True:
                print("\nYour are dealt two cards and instantly get 21. You are rewarded 5 dollars")
                changemoney(5)
                time.sleep(1)
                print("\nIt must be your lucky hat, good for you.")
                action_pick()
            else:
                blackjack()
        if curr_action == 'run':
            youdieanyways = random.getrandbits(1)
            if youdieanyways == True and checkitem("water") == False:
                time.sleep(1)
                print("\nYou somehow get away but without water, and no chance of walking near deadwood town again, you die in the middle of the desert, unlucky.")
                exit()
            if youdieanyways == True and checkitem('water') == True:
                time.sleep(1)
                print("\nYou get away, you don't really want to go anywhere near that town every again.")
                print("you get back to the crossroads at the dirt path")
                poss_loc = ['the time machine', 'gold rush town']
                place_pick()
            if youdieanyways == False:
                time.sleep(1)
                print("\nAs you try to run, one of them pulls out a gun and shoots you in the leg.")
                print("they take everything they can find and throw you in a ditch to die.")
                exit()
        if curr_action == 'fight':
            fought = True
            if checkitem('gun') == False and checkitem('knife') == False:
                time.sleep(1)
                print("\nYou try to fight them with your bare hands but they are 6 and you are one, they stab you till you die out and rob you of your possesions")
                print("\nWhat where you thinking?")
                time.sleep(2)
                print("\nYou die.")
                exit()
            elif checkitem('gun') == True and checkitem('hat') == True and checkbullets(4) == True:
                time.sleep(1)
                print("\nDespite the 6 men surrounding you, with your lucky hat and your gun, it only takes 4 bullets to take them all down.")
                changebullets(-4)
                changemoney(10)
                time.sleep(2)
                print("\nYou find a solid 10 dollars off of their bodies and leave them for the ravens in the middle of the desert.")
                deadwood()
            elif checkitem('gun') == True and checkitem('hat') == False and checkbullets(6) == True:
                time.sleep(1)
                print("\nThe six men around you pull knives out but they stand no match to your modern gun, as you dispatch all of them with ease.")
                changebullets(-6)
                changemoney(10)
                time.sleep(2)
                print("\nYou find a solid 10 dollars off of their bodies and leave them for the ravens in the middle of the desert.")
                deadwood()
            elif checkitem('gun') == True and checkitem('hat') == False and checkbullets(6) == False:
                time.sleep(1)
                print("\nAlthough you have your gun, You dont have enough bullets in your gun and only end up getting stabbed.")
                time.sleep(2)
                print("\nYou die.")
                exit()
            elif checkitem('knife') == True and checkitem('hat') == True:
                time.sleep(1)
                print("\nDespite your lack of a gun, you trust your combat skills and your lucky hat to win this fight.")
                print("\nYou manage to wound three of the 6 and as they fail to land a single hit on you, you somehow manage to get the rest to run away.")
                time.sleep(0.5)
                print("\nYou take all the money off the ones you wounded and make a solid 5 dollars.")
                changemoney(5)
                deadwood()
            else:
                time.sleep(1)
                print("\nYou try to fight them with your bare hands but they are 6 and you are one, they stab you till you die out and rob you of your possesions")
                print("\nWhat where you thinking?")
                time.sleep(2)
                print("\nYou die.")
                exit()
        if curr_action == 'play blackjack':
            broke()
            print("\nyou have " + str(moneyamt()) + " dollars")
            print("\nYou decide to play blackjack.")
            if checkitem('hat') == True:
                print("\nYour are dealt two cards and instantly get 21. You are rewarded 3 dollars")
                changemoney(3)
                time.sleep(1)
                print("\nIt must be your lucky hat, good for you.")
                action_pick()
            else:
                badblackjack()
        if curr_action == 'back to the bar':
            print("\nYou walk away from the table")
            bar()
        if curr_action == 'ask for water':
            print('\nYou walk up to the bartender and ask him to fill up your water bottle.')
            print("\nHe tells you that nothing is free and that it'll cost you 3 dollars.")
            print("\nYou have " + str(moneyamt()) + " dollars")
            poss_actions = ['pay for the water', 'back to the bar']
            action_pick()
        if curr_action == 'pay for the water':
            if checkmoney(3) == True:
                time.sleep(1)
                print("\nYou pay for the water.")
                inventory.append({'name': 'glass'})
                bar()
            else:
                time.sleep(0.5)
                print("\nYou don't have enough money for the water.")
                bar()

    def broke():
        if checkmoney(1) == False and (checkitem('tools') == False or checkitem('glass') == False):
            print("\nYou have no more money and cannot repair your machine.")
            time.sleep(1)
            print("\nYou die.")
            exit()
            


    def location_choices():
        global curr_loc
        global poss_loc
        if curr_loc == 'the dusty road':
            print("\nThe road is rough and wind blows in your face.")
            poss_loc = ['the dusty road', 'the time machine', 'gold rush town', 'deadwood town']
            place_pick()
        elif curr_loc == 'the time machine':
            if checkitem('tools') == True and checkitem('glass pane') == True:
                print("\nYou have tools and the glass pane, so you can repair your time machine.")
                time.sleep(3)
                print("\nIt took a while but after a bit you fixed the machine enough to travel again!")
                time.sleep(4)
                print("\n\nCONGRATS YOU COMPLETED THE OLD WEST!")
                time.sleep(4)
                exit()
            elif checkitem('tools') != True or checkitem('glass pane') != True:
                print("\nThere isnt much to do here since your machinese broken, you're going to need both some tools and a glass pane to repair your machine")
                time.sleep(2)
                poss_loc = ['the dusty road']
                place_pick()
        elif curr_loc == 'gold rush town':
            if checkitem('water bottle') != True:
                print("\nAs you begin to walk towards Gold Rush Town, you think about how far you are going to walk. You stop for a moment and consider the blazing sun and the dust blowing in your face.")
                print("\nYou might not have enough water to survive the walk and you dont want to die alone out in the desert in a year you dont even know. It'd probably be safer to at least get some water first")
                print("\nYou decide to head back to the dusty road")
                curr_loc = 'the dusty road'
                place_pick()
            if checkitem('water bottle') == True:
                print("\nYou begin to walk towards Gold Rush Town and 10 miles in you thank the heavens that you remembered your water.\nWho knows what the blistering sun would have done do you without it.")
                time.sleep(4)
                gold_rush_town()
        elif curr_loc == 'the workshop':
            workshop()
        elif curr_loc == 'the saloon':
            broke()
            saloon()
        elif curr_loc == 'deadwood town':
            deadwood()
        elif curr_loc == 'the shady dudes':
            shadydudes()
        elif curr_loc == 'the bar':
            bar()

    #Gold rush town
    def gold_rush_town():
        global poss_loc
        global town_first_time
        print("\nYou've arrived at Gold Rush Town and you look around at a nice little town filled with people going about their every day lives.")
        if town_first_time:
            print("\nYou ask someone for the year and although they look at you like you're crazy, they politely answer that its currently June 17th of 1873.")
            town_first_time = False
        print("\nYou see a few places you want to check out as you refill your water at a water trough nearby.")
        poss_loc = ['the dusty road', 'the workshop', 'the saloon']
        place_pick()

    def workshop():
        global poss_actions
        print("\nYou walk about a mile out to a workshop that you saw on a sign in town and you see someone working at an outside forge. When you walk up to him, he looks up and asks you how your days been.")
        poss_actions = ["Ask to buy tools", "Ask to buy Glass", "leave"]
        action_pick()

    def saloon():
        global poss_actions
        print("\nYou walk into the saloon and see people playing cards. This might make you some money. Do you want to play?")
        poss_actions = ['play', 'leave']
        action_pick()

    def blackjack():
        global poss_actions
        global chose
        print("\nYou sit down to play blackjack and are dealt 2 cards")
        deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        hand = []
        dealer = []
        def draw(person, wdeck):
            d = random.choice(deck)
            print("\n" + person + " drew a " + str(d))
            wdeck.append(d)
            time.sleep(0.5)
        draw('You',hand) 
        draw('You',hand) 
        draw('The dealer',dealer)
        draw('The dealer',dealer)
        def printhand(person, wdeck):
            if person == "You":
                sentence = person + " have " + str(sum(hand))
            if person == "The dealer":
                sentence = person + " has " + str(sum(dealer))
            print("\n" + sentence)
            time.sleep(0.5)
        printhand('You', hand)
        printhand('The dealer', dealer)
        
        chose = ""
        def act():
            global chose
            action = [
                inquirer.List('action',
                    message="What do you want to do?",
                    choices=["hit",'stand'])]
            action = inquirer.prompt(action)
            chose = action['action']
            if action['action'] == 'hit':
                draw('You',hand)
                printhand('You', hand)
                dealeract()
                printhand('The dealer', dealer)
                logic()
            if action['action'] == 'stand':
                print("\n You stand")
                printhand("You",hand)
                dealeract()
                logic()
        def dealeract():
            if sum(dealer) < 17:
                draw('The dealer',dealer)
                printhand('The dealer', dealer)
            else:
                pass
        def lose():
            global poss_actions
            print("\nUnlucky, you lost, you lose 5 dollars")
            changemoney(-5)
            poss_actions = ['play', 'leave']
            broke()
            action_pick()
        def win():
            global poss_actions
            print("\nLucky, you win, you got 5 dollars")
            changemoney(5)
            poss_actions = ['play', 'leave']
            action_pick()
        def tie():
            global poss_actions
            print("\nYou tied, nothing really happens")
            poss_actions = ['play', 'leave']
            action_pick()
        def logic():
            global poss_actions
            global chose
            if chose == 'stand' and sum(hand) == sum(dealer):
                tie()
            if sum(hand) > 21 and sum(dealer) > 21:
                tie()
            elif sum(hand) > 21:
                lose()
            elif sum(dealer) > 21:
                win()
            elif chose == 'stand' and sum(dealer) < 17:
                while sum(dealer) < 17:
                    dealeract()
            elif chose == 'stand' and sum(hand) > sum(dealer):
                win()
            elif chose == 'stand' and sum(hand) < sum(dealer):
                lose()
            else:
                act()
        logic()    

    #Deadwood Town
    def deadwood():
        global fought
        global poss_loc
        global town_first_time
        print("\nYou're now in Deadwood Town and you look around at a dim, shady looking broken down town with a few men walking around suspiciously.")
        if town_first_time:
            print("\nYou try to ask for the year but no one seems to care whatsoever. A kid runs past hearing you and tells you it is 1873 along with calling you an idiot.")
            town_first_time = False
        print("\nYou see a few places you might want to go")
        if fought == False:
            poss_loc = ['the dusty road', 'the bar', 'the shady dudes']
        else: 
            poss_loc == ['the dusty road', 'the bar']
        place_pick()

    def shadydudes():
        global poss_actions
        time.sleep(0.5)
        print("\nYou walk up to the shady dudes.")
        time.sleep(0.5)
        print("\nTerrible idea to be honest.")
        time.sleep(0.5)
        print("\nAs you walk up they stop their conversation and eye you suspiciously.")
        print("\nTwo other dudes walk up behind you and you now seem to be surrounded.")
        poss_actions = ['fight', 'run']
        action_pick()

    def bar():
        global poss_actions
        print("\nYou walk into the bar. You see some people playing cards and the bartender serving drinks.")
        poss_actions = ['ask for water', 'play blackjack']
        action_pick()

    def badblackjack():
        global poss_actions
        global chose
        print("\nYou sit down to play blackjack and are dealt 2 cards")
        deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        hand = []
        dealer = []
        def draw(person, wdeck):
            d = random.choice(deck)
            print("\n" + person + " drew a " + str(d))
            wdeck.append(d)
            time.sleep(0.5)
        draw('You',hand) 
        draw('You',hand) 
        draw('The dealer',dealer)
        draw('The dealer',dealer)
        def printhand(person, wdeck):
            if person == "You":
                sentence = person + " have " + str(sum(hand))
            if person == "The dealer":
                sentence = person + " has " + str(sum(dealer))
            print("\n" + sentence)
            time.sleep(0.5)
        printhand('You', hand)
        printhand('The dealer', dealer)
        
        chose = ""
        def act():
            global chose
            action = [
                inquirer.List('action',
                    message="What do you want to do?",
                    choices=["hit",'stand'])]
            action = inquirer.prompt(action)
            chose = action['action']
            if action['action'] == 'hit':
                draw('You',hand)
                printhand('You', hand)
                dealeract()
                printhand('The dealer', dealer)
                logic()
            if action['action'] == 'stand':
                print("\n You stand")
                printhand("You",hand)
                dealeract()
                logic()
        def dealeract():
            if sum(dealer) < 17:
                draw('The dealer',dealer)
                printhand('The dealer', dealer)
            else:
                pass
        def lose():
            global poss_actions
            print("\nUnlucky, you lost, you lose 8 dollars")
            changemoney(-8)
            poss_actions = ['play blackjack', 'back to the bar']
            broke()
            action_pick()
        def win():
            global poss_actions
            print("\nLucky, you win, you got 3 dollars")
            changemoney(3)
            poss_actions = ['play blackjack', 'back to the bar']
            action_pick()
        def tie():
            global poss_actions
            print("\nYou tied, nothing really happens")
            poss_actions = ['play blackjack', 'back to the bar']
            action_pick()
        def logic():
            global poss_actions
            global chose
            if chose == 'stand' and sum(hand) == sum(dealer):
                tie()
            if sum(hand) > 21 and sum(dealer) > 21:
                tie()
            elif sum(hand) > 21:
                lose()
            elif sum(dealer) > 21:
                win()
            elif chose == 'stand' and sum(dealer) < 17:
                while sum(dealer) < 17:
                    dealeract()
            elif chose == 'stand' and sum(hand) > sum(dealer):
                win()
            elif chose == 'stand' and sum(hand) < sum(dealer):
                lose()
            else:
                act()
        logic()    
    




    print("\nAs you walk out of the time machine, you are instantly hit by a wave of heat, dust and sun making it hard for you to see.")
    print("\nYou've landed in some deserty area, nothing around you but a path that leads off into the distance. It seems like you've landed yourself in the Old West")
    #time.sleep(3)
    print("\nLooking back into the time machine, you find the battery dead. Knowing it'll take a while to recharge, you know you'll need a way to survive for a while.")
    print("\nYou do see some items in the machine, that may help you on your journey. You think to yourself and decide you can only take 4 things with you for this jourey.\n")
    #time.sleep(3)


    #Picking first item
    def item_print(list):
        if list['items'] == 'Gun':
            bullets = random.randrange(2,10)
            inventory.append({'name': 'gun', 'bullets' : bullets})
            return('\nYou take your trusty Glock 43, and find the clip still has ' + str(bullets) + ' bullets left')
        if list['items'] == 'Money':
            money = random.randrange(5,20)
            inventory.append({'name': 'money', 'money' : money})
            return('\nYou find ' + str(money) + ' dollars')
        if list['items'] == 'Water':
            inventory.append({'name': 'water bottle'})
            return('\nYour water bottle is completely full')
        if list['items'] == 'Tools':
            inventory.append({'name': 'tools'})
            return('\nThese tools that might be useful to fix something')
        if list['items'] == 'Lucky hat':
            inventory.append({'name': 'hat'})
            return('\nYour trusty Lucky hat has never failed you before')
        if list['items'] == 'Tobacco':
            inventory.append({'name': 'tobacco'})
            return('\nYou find a container with some tobacco, you wonder why you have something like this')
        if list['items'] == 'Knife':
            inventory.append({'name': 'knife'})
            return('\nA knife would help for sure')

    def choice_1():
        item = [
            inquirer.List('items',
                        message="Take your first item:",
                        choices=items)
        ]
        item = inquirer.prompt(item)

        items.remove(item['items'])

        print(item_print(item))
    choice_1()
    time.sleep(2)

    def choice2():
        item = [
            inquirer.List('items',
                        message="Take your next item:",
                        choices=items)
        ]
        item = inquirer.prompt(item)

        items.remove(item['items'])

        print(item_print(item))
    choice2()
    time.sleep(2)

    def choice_3():
        item = [
            inquirer.List('items',
                        message="Take your last item:",
                        choices=items)
        ]
        item = inquirer.prompt(item)

        items.remove(item['items'])

        print(item_print(item))
    choice_3()
    time.sleep(2)

    if checkitem("money") == False:
        inventory.append({'name': 'money', 'money' : 0})
    #changemoney(-10000)


    print("\nSuddenly, you see a herd of bison charging towards your time machine. It seems as if the sound from your machine irritated them.")
    print("\nYou are able to run a safe distance away but you can't do anything as you watch your machine get trampled. \n")
    time.sleep(3)
    print("\nYou head back to check out the damage. Somehow the battery is completely intact and charging but the body got severely dented and the window was shattered.")
    if checkitem('tools') == True:
        print("\nLuckily, you brought your tools so it shouldn't be too hard to repair, but you're still going to need to find a piece of glass for the window if you want to leave.")
    else:
        print("\nUnfortunately, your tools were broken by the bison and you didn't take them beforehand so you're going to need to find some tools to fix the body and some glass for the window\n")

    time.sleep(1)
    place_pick()
    time.sleep(2)

    print("\nAs you walk down the dusty road, you see a sign in the distance")
    print("\nThe sign has two arrows, one says |GOLD RUSH TOWN 20 MI| and the other says |DEADWOOD TOWN 2 MI|")
    poss_loc.append('gold rush town')
    poss_loc.append('deadwood town')

    place_pick()
TravelToPast()