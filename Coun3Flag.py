
from tkinter import *
import tkinter.messagebox
from random import randint

root = Tk()
root.title("CountryFlag")
root.geometry("530x380")

# --- Part A: Layout ---

# --- 0. create elements---
playerID = Label(root, text = "Player ID")
idEntry = Entry (root)
password = Label(root, text = "Password")
passwordEntry = Entry (root)
loginButton = Button(root, text="Login", bd=2, relief=RAISED)
line0 = Label(root, text = "*******************************************************************************************************")
lbMaxGuess = Label(root, text = "Max Guess: 3")
lbNoOfGuess = Label(root, text = "Number of Guesses: 0", fg="purple")
cButton = Checkbutton(root, text="Save Records")
line1 = Label(root, text = "*******************************************************************************************************")
lbQuestion = Label(root, text="Which Country?", font=20, fg="purple")
lbLogs = Label(root, text = "Game Logs")
line2 = Label(root, text = "*******************************************************************************************************")

# upload flag photos
flags = []
for i in range (0,10):
    # upload flag photos with name format "i.png"
    flags.append(PhotoImage(file = r"flags/{}.png".format(i)))
#create flag buttons
buttons = []
for i in range (0,10):
    button = Button(root, text = i, image=flags[i], state=DISABLED, bd=0, width=90,command=lambda index=i : check(index))
    buttons.append(button)

#create Start/ Restart button
startButton = Button(root, text="Start", font=8, bg="green", fg="white", bd=5, relief=GROOVE, command=lambda : start())


# ---1. display elements using .grid---
playerID.grid(row=0, column=0, pady=5, sticky=E)
idEntry.grid(row=0, column=1, pady=5, sticky=W)
password.grid(row=0, column=2, pady=5, sticky=E)
passwordEntry.grid(row=0, column=3, pady=5, sticky=W)
loginButton.grid(row=0, column=4, pady=5, columnspan=1)
line0.grid(row=1, column=0, columnspan=5)        
lbMaxGuess.grid(row=2, column=0,columnspan=1)
lbNoOfGuess.grid(row=2, column=1, columnspan=3)
cButton.grid(row=2, column=4)
line1.grid(row=3, column=0, columnspan=5)
lbQuestion.grid(row=4, columnspan=5)
# row 5,6 for option buttons
line2.grid(row=7, column=0, columnspan=5)
# row 8 to 11 reserved for showing gameLog: showing hints
lbLogs.grid(row=8, column=0, columnspan=5, rowspan=4) 

# display option buttons
for row in range (0,2):
    for col in range (0,5):
        # i: the index/position of button | 5: total number of columns
        i = row*5 + col     
        buttons[i].grid(row=row+5, column = col)

# display Start button
startButton.grid(row=12, columnspan=5)



# --- Part B: Logic ---

guess = 0
totalGuesses = 0
# index in "countries" list is corresponding to the flag button index
# eg: index = 1, countries[1] = "BANGLADESH" => the flag of buttons[1]
countries = ["AUSTRALIA", "BANGLADESH", "NEPAL", "VIETNAM", "JAPAN", "INDIA", "GERMANY", "THE USA", "NIGERIA", "BRAZIL"]
# create a random index
index = randint(0,9)
country = countries[index]
lbLogs = []
# set the row for guess logs
log_row = 8

# reset function init()
def init():
    # declare "global" variables: so values of these global variables can be passed outside of this init()
    global buttons, guess, totalGuesses, index, country, lbNoOfGuess, lbLogs, log_row
    guess = 0
    totalGuesses = 0
    index = randint(0,9)
    country = countries[index]
    lbQuestion["text"] = country + " flag ?"
    lbNoOfGuess["text"] = "Number of Guesses: 0"
    log_row = 8

    # remove old logs from the previous play turn
    for lbLog in lbLogs:
        # grid_forget(): remove all elements displayed in grid
        lbLog.grid_forget() 
    lbLogs = []


# check function
# i: index of the pressed button 
def check(i):
    global totalGuesses, buttons, log_row
    guess = i
    # increase the number of guesses taken
    totalGuesses += 1
    lbNoOfGuess["text"] = "Number of Guesses: " + str(totalGuesses)

    # check if guess match the question flag index
    if guess == index:
        tkinter.messagebox.showinfo("You won!", "Excellent! Wanna Restart?")

        #stop:disable all option buttons except Restart
        for b in buttons:
            b["state"] = DISABLED
    else:
        # give player some hints
        lb = Label(root, text="That flag is of {} :)".format(countries[guess]), fg="red")
        lb.grid(row=log_row, column=0, columnspan=5)
        lbLogs.append(lb)
        log_row += 1
        
    # game is over when max no of guesses is reached
    if totalGuesses == 3:
        if guess != index:
            tkinter.messagebox.showinfo("Game Over", "Max Guesses Reached. Wanna Restart?")
        
        #stop:disable all option buttons except Restart
        for b in buttons:
            b["state"] = DISABLED

    # disable options, so user know which ones are already chosen
    buttons[i]["state"] = DISABLED


# initialise game status (has played before?): "none"
status = "none"

# when the Start(game is run 1st time)/Restart(game is replayed) button is triggerd
def start():
    global status
    # enable all option buttons
    for b in buttons:
        b["state"] = NORMAL

    # Game run for the 1st time?
    if status == "none":
        status = "started"
        lbQuestion["text"] = country + " flag ?"
        startButton["text"] = "Restart"
    else:
        status = "restarted"
        # reset the game
        init()
    print("Game started: " + country)


root.mainloop()

