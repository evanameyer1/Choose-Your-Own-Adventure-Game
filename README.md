# Game Overview

*Welcome to our choose your own adventure game!*
You are living in the near future when you stumble across an old time machine - you aren’t sure how to use it (they don’t exactly teach it in school) but your curiousity overpowers all else and you find the possibilities of time travel consuming your every thought. 
One night, when you’ve had enough, you grab a spare toolkit from your garage and attempt to fix it up...  

## How To Play

In order to play our choose your own adventure game, you have to download our virtual environment - our game’s own little bubble that allows you to access the packages and tools you need (but just when you play). Below are the steps to set this up: 

##### **For Windows Machines**

1. Download our game and it’s required packages at this [link](https://drive.google.com/drive/folders/12HL2gLqy2v0IkFKQ0jYISr8pCtoThxU9?usp=sharing)
2. Type ‘cmd’ into your search bar to open the command prompt
3. Right click on the folder that contains your download game and click “Copy as Path”. Then, in your command prompt, type ‘cd’ and paste your path. Click enter. 
4. Paste ‘venv/timemachineenv/Scripts/activate.bat’ into the command prompt next and click enter.
5. Paste 'pip install -r requirements.txt’ into your command prompt and click enter to install the required packages.
6. Finally, paste ‘python -m main’ to run the game and enjoy!

##### **For MacOS**

1. Download our game and it’s required packages at this link: insert link
2. Right click on the folder that contains your download game and click Services>New Terminal at Folder.  
4. Paste ‘venv/timemachineenv/bin/activate’ into the command prompt next and click enter.
5. Paste 'pip install -r requirements.txt’ into your command prompt and click enter to install the required packages.
6. Finally, paste ‘python “Main.py”’ to run the game and enjoy!

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

##### **For The Futuristic Timeline** - EVAN MEYER

I first drew out the paths via pen and paper to help me map out my process and ensure that all of the items were correctly accounted for. 
Once I had an end product I was satisfied with, I copied everything over to a digital format as shown below. 

![Futuristic Timeline Paths](https://user-images.githubusercontent.com/56325011/217443169-5be99c2c-9c88-4fa4-9b14-39db4d60f249.png)

I colored-coded things as follows: blue requires an item to access, green is a result where winning is possible, red is a result where winning is not possible, 
and the purple shapes are places where I didn’t have space to finish the paths so I continuted them someplace else. 

Once the paths were all planned out, I then wrote everything together with functions that consisted of nested if statements, while statements, and questions through python inquirer. 
