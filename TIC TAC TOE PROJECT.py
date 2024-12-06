import tkinter as tk
import random

# Fun messages for winning
WIN_MESSAGES = ["Brilliant Move!", "Victory!", "Well Played!", "You're a Star!", "Amazing!"]

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and not game_ended:
        buttons[row][column]['text'] = player
        buttons[row][column].config(fg="#0A1533" if player == "X" else "#960018")
        if not check_winner():
            if not check_tie():
                player = players[1] if player == players[0] else players[0]
                label.config(text=f"{player}'s Turn", fg="#0A1533" if player == "X" else "#960018")
            else:
                label.config(text="It's a Tie!", fg="#2B1B2D")
                scores["Tie"] += 1
                update_scoreboard()
                play_again_button.pack()
        else:
            win_message = random.choice(WIN_MESSAGES)
            label.config(text=f"{player} Wins! {win_message}", fg="#2B1B2D")
            scores[player] += 1
            update_scoreboard()
            play_again_button.pack()

def check_winner():
    global game_ended
    for win_condition in win_conditions:
        a, b, c = win_condition
        if buttons[a[0]][a[1]]['text'] == buttons[b[0]][b[1]]['text'] == buttons[c[0]][c[1]]['text'] != "":
            for i, j in win_condition:
                buttons[i][j].config(bg="#960018" if player == "X" else "#0A1533")
            game_ended = True
            return True
    return False

def check_tie():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return False
    global game_ended
    game_ended = True
    return True

def play_again():
    global player, game_ended
    player = random.choice(players)
    game_ended = False
    label.config(text=f"{player}'s Turn", fg="#0A1533" if player == "X" else "#960018")
    for row in buttons:
        for button in row:
            button.config(text="", bg="#F1EFD0")
    play_again_button.pack_forget()

def update_scoreboard():
    scoreboard_label.config(
        text=f"🎉 Victories of X: {scores['X']}   🎉 Victories of O: {scores['O']}   🤝 Ties: {scores['Tie']}",
        fg="white")

window = tk.Tk()
window.title("Tic Tac Toe - Fun Edition")
window.configure(bg="#D9CBD6")

players = ["X", "O"]
player = random.choice(players)
game_ended = False

buttons = [[None for _ in range(3)] for _ in range(3)]
win_conditions = [
    ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))
]

scores = {"X": 0, "O": 0, "Tie": 0}

label = tk.Label(text=f"{player}'s Turn", font=('Arial', 24, 'bold'), bg="#D9CBD6", fg="#0A1533")
label.pack()

scoreboard_label = tk.Label(
    text="🎉 Victories of X: 0   🎉 Victories of O: 0   🤝 Ties: 0", font=('Arial', 20, 'bold'),
    bg="#2B1B2D", fg="white")
scoreboard_label.pack()

frame = tk.Frame(window, bg="#D9CBD6")
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(frame, text="", font=('Arial', 40, 'bold'), width=5, height=2,
                                      bg="#F1EFD0", command=lambda r=row, c=col: next_turn(r, c))
        buttons[row][col].grid(row=row, column=col)

play_again_button = tk.Button(window, text="Play Again", font=('Arial', 16, 'bold'),
                              bg="#0A1533", fg="white", command=play_again)
play_again_button.pack_forget()

window.mainloop()
