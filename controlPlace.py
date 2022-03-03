#from art import *
import os
import tkinter as tk
from time import process_time
from place import Place
class ControlPlace(Place):
    def __init__(self,master,story, callback, r,c,options,timed,actions=[],message=[]):
        super().__init__(master,story, callback, r,c,options,timed,actions,message)
    def renderPlace(self,score):
        super().renderOnly(score)
        scrTxt="Your Score!\n{}".format(self.score)
        self.scrLabel=tk.Label(self.placeFrame, text=scrTxt, font=("Arial", 25), fg='#40e0d0', bg='black',wraplength=self.width-10,pady=10)
        super().packPlace()