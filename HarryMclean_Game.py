import random
from re import I
from tkinter import Tk
import tkinter   #Import library function

cardNum = random.randint(1, 101)
diceRoll = random.randint(1,6)
attempts = 0 #SET TRIES TO ZERO

def check_answer():
    global cardNum
    global diceRoll
    global attempts
    global text
    guess = str(entry_window.get())
    
    while True:
        text.set("You have " + str(diceRoll) + "guesses left") 
        diceRoll -= 1    
        
        #USER HAS NO GUESSES LEFT 
        if attempts == diceRoll:    
            text.set("You have no guesses remaining")
            btn_check.pack_forget()
            break   
       
       #USERS GUESS IS A NON NUMERIC VALUE
        elif not guess.isdigit():
            text.set("Only numeric characters are allowed. ")
            attempts += 1
            btn_check.pack_forget()
            break
                
            #GUESS IS CORRECT DISPLAY SUCCESS MESSAGE
        elif int(guess) == cardNum:
            attempts += 1
            text.set("Congratulations, you guessed correctly!!! ")                                                             
            break
        
        #GUESS OUT OF RANGE DISPLAY GUESS IS OUT OF RANGE
        elif int(guess) < 1 or int(guess) > 100:
            attempts += 1
            text.set("Guess is out of range, you have " + str(diceRoll) + " guesses left")
            
            break   
        
        #GUESS HIGHER THAN CARD NUMBER DISPLAY TOO HIGH
        elif int(guess) > cardNum:
            attempts += 1
            text.set("Number to high " + str(diceRoll) + " guesses left")                                              
            break
        
        #GUESS LOWER THAN CARD NUMBER DISPLAY TOO LOW
        elif int(guess) < cardNum:
            attempts += 1
            text.set("Number too low " + str(diceRoll) + " guesses left")    
            break

        #USER GUESSES CORRECTLY, DISPLAY WIN
        elif int(guess) == cardNum:   
            btn_check.pack_forget()
            break

root = Tk()
root.title("Number Guessing Game")
root.geometry("500x300")
label = tkinter.Label(root, text="Guess the number between 1 and 100")
label.pack()
entry_window = tkinter.Entry(root, width=40, borderwidth=4)
entry_window.pack()

btn_check = tkinter.Button(root, text="Check", command=check_answer)
btn_check.pack()

btn_quit = tkinter.Button(root, text="Quit", command=root.destroy)
btn_quit.pack()

text  = tkinter.StringVar()
text.set("You have " + str(cardNum) + " guesses left") 

guess_attempts= tkinter.Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()




  



