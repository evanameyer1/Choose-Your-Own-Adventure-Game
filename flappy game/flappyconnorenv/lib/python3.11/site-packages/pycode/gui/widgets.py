from sys import version_info
if version_info[0] == 2:
    # We are using Python 2.x
    import Tkinter as tk
elif version_info[0] == 3:
    # We are using Python 3.x
    import tkinter as tk


class MyWidget:
    def __init__(self, label):
        self.label = label


class TrueFalseWidget(MyWidget):
    def __init__(self, label):
        super(TrueFalseWidget, self).__init__(label)
        self.widget = None
        self.labelw = None

    def draw(self, root, line):
        self.widget = tk.Checkbutton(root)
        self.widget.grid(column=1, row=line, sticky=tk.NSEW)
        self.labelw = tk.Label(root, text=self.label, justify=tk.LEFT)
        self.labelw.grid(column=2, row=line, sticky=tk.NSEW)

class ScaleWidget(tk.Frame):
    def __init__(self,master,label,min_,max_,redundancy=0):
        super(ScaleWidget,self).__init__(master)
        self.min = min_
        self.max = max_
        self.variables = [tk.Entry(master,width=2) for i in range(redundancy+1)]
        self.label = tk.Label(master, text=label)


