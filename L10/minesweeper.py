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
            temp_list.append(0)
        discovered_map.append(temp_list.copy())

    on_game = True
    first_click = True

    bs = int(72 / level)


def show_block(i, j):
    base.create_rectangle(j * bs + 2, i * bs + 2, j * bs + bs, i * bs + bs, fill="white")
    base.create_text(j * bs + int(bs / 2), i * bs + int(bs / 2), font="Arial " + str(int(bs / 2)), text=mines_map[i][j])


def render():
    base.create_rectangle(0, 0, 576, 576, fill="white")
    for i in range(dimension):
        for j in range(dimension):
            base.create_rectangle(j * bs + 2, i * bs + 2, j * bs + bs, i * bs + bs, fill="lavender")
            if discovered_map[i][j]:
                show_block(i, j)


def count_discovered():
    global number_of_discovered
    number_of_discovered = 0
    for iterator in discovered_map:
        number_of_discovered += sum(iterator)
    discovered_label.configure(text="Discovered Blocks: " + str(number_of_discovered) + ' / ' + str(
        int(number_of_blocks - number_of_mines)))


def on_click(event):
    global first_click, on_game

    row = event.y // bs
    col = event.x // bs

    if on_game:
        if first_click:
            first_click = False
            # set mines in random places except the block I have just clicked on
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
            render()
            count_discovered()
        else:
            discovered_map[row][col] = 1
            render()

            # Check if mine
            if mines_map[row][col] == '*':
                for i in range(dimension):
                    for j in range(dimension):
                        if mines_map[i][j] == '*':
                            discovered_map[i][j] = 1
                render()
                on_game = False
                messagebox.showinfo("Lose", "You have Lost, You can try again")
            else:
                count_discovered()
                if number_of_discovered == number_of_blocks - number_of_mines:
                    messagebox.showinfo("Winning", "Congratulations !! you have won !!")
                    next_level()


def prev_level():
    global level
    if level > 1:
        level -= 1
        prepare()
        mines_label.configure(text="Num of Mines: " + str(int(number_of_mines)) + ' / ' + str(number_of_blocks))
        level_label.configure(text="Level " + str(level) + ' (' + str(dimension) + '*' + str(dimension) + ')')
        discovered_label.configure(text="Discovered Blocks: " + str(number_of_discovered) + ' / ' + str(
            int(number_of_blocks - number_of_mines)))
        render()


def next_level():
    global level
    if level < 3:
        level += 1
        prepare()
        mines_label.configure(text="Num of Mines: " + str(int(number_of_mines)) + ' / ' + str(number_of_blocks))
        level_label.configure(text="Level " + str(level) + ' (' + str(dimension) + '*' + str(dimension) + ')')
        discovered_label.configure(text="Discovered Blocks: " + str(number_of_discovered) + ' / ' + str(
            int(number_of_blocks - number_of_mines)))
        render()


def play_again():
    prepare()
    count_discovered()
    render()


root = Tk()
root.title("Minesweeper")
prepare()

top = Frame(root)
top.pack(side=TOP, fill=X)

mines_label = Label(top, text="Num of Mines: " + str(int(number_of_mines)) + ' / ' + str(number_of_blocks),
                    font=("Helvetica", "10"))
mines_label.pack(side=LEFT, expand=True)

level_label = Label(top, text="Level " + str(level) + ' (' + str(dimension) + '*' + str(dimension) + ')',
                    font=("Helvetica", "10"))
level_label.pack(side=LEFT, expand=True)

discovered_label = Label(top, text="Discovered Blocks: " + str(number_of_discovered) + ' / ' + str(
    int(number_of_blocks - number_of_mines)),
                         font=("Helvetica", "10"))
discovered_label.pack(side=LEFT, expand=True)

base = Canvas(root, width=576, height=576)
base.pack()
base.bind("<Button>", on_click)
render()

bottom = Frame(root)
bottom.pack(side=BOTTOM, fill=X)

backward = Button(bottom, text='<', font=("Helvetica", "10"), command=prev_level)
backward.pack(side=LEFT, expand=True)

again = Button(bottom, text='Play Again', font=("Helvetica", "10"), command=play_again)
again.pack(side=LEFT, expand=True)

forward = Button(bottom, text='>', font=("Helvetica", "10"), command=next_level)
forward.pack(side=LEFT, expand=True)

root.mainloop()
