# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from sys import flags
import os
import art
import time

print(art.logo)
biders_book = {}
flag=True
while flag:
    name= input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    biders_book[name]=bid
    choose = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if choose=='no':
        flag=False
        maxi=0
        name_max=""
        for bidder in biders_book:
            if biders_book[bidder]>maxi:
                maxi=biders_book[bidder]
                name_max=bidder
        print(f"The winner is {name_max} with a bid of ${maxi}")



