import guessNumber_logo
import random
print(f"Welcome to Number Guessing Game")
print(f"I am thinking of number between 1 and 100")
lst = [1,2,3,4,5,6,7,8,9,10,
       11,12,13,14,15,16,17,18,19,20,
       21,22,23,24,25,26,27,28,29,30,
       31,32,33,34,35,36,37,38,39,40,
       41,42,43,44,45,46,47,48,49,50,
       51,52,53,54,55,56,57,58,59,60,
       61,62,63,64,65,66,67,68,69,70,
       71,72,73,74,75,76,77,78,79,80,
       81,82,83,84,85,86,87,88,89,90,
       91,92,93,94,95,96,97,98,99,100]
#num = random.randint(1, 100)
#print(num)
num = random.choice(lst)

hard = 5
easy = 10

diff = input(f"Choose a difficulty. Type /'easy/' or /'hard/': ").lower()
if diff=="easy":
    for i in range(easy):
        print(f"You have {easy-i} attempts to guess the number: ")
        guess = int(input("Make a Guess: "))
        if guess!=num:
            if guess<num:
                print("Too Low")
                print("Guess Again")
            else:
                print("Too high")
                print("Guess Again")
        else:
            print(f"you got it! The answer is {num}")
            break
 
else:
    for i in range(hard):
        print(f"You have {hard-i} attempts to guess the number: ")
        guess = int(input("Make a Guess: "))
        if guess!=num:
            if guess<num:
                print("Too Low")
                print("Guess Again")
            else:
                print("Too high")
                print("Guess Again")
        else:
            print(f"You got it! The answer is {num}")
            break