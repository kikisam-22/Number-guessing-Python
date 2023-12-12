import random 

def guess(x):
    random_number = random.randint(0,x)
    user_guess = None

    while random_number != user_guess :
        ask_user = input(f"Guess a number :D between 0 and {x}   ")
        
        try : 
            ask_userint = int(ask_user)
        except : 
            print(f"{ask_user} is not a number :P, please try again !!   ")
            continue 
            
        user_guess = ask_userint
        
        if user_guess < random_number :
            print ("The number is HIIIGGHHERRRRR")
        elif user_guess > random_number : 
            print ("The number is looooooooowerrrr")
    
    print(f"GOOD JOB !! YOU have guessed the number {random_number} correctly :)")


def computer_guess(x):
    low = 1
    high = x 
    feedback = ""
    
    while feedback != "c":
        if low != high:
            computer_guess = random.randint(low,high)
        elif low == high : 
            computer_guess = low
            print("YOU'RE NUMBER MUST BE", computer_guess, "!!!")
            
        feedback = input(f"Is {computer_guess} too high [H], too low [L] or correct [C] ").lower()
        
        if feedback == "h":
            high = computer_guess - 1
        elif feedback == "l":
            low = computer_guess + 1
    
    print(f"The computer guessed your number {computer_guess} correctly")

which = int(input("Do you wanna guess a number [enter 1] or do you want the computer to guess the number [enter 2] ?"))
if which == 1 : 
    print("Great, you will have to guess a number")
    guess(int(input("You wanna guess a number between 0 and ? ")))

elif which == 2 : 
    print("The computer will now try to guess your number")
    computer_guess(int(input("You're number is between 0 and ? ")))