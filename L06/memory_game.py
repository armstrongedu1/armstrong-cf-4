from tkinter import *
import random

level = 4
rows, cols = 0, 0


def prepare():
    global rows, cols, level

    if level < 1 or level > 8:
        exit()
    elif level < 6:
        rows, cols = level, 6
    else:
        rows, cols = 6, level

    shapes = ['triangle', 'rectangle', 'pentagon', 'hexagon', 'circle']
    colors = ['red', 'green', 'blue', 'orange', 'black']

    # mix shapes with colors
    shapes_with_colors = []
    for s in shapes:
        for c in colors:
            shapes_with_colors.append([s, c])
    random.shuffle(shapes_with_colors)

    # create the list of cards
    temp_cards = []
    for i in range(level * 3):
        temp_cards.append(shapes_with_colors[i])
    temp_cards = temp_cards * 2
    random.shuffle(temp_cards)

    # create the 2D list of cards
    cards = []
    for i in range(0, len(temp_cards), cols):
        temp_list = []
        for j in range(i, i + cols):
            temp_list.append(temp_cards[j])
        cards.append(temp_list.copy())

    # 2D list same dimension as the card list indicating which cards have been already solved
    solved_map = []
    for i in range(rows):
        temp_list = []
        for j in range(cols):
            temp_list.append(0)
        solved_map.append(temp_list.copy())



prepare()

root = Tk()
root.title("Memory Game")

base = Canvas(root, width=cols * 70 - 2, height=rows * 70 - 2)
base.pack()

for y in range(rows):
    for x in range(cols):
        base.create_rectangle(x * 70, y * 70, x * 70 + 70, y * 70 + 70, fill="lavender")

root.mainloop()
