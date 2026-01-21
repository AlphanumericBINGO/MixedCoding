import tkinter as tk
import time
from random import uniform
import json
import sys

root = tk.Tk()
root.title("Reaction tester")
root.geometry("1200x800")
root.configure(bg="black")

score = 0
waiting = False
start_time = 0
reaction_time = 0

# -----------------------------
# UI SETUP
# -----------------------------
label = tk.Label(root,
                 text="Hit the button as soon as it turns green!",
                 font=("Helvetica", 36),
                 bg="black",
                 fg="white")
label.pack(pady=20)

button = tk.Button(root,
                   text="Wait for green...",
                   font=("Helvetica", 48),
                   bg="red",
                   fg="white")
button.pack(pady=20)

# Name entry
name_entry = tk.Entry(root, font=("Helvetica", 24))
name_entry.pack()
name_entry.insert(0, "Enter your name")

# -----------------------------
# SAVE SCORE TO JSON
# -----------------------------
def save_score(name, score, reaction_time):
    data = {
        "name": name,
        "score": score,
        "reaction_time_ms": reaction_time
    }

    try:
        with open("scores.json", "r") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = []

    scores.append(data)

    with open("scores.json", "w") as f:
        json.dump(scores, f, indent=4)

# -----------------------------
# CLEAR JSON FILE
# -----------------------------
def clear_json_file():
    with open("scores.json", "w") as f:
        f.write("[]")
    label.config(text="Scores cleared!")

# -----------------------------
# SHOW FASTEST TIMES
# -----------------------------
def show_fastest_times():
    try:
        with open("scores.json", "r") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = []

    # Sort by fastest reaction time
    scores = sorted(scores, key=lambda x: x["reaction_time_ms"])

    # Popup window
    top = tk.Toplevel(root)
    top.title("Fastest Reaction Times")
    top.geometry("600x500")
    top.configure(bg="black")

    tk.Label(top, text="Fastest Reaction Times",
             font=("Helvetica", 32),
             bg="black", fg="white").pack(pady=20)

    # Show top 5
    for entry in scores[:5]:
        tk.Label(top,
                 text=f"{entry['name']} — {entry['reaction_time_ms']} ms",
                 font=("Helvetica", 24),
                 bg="black",
                 fg="white").pack(pady=10)

# -----------------------------
# TURN BUTTON GREEN
# -----------------------------
def start_wait():
    global waiting
    waiting = True
    delay = int(uniform(1000, 3000))
    root.after(delay, turn_green)

def turn_green():
    global waiting, start_time
    waiting = False
    start_time = time.time()
    button.config(bg="green", text="CLICK!")

# -----------------------------
# HANDLE BUTTON CLICK
# -----------------------------
X = []
def on_button_click():

    global score, waiting, reaction_time

    if waiting:
        label.config(text="Too soon! Wait for green.")
        X.append('Spear')
        if len(X) == 3:
            sys.exit()
        return

    if button['bg'] == "green":
        score += 1
        reaction_time = (time.time() - start_time) * 1000

        label.config(text=f"Score: {score} | Time: {int(reaction_time)} ms")

        # Save score
        player_name = name_entry.get()
        save_score(player_name, score, int(reaction_time))

        # Reset button
        button.config(bg="red", text="Wait for green...")
       

        start_wait()

button.config(command=on_button_click)

# -----------------------------
# EXTRA BUTTONS
# -----------------------------
leaderboard_btn = tk.Button(root,
                            text="Show Fastest Times",
                            font=("Helvetica", 32),
                            bg="blue",
                            fg="white",
                            command=show_fastest_times)
leaderboard_btn.pack(pady=20)

clear_btn = tk.Button(root,
                      text="Clear Scores",
                      font=("Helvetica", 32),
                      bg="red",
                      fg="white",
                      command=clear_json_file)
clear_btn.pack(pady=20)

# Start game
start_wait()
root.mainloop()
