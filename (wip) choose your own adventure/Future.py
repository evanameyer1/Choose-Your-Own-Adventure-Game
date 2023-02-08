import os
import sys
import time
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer

import tkinter as tk
from tkinter import ttk

def print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
        
def future_end():
        game_end = [
            inquirer.List('gameend',
                        message="Select from the options below:",
                        choices=['Restart the game from the beginning', 'Restart the game to when the time machine was built', 'Restart your current timeline'])
        ]
        gameendanswer = inquirer.prompt(game_end)

        if gameendanswer == 'Restart the game from the beginning':
            game()
        elif gameendanswer == 'Restart the game to when the time machine was built':
            time_machine()
        else:
            travel_to_future()

def travel_to_future():

    print("\nYou step out the time machine and look around. The year is 3079.")
    print(" The beautifully futuristic buildings and vehicles you were expecting are nowhere to be found.\n")
    print("Instead, explosions, gunfire, and chaos are all that you see, as you watch two sides, humans and technology, completely destroy each other before your eyes.\n")

    print("\nYou turn around and look back into the machine.")
    print(" The time machine's battery is dead, and it'll take some time to get back up - for now you have to venture out.")
    print(" Fortunately there are 6 objects in the machine, all of which could be pivotal to your survival, but you can only grab two.\n")

    first_item = [
        inquirer.List('items',
                    message="Make your first selection:",
                    choices=['Leadership Manifesto', 'Gun', 'Medkit', 'Food supplies', 'Gas mask', 'Toolkit'])
    ]
    first_item = inquirer.prompt(first_item)

    if first_item['items'] == 'Leadership Manifesto':
        second_item = [
            inquirer.List('items',
                        message="Make your second selection:",
                        choices=['Gun', 'Medkit', 'Food supplies', 'Gas mask', 'Toolkit'])
        ]
        second_item = inquirer.prompt(second_item)

    elif first_item['items'] == 'Gun':
        second_item = [
            inquirer.List('items',
                        message="Make your second selection:",
                        choices=['Leadership Manifesto', 'Medkit', 'Food supplies', 'Gas mask', 'Toolkit'])
        ]
        second_item = inquirer.prompt(second_item)
    
    elif first_item['items'] == 'Medkit':
        second_item = [
            inquirer.List('items',
                        message="Make your second selection:",
                        choices=['Leadership Manifesto', 'Gun', 'Food supplies', 'Gas mask', 'Toolkit'])
        ]
        second_item = inquirer.prompt(second_item)

    elif first_item['items'] == 'Food supplies':
        second_item = [
            inquirer.List('items',
                        message="Make your second selection:",
                        choices=['Leadership Manifesto', 'Gun', 'Medkit', 'Gas mask', 'Toolkit'])
        ]
        second_item = inquirer.prompt(second_item)

    elif first_item['items'] == 'Gas mask':
        second_item = [
            inquirer.List('items',
                        message="Make your second selection:",
                        choices=['Leadership Manifesto', 'Gun', 'Medkit', 'Food Supplies', 'Toolkit'])
        ]
        second_item = inquirer.prompt(second_item)

    else:
        second_item = [
            inquirer.List('items',
                        message="Make your second selection:",
                        choices=['Leadership Manifesto', 'Gun', 'Medkit', 'Food Supplies', 'Gas mask'])
        ]
        second_item = inquirer.prompt(second_item)

    print(f"\nYou grab the {first_item['items'].lower()} and {second_item['items'].lower()} and decide to head out.".format())
    print(" As soon as you leave your ship, you run into two groups of people.")
    print("\nThe two groups, technology and humans, stand across from each other, weapons in hand.")
    print(" You can tell that battle is about to ensue.")
    print(" Desperate to survive the upcoming destruction, you have to pick a side.\n")

    pick_a_side = [
        inquirer.List('faction',
                    message="Who's side do you pick: ",
                    choices=['Technology', 'Humans'])
    ]
    faction = inquirer.prompt(pick_a_side)

    if faction['faction'] == 'Technology':

        print(" You have selected to join technology.")
        print("You run over to the technology baracks, and pretend like you belong. ")
        print("After hiding in the bathroom for what feels like hours, the shooting stops. ")
        print("Someone you can only assume as your commander calls out to your unit that the battle is over and everyone is returning to HQ. That includes you.\n")
        tech_official_join = [
            inquirer.List('technology1',
                        message="Do you return to their headquarters: ",
                        choices=['Return to headquarters as one of their own', 'Sneak away when no one is looking'])
        ]
        technology1answer = inquirer.prompt(tech_official_join)

        if technology1answer['technology1'] == 'Return to headquarters as one of their own' and (first_item['items'] == 'Leadership Manifesto' or second_item['items'] == 'Leadership Manifesto'):
            print("\nYou arrive back at the technology headquarters. It's massive. Robots, cyborgs, and the humans that are allied with them, all coexisting in peace. It's clear you picked the winning side.")
            print(" When you finally walk into the building, and approach the front desk, they give you your assignment - work up the ranks as a leader or fight on the front lines.")
            print(" Luckily, it looks like you grabbed the leadership manifesto!\n")
            tech_work_up_ranks = [
                inquirer.List('ranks',
                            message="Do you: ",
                            choices=['Stay at HQ as a leader and attempt to work up the ranks', 'Head into battle as a soldier',])
            ]
            workupranksanswer = inquirer.prompt(tech_work_up_ranks)

            if workupranksanswer['ranks'] == 'Stay at HQ as a leader and attempt to work up the ranks':
                print(" You stay decide to stay at HQ, and apply what you learned from the Leadership Manifesto to work your way up the officer ranks. ")
                print("After many years of late nights and hard work, you do it - you are now leading technology's army.\n")
                print(" War is still brewing, as unrest between technology and humans doesn't seem to quench. Your first role as leader is to define how you intend to lead.\n")
                tech_leadership = [
                inquirer.List('tech_lead',
                            message="Will you: ",
                            choices=['Pursue peace with the human organizations and push for co-existing harmony', 'Continue to destroy the remaining human populations, until all that is left is the technological world'])
                ]
                answertechleadership = inquirer.prompt(tech_leadership)

                if answertechleadership['tech_lead'] == 'Pursue peace with the human organizations and push for co-existing harmony':             
                    print(" You inform the humans that you are willing to compromise, and plan to divide the states into two territories, where each organization will live. ")
                    print("Their numbers have been decreasing increasingly with each year, so they accept.")
                    print(" All they want is help moving their people out, and some financial help with the starting of their new country. ")
                    print("How much financial aid do you give them:\n")
                    
                    # root window
                    root = tk.Tk()
                    root.geometry('300x200')
                    root.resizable(False, False)
                    root.title('Financial Aid')


                    root.columnconfigure(0, weight=1)
                    root.columnconfigure(1, weight=3)


                    # slider current value
                    current_value = tk.DoubleVar()


                    def get_current_value():
                        return '{: .2f}'.format(current_value.get())


                    def slider_changed(event):
                        value_label.configure(text=get_current_value())


                    # label for the slider
                    slider_label = ttk.Label(
                        root,
                        text='Slider:'
                    )

                    slider_label.grid(
                        column=0,
                        row=0,
                        sticky='w'
                    )

                    #  slider
                    slider = ttk.Scale(
                        root,
                        from_=1,
                        to=10,
                        orient='horizontal',  # vertical
                        command=slider_changed,
                        variable=current_value
                    )

                    slider.grid(
                        column=1,
                        row=0,
                        sticky='we'
                    )

                    # current value label
                    current_value_label = ttk.Label(
                        root,
                        text='In Billions($):'
                    )

                    current_value_label.grid(
                        row=1,
                        columnspan=2,
                        sticky='n',
                        ipadx=10,
                        ipady=10
                    )

                    # value label
                    value_label = ttk.Label(
                        root,
                        text=get_current_value()
                    )
                    value_label.grid(
                        row=2,
                        columnspan=2,
                        sticky='n'
                    )

                    root.mainloop()

                    if float(get_current_value()) > 7:
                        print(f"Your amount of ${get_current_value()} billion was way too much - your own people were disappointed in you and saw you as a weak leader, and ultimately you were assassinated. GAME OVER\n")
                        future_end()
                    elif float(get_current_value()) < 4:    
                        print(f"Your amount of ${get_current_value()} billion wasn't nearly enough, and the humans felt mocked and played. They mustered up an assassination on you. GAME OVER\n")
                        future_end()
                    else:
                        print(f"Your amount of ${get_current_value()} billion was the perfect amount, and were able to find harmony between the technology and human sides. Now, you must decide if you want to live out your days here, or return to the time machine.\n")
                        return_to_time_machine = [
                        inquirer.List('time_machine',
                                message="Do you: ",
                                choices=['Live off your days as a successful ruler', 'Attempt to make your way back to the time machine'])
                        ]
                        answertimemachine = inquirer.prompt(return_to_time_machine)

                        if answertimemachine['time_machine'] == 'Live off your days as a successful ruler' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                            print(" You retire, and live off your days as the future's most successful leader. ")
                            print("You ended a war that almost saw the end of the human race.")
                            print(" Ultimately, you live happily ever after. GAME OVER\n")
                            future_end()
                        elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
                            print(" You start making your way back to where you left the time machine all the years before. ")
                            print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                            print(" You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n")
                            future_end() 
                        else: 
                            print(" You start making your way back to where you left the time machine all the years before. ")
                            print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.")
                            print(" Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n")
                            future_end()  

                elif answertechleadership['tech_lead'] == 'Continue to destroy the remaining human populations, until all that is left is the technological world' and (first_item['items'] == 'Gas mask' or second_item['items'] == 'Gas mask'):
                    print("You have decided to continue the destruction, and behind your leadership, in just a couple years almost all of the population is wiped out. ")
                    print("Those that remain result to nuclear methods, sacrificing their world to stop you.")
                    print(" The bombs strike when you are out, and you find yourself with just minutes of time to react. ")
                    print("Luckily, you grabbed the gas mask from the time machine, and you survive. ")
                    print("There isn't much of anything after the bombs, and you return home on the time machine. GAME OVER \n")
                    future_end()
                else: 
                    print("You have decided to continue the destruction, and behind your leadership, in just a couple years almost all of the population is wiped out. ")
                    print("Those that remain result to nuclear methods, sacrificing their world to stop you.")
                    print(" The bombs strike when you are out, and you find yourself with just minutes of time to react. ")
                    print("Unfortunately, you lack the tools to survive the bombs, and you are killed alongside your empire. GAME OVER \n")
                    future_end()

            else:
                print("After months of training, and bonding with friends, you're finally battle ready. ")
                print("As you and your platoon head deep into enemy lines, and you sing battle songs and make fun of each other, you feel a sense of community. ")
                print("\nUnfortunatly, that feeling doesn't last long. Your world flips on it's head as your truck drives over a mine. ")
                print("When you come to, you can hear the echoes of thousands of human soliders coming. ")
                print("As you make your way out of the flipped truck, you crawl past the dead bodies of your friends. ")
                print("You're about to leave, when you hear someone call your name. ")
                print("You turn and it's your best friend, and they're hurt.\n")
                save_friend = [
                inquirer.List('friend',
                                message="However, you know that the human soliders will be there soon. Do you: ",
                                choices=['Attempt to save your friend', 'Run away to save yourself, and effectively leave the cause'])
                ]
                answersavefriend = inquirer.prompt(save_friend)

                if answersavefriend['friend'] == 'Attempt to save your friend' and (first_item['items'] == 'Medkit' or second_item['items'] == 'Medkit'):
                        print("You rush over to your friend, pull out your medkit, and quickly get them patched up. ")
                        print("However, as you're helping them you get hit by a stray bullet from the incoming soliders.")
                        print( "Your friend is able to escape, but because you used your medkit on them, you are killed. GAME OVER\n")
                        future_end()
                elif answersavefriend['friend'] == 'Attempt to save your friend' and (first_item['items'] != 'Medkit' or second_item['items'] != 'Medkit'):
                        print("You rush over to your friend, reach for your bag, but realize you forgot your medkit in the time machine. ")
                        print("Because you tried to save them, the enemy soldiers are closer, and you get hit by a stray bullet. ")
                        print("You are killed. GAME OVER\n")
                        future_end()
                else: 
                        print("You turn away from their cries, and run away. ")
                        print("You know you can't go back ever again, as you will be labeled as a deserter and tried for treason.\n")
                        return_to_time_machine = [
                        inquirer.List('time_machine',
                                    message="Unsure of where to go next, you have two options: ",
                                    choices=['Live off grid', 'Attempt to make your way back to the time machine'])
                        ]
                        answertimemachine = inquirer.prompt(return_to_time_machine)

                        if answertimemachine['time_machine'] == 'Live off grid' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                            print("After a couple miles of running, you find a nice spot to camp for the night. ")
                            print("You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine. ")
                            print("Inside, you find seeds and the materials needed to start a full off-grid farm. ")
                            print(" Ultimately, you live happily ever after. GAME OVER\n")
                            future_end()
                        elif answertimemachine['time_machine'] == 'Live off grid' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
                            print(f"After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
                            print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n") 
                            future_end()
                        elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
                            print("You start making your way back to where you left the time machine all the years before. ")
                            print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n") 
                            print(" You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n")
                            future_end() 
                        else: 
                            print("You start making your way back to where you left the time machine all the years before. ")
                            print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
                            print(" Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n")
                            future_end()     

        elif technology1answer['technology1'] == 'Return to headquarters as one of their own' and (first_item['items'] != 'Leadership Manifesto' or second_item['items'] != 'Leadership Manifesto'):
            print("\nYou arrive back at the technology headquarters. It's massive. Robots, cyborgs, and the humans that are allied with them, all coexisting in peace. It's clear you picked the winning side.")
            print("When you finally walk into the building, and approach the front desk, they give you your assignment - work up the ranks as a leader or fight on the front lines.")
            print("But, it looks like you left the leadership manifesto in the time machine, so you're forced to head into battle as a soldier.\n")

            print("After months of training, and bonding with friends, you're finally battle ready. ")
            print("As you and your platoon head deep into enemy lines, and you sing battle songs and make fun of each other, you feel a sense of community.")
            print("\nUnfortunatly, that feeling doesn't last long. Your world flips on it's head as your truck drives over a mine. When you come to, you can hear the echoes of thousands of human soliders coming.")
            print("As you make your way out of the flipped truck, you crawl past the dead bodies of your friends. ")
            print("You're about to leave, when you hear someone call your name. ")
            print("You turn and it's your best friend, and they're hurt.\n")
            save_friend = [
                inquirer.List('friend',
                            message="However, you know that the human soliders will be there soon. Do you: ",
                            choices=['Attempt to save your friend', 'Run away to save yourself, and effectively leave the cause'])
            ]
            answersavefriend = inquirer.prompt(save_friend)

            if answersavefriend['friend'] == 'Attempt to save your friend' and (first_item['items'] == 'Medkit' or second_item['items'] == 'Medkit'):
                print("You rush over to your friend, pull out your medkit, and quickly get them patched up. ")
                print("However, as you're helping them you get hit by a stray bullet from the incoming soliders.")
                print("Your friend is able to escape, but because you used your medkit on them, you are killed. GAME OVER\n")
                future_end()
            elif answersavefriend['friend'] == 'Attempt to save your friend' and (first_item['items'] != 'Medkit' or second_item['items'] != 'Medkit'):
                print("You rush over to your friend, reach for your bag, but realize you forgot your medkit in the time machine. ")
                print("Because you tried to save them, the enemy soldiers are closer, and you get hit by a stray bullet.")
                print("You are killed. GAME OVER\n")
                future_end()
            else: 
                print("You turn away from their cries, and run away. ")
                print("You know you can't go back ever again, as you will be labeled as a deserter and tried for treason.\n")
                return_to_time_machine = [
                inquirer.List('time_machine',
                            message="Unsure of where to go next, you have two options: ",
                            choices=['Live off grid', 'Attempt to make your way back to the time machine'])
                ]
                answertimemachine = inquirer.prompt(return_to_time_machine)

                if answertimemachine['time_machine'] == 'Live off grid' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                    print("After a couple miles of running, you find a nice spot to camp for the night. ")
                    print("You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine.")
                    print("Inside, you find seeds and the materials needed to start a full off-grid farm. ")
                    print("Ultimately, you live happily ever after. GAME OVER\n")
                    future_end()
                elif answertimemachine['time_machine'] == 'Live off grid' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
                    print(f"After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
                    print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n")
                    future_end() 
                elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
                    print("You start making your way back to where you left the time machine all the years before. ")
                    print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                    print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n")
                    future_end() 
                else: 
                    print("You start making your way back to where you left the time machine all the years before. ")
                    print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
                    print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n")
                    future_end()      

        else: 
            print("You have deserted the technology's cause. You know you can't go back ever again, as you will be labeled as a deserter and tried for treason. ")
            print("After a little bit of running you find some small encampments, and after talking with them, you learn that they are the peaceful neutral people.\n")
            return_to_time_machine = [
            inquirer.List('time_machine',
                        message="Unsure of where to go next, you have two options: ",
                        choices=['Live with the neutral people', 'Live off-grid by yourself', 'Attempt to make your way back to the time machine'])
                ]
            answertimemachine = inquirer.prompt(return_to_time_machine)

            if answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                print("After a couple miles of running, you find a nice spot to camp for the night. ")
                print("You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine.")
                print("Inside, you find seeds and the materials needed to start a full off-grid farm. ")
                print("Ultimately, you live happily ever after. GAME OVER\n")
                future_end()
            elif answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
                print(f"After a couple miles of running, you find a nice spot to camp for the night. ")
                print("You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
                print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n")
                future_end()  
            elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] == 'Gas mask' or second_item['items'] == 'Gas mask'):
                print("You stay with the neutral people, and live with them well for a couple years. ")
                print("They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. ")
                print("Luckily, you grabbed the gas mask from the time machine, and you survive. There isn't much of anything after the bombs, and you return home on the time machine. GAME OVER \n")
                future_end()
            elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] != 'Gas mask' or second_item['items'] != 'Gas mask'):
                print("You stay with the neutral people, and live with them well for a couple years. ")
                print("They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. ")
                print("The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. ")
                print("Unfortunately, you lack the tools to survive the bombs, and you are killed. GAME OVER \n")
                future_end()
            elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
                print("You start making your way back to where you left the time machine all the years before. ")
                print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n") 
                future_end()
            else: 
                print("You start making your way back to where you left the time machine all the years before. ")
                print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
                print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n") 
                future_end()   

    elif faction['faction'] == 'Humans' and (first_item['items'] == 'Gun' or second_item['items'] == 'Gun'):
        print(" You have selected to join the humans. You run over to the their baracks, and pretend like you belong. ")
        print("After hiding in the bathroom for what feels like hours, the shooting stops.")
        print(" When the fighting silences you apprehensively leave your hiding spot, only to run into a revolution commander. ")
        print("He has no clue who you are and demands you prove your allegience.\n")
        print("They bring a technology-prisoner in front of you and demand you execute him for the cause. ")
        print("Luckily, you realize you grabbed your gun from the time machine.\n")
        human_official_join = [
            inquirer.List('technology1',
                        message="You have three options. Do you: ",
                        choices=['Shoot the prisoner', 'Run away and leave the cause', 'Deny that you will participate in a wrongful execution'])
        ]
        humans1answer = inquirer.prompt(human_official_join)

        if humans1answer['technology1'] == 'Shoot the prisoner' and (first_item['items'] == 'Leadership Manifesto' or second_item['items'] == 'Leadership Manifesto'):
            print("You execute the prisoner. The human restoralists are statisfied, and, as the battle has ended, offer to show you back to their base.")
            print("You return with them, and are amazed. They have developed a society without technology, understanding that otherwise their enemy could manipulate it against them.")
            print("Upon entering their complex, you are shown around to the different branches of their military. They bring you to a reporting desk, and ask you for your ideal assignment.")
            print("However, you aren't sure what you should do - this decision deciedes whether or not you will be officially joining their cause.")
            human_assignment = [
                inquirer.List('milassignment',
                            message="You have three options. Do you: ",
                            choices=['Work your way up the ranks as an officer', 'Fight on the front lines as a solider', 'Look for an opening to escape and flee'])
            ]
            humanassignmentanswer = inquirer.prompt(human_assignment) 

            if humanassignmentanswer['milassignment'] == 'Look for an opening to escape and flee':
                print("While the soldiers aren't looking you run away and, although narrowly, escape. ")
                print("After running for a couple of miles, and building some distance between you and the army, you have to make a decision on where to go next.")
                print("You remember hearing talks of the neutral people, that live fully remote and avoid the conflicts and suffering of the war. ")
                print("But, you aren't sure if you would enjoy that lifestyle.")
                return_to_time_machine = [
                inquirer.List('time_machine',
                            message="Unsure of where to go next, you have two options: ",
                            choices=['Live with the neutral people', 'Live off-grid by yourself', 'Attempt to make your way back to the time machine'])
                    ]
                answertimemachine = inquirer.prompt(return_to_time_machine)

                if answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                    print("After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine.")
                    print("Inside, you find seeds and the materials needed to start a full off-grid farm. Ultimately, you live happily ever after. GAME OVER\n")
                    future_end()
                elif answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
                    print(f"After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
                    print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n")
                    future_end()  
                elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] == 'Gas mask' or second_item['items'] == 'Gas mask'):
                    print("You stay with the neutral people, and live with them well for a couple years. ")
                    print("They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                    print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. ")
                    print("The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                    print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. Luckily, you grabbed the gas mask from the time machine, and you survive. ")
                    print("There isn't much of anything after the bombs, and you return home on the time machine. GAME OVER \n")
                    future_end()
                elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] != 'Gas mask' or second_item['items'] != 'Gas mask'):
                    print("You stay with the neutral people, and live with them well for a couple years. They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                    print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                    print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. Unfortunately, you lack the tools to survive the bombs, and you are killed. GAME OVER \n")
                    future_end()
                elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
                    print("You start making your way back to where you left the time machine all the years before. When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                    print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n") 
                    future_end()
                else: 
                    print("You start making your way back to where you left the time machine all the years before. ")
                    print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
                    print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n") 
                    future_end()    

            elif humanassignmentanswer['milassignment'] == 'Fight on the front lines as a solider':
                print("You have elected to serve on the front lines as a solider. You begin training immediately, and prep for your first upcoming battle.")
                print("\n Weeks past, and your first battle is around the corner. ")
                print("As your team rides into battle, you notice some enemies on the flank - if they were to get through it would be absolutely devestating for your army.")
                print("However, you aren't sure if you alone can stop them, and you know you won't be able to get information to your commander in time.")
                human_battle = [
                inquirer.List('battleassignment',
                            message="Do you: ",
                            choices=['Ignore the threat and continue with the original plan', 'Go toward the situation and attempt to stop them yourself'])
                ]
                humanbattleanswer = inquirer.prompt(human_battle) 

                if humanbattleanswer['battleassignment'] == "Ignore the threat and continue with the original plan":
                    print("You decide to ignore the situation and carry out with the original plan. ")
                    print("However, that decision would prove to be fatal, as the enemy destroys your entire backline, and you find yourself surrounded.")
                    print("Almost as if fate, you find yourself the last one from your squad alive. ")
                    print("There are enemies on all sides, closing in with each passing moment. Ultimately, you do not surive the assualt. GAME OVER \n")
                    future_end()
                
                elif humanbattleanswer['battleassignment'] == "Go toward the situation and attempt to stop them yourself":
                    print("You leave your post, and go directly toward the flanking enemy. You are able to successfully defeat the threat, and save the integrity of your squad.")
                    print("You are branded a war-hero, and find yoursel returning to a promotion. ")
                    print("After a few months that pass, and the convient deaths of the officers above you, you find yourself as the commander of the entire human army.")
                    print("\nThe enemy is still winning the war, and it's now up to you and your decisions to stop it. ")
                    print("You are tasked with determining your military objective, and how you will keep the enemy at bay.")
                    war_direction = [
                    inquirer.List('war',
                            message="Do you: ",
                            choices=['Storm DC and attempt to take back the capital', 'Move toward the coast and attempt to control the ports', 'Screw the plan, and lead your army straight through the heart of the enemy'])
                    ]
                    wardirectionanswer = inquirer.prompt(war_direction)    

                    if wardirectionanswer['war'] == 'Screw the plan, and lead your army straight through the heart of the enemy':
                        print("You make the call to assemble the army together as one, and move straight at the enemy. ")
                        print("You give a blood-boiling speech, motivating your armies, and for a moment there's hope.")
                        print("That hope will be short-lived, as your inability to effectively plan a strategic attack left your losses immeasurable. ")
                        print("Ultimately, you fell alongside your own army. GAME OVER")
                        future_end()
                    
                    elif wardirectionanswer['war'] == 'Move toward the coast and attempt to control the ports':
                        print("You gather the troops and attack the coastal cities. You succeed, and before long, you control the coasts of the US. ")
                        print("While the enemy still controls more land and has more troops, you weed out their resouces and, with time, you become strong enough to challenge them.")
                        print("\n This also means that the enemy is willing to respond to dipolmatic efforts. ")
                        print("You find your population divided, with half pushing for peace and half pushing for war. You have to decide how the army will proceed.")
                        diplomacy = [
                        inquirer.List('dip',
                            message="Will you use the opportunity to: ",
                            choices=['fight and attempt to destroy the enemy once and for all', 'push for a diplomatic conclusion to the war'])
                        ]
                        diplomacyanswer = inquirer.prompt(diplomacy)    

                        if diplomacyanswer['dip'] == 'fight and attempt to destroy the enemy once and for all':
                            print("You rally the troops and move forward yet again with one final strike at the enemy. ")
                            print("You have weeded them out of valuable resources over time, and they are now weaker than ever before.")
                            print("However, yet again you have underestimated your enemy. Even weaker, the human army still stands no match to technology, and your assualt fails. GAME OVER")
                            future_end()
                        else: 
                            print("You take advantage of the weakened enemy, and you push for diplomacy. ")
                            print("The enemy reluctantly accepts and after years and years of destruction, peace is finally accomplished. GAME OVER")
                            future_end()
                    else:
                        print("You gather your army and make plans to move toward the capital. ")
                        print("Although the fight is tough, by focusing all of your manpower on the specific area, you are able to succeed.")
                        print("Now, as ruler of the army, you have yet another decision - where to go next.")
                        outsideus = [
                        inquirer.List('us',
                            message="Will you: ",
                            choices=['stay within the states and continue to rule the army', 'look outward, and attempt to further your power by invading other countries'])
                        ]
                        outsideusanswer = inquirer.prompt(outsideus)    

                        if outsideusanswer['us'] == 'stay within the states and continue to rule the army':
                            print("You decide to let go of the gas and rule comfortably for the remainder of your life. ")
                            print("However, your subjects sense weakness in their previously battle-hardened leader")
                            print("Before long whispers turn to riots, and soon you find yourself with a rebellion. They are disappointed you didn't continue to push further around the world. ")
                            print("Ultimately, an assassination attempt succeeds, and you fell at the hands of those you swore to protect. GAME OVER")
                            future_end()
                        
                        else:
                            print("You let your generals know you have no plans of stopping anytime soon, and you want a report done on external territories. ")
                            print("They return with four possible avenues, and each of their respective strengths and weaknesses.")
                            globalterritories = [
                            inquirer.List('global',
                                message="Which do you pick: ",
                                choices=['Africa is technologically inferior to your army, but the land is unfamilar and disease-ridden.', "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.", 
                                "South America is the closest and technologically inferior, but they are run by the cartels.", "Asia has by far the most centralized government with the largest army, but there are already talks of rebellion that could be leveraged against them. "])
                            ]
                            globalterritoriesanswer = inquirer.prompt(globalterritories)  

                            if globalterritoriesanswer['global'] == 'Africa is technologically inferior to your army, but the land is unfamilar and disease-ridden.':
                                print("You pick Africa as your first target and, after years of planning and training, get ready for the global attack. ")
                                print("You strike at the bottom of the continent and move up throughout the various countries.")
                                print("Ultimately, your technologically superior army overpowers theirs and, although you take heavy losses due to the overseas traveling, you succeed.")
                                expanding2 = [
                                inquirer.List('expand',
                                    message="What is your next move? ",
                                    choices=["Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.", "South America is the closest and technologically inferior, but they are run by the cartels.", 
                                    "Asia has by far the most centralized government with the largest army, but there are already talks of rebellion that could be leveraged against them. "])
                                ]
                                expanding2sanswer = inquirer.prompt(expanding2)  

                                if expanding2sanswer['expand'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                    print("Confident after your previous excursion, you decide to take on the European territories next. ")
                                    print("However, due to your already heavy losses, and the tough terrain, you and your army didn't come close. GAME OVER")
                                    future_end()
                                
                                elif expanding2sanswer['expand'] == "Asia has by far the most centralized government with the largest army, but there are already talks of rebellion that could be leveraged against them. ":
                                    print("Confident after your previous excursion, you decide to take on the Asian territories next. ")
                                    print("However, due to your already heavy losses, and the sheer size of the Asian armies, you and your army didn't come close. GAME OVER")
                                    future_end()

                                else: 
                                    print("Confident after your previous excursion, you decide to take on the South American territories next. ")
                                    print("Although you previously experienced heavy losses, due to their technological inferiority and close proximity, this war was significantly easier.")
                                    expanding3 = [
                                    inquirer.List('expand',
                                        message="What is your next move? ",
                                        choices=["Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.", "Asia has by far the most centralized government with the largest army, but there are already talks of rebellion that could be leveraged against them. "])
                                    ]
                                    expanding3sanswer = inquirer.prompt(expanding3)  

                                    if expanding2sanswer['expand'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                        print("Confident after your previous excursion, you decide to take on the European territories next. ")
                                        print("However, due to your already heavy losses, and the tough terrain, you and your army didn't come close. GAME OVER")
                                        future_end()
                                    
                                    else:
                                        print("Confident after your previous excursion, you decide to take on the Asian territories next. ")
                                        print("However, due to your already heavy losses, and the sheer size of the Asian armies, you and your army didn't come close. GAME OVER")
                                        future_end()

                            elif globalterritoriesanswer['global'] == 'South America is the closest and technologically inferior, but they are run by the cartels.':
                                print("You pick South America as your first target and, after years of planning and training, get ready for the global attack. ")
                                print("You strike at the bottom of the continent and move up throughout the various countries.")
                                print(" Ultimately, your technologically superior army overpowers theirs and, although you take heavy losses due to the overseas traveling, you succeed.")
                                expanding2 = [
                                inquirer.List('expand',
                                    message="What is your next move? ",
                                    choices=["Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.", "Africa is technologically inferior to your army, but the land is unfamilar and disease-ridden.", 
                                    "Asia has by far the most centralized government with the largest army, but there are already talks of rebellion that could be leveraged against them. "])
                                ]
                                expanding2sanswer = inquirer.prompt(expanding2)  

                                if expanding2sanswer['expand'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                    print("Confident after your previous excursion, you decide to take on the European territories next. ")
                                    print("However, due to your already heavy losses, and the tough terrain, you and your army didn't come close. GAME OVER")
                                    future_end()
                                
                                elif expanding2sanswer['expand'] == "Asia has by far the most centralized government with the largest army, but there are already talks of rebellion that could be leveraged against them. ":
                                    print("Confident after your previous excursion, you decide to take on the Asian territories next. ")
                                    print("However, due to your already heavy losses, and the sheer size of the Asian armies, you and your army didn't come close. GAME OVER")
                                    future_end()

                                else: 
                                    print("Confident after your previous excursion, you decide to take on the African territories next. ")
                                    print("Although you previously experienced heavy losses, due to their technological inferiority, this war was significantly easier.")
                                    expanding3 = [
                                    inquirer.List('expand',
                                        message="What is your next move? ",
                                        choices=["Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.", "Asia has by far the most centralized government with the largest army, but there are already talks of rebellion that could be leveraged against them. "])
                                    ]
                                    expanding3sanswer = inquirer.prompt(expanding3)  

                                    if expanding2sanswer['expand'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                        print("Confident after your previous excursion, you decide to take on the European territories next. ")
                                        print("However, due to your already heavy losses, and the tough terrain, you and your army didn't come close. GAME OVER")
                                        future_end()
                                    
                                    else:
                                        print("Confident after your previous excursion, you decide to take on the Asian territories next. ")
                                        print("However, due to your already heavy losses, and the sheer size of the Asian armies, you and your army didn't come close. GAME OVER")
                                        future_end()


                            elif globalterritoriesanswer['global'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                print("Confident in your army, you decide to take on the European territories next. ")
                                print("However, due to their technological superiority, and the tough terrain, you and your army didn't come close. GAME OVER")
                                future_end()

                            else:
                                print("You decide to take on Asia. Understanding that their sheer size, and inability to keep everyone satisfied, is their biggest weakness, you use spies to strike from within.")
                                print("After years of spy work and assassinations, Asia becomes weak enough for you to attack. ")
                                print("While they're focused on internal affairs you strike with your armies full might, and destroy their torn army.")
                                print(" Now, with the largest army on your side, where do you attack next?")
                                expanding2 = [
                                inquirer.List('expand',
                                    message="What is your next move? ",
                                    choices=["Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.", "Africa is technologically inferior to your army, but the land is unfamilar and disease-ridden.", 
                                    "South America is the closest and technologically inferior, but they are run by the cartels."])
                                ]
                                expanding2sanswer = inquirer.prompt(expanding2)  

                                if expanding2sanswer['expand'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                    print("Confident after your previous excursion, you decide to take on the European territories next. ")
                                    print("However, due to your already heavy losses, and the tough terrain, you and your army didn't come close. GAME OVER")
                                    future_end()
                                
                                elif expanding2sanswer['expand'] == "Africa is technologically inferior to your army, but the land is unfamilar and disease-ridden.":
                                    print("Confident after your previous excursion, you decide to take on the African territories next. ")
                                    print("Although you previously experienced heavy losses, due to their technological inferiority, this war was significantly easier.")
                                    expanding3 = [
                                    inquirer.List('expand',
                                        message="What is your next move? ",
                                        choices=["Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.", "South America is the closest and technologically inferior, but they are run by the cartels."])
                                    ]
                                    expanding3sanswer = inquirer.prompt(expanding3)  

                                    if expanding2sanswer['expand'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                        print("Confident after your previous excursion, you decide to take on the European territories next. ")
                                        print("However, due to your already heavy losses, and the tough terrain, you and your army didn't come close. GAME OVER")
                                        future_end()
                                    
                                    else:
                                        print("Confident after your previous excursion, you decide to take on the South American territories next. ")
                                        print("Although you previously experienced heavy losses, due to their technological inferiority and close proximity, this war was significantly easier.")

                                        expanding4 = [
                                        inquirer.List('expand',
                                            message="What is your next move? ",
                                            choices=["Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards."])
                                        ]
                                        expanding4sanswer = inquirer.prompt(expanding4) 

                                        if expanding4sanswer['expand'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                            print("Finally, you look to conquer Europe, the only remaining territory. ")
                                            print("Although their armies are larger and technology superior, with sheer numbers you attack from all sides and are able to defeat them.")
                                            print("You are history's first ruler of the entire world - congratulations, you just made history. GAME OVER")
                                            future_end()

                                else: 
                                    print("Confident after your previous excursion, you decide to take on the South American territories next. ")
                                    print("Although you previously experienced heavy losses, due to their technological inferiority and close proximity, this war was significantly easier.")
                                    expanding3 = [
                                    inquirer.List('expand',
                                        message="What is your next move? ",
                                        choices=["Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.", "Africa is technologically inferior to your army, but the land is unfamilar and disease-ridden."])
                                    ]
                                    expanding3sanswer = inquirer.prompt(expanding3)  

                                    if expanding2sanswer['expand'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                        print("Confident after your previous excursion, you decide to take on the European territories next. ")
                                        print("However, due to your already heavy losses, and the tough terrain, you and your army didn't come close. GAME OVER")
                                        future_end()
                                    
                                    else:
                                        print("Confident after your previous excursion, you decide to take on the African territories next. ")
                                        print("Although you previously experienced heavy losses, due to their technological inferiority, this war was significantly easier.")

                                        expanding4 = [
                                        inquirer.List('expand',
                                            message="What is your next move? ",
                                            choices=["Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards."])
                                        ]
                                        expanding4sanswer = inquirer.prompt(expanding4) 

                                        if expanding4sanswer['expand'] == "Europe's armies are tougher with a lot more allies, but as the biggest challenge they offer the highest rewards.":
                                            print("Finally, you look to conquer Europe, the only remaining territory. Although their armies are larger and technology superior, with sheer numbers you attack from all sides and are able to defeat them.")
                                            print("You are history's first ruler of the entire world - congratulations, you just made history. GAME OVER")
                                            future_end()

            else: 
                print("You stay decide to stay and apply what you learned from the Leadership Manifesto to work your way up the officer ranks. ")
                print("After many years of late nights and hard work, you do it - you are now leading the human rebellion's army.\n")
                print("Following the teachings of the Leadership Manifesto, you push for peace with the technological organizations. ")
                print("After years of negotiations you finally achieve peace - a world where robots and humans can now co-exist.\n")
                tech_leadership = [
                inquirer.List('tech_lead',
                            message="What is your next move? ",
                            choices=['Retire as a successful leader and attempt to go back to the time machine', 'Stay on as leader and continue to rule the states'])
                ]
                answertechleadership = inquirer.prompt(tech_leadership)

                if answertechleadership['tech_lead'] == 'Retire as a successful leader and attempt to go back to the time machine':
                    print("You start making your way back to where you left the time machine all the years before. ")
                    print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                    print(" You have to work quickly to fix the machine, but luckily you are able to make it out and return home. GAME OVER\n")
                    future_end() 
                
                else: 
                    print("You decide to stay on as the leader.")
                    usleadership = [
                    inquirer.List('usleader',
                                message="What kind of government are you interested in leading?",
                                choices=['Dictatorship', 'Communist', 'Socialist', 'Democracy'])
                    ]
                    usleadershipanswer = inquirer.prompt(usleadership)

                    if usleadershipanswer['usleader'] == 'Dictatorship':
                        print("You take the government by your hands and lead as a dictator. You rule ruthlessly, destroying anyone and anything that stands in your way. ")
                        print("Before long, your enemies outnumber your allies, and you get assassinated. GAME OVER")
                        future_end()              
                    elif usleadershipanswer['usleader'] == 'Communist':
                        print("You lead the country as a communist leader. ")
                        print("You attempt to fix the mistakes of the previous communist leaders that failed, but your attempts ultimately fall short and the country falls into ruins. GAME OVER")
                        future_end()
                    elif usleadershipanswer['usleader'] == 'Socialist':
                        print("You decide to lead the country as a socialist power. With the work of other global nations, and the newfound technological insights of the 3000s, you are able to cure world hunger and solve environment challenges. Yay! GAME OVER")
                        future_end()
                    else:
                        print("You restore the democratic power that was ruling when you were in power. ")
                        print("Prosperity returns to the country, and everybody live happily ever after. GAME OVER")
                        future_end()

        elif humans1answer['technology1'] == 'Shoot the prisoner' and (first_item['items'] != 'Leadership Manifesto' or second_item['items'] != 'Leadership Manifesto'):
            print("You execute the prisoner. The human restoralists are statisfied, and, as the battle has ended, offer to show you back to their base.")
            print("You return with them, and are amazed. They have developed a society without technology, understanding that otherwise their enemy could manipulate it against them.")
            print("Upon entering their complex, you are shown around to the different branches of their military. ")
            print("They bring you to a reporting desk, and ask you for your ideal assignment.")
            print("However, you aren't sure what you should do - this decision deciedes whether or not you will be officially joining their cause.")
            human_assignment = [
                inquirer.List('milassignment',
                            message="You have two options. Do you: ",
                            choices=['Fight on the front lines as a solider', 'Look for an opening to escape and flee'])
            ]
            humanassignmentanswer = inquirer.prompt(human_assignment)    

            if humanassignmentanswer['milassignment'] == 'Look for an opening to escape and flee':
                print("While the soldiers aren't looking you run away and, although narrowly, escape. ")
                print("After running for a couple of miles, and building some distance between you and the army, you have to make a decision on where to go next.")
                print("You remember hearing talks of the neutral people, that live fully remote and avoid the conflicts and suffering of the war. ")
                print("But, you aren't sure if you would enjoy that lifestyle.")
                return_to_time_machine = [
                inquirer.List('time_machine',
                            message="Unsure of where to go next, you have two options: ",
                            choices=['Live with the neutral people', 'Live off-grid by yourself', 'Attempt to make your way back to the time machine'])
                    ]
                answertimemachine = inquirer.prompt(return_to_time_machine)

                if answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                    print("After a couple miles of running, you find a nice spot to camp for the night. ")
                    print("You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine.")
                    print("Inside, you find seeds and the materials needed to start a full off-grid farm. ")
                    print("Ultimately, you live happily ever after. GAME OVER\n")
                    future_end()
                elif answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
                    print(f"After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
                    print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n")  
                    future_end()
                elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] == 'Gas mask' or second_item['items'] == 'Gas mask'):
                    print("You stay with the neutral people, and live with them well for a couple years. ")
                    print("They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                    print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. ")
                    print("The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                    print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. ")
                    print("Luckily, you grabbed the gas mask from the time machine, and you survive. ")
                    print("There isn't much of anything after the bombs, and you return home on the time machine. GAME OVER \n")
                    future_end()
                elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] != 'Gas mask' or second_item['items'] != 'Gas mask'):
                    print("You stay with the neutral people, and live with them well for a couple years. ")
                    print("They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                    print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. ")
                    print("The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                    print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. ")
                    print("Unfortunately, you lack the tools to survive the bombs, and you are killed. GAME OVER \n")
                    future_end()
                elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
                    print("You start making your way back to where you left the time machine all the years before. ")
                    print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                    print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n") 
                    future_end()
                else: 
                    print("You start making your way back to where you left the time machine all the years before. ")
                    print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
                    print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n") 
                    future_end()
        
        elif humans1answer['technology1'] == 'Run away and leave the cause':
            print("While the soldiers aren't looking you run away and, although narrowly, escape. ")
            print("After running for a couple of miles, and building some distance between you and the army, you have to make a decision on where to go next.")
            print("You remember hearing talks of the neutral people, that live fully remote and avoid the conflicts and suffering of the war. ")
            print("But, you aren't sure if you would enjoy that lifestyle.")
            return_to_time_machine = [
            inquirer.List('time_machine',
                        message="Unsure of where to go next, you have two options: ",
                        choices=['Live with the neutral people', 'Live off-grid by yourself', 'Attempt to make your way back to the time machine'])
                ]
            answertimemachine = inquirer.prompt(return_to_time_machine)

            if answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                print("After a couple miles of running, you find a nice spot to camp for the night. ")
                print("You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine.")
                print("Inside, you find seeds and the materials needed to start a full off-grid farm. ")
                print("Ultimately, you live happily ever after. GAME OVER\n")
                future_end()
            elif answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
                print(f"After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
                print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n")  
                future_end()
            elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] == 'Gas mask' or second_item['items'] == 'Gas mask'):
                print("You stay with the neutral people, and live with them well for a couple years. ")
                print("They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. ")
                print("The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. Luckily, you grabbed the gas mask from the time machine, and you survive. There isn't much of anything after the bombs, and you return home on the time machine. GAME OVER \n")
                future_end()
            elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] != 'Gas mask' or second_item['items'] != 'Gas mask'):
                print("You stay with the neutral people, and live with them well for a couple years. ")
                print("They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. ")
                print("The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. ")
                print("Unfortunately, you lack the tools to survive the bombs, and you are killed. GAME OVER \n")
                future_end()
            elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
                print("You start making your way back to where you left the time machine all the years before. ")
                print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n") 
                future_end()
            else: 
                print("You start making your way back to where you left the time machine all the years before. ")
                print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
                print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n")   
                future_end() 
        
        else:
            print("You valiantly let them know that you will not participate in an unjust execution - especially of a solider that is unarmed and surrending.")
            print("Unfortunately, valiance gets you nothing, and you are executed as an example for the others that are considering desertion. GAME OVER")
            future_end()

    else:
        print("You have selected to join the humans. You run over to the their baracks, and pretend like you belong. ")
        print("After hiding in the bathroom for what feels like hours, the shooting stops.")
        print("When the fighting silences you apprehensively leave your hiding spot, only to run into a revolution commander. ")
        print("He has no clue who you are and demands you prove your allegience.\n")
        print("They bring a technology-prisoner in front of you and demand you execute him for the cause. ")
        print("However, you realize you forgot your gun in the time machine.\n")
        human_official_join = [
            inquirer.List('technology1',
                        message="You're left with two options. Do you: ",
                        choices=['Run away and leave the cause', 'Deny that you will participate in a wrongful execution'])
        ]
        humans1answer = inquirer.prompt(human_official_join)

        if humans1answer['technology1'] == 'Run away and leave the cause':
            print("While the soldiers aren't looking you run away and, although narrowly, escape. ")
            print("After running for a couple of miles, and building some distance between you and the army, you have to make a decision on where to go next.")
            print("You remember hearing talks of the neutral people, that live fully remote and avoid the conflicts and suffering of the war. ")
            print("But, you aren't sure if you would enjoy that lifestyle.")
            return_to_time_machine = [
            inquirer.List('time_machine',
                        message="Unsure of where to go next, you have two options: ",
                        choices=['Live with the neutral people', 'Live off-grid by yourself', 'Attempt to make your way back to the time machine'])
                ]
            answertimemachine = inquirer.prompt(return_to_time_machine)

            if answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                print("After a couple miles of running, you find a nice spot to camp for the night. ")
                print("You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine.")
                print("Inside, you find seeds and the materials needed to start a full off-grid farm. ")
                print("Ultimately, you live happily ever after. GAME OVER\n")
                future_end()
            elif answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
                print(f"After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
                print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n") 
                future_end() 
            elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] == 'Gas mask' or second_item['items'] == 'Gas mask'):
                print("You stay with the neutral people, and live with them well for a couple years. ")
                print("hey teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. ")
                print("The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. ")
                print("Luckily, you grabbed the gas mask from the time machine, and you survive. ")
                print("There isn't much of anything after the bombs, and you return home on the time machine. GAME OVER \n")
                future_end()
            elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] != 'Gas mask' or second_item['items'] != 'Gas mask'):
                print("You stay with the neutral people, and live with them well for a couple years. ")
                print("They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
                print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. ")
                print("The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
                print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. ")
                print("Unfortunately, you lack the tools to survive the bombs, and you are killed. GAME OVER \n")
                future_end()
            elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
                print("You start making your way back to where you left the time machine all the years before. ")
                print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n") 
                future_end()
            else: 
                print("You start making your way back to where you left the time machine all the years before. ")
                print("When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
                print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n") 
                future_end()   
        
        else:
            print("You valiantly let them know that you will not participate in an unjust execution - especially of a solider that is unarmed and surrending.")
            print("Unfortunately, valiance gets you nothing, and you are executed as an example for the others that are considering desertion. GAME OVER")
            future_end()
    
travel_to_future()