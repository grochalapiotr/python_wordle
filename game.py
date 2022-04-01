import random
from termcolor import colored

words=[]
with open("words.txt","r") as w:
    for word in w:
        words.append(word[:-1])


def play_game():
    answer=random.choice(words)
    print(answer)           #testing word
    while True:
        guess = input("Enter 5 letter word: ")
        
        while len(guess) > 5:
            print("Word is too long")
            guess = input("Enter 5 letter word: ")
        
        while len(guess) < 5:
            print("Word is too short")
            guess = input("Enter 5 letter word: ")

        while guess not in words:
            print("It's not a word")
            guess = input("Enter 5 letter word: ")
        
        if guess == answer:
            print(colored(guess, "green"))
            break
        for letter in range(len(guess)):
            if guess[letter] == answer[letter]:
                print(colored(guess[letter], "green"), end = "")
            elif guess[letter] in answer:
                print(colored(guess[letter], "yellow"), end = "")
            else:
                print(colored(guess[letter], "red"), end = "")
        print("")
    print("You won!!!")



play_game()
