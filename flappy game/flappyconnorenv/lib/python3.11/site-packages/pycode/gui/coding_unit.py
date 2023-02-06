import yaml
from sys import version_info
if version_info[0] == 2:
    # We are using Python 2.x
    import Tkinter as tk
    import tkFileDialog as filedialog
    from Tkinter import ttk
elif version_info[0] == 3:
    # We are using Python 3.x
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog


class Paper(tk.Frame):
    def __init__(self,master,coding,data):
        super(Paper,self).__init__(master)



if __name__ == "__main__":
    Paper("config.yml",None)

