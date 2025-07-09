# import all the requried fucntions
from highorLow_logo import vs
from highorLow_logo import logo
import random
from highorLow_data import data

play = True
sys = True
mark = 0

A = random.choice(data)
 # Only once

while play:

    while sys:
        print("\n"*20)
        print(logo) 
        B = random.choice(data)
        while A == B:
            B = random.choice(data)

        def check(A, B):
            print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")
            print(vs)
            print(f"Against B: {B['name']}, a {B['description']} from {B['country']}")

        check(A, B)

        choice = input("Who has more Followers? 'A' or 'B': ").upper()

        if (A['followers'] > B['followers'] and choice == 'A') or \
        (B['followers'] > A['followers'] and choice == 'B'):
            mark += 1
            print(f"You're right! Current score: {mark}\n")
            A = B  #Keep winner as A
        else:
            print(f"Sorry, that's wrong. Final score is: {mark}")
            sys = False

    cont = input("Do you want to play again? say '/yes'/ or '/no'/: ").lower()
    if(cont == "no"):
        play = False
