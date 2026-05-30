from tkinter import *

root = Tk()
root.geometry("600x600")
root.config(background="light green")
root.title("rock paper scissors SHOOT")

heading = Label(root,text="Lets play rock paper scissors!",font=("Arial",30),bg="light green",fg="black")
heading.pack()

comments = Label(root,text="Start Game",font=("Arial",20),bg="green",fg="pink")
comments.pack()

choicesframe = Frame(root,bg="light green")
choicesframe.pack()
rock=Button(choicesframe,text="ROCK")
rock.pack()

root.mainloop()