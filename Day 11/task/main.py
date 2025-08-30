import art
import random
choice = input("Do you want to play a game of Blackjack? Type 'Yes' or 'No': ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

flag= choice == 'yes'
Total_deal=0

while flag:
    print(art.logo)
    deal = int(input("insert how much you wanna deal: $"))
    your_card = []
    computer_card = []
    for i in range(2):
        x=random.choice(cards)
        y=random.choice(cards)
        your_card.append(x)
        computer_card.append(y)
    your_card_sum=sum(your_card)
    print(f"Your cards: {your_card}, current score: {your_card_sum}")
    print(f"Computer's first card: {computer_card[0]}")
    Another_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if Another_choice == 'y':
        your_card.append(random.choice(cards))
        print(f"Your cards: {your_card}, current score: {sum(your_card)}")
        print(f"Computer's first card: {computer_card[0]}")
        if sum(computer_card) < 17:
            computer_card.append(random.choice(cards))
        if sum(your_card)>21 and (11 in your_card):
            your_card.remove(11)
            your_card.append(1)
        if sum(computer_card)>21 and (11 in computer_card):
            your_card.remove(11)
            your_card.append(1)
    print(f"Your final hand: {your_card}, final score: {sum(your_card)}")
    print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")

    if sum(your_card)>21:
        print(f"You went over. You lose ${deal} 😌😌 your total money is {Total_deal}")
    elif sum(your_card)==sum(computer_card):
        print("its a tie")
    elif sum(computer_card)>21:
        Total_deal += deal * 2
        print(f"computer went over so You win ${deal} 🎉🎉 your total money is {Total_deal}")
    elif sum(your_card) < sum(computer_card):
        print(f"computer won. You lose ${deal} 😌😌")
    else:
        Total_deal+=deal*2
        print(f"You win ${deal} 🎉🎉 your total money is {Total_deal}")
    keep_playing=input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
    if keep_playing=='yes':
        flag=True
    else:flag=False



