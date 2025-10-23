#Name:Sanjida Chowdhury
#Date:10/17/2025
#Assignment:Final Assignment

import pandas as pd
import numpy as np

colors = ['Red','Orange','Blue','Violet','Brown','Pink','Aqua',
          'Green','Silver','Gold','Yellow','White','Black']

def get_user_guess():
    while True:
        g = input("Enter your guess (type 'list' to see options): ").strip()
        if g.lower() == 'list':
            print("Colors:", ', '.join(colors))
            continue
        for c in colors:
            if g.lower() == c.lower():
                return c
        print("Not in the list. Try again.")
            
def computer_guess(secret):
    t = 0
    for c in colors:
        t += 1
        if c == secret:
            break
    return t
    
def coin_toss():
    print("Tie! Coin toss.")
    while True:
        pick = input("Heads or Tails (H/T): ").strip().lower()
        if pick in ('h','t','heads','tails'):
            break
        print("Invalid choice. Enter H or T.")
    coin = np.random.choice(['h','t'])
    print("Coin shows:", "Heads" if coin == 'h' else "Tails")
    if (pick.startswith('h') and coin == 'h') or (pick.startswith('t') and coin == 't'):
        return "user"
    return "computer"
    
def play_again():
    while True:
        a = input("Play again? (Y/N): ").strip().lower()
        if a in ('y','n'):
            return a == 'y'
        print("Please enter Y or N.")
        
print("------------------------------")
print("Two-Player Color Guessing Game")
print("------------------------------")
print("Goal:Guess the secret color faster than the computer!\n")

while True:
    secret = np.random.choice(colors)
    print("A secret color has been chosen.\n")
    
    user_tries = 0
    while True:
        guess = get_user_guess()
        user_tries += 1
        if guess.lower() == secret.lower():
           print(f"Correct! You got it in {user_tries} tries.\n")
           break
        else:
           print("Wrong, try again.\n")
        
    comp_tries = computer_guess(secret)
    print(f"Computer guessed it in {comp_tries} tries.\n")
        
    results= pd.DataFrame({'Player': ['You', 'Computer'],
                           'Guesses': [user_tries, comp_tries]})
        
    print("Score Table (pandas):")
    print(results, "\n")
        
    if user_tries < comp_tries:
        print("You win!\n")
    elif user_tries > comp_tries:
          print("Computer wins!\n")
    else:
        winner = coin_toss()
        print("You win the tiebreaker!\n" if winner == "user" else "Computer wins the tiebreaker!\n")
        
    if not play_again():
        print("Thanks for Playing! Goodbye.")
        break
                               
        
    