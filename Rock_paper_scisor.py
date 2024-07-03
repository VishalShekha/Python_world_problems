import random

# # def randl(x):
#     a = random.randint(0,11)
#     if (a==x) :
#         print("You gay!")
#         print(a)
#     else:
#         print("You lost. Try again")

# # for f in range(3):
#     b = int(input("Enter Number:"))
#     randl(b)



lit = ["Rock" , "Paper" , "Scissors"]

def getChoices():

    playerChoice = input("Enter a choice (RPS): ")

    computerChoice = random.choice(lit)
    
##Random library 'choice' is choosing randomly from the list
    choices = {"player" : playerChoice, "computer": computerChoice}

    return choices

choices = getChoices()
##print(choices)

def checkWin(player, computer):
    print(f"Your chose {player} and computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    
    elif player == "Rock":
        if computer == "Paper":
            return "Computer wins!"
        elif computer == lit[2]:
            return "PLayer wins"
        
    elif player == "Paper":
        if computer == "Rock":
            return "Player wins!"
        elif computer == lit[2]:
            return "Computer wins"
        
    elif player == lit[2]:
        if computer == "Paper":
            return "Player wins!"
        elif computer == "Rock":
            return "Computer wins"
    else:
        return "Type Rock , Paper , Scissors... to get the resulit."

'''
instead of this you can do this ^

    elif player ==lit[0] and computer == lit[1]:
        return "Computer is the winner!"

    elif player ==lit[1] and computer == lit[2]:
        return "Computer is the winner!"
    
    elif player ==lit[0] and computer == lit[2]:
        return "You are the winner!"

    elif player ==lit[1] and computer == lit[0]:
        return "You are the winner!"

    elif player ==lit[2] and computer == lit[1]:
        return "You are the winner!"

    elif player ==lit[2] and computer == lit[0]:
        return "Computer is the winner!"

'''          

Resulit = checkWin(choices["player"], choices["computer"])

print(Resulit)