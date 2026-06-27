from tkinter import *
import random

def diceroll():
    dice.config(text=random.randint(1,6))

root = Tk()
root.geometry("500x500")
root.config(background="blue")
root.title("dice roll")

heading = Label(root,text="Roll the dice!",font=("Arial",40),bg="pink",fg="black")
heading.pack()

dice=Label(root,text="-",font=("Arial",70),bg="white",fg="black")
dice.pack(pady=40)

roll=Button(root,text="ROLL",command=diceroll)
roll.pack(pady=50)


root.mainloop()