import pygame
import os
import sys
import time
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer

import tkinter as tk
from tkinter import ttk
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

# BLUE = (106, 159, 181)
# WHITE = (255, 255, 255)


# def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
#     """ Returns surface with text written on """
#     font = pygame.freetype.SysFont("Courier", font_size, bold=True)
#     surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
#     return surface.convert_alpha()


# class UIElement(Sprite):
#     """ An user interface element that can be added to a surface """

#     def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
#         """
#         Args:
#             center_position - tuple (x, y)
#             text - string of text to write
#             font_size - int
#             bg_rgb (background colour) - tuple (r, g, b)
#             text_rgb (text colour) - tuple (r, g, b)
#             action - the gamestate change associated with this button
#         """
#         self.mouse_over = False

#         default_image = create_surface_with_text(
#             text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
#         )

#         highlighted_image = create_surface_with_text(
#             text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
#         )

#         self.images = [default_image, highlighted_image]

#         self.rects = [
#             default_image.get_rect(center=center_position),
#             highlighted_image.get_rect(center=center_position),
#         ]

#         self.action = action

#         super().__init__()

#     @property
#     def image(self):
#         return self.images[1] if self.mouse_over else self.images[0]

#     @property
#     def rect(self):
#         return self.rects[1] if self.mouse_over else self.rects[0]

#     def update(self, mouse_pos, mouse_up):
#         """ Updates the mouse_over variable and returns the button's
#             action value when clicked.
#         """
#         if self.rect.collidepoint(mouse_pos):
#             self.mouse_over = True
#             if mouse_up:
#                 return self.action
#         else:
#             self.mouse_over = False

#     def draw(self, surface):
#         """ Draws element onto a surface """
#         surface.blit(self.image, self.rect)


# def main():
#     pygame.init()

#     screen = pygame.display.set_mode((800, 600))
#     game_state = GameState.TITLE

#     while True:
#         if game_state == GameState.TITLE:
#             game_state = title_screen(screen)

#         if game_state == GameState.NEWGAME:
#             game_state = play_level(screen)

#         if game_state == GameState.QUIT:
#             pygame.quit()
#             return


# def title_screen(screen):
#     start_btn = UIElement(
#         center_position=(400, 400),
#         font_size=30,
#         bg_rgb=BLUE,
#         text_rgb=WHITE,
#         text="Start",
#         action=GameState.NEWGAME,
#     )
#     quit_btn = UIElement(
#         center_position=(400, 500),
#         font_size=30,
#         bg_rgb=BLUE,
#         text_rgb=WHITE,
#         text="Quit",
#         action=GameState.QUIT,
#     )

#     buttons = [start_btn, quit_btn]

#     while True:
#         mouse_up = False
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#                 mouse_up = True
#         screen.fill(BLUE)

#         for button in buttons:
#             ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
#             if ui_action is not None:
#                 return ui_action
#             button.draw(screen)

#         pygame.display.flip()


# class GameState(Enum):
#     QUIT = -1
#     TITLE = 0
#     NEWGAME = 1


# if __name__ == "__main__":
#     main()

def game():
    print("The year is 2056\nYou need to rebuild your old time machine, as you're looking to vacation.\nPlease input the components in the correct order. The parts are: flux capacitor, power converter, and the operating switch")
    part_options = [
        inquirer.List('items',
                    message="Enter first part:",
                    choices=['flux capacitor', 'operating switch', 'power converter'])
    ]

    while True:
        part = inquirer.prompt(part_options)
        if part['items'] == 'flux capacitor':
            print("Incorrect. Try again.")
        elif part['items'] == 'operating switch':
            print("Incorrect. Try again.")
        elif part['items'] == 'power converter':
            print('Correct! What do we install next?')
            break
        else:
            print('Not an answer. Try again')
    
    part_options = [
        inquirer.List('items',
                    message="Enter second part:",
                    choices=['flux capacitor', 'operating switch'])
    ]
    while True:
        part = inquirer.prompt(part_options)
        if part['items'] == 'flux capacitor':
            print("Correct! What's next?")
            break
        elif part['items'] == 'operating switch':
            print('Incorrect. Try again.')
    
    part_options = [
        inquirer.List('items',
                    message="Enter third part:",
                    choices=['operating switch'])
    ]
    while True:
        part = inquirer.prompt(part_options)
        if part['items'] == 'operating switch':
            print("Perfect!")
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
                        message="Select a strength:",
                        choices=['Extra Weak', 'Weak', 'Normal', 'Strong', 'Extra Strong'])
        ]
        return inquirer.prompt(strength_choice)
    while True:
        strength_answer = strength_options()
        if strength_answer['items'] == "Strong":
            print("The strength seems ideal! Let's get ready to time travel!")
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
        riddle = "I am in the past,\nNever in the future.\nI don't exist,\nBut have existed.\nI saw what you saw,\nand this is what I will ever see.\nWhat am I?"

        print(f"You have chosen {destination['destination']}. Please solve the following riddle:\n{riddle}")
        answer = input("Enter your answer: ")

        if answer == 'memory':
            print("Correct! Time to travel back in time. Try again")
        else:
            print("Incorrect. Time travel to the past failed.")

    riddle = "I never was\nAm always to be,\nNoone ever saw me\nnor ever will.\nAnd yet I am the confidence of all\nto live and breathe on this terrestrial ball."

    while destination['destination'] == 'Future':
        print(f"You have chosen {destination['destination']}. Please solve the following riddle:\n{riddle}")
        answer = input("Enter your answer: ")

        if answer == 'Tomorrow':
            print("Correct! Time to travel to the future.")
            break
        else:
            print("Incorrect. Time travel to the future failed. Try again")

print(game())