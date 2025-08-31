import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Game state
player_score = 0
computer_score = 0
rounds_history = []
round_number = 1


def computer_choice():
    return random.choice(choices)


def play(choice):
    global player_score, computer_score, rounds_history, round_number

    comp = computer_choice()
    result = ""

    if choice == comp:
        result = f"Round {round_number}: Both chose {choice}. It's a Tie!"
    elif (choice == "Rock" and comp == "Scissors") or \
         (choice == "Paper" and comp == "Rock") or \
         (choice == "Scissors" and comp == "Paper"):
        player_score += 1
        result = f"Round {round_number}: You Win! {choice} beats {comp}"
    else:
        computer_score += 1
        result = f"Round {round_number}: You Lose! {comp} beats {choice}"

    rounds_history.append(result)
    round_number += 1
    update_display(result)


def update_display(result):
    result_label.config(text=result)
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}")

    history_text.delete(1.0, tk.END)
    for i, round_result in enumerate(rounds_history[-5:], start=1):  # Show last 5 rounds
        history_text.insert(tk.END, f"{round_result}\n")


def reset_game():
    global player_score, computer_score, rounds_history, round_number
    player_score = 0
    computer_score = 0
    rounds_history = []
    round_number = 1
    result_label.config(text="Game reset! Starting at Round 1.")
    score_label.config(text="Player: 0 | Computer: 0")
    history_text.delete(1.0, tk.END)


# Tkinter window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("550x450")
root.config(bg="#090909")  # Dark background

# Title
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 22, "bold"), fg="#f5c542", bg="#1e1e2e")
title_label.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Starting at Round 1", font=("Arial", 14, "bold"), fg="#ffffff", bg="#1e1e2e")
result_label.pack(pady=10)

# Score display
score_label = tk.Label(root, text="Player: 0 | Computer: 0", font=("Arial", 13, "bold"), fg="#42f57b", bg="#1e1e2e")
score_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#000000")
button_frame.pack(pady=15)

btn_style = {"font": ("Arial", 12, "bold"), "width": 12, "height": 2, "bd": 0}

rock_btn = tk.Button(button_frame, text="Rock", **btn_style, bg="#ff6b6b", fg="white", command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", **btn_style, bg="#4d96ff", fg="white", command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", **btn_style, bg="#6bcf63", fg="white", command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# History display
history_label = tk.Label(root, text="Game History (last 5 rounds):", font=("Arial", 12, "bold"), fg="#f5c542", bg="#1e1e2e")
history_label.pack(pady=5)

history_text = tk.Text(root, height=7, width=60, font=("Arial", 10), bg="#060505", fg="#ffffff")
history_text.pack(pady=5)

# Reset and Exit buttons
control_frame = tk.Frame(root, bg="#B4B4B9")
control_frame.pack(pady=10)

reset_btn = tk.Button(control_frame, text="Reset Game", font=("Arial", 12, "bold"), bg="#ffaa33", fg="black", command=reset_game)
reset_btn.grid(row=0, column=0, padx=15)

exit_btn = tk.Button(control_frame, text="Exit", font=("Arial", 12, "bold"), bg="#ff3333", fg="white", command=root.quit)
exit_btn.grid(row=0, column=1, padx=15)

# Run window
root.mainloop()
