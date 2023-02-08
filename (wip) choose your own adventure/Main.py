import pygame
import os
import sys
import time
from pprint import pprint
import tkinter as tk
from tkinter import ttk
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import inquirer

sys.path.append(os.path.realpath("."))


def print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)

def game():
    print("The year is 2056. The world was in chaos. The time traveling machine, once considered the greatest invention of all time, had fallen into disrepair. The future was uncertain, and the past seemed to be slipping away from humanity's grasp. You set out on a journey to restore the time traveling machine and secure the future of humanity. However, the journey would not be easy, as you must navigate through time and overcome obstacles. The first task is to repair your time machine, as it has not been running for some time. Please input the components in the correct order. The parts are: Flux Capacitor, Power Converter, and the Operating Switch")
    part_options = [
        inquirer.List('items',
                    message="Enter first part:",
                    choices=['Flux Capacitor', 'Operating Switch', 'Power Converter'])
    ]

    while True:
        part = inquirer.prompt(part_options)
        if part['items'] == 'Flux Capacitor':
            print("Incorrect. Try again.")
        elif part['items'] == 'Operating Switch':
            print("Incorrect. Try again.")
        elif part['items'] == 'Power Converter':
            print('Correct! What do we install next?')
            break
        else:
            print('Not an answer. Try again')
    
    part_options = [
        inquirer.List('items',
                    message="Enter second part:",
                    choices=['Flux Capacitor', 'Operating Switch'])
    ]
    while True:
        part = inquirer.prompt(part_options)
        if part['items'] == 'Flux Capacitor':
            print("Correct! What's next?")
            break
        elif part['items'] == 'Operating Switch':
            print('Incorrect. Try again.')
    
    part_options = [
        inquirer.List('items',
                    message="Enter third part:",
                    choices=['Operating Switch'])
    ]
    while True:
        part = inquirer.prompt(part_options)
        if part['items'] == 'Operating Switch':
            print("Perfect! ")
            break
        else:
            print('Not a valid response')
    print("All parts are together, but the machine won't turn on. Choose a wire to splice and connect to get the system running")

    wire_color = [
        inquirer.List('items',
                    message="Select the correct color:",
                    choices=['Red', 'Green', 'Blue', 'Yellow', 'Black'])
    ]
    wire_color = inquirer.prompt(wire_color)
    while True:
        wire_choice = wire_color['items']
        if wire_choice == 'Blue':
            print("You chose correctly! Let's start it up!")
            break
        elif wire_choice == 'Green':
            print(
                "You just overheated the machine and melted the internal components. Start Over")
            print(game())
            break
        elif wire_choice == "Red":
            print("You just blew up your house and died. Start Over")
            print(game())
            break
        elif wire_choice == 'Yellow':
            print(
                'This was not the right choice, but luckily nothing bad seemed to have happened. Try again')
            wire_color = inquirer.prompt(wire_color)
        elif wire_choice == 'Black':
            print(
                "You felt a small shock, but everything seems to be working okay. Let's try a different wire")
            wire_color = inquirer.prompt(wire_color)
    def strength_options():
        strength_choice = [
            inquirer.List('items',
                        message="The there'a a sSelect a strength:",
                        choices=['Extra Weak', 'Weak', 'Normal', 'Strong', 'Extra Strong'])
        ]
        return inquirer.prompt(strength_choice)
    while True:
        strength_answer = strength_options()
        if strength_answer['items'] == "Strong":
            print("The strength seems ideal! Let's get ready to time travel! ")
            break
        elif strength_answer['items'] == "Extra Weak":
            print("...you're kidding right? Try again.")
        elif strength_answer['items'] == "Weak":
            print("You're choice was like the answer: weak! Choose again.")
        elif strength_answer['items'] == "Normal":
            print(
                "This doesn't appear to be enough strength for transtemporal navigation... but that's just me.")
        elif strength_answer['items'] == "Extra Strong":
            print(
                "Although this option is not lacking a decifiency in strength, this might be overdoing it.")
    print("Okay, now we must decide if we want to go to the future or the past.")
    
    destination_choice = [inquirer.List('destination', message="Where do you want to go, the past or the future?", choices=['Past', 'Future'])
    ]

    destination = inquirer.prompt(destination_choice)

    while destination['destination'] == 'Past':
        riddle = "I am in the past,\nNever in the future.\nI don't exist,\nBut have existed.\nI saw what you saw,\nAnd this is what I will ever see.\nWhat am I?"

        print(f"You have chosen {destination['destination']}. Please solve the following riddle:\n{riddle}")
        answer = input("Enter your answer: ")

        if answer.lower() == 'memory':
            print("Correct! Time to travel back in time.")
            import Past.py
            past.py
        else:
            print("Incorrect. Time travel to the past failed. Try again")

    riddle = "I never was\nAm always to be,\nNoone ever saw me\nNor ever will.\nAnd yet I am the confidence of all\nTo live and breathe on this terrestrial ball."

    while destination['destination'] == 'Future':
        print(f"You have chosen {destination['destination']}. Please solve the following riddle:\n{riddle}")
        answer = input("Enter your answer: ")

        if answer.lower() == 'tomorrow':
            print("Correct! Time to travel to the future.")
            import Future.py
            future.py
        else:
            print("Incorrect. Time travel to the future failed. Try again")

print(game())