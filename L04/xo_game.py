# ARMSTRONG CF-4 L04 - XO Game: Windows, Buttons and Turns
# The program at the end of L04, as Eng. Mazen Nasr builds it: a 3x3 window of buttons,
# one function per button, and the turns (X, then O). Winner, draw, Play Again and the score come in L05.

from tkinter import *
from tkinter import messagebox

player = "X"


def click(row, col):
    global player

    if player == 'X' and game_map[row][col] == '':
        buttons[row][col].configure(text="X")
        game_map[row][col] = "X"
        player = "O"
    elif player == 'O' and game_map[row][col] == '':
        buttons[row][col].configure(text="O")
        game_map[row][col] = "O"
        player = "X"


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

# Buttons
buttons = [
    [Button(root, command=b1), Button(root, command=b2), Button(root, command=b3)],
    [Button(root, command=b4), Button(root, command=b5), Button(root, command=b6)],
    [Button(root, command=b7), Button(root, command=b8), Button(root, command=b9)]
]

for i in range(3):
    for j in range(3):
        buttons[i][j].configure(height=4, width=8, font=("Helvetica", "28"))
        buttons[i][j].grid(row=i, column=j)

mainloop()
