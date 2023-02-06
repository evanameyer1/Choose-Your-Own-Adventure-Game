# -*- coding: utf-8 -*-
from pycode.gui.core import MainApplication
import tkinter as tk
import click

@click.command()
def main(args=None): #pragma no cover
    """Console script for pycode"""
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.geometry("640x480")
    root.mainloop()


if __name__ == "__main__": #pragma no cover
    main()
