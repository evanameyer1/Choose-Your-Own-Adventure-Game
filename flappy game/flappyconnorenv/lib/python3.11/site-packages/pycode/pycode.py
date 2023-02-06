# -*- coding: utf-8 -*-
import sys
for i in sys.path:
    print(i)
from pycode.gui.dialogs import NameDialog
from pycode.gui.core import MainFrame

mf = MainFrame()
name = NameDialog()
mf.init()
