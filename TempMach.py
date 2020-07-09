from tkinter import *
from math import sqrt
from sys import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
class windows:                       #Class for the output window you need to create
    def __init__(self,win):
        self.label1 = Label(win, text='Enter the altitude:')
        self.label1.place(x=50, y=50)
        self.entry1 = Entry(bd=6)
        self.entry1.place(x=80, y=80)
        self.label5 = Label(win, text='Enter the flight speed:')
        self.label5.place(x=50, y=120)
        self.entry5 = Entry(bd=6)
        self.entry5.place(x=80, y=150)
        self.button1 = Button(win, text='   Ok   ', command=self.calc)
        self.button1.place(x=250, y=110)
        self.label2 = Label(win, text='Temp')
        self.label2.place(x=20, y=190)
        self.entry2 = Entry(bd=6)
        self.entry2.place(x=80, y=190)
        self.label3 = Label(win, text='Speed')
        self.label3.place(x=20, y=220)
        self.entry3 = Entry(bd=6)
        self.entry3.place(x=80, y=220)
        self.label4 = Label(win, text='Mach')
        self.label4.place(x=20, y=250)
        self.entry4 = Entry(bd=6)
        self.entry4.place(x=80, y=250)
    def calc(self):                       #Function for calculating all parmeters
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        h1 = float(self.entry1.get())
        v1 = float(self.entry5.get())
        t = 288 - (6.5*0.001*h1)
        a = sqrt(1.4*287*t)
        m = v1/a
        self.entry2.insert(END, str(t))
        self.entry3.insert(END, str(a))
        self.entry4.insert(END, str(m))
        c1 = float(self.entry1.get())
        if c1 > 11000:                    #Code to verify that input falls within the tropospheric constraint
            self.label6 = Label(text='Please enter a value under 11000 meters')
            self.label6.place(x=250, y=130)
            self.entry2.delete(0, 'end')
            self.entry3.delete(0, 'end')
            self.entry4.delete(0, 'end')
        p1 = np.linspace(0, c1, 100)
        p2 = np.linspace(0, t, 100)
        fig, ax = plt.subplots()
        line, = ax.plot(p1, p2, color='g')
        def update(num, p1, p2, line):
            line.set_data(p1[:num], p2[:num])
            line.axes.axis([0, c1, 0, t])
            return line,

        ani = animation.FuncAnimation(fig, update, fargs=[p1, p2, line], interval=25, blit=True)
        plt.show()

window = Tk()
mywin = windows(window)
window.title('Temperature-Mach relation for Troposphere')
window.geometry("600x300+10+10")
window.mainloop()

