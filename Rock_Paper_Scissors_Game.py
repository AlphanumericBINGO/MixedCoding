from random import randint
from time import sleep
import sys
import str_mod
str_mod = str_mod.str_mod()
tries = 0
score = 0
choices = ['rock', 'paper', 'scissors']
Bot_Wins = None
Player_Wins = None
def logic(user_choice, bot_choice):
    global Player_Wins, Bot_Wins
    if Player_Wins:
        if user_choice == 'rock':
            return 'paper'
        elif user_choice == 'paper':
            return 'scissors'
        elif user_choice == 'scissors':
            return 'rock'
    if Bot_Wins:
        if user_choice == 'rock':
            return 'scissors'
        elif user_choice == 'paper':
            return 'rock'
        elif user_choice == 'scissors':
            return 'paper'
   
        if Player_Wins is None and Bot_Wins is None:
           bot_choice = choices[randint(0, 2)]
        return bot_choice

str_mod.typing("Welcome to Rock, Paper, Scissors!")
sleep(1)
str_mod.typing('Get ready to play against the bot!')
sleep(1)

while True:
    user_choice = str_mod.typing_input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ")

    if user_choice == 'quit':
        str_mod.typing("Thanks for playing! Goodbye!")
        str_mod.typing(f"Your final score was: {score}")
        str_mod.typing(f"Total tries: {tries}")
        sys.exit()

    if user_choice not in choices:
        str_mod.typing("Invalid choice. Please try again.")
        continue

    if tries == 0:
        bot_choice = choices[randint(0, 2)]
    else:
        bot_choice = logic(user_choice, bot_choice)

    str_mod.typing(f"The bot chose: {bot_choice}")

    if user_choice == bot_choice:
        Bot_Wins = None
        Player_Wins = None
        str_mod.typing("It's a tie!")
        sleep(1)
        str_mod.typing("Let's play again!")
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        str_mod.typing("You win!")
        Player_Wins = True
        Bot_Wins = False
        score += 1
    else:
        str_mod.typing("Bot wins!")
        Bot_Wins = True
        Player_Wins = False

    tries += 1

    play_again = str_mod.typing_input("Do you want to carry on? (yes/no): ").lower()
    if play_again != 'yes':
        str_mod.typing("Thanks for playing! Goodbye!")
        str_mod.typing(f"Your final score was: {score}")
        str_mod.typing(f"Total tries: {tries}")
        sys.exit()
