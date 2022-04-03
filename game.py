import random
from termcolor import colored

words=[]
with open("words.txt","r") as w:
    for word in w:
        words.append(word[:-1])


def play_game():
    keyboard = """[q] [w] [e] [r] [t] [y] [u] [i] [o] [p]
  [a] [s] [d] [f] [g] [h] [j] [k] [l]
    [z] [x] [c] [v] [b] [n] [m]"""
    answer=random.choice(words)
    #print(answer)           #for testing
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

        guess = list(guess)
        
        
        for letter in range(len(guess)):   
            #green color   
            if guess[letter] == answer[letter]:
                keyboard = keyboard.replace("["+guess[letter]+"]", "["+colored(guess[letter], "green")+"]")
                keyboard = keyboard.replace("["+colored(guess[letter], "yellow")+"]", "["+colored(guess[letter], "green")+"]")
                guess[letter] = colored(guess[letter], "green")
            
            #yellow color
            elif guess[letter] in answer:     
                if guess.count(guess[letter]) > answer.count(guess[letter]):
                    for letter_temp in range(letter+1, len(guess)):
                        if guess[letter_temp] == answer[letter_temp]:
                            break
                        elif guess.count(colored(guess[letter], "yellow")) < answer.count(answer[letter]):
                            guess[letter] = colored(guess[letter], "yellow")
                elif colored(guess[letter], "yellow") not in guess:
                    if colored(guess[letter], "green") not in keyboard:
                        keyboard = keyboard.replace("["+guess[letter]+"]", "["+colored(guess[letter], "yellow")+"]")
                    if guess.count(colored(guess[letter], "green")) != answer.count(guess[letter]):
                        guess[letter] = colored(guess[letter], "yellow")
            
            #red color
            else:       
                keyboard = keyboard.replace("["+guess[letter]+"]", "["+colored(guess[letter], "red")+"]")
                guess[letter] = colored(guess[letter], "red")

        print(''.join(guess))
        print("\n", keyboard,"\n")
    print("You won!!!")



play_game()
