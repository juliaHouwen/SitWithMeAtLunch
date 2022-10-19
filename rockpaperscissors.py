import random

def num_to_word(num):
    ''' int->str
    this function takes the number 1,2, or 3 and returns rock paper or scissors. Otherwise it returns None.
    
    >>>num_to_word(1)
    "rock"
    >>>num_to_word(2)
    "paper"
    >>>num_to_word(3)
    "scissors"
    '''
    
    if num==1:
        return "rock"
    elif num==2:
        return "paper"
    elif num==3:
        return "scissors"

def find_winner(you, comp):
    ''' (int, int)->str
    this function takes two integers representing rock paper or scissors as input and returns a string that tells
    the user who won.
    
    >>>find_winner(1,2)
    "You lost"
    >>>find_winner(1,3)
    "You won!"
    >>>find_winner(2,2)
    "It's a tie!"
    '''
    
    if you==comp:
        return "It's a tie!"
    if (you==1 and comp==2) or (you==2 and comp==3) or (you==3 and comp==1):
        return "You lost"
    else:
        return "You won!"
        
    
        


print("Rock, paper, scissors, shoot!\n1-Rock\n2-Paper\n3-Scissors")
inp= int(input("(input the number that corresponds to your choice): "))


print("You chose: ", num_to_word(inp))

num= random.randint(1,3)
print("The computer chose: ", num_to_word(num))

print(find_winner(inp,num))




    