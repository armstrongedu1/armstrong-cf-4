# ARMSTRONG CF-4 L04 + L05 - XO Game (tic-tac-toe) with tkinter
# The finished program from the lesson videos, as Eng. Mazen Nasr builds it:
# L04: the window, the 3x3 buttons, one function per button and the turns (X then O);
# L05: the winner (rows, columns, diagonals), the draw, Play Again and the score labels.

from tkinter import *
from tkinter import messagebox

player = "X"
on_game = True

x_score, o_score = 0, 0


def winner(symbol):
    global x_score, o_score, on_game

    if symbol == "X":
        x_score += 1
        x_label.configure(text="Player x : " + str(x_score))
    elif symbol == "O":
        o_score += 1
        o_label.configure(text="Player O : " + str(o_score))

    on_game = False
    messagebox.showinfo("Winner", "Player " + symbol + " Won")


def play_again():
    global on_game

    on_game = True
    for r in range(3):
        for c in range(3):
            buttons[r][c].configure(text="")
            game_map[r][c] = ''


def check_draw():
    global on_game
    draw = True
    for iterator in game_map:
        if '' in iterator:
            draw = False

    if draw:
        messagebox.showinfo("Draw", "No Winner")
        on_game = False


def check_win():
    global on_game

    for row in range(3):
        if game_map[row][0] == game_map[row][1] == game_map[row][2] != '':
            winner(game_map[row][1])
            return
    for col in range(3):
        if game_map[0][col] == game_map[1][col] == game_map[2][col] != '':
            winner(game_map[0][col])
            return
    if game_map[0][0] == game_map[1][1] == game_map[2][2] != '':
        winner(game_map[0][0])
        return
    if game_map[0][2] == game_map[1][1] == game_map[2][0] != '':
        winner(game_map[0][2])
        return
    check_draw()


def click(row, col):
    global player, on_game

    if on_game:
        if player == 'X' and game_map[row][col] == '':
            buttons[row][col].configure(text="X")
            game_map[row][col] = "X"
            player = "O"
            player_turn.configure(text="Player " + player)
        elif player == 'O' and game_map[row][col] == '':
            buttons[row][col].configure(text="O")
            game_map[row][col] = "O"
            player = "X"
            player_turn.configure(text="Player " + player)

        check_win()


def b1():
    click(0, 0)


def b2():
    click(0, 1)


def b3():
    click(0, 2)


def b4():
    click(1, 0)


def b5():
    click(1, 1)


def b6():
    click(1, 2)


def b7():
    click(2, 0)


def b8():
    click(2, 1)


def b9():
    click(2, 2)


game_map = [['', '', ''],
            ['', '', ''],
            ['', '', '']]

# Create window
root = Tk()
root.title("X-O Game")

# Label
player_turn = Label(root, text="Player " + player, font=("Helvetica", "28"))
player_turn.grid(row=0, column=1)

x_label = Label(root, text="Player x : 0", font=("Helvetica", "22"))
x_label.grid(row=4, column=0)

o_label = Label(root, text="Player O : 0", font=("Helvetica", "22"))
o_label.grid(row=4, column=2)

# Buttons
buttons = [
    [Button(root, command=b1), Button(root, command=b2), Button(root, command=b3)],
    [Button(root, command=b4), Button(root, command=b5), Button(root, command=b6)],
    [Button(root, command=b7), Button(root, command=b8), Button(root, command=b9)]
]

for i in range(3):
    for j in range(3):
        buttons[i][j].configure(height=4, width=8, font=("Helvetica", "28"))
        buttons[i][j].grid(row=i + 1, column=j)

again = Button(root, height=1, width=8, font=("Helvetica", "28"), text="Play Again", command=play_again)
again.grid(row=4, column=1)

mainloop()
