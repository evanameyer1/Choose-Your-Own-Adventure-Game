# Game Overview

*Welcome to our choose your own adventure game!*
You are living in the near future when you stumble across an old time machine - you aren’t sure how to use it (they don’t exactly teach it in school) but your curiousity overpowers all else and you find the possibilities of time travel consuming your every thought. 
One night, when you’ve had enough, you grab a spare toolkit from your garage and attempt to fix it up...  

## How To Play

1. Clone the repository: git clone https://github.com/evanameyer1/Choose-Your-Own-Adventure
2. Change directory: cd <folder name>
3. Run the script: python Main.py

#####Prerequisites
* Python 3
* tkinter
* inquirer
* pprint
#####Installing Process
* Install Python 3: https://www.python.org/downloads/
* Install required packages:
* tkinter: pip install python-tk
* inquirer: pip install inquirer
* pprint: already included in Python 3

## Tools Used

##### **Imports:**
```
import os 
import sys 
import time
from pprint import pprint
import tkinter as tk 
from tkinter import ttk 
import inquirer 
sys.path.append(os.path.realpath(".")) 
```
##### **Function For Typing Print:**
```
def print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
```
## Process
##### **For The Main Timeline** - YAMATO KASHIMA

The game starts by printing a brief introduction to the story. The player is then prompted to select parts to repair the time machine in a specific order. Once all parts are assembled, the player selects a wire color to connect to start the machine. Finally, the player calibrates the strength of the time machine before being prompted to decide on when to travel to.

##### **For The Futuristic Timeline** - EVAN MEYER

I first drew out the paths via pen and paper to help me map out my process and ensure that all of the items were correctly accounted for. 
Once I had an end product I was satisfied with, I copied everything over to a digital format as shown below. 

![Futuristic Timeline Paths](https://user-images.githubusercontent.com/56325011/217443169-5be99c2c-9c88-4fa4-9b14-39db4d60f249.png)

I colored-coded things as follows: blue requires an item to access, green is a result where winning is possible, red is a result where winning is not possible, 
and the purple shapes are places where I didn’t have space to finish the paths so I continuted them someplace else. 

Once the paths were all planned out, I then wrote everything together with functions that consisted of nested if statements, while statements, and questions through python inquirer. 
