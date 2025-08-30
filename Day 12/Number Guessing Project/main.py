import random
import art
print(art.logo)
print("Wellcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
choosen_number=random.randint(1,101)
choose_difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
def guess(level):
    counter=10
    if level=="hard":
        counter=5
    win=False
    while counter>0 and (not win):
        print(f"You have {counter} attempts remaining to guess the number.")
        ur_guess=int(input("Make a guess: "))
        if ur_guess==choosen_number:
            print("you win 🎉🎉🎉")
            win=True

        elif ur_guess>choosen_number:
            print("Too high.")
            counter-=1
        elif ur_guess<choosen_number:
            print("Too low.")
            counter-=1
        if counter>0 and win==False:
            print("guess again")
    if counter==0 and win==False:
        print("You've run out of guesses, you lose.")


guess(choose_difficulty)