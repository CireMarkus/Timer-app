# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:37:03 2020

@author: MrKim
"""
import time as tm
from tkinter import *
from tkinter import ttk

class clock():
    def __init__(self,time):
        self.time = time.split(':')
        self.hours = int(self.time[0])
        self.minutes = int(self.time[1])
        self.seconds = int(self.time[2])
        self.run()
    
    def run(self):
        while True:
            if(self.seconds!=0):
                self.seconds-=1
                self.count_seconds(self.seconds)
            if(self.minutes != 0):
                self.minutes-=1
                self.count_minutes(self.minutes)
            if(self.hours != 0):
                self.hours-=1
                self.count_hours(self.hours)
            else:
                break
    # loop that tracks the number of seconds that have passed. 
    def count_seconds(self,seconds):
       while self.seconds>=0:
           tm.sleep(1)
           root.update()
           timer_label.set("{:02d}:{:02d}:{:02d}".format(self.hours,self.minutes,self.seconds))
           self.seconds -=1
           
	#loop that tracks the number of minutes that are left. 
    def count_minutes(self,minutes):
        while self.minutes >=0:
            self.seconds=59
            self.count_seconds(self.seconds)
            self.minutes -=1
    #loop that tracks the number of hours that are left. 
    def count_hours(self,hours):
        while self.hours>=0:
            self.minutes=59
            self.count_minutes(self.minutes)
            self.hours-=1

#takes the entered time and splits it up for the clock class.  
def start():
    try:
        clock(str(time.get()))
    except ValueError:
        pass


#GUI stuff 
root = Tk()
root.title('Timer')
    
mainframe = ttk.Frame(root,padding='12 12 12 12')
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

time = StringVar()
timer_label = StringVar()



time_entry = ttk.Entry(mainframe, width=10,textvariable=time)
time_entry.grid(column = 2, row = 3, sticky=(W,E))
ttk.Button(mainframe, text = 'Start', command = start).grid(column = 2, row=4, sticky =E)

ttk.Label(mainframe,text = 'Time Remaining').grid(columnspan = 4, row = 0, sticky = (N,S,E,W))
ttk.Label(mainframe, textvariable = timer_label).grid(column = 2, row = 1)

time_entry.focus()

root.mainloop()


