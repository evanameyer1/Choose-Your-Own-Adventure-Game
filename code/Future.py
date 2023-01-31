import os
import sys
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer

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
        print("Luckily, it looks like you grabbed the leadership manifesto!")
        tech_work_up_ranks = [
            inquirer.List('ranks',
                        message="Do you: ",
                        choices=['Stay at HQ as a leader and attempt to work up the ranks', 'Head into battle as a soldier',])
        ]
        workupranksanswer = inquirer.prompt(tech_work_up_ranks)
    else:
        print("\nYou arrive back at the technology headquarters. It's massive. Robots, cyborgs, and the humans that are allied with them, all coexisting in peace. It's clear you picked the winning side.")
        print("When you finally walk into the building, and approach the front desk, they give you your assignment - work up the ranks as a leader or fight on the front lines.")
        print("But, it looks like you left the leadership manifesto in the time machine, so you're forced to head into battle as a soldier.")

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
            print("Your friend is able to escape, but because you used your medkit on them, you are killed. GAME OVER")
        elif answersavefriend['friend'] == 'Attempt to save your friend' and (first_item['items'] != 'Medkit' or second_item['items'] != 'Medkit'):
            print("You rush over to your friend, reach for your bag, but realize you forgot your medkit in the time machine. Because you tried to save them, the enemy soldiers are closer, and you get hit by a stray bullet.")
            print("You are killed. GAME OVER")
        else: 
            print("You turn away from their cries, and run away. You know you can't go back ever again, as you will be labeled as a deserter and tried for treason.")
            return_to_time_machine = [
            inquirer.List('time_machine',
                        message="Unsure of where to go next, you have two options: ",
                        choices=['Live off grid', 'Attempt to make your way back to the time machine'])
            ]
            answertimemachine = inquirer.prompt(return_to_time_machine)

            if answertimemachine['time_machine'] == 'Live off grid' and (first_item['items'] == 'Food supplies' or second_item['items'] == 'Food supplies'):
                print("You move to")
                   
elif faction['faction'] == 'Humans' and (first_item['items'] == 'Gun' or second_item['items'] == 'Gun'):
    print("You have selected to join the humans. You run over to the their baracks, and pretend like you belong. After hiding in the bathroom for what feels like hours, the shooting stops.")
    print("When the fighting silences you apprehensively leave your hiding spot, only to run into a revolution commander. He has no clue who you are and demands you prove your allegience.\n")
    print("They bring a technology-prisoner in front of you and demand you execute him for the cause. Luckily, you realize you grabbed your gun from the time machine.")
    human_official_join = [
        inquirer.List('technology1',
                    message="You have three options. Do you: ",
                    choices=['Shoot the prisoner', 'Run away and leave the cause', 'Deny that you will participate in a wrongful execution'])
    ]
    humans1answer = inquirer.prompt(human_official_join)
else:
    print("You have selected to join the humans. You run over to the their baracks, and pretend like you belong. After hiding in the bathroom for what feels like hours, the shooting stops.")
    print("When the fighting silences you apprehensively leave your hiding spot, only to run into a revolution commander. He has no clue who you are and demands you prove your allegience.\n")
    print("They bring a technology-prisoner in front of you and demand you execute him for the cause. However, you realize you forgot your gun in the time machine.")
    human_official_join = [
        inquirer.List('technology1',
                    message="You're left with two options. Do you: ",
                    choices=['Run away and leave the cause', 'Deny that you will participate in a wrongful execution'])
    ]
    humans1answer = inquirer.prompt(human_official_join)