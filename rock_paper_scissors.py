import random
print("Welcome to Rock-Paper-Scissors Game")
print("If you win, you get 2 points added to your score.\nIf you lose, there won't be any change in your score.\nIf it's a draw, you will get 1 point added to your score.")
print("Enter your name:")
user=input()
user_score=0
com_score=0

while True:
    print("Available options: \n 1 for Rock \n 2 for Paper \n 3 for Scissors \n")
    choice=int(input("Enter your choice:"))
    while choice>3 or choice<1:
        choice=int(input("Enter a valid choice please--"))
    if choice==1:
        choice_name="Rock"
    elif choice==2:
        choice_name="Paper"
    else:
        choice_name="Scissors"
    print("You chose \n",choice_name)
    print("Now it's computer's turn--")
    com_choice=random.randint(1,3)
    if com_choice==1:
        com_choice_name="Rock"
    elif com_choice==2:
        com_choice_name="Paper"
    else:
        com_choice_name="Scissors"
    print("Computer chose \n",com_choice_name)
    print(choice_name,"vs",com_choice_name)
    if choice==com_choice:
        print("It's as Draw")
        res='DRAW'
    elif((choice==1 and com_choice==2) or (choice==2 and com_choice==1)):
        print("Paper wins-->",end="")
        res='Paper'
    elif((choice==1 and com_choice==3) or (choice==3 and com_choice==1)):
        print("Rock wins-->",end="")
        res='Rock'
    elif((choice==2 and com_choice==3) or (choice==3 and com_choice==2)):
        print("Scissors wins-->",end="")
        res='Scissors'
    
    if res=='DRAW':
        print("<=It's a TIE=>")
        com_score+=1
        user_score+=1
    elif(res==com_choice_name):
        print("Computer wins")
        com_score+=2
    else:
        print("You win")
        user_score+=2
    
    print("Do you want to play again? (Y/N)")
    reply=input().lower()
    if(reply=='n'):
        break

print("Scoreboard: ")
print("{}'s score {}".format(user,user_score))
print("Computer's score {}".format(com_score))
if(user_score>com_score):
    print("Congratulations!!You have dominated the system.")
elif(user_score<com_score):
    print("This time it's system's upperhand.You can beat next time.")
else:
    print("That's very close!!But you have levelled with the system.")
print("--Thanks for playing--")