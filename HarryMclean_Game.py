#Display game intro
print("="*25)
print("Number Guessing game")   
print("="*25)

import random   #Import library function

cardNum = random.randint(1, 101)    #Define random integers range
diceRoll = random.randint(1,6)      
trys = 0    #Set trys to zero

#Ask user for their name
name = input("\nEnter your name please: ")

while True: 
    print("\nYou have",diceRoll,"guesses left")
    diceRoll -= 1    #Return to start losing a Guess when guess is incorrect 
    while True:
        #Ask user to guess random card nummber                                                                      
        guess = input("Please enter a card number between 1 and 100: ") 
        #If users number guess is non numeric value display error
        if not guess.isdigit():
            trys += 1 
            print("\nOnly numeric characters are allowed. ")
            break 
        #If Guess correct display congrats message
        elif int(guess) == cardNum:
            trys += 1                                                            
            print("Congratulations", name,"That is correct!!! ")    
            break
        #If geuess of range display out of range
        elif int(guess) < 1 or int(guess) > 100:
            trys += 1
            print("Guess out of range ")
            break       
        #If Guess higher than Card number display too high
        elif int(guess) > cardNum:
            trys += 1     
            print("\nNumber too high ")                                         
            break
        #If Guess lower than Card number display too low
        elif int(guess) < cardNum:
            trys += 1     
            print("\nNumber too low ")
            break
    #If guess is not a numeric value display loss and end program
    if not guess.isdigit():
        status = "loss"
        print("\nProgram Ended...")
        break
    #If user guesses correctly display win
    if int(guess) == cardNum:   
        status = "Win"
        break
    #if user has no guesses left display lose    
    elif int(diceRoll) == 0:    
        status = "Loss"                                                            
        print("You have no more guesses left")
        break
#Save to Statistics.txt if file 
file = open("Statistics.txt","a+")  
datarecord = str(name) + "|" + str(status) + "|" + str(trys) + "\n"
file.write(datarecord)
file.close()
#Results graphic decoration
print("="*25)   
print("Results")
print("="*25)
#Open and display statistics.txt 
file = open("statistics.txt","r")   
content = file.read()
print(content)


  



