import os
import sys
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer

import tkinter as tk
from tkinter import ttk

print("\nYou step out the time machine and look around. The year is 3079. The beautifully futuristic buildings and vehicles you were expecting are nowhere to be found.")
print("Instead, explosions, gunfire, and chaos are all that you see, as you watch two sides, humans and technology, completely destroy each other before your eyes.")

print("\nYou turn around and look back into the machine. The time machine's battery is dead, and it'll take some time to get back up - for now you have to venture out.")
print("Fortunately there are 6 objects in the machine, all of which could be pivotal to your survival, but you can only grab two.\n")

first_item = [
    inquirer.List('items',
                  message="Make your first selection:",
                  choices=['Leadership Manifesto', 'Gun', 'Medkit', 'Food supplies', 'Gas mask', 'Toolkit'])
]
first_item = inquirer.prompt(first_item)

second_item = [
    inquirer.List('items',
                  message="Make your second selection:",
                  choices=['Leadership Manifesto', 'Gun', 'Medkit', 'Food supplies', 'Gas mask', 'Toolkit'])
]
second_item = inquirer.prompt(second_item)

print(f"\nYou grab the {first_item['items']} and {second_item['items']} and decide to head out. As soon as you leave your ship, you run into two groups of people.")
print("\nThe two groups, technology and humans, stand across from each other, weapons in hand. You can tell that battle is about to ensue.")
print("Desperate to survive the upcoming destruction, you have to pick a side.\n")

pick_a_side = [
    inquirer.List('faction',
                  message="Who's side do you pick: ",
                  choices=['Technology', 'Humans'])
]
faction = inquirer.prompt(pick_a_side)

if faction['faction'] == 'Technology':

    print("You have selected to join technology. You run over to the technology baracks, and pretend like you belong. After hiding in the bathroom for what feels like hours, the shooting stops.")
    print("Someone you can only assume as your commander calls out to your unit that the battle is over and everyone is returning to HQ. That includes you.\n")
    tech_official_join = [
        inquirer.List('technology1',
                    message="Do you return to their headquarters: ",
                    choices=['Return to headquarters as one of their own', 'Sneak away when no one is looking'])
    ]
    technology1answer = inquirer.prompt(tech_official_join)

    if technology1answer['technology1'] == 'Return to headquarters as one of their own' and (first_item['items'] == 'Leadership Manifesto' or second_item['items'] == 'Leadership Manifesto'):
        print("\nYou arrive back at the technology headquarters. It's massive. Robots, cyborgs, and the humans that are allied with them, all coexisting in peace. It's clear you picked the winning side.")
        print("When you finally walk into the building, and approach the front desk, they give you your assignment - work up the ranks as a leader or fight on the front lines.")
        print("Luckily, it looks like you grabbed the leadership manifesto!\n")
        tech_work_up_ranks = [
            inquirer.List('ranks',
                        message="Do you: ",
                        choices=['Stay at HQ as a leader and attempt to work up the ranks', 'Head into battle as a soldier',])
        ]
        workupranksanswer = inquirer.prompt(tech_work_up_ranks)

        if workupranksanswer['ranks'] == 'Stay at HQ as a leader and attempt to work up the ranks':
            print("You stay decide to stay at HQ, and apply what you learned from the Leadership Manifesto to work your way up the officer ranks. After many years of late nights and hard work, you do it - you are now leading technology's army.\n")
            print("War is still brewing, as unrest between technology and humans doesn't seem to quench. Your first role as leader is to define how you intend to lead.\n")
            tech_leadership = [
            inquirer.List('tech_lead',
                        message="Will you: ",
                        choices=['Pursue peace with the human organizations and push for co-existing harmony', 'Continue to destroy the remaining human populations, until all that is left is the technological world'])
            ]
            answertechleadership = inquirer.prompt(tech_leadership)

            if answertechleadership['tech_lead'] == 'Pursue peace with the human organizations and push for co-existing harmony':             
                print("You inform the humans that you are willing to compromise, and plan to divide the states into two territories, where each organization will live. Their numbers have been decreasing increasingly with each year, so they accept.")
                print("All they want is help moving their people out, and some financial help with the starting of their new country. How much financial aid do you give them:\n")
                
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
                elif float(get_current_value()) < 4:    
                    print(f"Your amount of ${get_current_value()} billion wasn't nearly enough, and the humans felt mocked and played. They mustered up an assassination on you. GAME OVER\n")
                else:
                    print(f"Your amount of ${get_current_value()} billion was the perfect amount, and were able to find harmony between the technology and human sides. Now, you must decide if you want to live out your days here, or return to the time machine.\n")
                    return_to_time_machine = [
                    inquirer.List('time_machine',
                            message="Do you: ",
                            choices=['Live off your days as a successful ruler', 'Attempt to make your way back to the time machine'])
                    ]
                    answertimemachine = inquirer.prompt(return_to_time_machine)

                    if answertimemachine['time_machine'] == 'Live off your days as a successful ruler' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                        print("You retire, and live off your days as the future's most successful leader. You ended a war that almost saw the end of the human race.")
                        print("Ultimately, you live happily ever after. GAME OVER\n")
                    elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] != 'Toolkit' or second_item['items'] != 'Toolkit'):
                        print("You start making your way back to where you left the time machine all the years before. When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                        print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n") 
                    else: 
                        print("You start making your way back to where you left the time machine all the years before. When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.")
                        print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n")  

            elif answertechleadership['tech_lead'] == 'Continue to destroy the remaining human populations, until all that is left is the technological world' and (first_item['items'] == 'Gas mask' or second_item['items'] == 'Gas mask'):
                print("You have decided to continue the destruction, and behind your leadership, in just a couple years almost all of the population is wiped out. Those that remain result to nuclear methods, sacrificing their world to stop you.")
                print("The bombs strike when you are out, and you find yourself with just minutes of time to react. Luckily, you grabbed the gas mask from the time machine, and you survive. There isn't much of anything after the bombs, and you return home on the time machine. GAME OVER \n")
            else: 
                print("You have decided to continue the destruction, and behind your leadership, in just a couple years almost all of the population is wiped out. Those that remain result to nuclear methods, sacrificing their world to stop you.")
                print("The bombs strike when you are out, and you find yourself with just minutes of time to react. Unfortunately, you lack the tools to survive the bombs, and you are killed alongside your empire. GAME OVER \n")

        else:
           print("After months of training, and bonding with friends, you're finally battle ready. As you and your platoon head deep into enemy lines, and you sing battle songs and make fun of each other, you feel a sense of community.")
           print("\nUnfortunatly, that feeling doesn't last long. Your world flips on it's head as your truck drives over a mine. When you come to, you can hear the echoes of thousands of human soliders coming.")
           print("As you make your way out of the flipped truck, you crawl past the dead bodies of your friends. You're about to leave, when you hear someone call your name. You turn and it's your best friend, and they're hurt.\n")
           save_friend = [
           inquirer.List('friend',
                        message="However, you know that the human soliders will be there soon. Do you: ",
                        choices=['Attempt to save your friend', 'Run away to save yourself, and effectively leave the cause'])
           ]
           answersavefriend = inquirer.prompt(save_friend)

           if answersavefriend['friend'] == 'Attempt to save your friend' and (first_item['items'] == 'Medkit' or second_item['items'] == 'Medkit'):
                print("You rush over to your friend, pull out your medkit, and quickly get them patched up. However, as you're helping them you get hit by a stray bullet from the incoming soliders.")
                print("Your friend is able to escape, but because you used your medkit on them, you are killed. GAME OVER\n")
           elif answersavefriend['friend'] == 'Attempt to save your friend' and (first_item['items'] != 'Medkit' or second_item['items'] != 'Medkit'):
                print("You rush over to your friend, reach for your bag, but realize you forgot your medkit in the time machine. Because you tried to save them, the enemy soldiers are closer, and you get hit by a stray bullet.")
                print("You are killed. GAME OVER\n")
           else: 
                print("You turn away from their cries, and run away. You know you can't go back ever again, as you will be labeled as a deserter and tried for treason.\n")
                return_to_time_machine = [
                inquirer.List('time_machine',
                            message="Unsure of where to go next, you have two options: ",
                            choices=['Live off grid', 'Attempt to make your way back to the time machine'])
                ]
                answertimemachine = inquirer.prompt(return_to_time_machine)

                if answertimemachine['time_machine'] == 'Live off grid' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                    print("After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine.")
                    print("Inside, you find seeds and the materials needed to start a full off-grid farm. Ultimately, you live happily ever after. GAME OVER\n")
                elif answertimemachine['time_machine'] == 'Live off grid' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
                    print(f"After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
                    print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n") 
                elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] != 'Toolkit' or second_item['items'] != 'Toolkit'):
                    print("You start making your way back to where you left the time machine all the years before. When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n") 
                    print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n") 
                else: 
                    print("You start making your way back to where you left the time machine all the years before. When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
                    print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n")     

    elif technology1answer['technology1'] == 'Return to headquarters as one of their own' and (first_item['items'] != 'Leadership Manifesto' or second_item['items'] != 'Leadership Manifesto'):
        print("\nYou arrive back at the technology headquarters. It's massive. Robots, cyborgs, and the humans that are allied with them, all coexisting in peace. It's clear you picked the winning side.")
        print("When you finally walk into the building, and approach the front desk, they give you your assignment - work up the ranks as a leader or fight on the front lines.")
        print("But, it looks like you left the leadership manifesto in the time machine, so you're forced to head into battle as a soldier.\n")

        print("After months of training, and bonding with friends, you're finally battle ready. As you and your platoon head deep into enemy lines, and you sing battle songs and make fun of each other, you feel a sense of community.")
        print("\nUnfortunatly, that feeling doesn't last long. Your world flips on it's head as your truck drives over a mine. When you come to, you can hear the echoes of thousands of human soliders coming.")
        print("As you make your way out of the flipped truck, you crawl past the dead bodies of your friends. You're about to leave, when you hear someone call your name. You turn and it's your best friend, and they're hurt.\n")
        save_friend = [
            inquirer.List('friend',
                        message="However, you know that the human soliders will be there soon. Do you: ",
                        choices=['Attempt to save your friend', 'Run away to save yourself, and effectively leave the cause'])
        ]
        answersavefriend = inquirer.prompt(save_friend)

        if answersavefriend['friend'] == 'Attempt to save your friend' and (first_item['items'] == 'Medkit' or second_item['items'] == 'Medkit'):
            print("You rush over to your friend, pull out your medkit, and quickly get them patched up. However, as you're helping them you get hit by a stray bullet from the incoming soliders.")
            print("Your friend is able to escape, but because you used your medkit on them, you are killed. GAME OVER\n")
        elif answersavefriend['friend'] == 'Attempt to save your friend' and (first_item['items'] != 'Medkit' or second_item['items'] != 'Medkit'):
            print("You rush over to your friend, reach for your bag, but realize you forgot your medkit in the time machine. Because you tried to save them, the enemy soldiers are closer, and you get hit by a stray bullet.")
            print("You are killed. GAME OVER\n")
        else: 
            print("You turn away from their cries, and run away. You know you can't go back ever again, as you will be labeled as a deserter and tried for treason.\n")
            return_to_time_machine = [
            inquirer.List('time_machine',
                        message="Unsure of where to go next, you have two options: ",
                        choices=['Live off grid', 'Attempt to make your way back to the time machine'])
            ]
            answertimemachine = inquirer.prompt(return_to_time_machine)

            if answertimemachine['time_machine'] == 'Live off grid' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                print("After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine.")
                print("Inside, you find seeds and the materials needed to start a full off-grid farm. Ultimately, you live happily ever after. GAME OVER\n")
            elif answertimemachine['time_machine'] == 'Live off grid' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
                print(f"After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
                print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n") 
            elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
                print("You start making your way back to where you left the time machine all the years before. When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
                print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n") 
            else: 
                print("You start making your way back to where you left the time machine all the years before. When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
                print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n")      

    else: 
        print("You have deserted the technology's cause. You know you can't go back ever again, as you will be labeled as a deserter and tried for treason. After a little bit of running you find some small encampments, and after talking with them, you learn that they are the peaceful neutral people.\n")
        return_to_time_machine = [
        inquirer.List('time_machine',
                    message="Unsure of where to go next, you have two options: ",
                    choices=['Live with the neutral people', 'Live off-grid by yourself', 'Attempt to make your way back to the time machine'])
            ]
        answertimemachine = inquirer.prompt(return_to_time_machine)

        if answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
            print("After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, and luckily, you find the food supplies you grabbed from the time machine.")
            print("Inside, you find seeds and the materials needed to start a full off-grid farm. Ultimately, you live happily ever after. GAME OVER\n")
        elif answertimemachine['time_machine'] == 'Live off-grid by yourself' and (first_item['items'] != 'Food supplies' or second_item['items'] != 'Food supplies'):
            print(f"After a couple miles of running, you find a nice spot to camp for the night. You check your backpack for things that you might need, but unfortunately all you find are the {first_item['items']} and {second_item['items']}.") 
            print("You are unable to substain yourself, without the necessary food supplies to set up a food source, and before long you perish. GAME OVER\n")  
        elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] == 'Gas mask' or second_item['items'] == 'Gas mask'):
            print("You stay with the neutral people, and live with them well for a couple years. They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
            print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
            print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. Luckily, you grabbed the gas mask from the time machine, and you survive. There isn't much of anything after the bombs, and you return home on the time machine. GAME OVER \n")
        elif answertimemachine['time_machine'] == 'Live with the neutral people' and (first_item['items'] != 'Gas mask' or second_item['items'] != 'Gas mask'):
            print("You stay with the neutral people, and live with them well for a couple years. They teach you to farm and live off of the land, and you see a level of piece and contentment you aren't used to.")
            print("\n However, the war continued to get worse and worse, until the technological forces had humans on their last legs. The final humans set nuclear bombs, sacrificing themselves to stop the technology.")
            print("\n The bombs strike when you are out, and you find yourself with just minutes of time to react. Unfortunately, you lack the tools to survive the bombs, and you are killed. GAME OVER \n")
        elif answertimemachine['time_machine'] == 'Attempt to make your way back to the time machine' and (first_item['items'] == 'Toolkit' or second_item['items'] == 'Toolkit'):
            print("You start making your way back to where you left the time machine all the years before. When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.") 
            print("You have to work quickly to fix the machine, but luckily you grabbed the toolkit from the time machine, and you are able to make it out and return home. GAME OVER\n") 
        else: 
            print("You start making your way back to where you left the time machine all the years before. When you arrive, you find the machine slightly overgrown, and surrounded by empty tents and campfires, implying people are living out of it.\n")
            print("Unfortunately, you lack the tools or resources to quickly fix the machine in time, and before long you here the inhabitants return - they don't listen to your attempt to explain that the machine is yours, fights break out, and, outnumbered, you perish. GAME OVER\n")    

elif faction['faction'] == 'Humans' and (first_item['items'] == 'Gun' or second_item['items'] == 'Gun'):
    print("You have selected to join the humans. You run over to the their baracks, and pretend like you belong. After hiding in the bathroom for what feels like hours, the shooting stops.")
    print("When the fighting silences you apprehensively leave your hiding spot, only to run into a revolution commander. He has no clue who you are and demands you prove your allegience.\n")
    print("They bring a technology-prisoner in front of you and demand you execute him for the cause. Luckily, you realize you grabbed your gun from the time machine.\n")
    human_official_join = [
        inquirer.List('technology1',
                    message="You have three options. Do you: ",
                    choices=['Shoot the prisoner', 'Run away and leave the cause', 'Deny that you will participate in a wrongful execution'])
    ]
    humans1answer = inquirer.prompt(human_official_join)
else:
    print("You have selected to join the humans. You run over to the their baracks, and pretend like you belong. After hiding in the bathroom for what feels like hours, the shooting stops.")
    print("When the fighting silences you apprehensively leave your hiding spot, only to run into a revolution commander. He has no clue who you are and demands you prove your allegience.\n")
    print("They bring a technology-prisoner in front of you and demand you execute him for the cause. However, you realize you forgot your gun in the time machine.\n")
    human_official_join = [
        inquirer.List('technology1',
                    message="You're left with two options. Do you: ",
                    choices=['Run away and leave the cause', 'Deny that you will participate in a wrongful execution'])
    ]
    humans1answer = inquirer.prompt(human_official_join)