import random

from tkinter import filedialog


def open_file(self):
    filename = filedialog.askopenfilename()
    try:
        file = open(filename, 'r')
        self.open_files["open"] = file
        self.__input = file.readlines()
        self.act = self.__input.pop(random.randrange(len(self.__input))).split("\\\\")
        self.showResults(self.act[0], self.act[1])
    except FileNotFoundError:
        pass
