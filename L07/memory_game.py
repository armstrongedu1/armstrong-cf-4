from tkinter import *
import random
from tkinter import messagebox

level = 1
rows, cols = 0, 0
cards = []
solved_map = []
previous = []
previous_location = []


def check_win():
    for iterator in solved_map:
        if 0 in iterator:
            return
    messagebox.showinfo("Win", "You Have Won")
    level_up()


def render():
    for y in range(rows):
        for x in range(cols):
            base.create_rectangle(x * 70, y * 70, x * 70 + 70, y * 70 + 70, fill="lavender")
            if solved_map[y][x]:
                show_card(y, x)


def show_card(row, col):
    shape, color = cards[row][col]

    row *= 70
    col *= 70

    if shape == 'triangle':
        base.create_polygon([col + 35, row + 10,
                             col + 10, row + 60,
                             col + 60, row + 60], fill=color)
    elif shape == 'rectangle':
        base.create_rectangle([col + 10, row + 10,
                               col + 60, row + 60], fill=color)
    elif shape == 'pentagon':
        base.create_polygon([col + 35, row + 10,
                             col + 10, row + 35,
                             col + 22, row + 60,
                             col + 48, row + 60,
                             col + 60, row + 35], fill=color)
    elif shape == 'hexagon':
        base.create_polygon([col + 23, row + 10,
                             col + 10, row + 35,
                             col + 23, row + 60,
                             col + 47, row + 60,
                             col + 60, row + 35,
                             col + 47, row + 10], fill=color)
    elif shape == 'circle':
        base.create_oval([col + 10, row + 10,
                          col + 60, row + 60], fill=color)


def on_click(event):
    global previous, previous_location
    row = event.y // 70
    col = event.x // 70

    show_card(row, col)

    if not solved_map[row][col]:
        if not previous and not previous_location:
            previous = cards[row][col]
            previous_location = [row, col]
        elif cards[row][col] == previous and previous_location != [row, col]:
            solved_map[row][col] = 1
            solved_map[previous_location[0]][previous_location[1]] = 1
            previous = []
            previous_location = []
            check_win()
        else:
            render()
            show_card(row, col)
            previous = cards[row][col]
            previous_location = [row, col]


def prepare():
    global rows, cols, level, cards, solved_map

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


def level_up():
    global level, rows, cols, base, label

    if level < 8:
        level += 1

        prepare()
        base.config(width=cols * 70 - 2, height=rows * 70 - 2)
        label.config(text="Level " + str(level))
        render()


def level_down():
    global level, rows, cols, base, label

    if level > 1:
        level -= 1

        prepare()
        base.config(width=cols * 70 - 2, height=rows * 70 - 2)
        label.config(text="Level " + str(level))
        render()


prepare()

root = Tk()
root.title("Memory Game")

base = Canvas(root, width=cols * 70 - 2, height=rows * 70 - 2)
base.pack()
base.bind("<Button>", on_click)

render()

backward = Button(root, text="<", font=("Arial", "20"), command=level_down)
backward.pack(side=LEFT)

label = Label(root, text="Level " + str(level), font=("Arial", "20"))
label.pack(side=LEFT, expand=True)

forward = Button(root, text=">", font=("Arial", "20"), command=level_up)
forward.pack(side=LEFT)

root.mainloop()
