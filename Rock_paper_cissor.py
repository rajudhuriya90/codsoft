print("******* ROCK PAPER SCISSOR***********")

import random
item_list=["Rock","Scissor","Paper"]
user_choice=input("Enter your move= Rock,Scissor,Paper=")
computer_choice=random.choice(item_list)
print(f"User choice={user_choice} \ncomputer_choice={computer_choice}")
if user_choice==computer_choice:
    print("Both chooses same:\n :@@@ match will tie@@@!!")
elif user_choice=="Rock":
    if computer_choice=="Paper":
        print("Paper covers Rock : \n***computer will win***!!")
    else:
        print("Rock smashes Scissor:\n ***you will win***!!") 
elif user_choice=="Paper":
    if computer_choice =="Rock":
        print("Paper cover the Rock:\n***you will win")
    else:
        print("Scissor cut the Paper :\n***computer will win***!!")
elif user_choice=="Scissor":
    if computer_choice=="Paper":
        print("Scissor smashes the Paper :\n***you will win***!! ")
    else:
        print("Rock smashes the Scissor :\n*** computer will win***!!")              


     

