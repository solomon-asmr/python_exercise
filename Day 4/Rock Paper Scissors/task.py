import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices= [rock, paper, scissors]
Player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissor.\n"))
if Player_choice>=3 or Player_choice<=-1:
    print("wrong choice")
else:
    print(choices[Player_choice])
    computer_choice=random.randint(0,2)
    print("computer chose:")
    print(choices[computer_choice])

    if Player_choice==0 & computer_choice==2:
        print("you win")
    elif computer_choice==0 & Player_choice==2:
        print("you loose")
    elif computer_choice>Player_choice:
        print("you lose")
    elif Player_choice > computer_choice:
        print("you win")
    elif computer_choice==Player_choice:
        print("Its a tie")
    else:
        print("You insert the wrong number")