import tkinter as tk
from random import randint

player_score = 0
bot_score = 0
past_user_choices = []
past_bot_choices = []
Player_Wins = None
Bot_Wins = None
user_choice = None
bot_choice = None
rounds_played = 0
darkmode = False   # <-- ADDED

root = tk.Tk()
root.geometry('1200x800')
root.configure(bg='black')
root.title('Rock, Paper, Scissors')

CHOICES = ['rock', 'paper', 'scissors']

# -----------------------------
# DARK MODE SYSTEM (INSERTED)
# -----------------------------
def apply_theme():
    if darkmode:
        bg = "black"
        fg = "white"
        btn_bg = "gray25"
    else:
        bg = "white"
        fg = "black"
        btn_bg = "lightgray"

    # Window background
    root.config(bg=bg)

    # Update main label
    label.config(bg=bg, fg=fg)

    # Update score labels
    label_bot_score.config(bg=bg, fg=fg)
    label_player_score.config(bg=bg, fg=fg)
    label_rounds_played.config(bg=bg, fg=fg)

    # Update dark mode button
    btn_darkmode.config(bg=btn_bg, fg=fg)

    # Update RPS buttons
    but_rock.config(bg=btn_bg, fg=fg)
    but_paper.config(bg=btn_bg, fg=fg)
    but_scissors.config(bg=btn_bg, fg=fg)

def toggle_darkmode():
    global darkmode
    darkmode = not darkmode
    btn_darkmode.config(text=f"Dark Mode: {'ON' if darkmode else 'OFF'}")
    apply_theme()

btn_darkmode = tk.Button(root, text="Dark Mode: OFF", font=("Arial", 12),
                         command=toggle_darkmode, fg="white", bg="darkblue")
btn_darkmode.place(x=300, y=50)

# -----------------------------
# MAIN LABEL
# -----------------------------
label = tk.Label(root, text="Rock, Paper, Scissors!", fg='lightblue',
                 bg='black', font=('Helvetica', 24))
label.pack(pady=20)

# -----------------------------
# SCORE LABELS
# -----------------------------
label_bot_score = tk.Label(root, text="Bot Score: 0", fg='white',
                           bg='black', font=('Helvetica', 18))
label_bot_score.pack(pady=10)

label_player_score = tk.Label(root, text="Player Score: 0", fg='white',
                              bg='black', font=('Helvetica', 18))
label_player_score.pack(pady=10)

label_rounds_played = tk.Label(root, text="Rounds Played: 0", fg='white',
                               bg='black', font=('Helvetica', 18))
label_rounds_played.pack(pady=10)

# -----------------------------
# BUTTON COMMANDS
# -----------------------------
def rock_command():
    choose("rock")

def paper_command():
    choose("paper")

def scissors_command():
    choose("scissors")

def choose(choice):
    global user_choice
    user_choice = choice
    past_user_choices.append(choice)
    play_game()

# -----------------------------
# BOT LOGIC
# -----------------------------
def logic(user_choice):
    global Player_Wins, Bot_Wins

    if Player_Wins:
        return {"rock": "paper", "paper": "scissors", "scissors": "rock"}[user_choice]

    if Bot_Wins:
        return {"rock": "scissors", "paper": "rock", "scissors": "paper"}[user_choice]

    return CHOICES[randint(0, 2)]

# -----------------------------
# MAIN GAME FUNCTION
# -----------------------------
def play_game():
    global user_choice, bot_choice, Player_Wins, Bot_Wins
    global player_score, bot_score, rounds_played

    if user_choice is None:
        return

    bot_choice = logic(user_choice)
    past_bot_choices.append(bot_choice)

    result = f"The bot chose: {bot_choice}\n"

    if user_choice == bot_choice:
        Player_Wins = None
        Bot_Wins = None
        result += "It's a tie!"
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        Player_Wins = True
        Bot_Wins = False
        player_score += 1
        result += "You win!"
    else:
        Player_Wins = False
        Bot_Wins = True
        bot_score += 1
        result += "Bot wins!"

    rounds_played += 1

    # UPDATE LABELS
    label.config(text=result)
    label_bot_score.config(text=f"Bot Score: {bot_score}")
    label_player_score.config(text=f"Player Score: {player_score}")
    label_rounds_played.config(text=f"Rounds Played: {rounds_played}")

# -----------------------------
# BUTTONS (REFERENCES SAVED)
# -----------------------------
but_rock = tk.Button(root, text="Rock", fg='green', bg='lightblue',
                     font=('Helvetica', 18), command=rock_command)
but_rock.pack(pady=10)

but_paper = tk.Button(root, text="Paper", fg='blue', bg='lightblue',
                      font=('Helvetica', 18), command=paper_command)
but_paper.pack(pady=10)

but_scissors = tk.Button(root, text="Scissors", fg='red', bg='lightblue',
                         font=('Helvetica', 18), command=scissors_command)
but_scissors.pack(pady=10)

root.mainloop()
