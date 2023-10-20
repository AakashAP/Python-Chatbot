"""
@author: Aakash Maurya
"""
from tkinter import Tk
from Graphic import StartPage

class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.Screen = None
        self.Switch(StartPage)

    def Switch(self, FrameClass):
        NewFrame = FrameClass(self)
        if self.Screen is not None:
            self.Screen.destroy()
        self.Screen = NewFrame
        self.Screen.pack()


Chatbot = Interface()
Chatbot.title("ChatBot")
Chatbot.geometry("500x800")
Chatbot.resizable(width=False, height=False)
Chatbot.mainloop()