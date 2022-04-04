from calendar import c
import random
from termcolor import colored
import time

words=[]
with open("words.txt","r") as w:
    for word in w:
        words.append(word[:-1])



def start_game():
    print( """ ___         _    _             
| . \ _ _  _| |_ | |_  ___ ._ _ 
|  _/| | |  | |  | . |/ . \| ' |
|_|  `_. |  |_|  |_|_|\___/|_|_|
     <___'                      
 _ _ _              _  _        
| | | | ___  _ _  _| || | ___   
| | | |/ . \| '_>/ . || |/ ._>  
|__/_/ \___/|_|  \___||_|\___. """)

    print("""\nMENU
    1. Start game
    2. About
    3. Quit""")
    menu = input("\nInput: ")
    match menu:
        case "1":
            play_game()
        case "2":
            about()
        case "3":
            exit()


def play_game():
    commands = ["*quit*", "*cheat*", "*again*"]
    keyboard = """[q] [w] [e] [r] [t] [y] [u] [i] [o] [p]
  [a] [s] [d] [f] [g] [h] [j] [k] [l]
    [z] [x] [c] [v] [b] [n] [m]"""

    answer=random.choice(words)
    #print(answer)           #for testing

    while True:
        guess = input("\nEnter 5 letter word: ")

        if guess in commands:
            match guess:
                case "*quit*":
                    start_game()
                case "*cheat*":
                    print("["+answer+"]")
                    continue
                case "*again*":
                    play_game()

        if len(guess) > 5:
            print("Word is too long")
            continue
        
        if len(guess) < 5:
            print("Word is too short")
            continue

        if guess not in words:
            print("It's not a word")
            continue
        
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
    time.sleep(2)
    start_game()

def about():
    print("""\nAuthor:
Year:""")
    x = input("\nPress enter")
    if x or not x:
        start_game()


start_game()
#play_game()
