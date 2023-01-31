import os
import sys
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer

print("You step out the time machine and look around. The year is 3079. The beautifully futuristic buildings and vehicles you were expecting are nowhere to be found.")
print("Instead, explosions, gunfire, and chaos are all that you see, as you watch two sides, humans and technology, completely destroy each other before your eyes.")

print("You turn around and look back into the machine. The time machine's battery is dead, and it'll take some time to get back up - for now you have to venture out.")
print("Fortunately there are 6 objects in the machine, all of which could be pivotal to your survival, but you can only grab two.")

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

print(f"You grab the {first_item} and {second_item} and decide to head out. As soon as you leave your ship, you run into two groups of people.")
print("The two groups, technology and humans, stand across from each other, weapons in hand. You can tell that battle is about to ensue.")
print("Desperate to survive the upcoming destruction, you have to pick a side.")

pick_a_side = [
    print('test'),
    inquirer.List('faction',
                  message="Who's side do you pick: ",
                  choices=['Technology', 'Humans'])
]
faction = inquirer.prompt(pick_a_side)

