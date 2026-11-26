from tkinter import *
from tkinter import messagebox
import random

level = 1
if level < 1 or level > 3:
    exit()

dimension = 0
number_of_blocks = 0
number_of_mines = 0
number_of_discovered = 0

mines_map = []
discovered_map = []

on_game = True
first_click = True

bs = 0


def prepare():
    global dimension, number_of_blocks, number_of_mines, number_of_discovered, mines_map, \
        discovered_map, on_game, first_click, bs
    dimension = level * 8
    number_of_blocks = dimension ** 2
    number_of_mines = number_of_blocks / 4
    number_of_discovered = 0

    mines_map = []
    for i in range(dimension):
        temp_list = []
        for j in range(dimension):
            temp_list.append('')
        mines_map.append(temp_list.copy())

    discovered_map = []
    for i in range(dimension):
        temp_list = []
        for j in range(dimension):
            temp_list.append('')
        discovered_map.append(temp_list.copy())

    on_game = True
    first_click = True

    bs = int(72 / level)


def render():
    for i in range(dimension):
        for j in range(dimension):
            base.create_rectangle(j * bs + 2, i * bs, j * bs + bs, i * bs + bs, fill="lavender")


def on_click(event):
    global first_click

    row = event.y // bs
    col = event.x // bs

    if on_game:
        if first_click:
            first_click = False
            # set mines in random places except the block i have just clicked on
            mines_counter = 0
            while mines_counter < number_of_mines:
                x, y = random.randint(0, dimension - 1), random.randint(0, dimension - 1)
                if x != row and y != col and mines_map[x][y] == '':
                    mines_map[x][y] = '*'
                    mines_counter += 1
            # fill numbers around mines
            for i in range(dimension):
                for j in range(dimension):
                    if mines_map[i][j] == '':
                        sum_of_mines = 0
                        for x in range(i - 1, i + 2):
                            for y in range(j - 1, j + 2):
                                if 0 <= x < dimension and 0 <= y < dimension and mines_map[x][y] == '*':
                                    sum_of_mines += 1
                        mines_map[i][j] = sum_of_mines
            # discover some blocks for the user to start playing from
            for i in range(row - level, row + level + 1):
                for j in range(col - level, col + level + 1):
                    if 0 <= i < dimension and 0 <= j < dimension and mines_map[i][j] != '*':
                        discovered_map[i][j] = 1


root = Tk()
root.title("Minesweeper")
prepare()

base = Canvas(root, width=576, height=576)
base.pack()
base.bind("<Button>", on_click)

render()

root.mainloop()
