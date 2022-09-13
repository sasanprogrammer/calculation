import os , sys
import time
from tkinter import *
from tkinter import ttk, messagebox
Num1 = ""
Num2 = ""
class EXECUTE():
    def __init__(self,Pos1,Pos2):
        self.Pos1 = Pos1
        self.Pos2 = Pos2
    def calculation(self):
        with open(self.Pos1,"r",encoding="utf-8") as POS1:
            with open(self.Pos2,"r",encoding="utf-8") as POS2:
                if (POS1.read() == POS2.read()):
                    return True
                else:
                    return False
    def Change_Pos(self,Pos1,Pos2):
        self.Pos1 = Pos1
        self.Pos2 = Pos2


def FILE():
    Top = Toplevel()
    Top.title("Enter address")
    Top.geometry("170x70")
    Top.resizable(False,False)
    EN = ttk.Entry(Top)
    EN2 = ttk.Entry(Top)
    def ENTER():
        global Num1 , Num2
        Num1 = EN.get()
        Num2 = EN2.get()
        Top.destroy()
    BTN = ttk.Button(Top,text="Enter",command=ENTER)


    EN.pack()
    EN2.pack()
    BTN.pack()


def Insert_OUTPUT(TEXT):
    Txt.insert(END,"Scanning\n")
    time.sleep(1)
    Txt.insert(END,"Scanning Text\n")
    Txt.insert(END,"Scanning File\n")
    Txt.insert(END,"OUTPUT:\n")
    Txt.insert(END,TEXT)

def Scan():
    global Num1 , Num2
    Execute.Change_Pos(Num1,Num2)
    Insert_OUTPUT(str(bool(Execute.calculation())))





#GUI



Execute = EXECUTE(Num1,Num2)

window = Tk()
MENU = Menu(window)
MENU2 = Menu(MENU,tearoff=0)
MENU2.add_command(label="Enter File",command=FILE)
MENU2.add_command(label="Exit  (Alt+F4)")
MENU2.add_command(label="Scan File",command=Scan)

MENU.add_cascade(label="Tools",menu=MENU2)

Txt = Text(window)
window.config(menu=MENU)
Txt.pack(fill=BOTH,expand=True)
mainloop()