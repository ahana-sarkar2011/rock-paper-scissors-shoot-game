from tkinter import *
import random

root = Tk()
root.geometry("600x600")
root.config(background="light green")
root.title("rock paper scissors SHOOT")

pscore = 0
cscore=0

def tie():
    comments.config(text="It's a tie!")
def playerwin():
    global pscore
    comments.config(text="You win!")
    pscore=pscore+1
    playerscore.config(text=str(pscore))
def compwin():
    global cscore
    comments.config(text="Computer wins!")
    cscore=cscore+1
    compscore.config(text=str(cscore))

opts = ["rock","paper","scissors"]

def playerchoice(pc):
    cc = random.choice(opts)
    compob.config(text=cc)
    playerob.config(text=pc)
    if cc == pc:
        tie()
    elif cc=="rock":
        if pc == "paper":
            playerwin()
        elif pc == "scissors":
            compwin()
    elif cc=="paper":
        if pc=="rock":
            compwin()
        elif pc=="scissors":
            playerwin()
    elif cc=="scissors":
        if pc=="rock":
            playerwin()
        elif pc=="paper":
            compwin()

heading = Label(root,text="Lets play rock paper scissors!",font=("Arial",30),bg="light green",fg="black")
heading.pack()

comments = Label(root,text="Start Game",font=("Arial",20),bg="green",fg="pink")
comments.pack()

choicesframe = Frame(root,bg="light green")
choicesframe.pack(pady=40)
options=Label(choicesframe,text="Player choices: ",font=("Arial",20),bg="light green")
options.grid(row=0,column=0)
rock=Button(choicesframe,text="ROCK",command=lambda:playerchoice(opts[0]))
rock.grid(row=0,column=1)
paper=Button(choicesframe,text="PAPER",command=lambda:playerchoice(opts[1]))
paper.grid(row=0,column=2)
scissors=Button(choicesframe,text="SCISSORS",command=lambda:playerchoice(opts[2]))
scissors.grid(row=0,column=3)

gameframe = Frame(root, bg="light pink")
gameframe.pack(pady=30)
playerlab=Label(gameframe,text="YOU",font=("Arial",25),justify=LEFT)
playerlab.grid(row=0,column=0)
playerob=Label(gameframe,text="-",bg="light pink")
playerob.grid(row=1,column=0)
lab=Label(gameframe,text="     ",font=("Arial",25))
lab.grid(row=0,column=1,)
complab=Label(gameframe,text="COMPUTER",font=("Arial",25),justify=RIGHT)
complab.grid(row=0,column=2,)
compob=Label(gameframe,text="-",bg="light pink")
compob.grid(row=1,column=2)

scoreframe = Frame(root,bg="dark green")
scoreframe.pack(pady=50)
playerscorelab=Label(scoreframe,text="Your score:",font=("Arial",20),bg="dark green",fg="white")
playerscorelab.grid(row=0,column=0)
compscorelab=Label(scoreframe,text="Computer score:",font=("Arial",20),bg="dark green",fg="white")
compscorelab.grid(row=1,column=0)
playerscore=Label(scoreframe,text="0",font=("Arial",20),bg="dark green",fg="white")
playerscore.grid(row=0,column=1)
compscore=Label(scoreframe,text="0",font=("Arial",20),bg="dark green",fg="white")
compscore.grid(row=1,column=1)

root.mainloop()