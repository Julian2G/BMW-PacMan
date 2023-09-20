import tkinter as tk
import random

map = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
map[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
map[1] = [0,2,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,2,2,2,2,2,0]
map[2] = [0,3,0,0,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,0,0,2,0,0,0,0,3,0]
map[3] = [0,2,0,0,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,0,0,2,0,0,0,0,2,0]
map[4] = [0,2,0,0,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,0,0,2,0,0,0,0,2,0]
map[5] = [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0]
map[6] = [0,2,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,2,0]
map[7] = [0,2,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,2,0]
map[8] = [0,2,2,2,2,2,2,0,0,2,2,2,2,0,0,2,2,2,2,0,0,2,2,2,2,2,2,0]
map[9] = [0,0,0,0,0,0,2,0,0,0,0,0,1,0,0,1,0,0,0,0,0,2,0,0,0,0,0,0]
map[10] = [-1,-1,-1,-1,-1,0,2,0,0,0,0,0,1,0,0,1,0,0,0,0,0,2,0,-1,-1,-1,-1,-1]
map[11] = [-1,-1,-1,-1,-1,0,2,0,0,1,1,1,1,1,1,1,1,1,1,0,0,2,0,-1,-1,-1,-1,-1]
map[12] = [-1,-1,-1,-1,-1,0,2,0,0,1,0,0,0,1,1,0,0,0,1,0,0,2,0,-1,-1,-1,-1,-1]
map[13] = [0,0,0,0,0,0,2,0,0,1,0,6,-1,-1,-1,-1,9,0,1,0,0,2,0,0,0,0,0,0]
map[14] = [1,1,1,1,1,1,2,1,1,1,0,-1,-1,-1,-1,-1,-1,0,1,1,1,2,1,1,1,1,1,1]
map[15] = [0,0,0,0,0,0,2,0,0,1,0,7,-1,-1,-1,-1,8,0,1,0,0,2,0,0,0,0,0,0]
map[16] = [-1,-1,-1,-1,-1,0,2,0,0,1,0,0,0,0,0,0,0,0,1,0,0,2,0,-1,-1,-1,-1,-1]
map[17] = [-1,-1,-1,-1,-1,0,2,0,0,1,1,1,1,1,5,1,1,1,1,0,0,2,0,-1,-1,-1,-1,-1]
map[18] = [-1,-1,-1,-1,-1,0,2,0,0,1,0,0,0,0,0,0,0,0,1,0,0,2,0,-1,-1,-1,-1,-1]
map[19] = [0,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0,0]
map[20] = [0,2,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,2,2,2,2,2,0]
map[21] = [0,2,0,0,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,0,0,2,0,0,0,0,2,0]
map[22] = [0,2,0,0,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,0,0,2,0,0,0,0,2,0]
map[23] = [0,2,2,2,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2,0]
map[24] = [0,0,0,2,0,0,2,0,0,2,0,0,0,0,0,0,0,0,2,0,0,2,0,0,2,0,0,0]
map[25] = [0,0,0,2,0,0,2,0,0,2,0,0,0,0,0,0,0,0,2,0,0,2,0,0,2,0,0,0]
map[26] = [0,2,2,2,2,2,2,0,0,2,2,2,2,0,0,2,2,2,2,0,0,2,2,2,2,2,2,0]
map[27] = [0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0]
map[28] = [0,3,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0]
map[29] = [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0]
map[30] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Wall: 0
# Leere Fläche: 1
# Mit Punkt: 2
# Mit Münze: 3
# Leere Fläche außerhalb der Map: -1
# Geist: Pinky: 6 Clyde: 7 Inky: 8 Blinky: 9 wenn blau: 10,11,12,13
# Pacman: 5

score = 0
counter = 0
ghost_vulnerability = 0
eaten_coins = 0
pacman_direction = 0
pacman_x = 14
pacman_y = 17
cache_pinky = -1
cache_clyde = -1
cache_inky = -1
cache_blinky = -1


new_map = map.copy()
for x in range(len(new_map)):
    new_map[x] = map[x].copy()

window = tk.Tk()
window.geometry('%dx%d+%d+%d' % (560, 640, 360, 40))

def initialize_gui():
    label1 = tk.Label(window, height=1, width=79, background="green", text='Score: 0')
    label1.grid(row=0, columnspan=28)
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 0:
                frame1 = tk.Frame(window, height=20, width=20, background="blue4")
                frame1.grid(row=x+1, column=y)
            elif map[x][y] == 1 or map[x][y] == -1:
                frame1 = tk.Frame(window, height=20, width=20, background="black")
                frame1.grid(row=x+1, column=y)
            elif map[x][y] == 2:
                dot = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                dot.create_oval(7, 7, 13, 13, fill="gold")
                dot.grid(row=x+1, column=y)
            elif map[x][y] == 3:
                dot = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                dot.create_oval(3, 3, 17, 17, fill="gold")
                dot.grid(row=x+1, column=y)
            elif map[x][y] == 5:
                dot = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                dot.create_oval(1, 1, 19, 19, fill="yellow")
                dot.grid(row=x+1, column=y)
            elif map[x][y] == 6:    #Pinky
                ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                ghost.create_oval(1, 1, 19, 19, fill="HotPink2")
                ghost.grid(row=x+1, column=y)
            elif map[x][y] == 7:    #Clyde
                ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                ghost.create_oval(1, 1, 19, 19, fill="dark orange")
                ghost.grid(row=x+1, column=y)
            elif map[x][y] == 8:    #Inky
                ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                ghost.create_oval(1, 1, 19, 19, fill="cyan")
                ghost.grid(row=x+1, column=y)
            elif map[x][y] == 9:    #Blinky
                ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                ghost.create_oval(1, 1, 19, 19, fill="red")
                ghost.grid(row=x+1, column=y)
def redraw():
    global map
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] != new_map[x][y]:
                if new_map[x][y] == 1 or new_map[x][y] == -1:
                    frame1 = tk.Frame(window, height=20, width=20, background="black")
                    frame1.grid(row=x+1, column=y)
                elif new_map[x][y] == 2:
                    dot = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    dot.create_oval(7, 7, 13, 13, fill="gold")
                    dot.grid(row=x+1, column=y)
                elif new_map[x][y] == 3:
                    dot = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    dot.create_oval(3, 3, 17, 17, fill="gold")
                    dot.grid(row=x+1, column=y)
                elif new_map[x][y] == 5:
                    dot = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    dot.create_oval(1, 1, 19, 19, fill="yellow")
                    dot.grid(row=x+1, column=y)
                elif new_map[x][y] == 6:
                    ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    ghost.create_oval(1, 1, 19, 19, fill="HotPink2")
                    ghost.grid(row=x + 1, column=y)
                elif new_map[x][y] == 7:
                    ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    ghost.create_oval(1, 1, 19, 19, fill="dark orange")
                    ghost.grid(row=x + 1, column=y)
                elif new_map[x][y] == 8:
                    ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    ghost.create_oval(1, 1, 19, 19, fill="cyan")
                    ghost.grid(row=x + 1, column=y)
                elif new_map[x][y] == 9:
                    ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    ghost.create_oval(1, 1, 19, 19, fill="red")
                    ghost.grid(row=x + 1, column=y)
                elif new_map[x][y] == 10:
                    ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    ghost.create_oval(1, 1, 19, 19, fill="blue2")
                    ghost.grid(row=x + 1, column=y)
                elif new_map[x][y] == 11:
                    ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    ghost.create_oval(1, 1, 19, 19, fill="blue2")
                    ghost.grid(row=x + 1, column=y)
                elif new_map[x][y] == 12:
                    ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    ghost.create_oval(1, 1, 19, 19, fill="blue2")
                    ghost.grid(row=x + 1, column=y)
                elif new_map[x][y] == 13:
                    ghost = tk.Canvas(window, height=20, width=20, background="black", highlightthickness=0)
                    ghost.create_oval(1, 1, 19, 19, fill="blue2")
                    ghost.grid(row=x + 1, column=y)
    for x in range(len(new_map)):
        map[x] = new_map[x].copy()
def move_pacman():
    global pacman_x
    global pacman_y
    global score
    global eaten_coins
    global ghost_vulnerability
    if pacman_direction == 1:
        if map[pacman_y - 1][pacman_x] > 0:
            new_map[pacman_y][pacman_x] = 1
            pacman_y -= 1
            new_map[pacman_y][pacman_x] = 5
            if map[pacman_y][pacman_x] == 2:
                score += 10
                eaten_coins += 1
            elif map[pacman_y][pacman_x] == 3:
                ghost_vulnerability = 40
            elif map[pacman_y][pacman_x] > 9:
                score += 200
                respawn_ghost(map[pacman_y][pacman_x])
            elif map[pacman_y][pacman_x] > 5:
                pacman_x = 0
    elif pacman_direction == 2:
        if map[pacman_y + 1][pacman_x] > 0:
            new_map[pacman_y][pacman_x] = 1
            pacman_y += 1
            new_map[pacman_y][pacman_x] = 5
            if map[pacman_y][pacman_x] == 2:
                score += 10
                eaten_coins += 1
            elif map[pacman_y][pacman_x] == 3:
                ghost_vulnerability = 40
            elif map[pacman_y][pacman_x] > 9:
                score += 200
                respawn_ghost(map[pacman_y][pacman_x])
            elif map[pacman_y][pacman_x] > 5:
                pacman_x = 0
    elif pacman_direction == 3:
        if map[pacman_y][pacman_x - 1] > 0:
            new_map[pacman_y][pacman_x] = 1
            pacman_x -= 1
            new_map[pacman_y][pacman_x] = 5
            if map[pacman_y][pacman_x] == 2:
                score += 10
                eaten_coins += 1
            elif map[pacman_y][pacman_x] == 3:
                ghost_vulnerability = 40
            elif map[pacman_y][pacman_x] > 9:
                score += 200
                respawn_ghost(map[pacman_y][pacman_x])
            elif map[pacman_y][pacman_x] > 5:
                pacman_x = 0

    elif pacman_direction == 4:
        if map[pacman_y][pacman_x + 1] > 0:
            new_map[pacman_y][pacman_x] = 1
            pacman_x += 1
            new_map[pacman_y][pacman_x] = 5
            if map[pacman_y][pacman_x] == 2:
                score += 10
                eaten_coins += 1
            elif map[pacman_y][pacman_x] == 3:
                ghost_vulnerability = 40
            elif map[pacman_y][pacman_x] > 9:
                score += 200
                respawn_ghost(map[pacman_y][pacman_x])
            elif map[pacman_y][pacman_x] > 5:
                pacman_x = 0
def respawn_ghost(ghost_value):
    print("Geist besiegt")
def move_ghost():
    global ghost_vulnerability
    if ghost_vulnerability > 0:
        ghost_vulnerability -= 1
        for x in range(len(map)):
            for y in range(len(map[x])):
                if map[x][y] == 6:
                    map[x][y] = 10
                elif map[x][y] == 7:
                    map[x][y] = 11
                elif map[x][y] == 8:
                    map[x][y] = 12
                elif map[x][y] == 9:
                    map[x][y] = 13
                if map[x][y] == 10 or map[x][y] == 11 or map[x][y] == 12 or map[x][y] == 13:
                    move_ghost_random(y, x)

    else:
        for x in range(len(map)):
            for y in range(len(map[x])):
                if map[x][y] == 10:
                    new_map[x][y] = 6
                    # move Methode einfügen
                elif map[x][y] == 11:
                    new_map[x][y] = 7
                    # move Methode einfügen
                elif map[x][y] == 12:
                    new_map[x][y] = 8
                    # move Methode einfügen
                elif map[x][y] == 13:
                    new_map[x][y] = 9
                if map[x][y] == 6 or map[x][y] == 7 or map[x][y] == 8 or map[x][y] == 9:
                    move_ghost_colored(y, x)
def move_ghost_colored(current_x, current_y):
    global new_map
    global cache_pinky
    global cache_clyde
    global cache_inky
    global cache_blinky
    global cache
    global pacman_x
    can_move = False
    direction = random.randint(1, 4)

    if direction == 1:
        if (map[current_y - 1][current_x] == -1 or 0 < map[current_y - 1][current_x] < 6) and new_map[current_y - 1][current_x] < 6:
            new_map[current_y - 1][current_x] = map[current_y][current_x]
            cache = map[current_y - 1][current_x]
            can_move = True
            if map[current_y - 1][current_x] == 5 or new_map[current_y - 1][current_x] == 5 or new_map[current_y][current_x] == 5:
                pacman_x = 0
        else: cache = map[current_y][current_x]
    elif direction == 2:
        if (map[current_y + 1][current_x] == -1 or 0 < map[current_y + 1][current_x] < 6) and new_map[current_y + 1][current_x] < 6:
            new_map[current_y + 1][current_x] = map[current_y][current_x]
            cache = map[current_y + 1][current_x]
            can_move = True
            if map[current_y + 1][current_x] == 5 or new_map[current_y + 1][current_x] == 5 or new_map[current_y][current_x] == 5:
                pacman_x = 0
        else: cache = map[current_y][current_x]
    elif direction == 3 and current_x != 0:
        if (map[current_y][current_x - 1] == -1 or 0 < map[current_y][current_x - 1] < 6) and new_map[current_y][current_x - 1] < 6:
            new_map[current_y][current_x - 1] = map[current_y][current_x]
            cache = map[current_y][current_x - 1]
            can_move = True
            if map[current_y][current_x - 1] == 5 or new_map[current_y][current_x - 1] == 5 or new_map[current_y][current_x] == 5:
                pacman_x = 0
        else: cache = map[current_y][current_x]
    elif direction == 4 and current_x != 27:
        if (map[current_y][current_x + 1] == -1 or 0 < map[current_y][current_x + 1] < 6) and new_map[current_y][current_x + 1] < 6:
            new_map[current_y][current_x + 1] = map[current_y][current_x]
            cache = map[current_y][current_x + 1]
            can_move = True
            if map[current_y][current_x + 1] == 5 or new_map[current_y][current_x + 1] == 5 or new_map[current_y][current_x] == 5:
                pacman_x = 0
        else: cache = map[current_y][current_x]

    if can_move:
        if map[current_y][current_x] == 6:
            new_map[current_y][current_x] = cache_pinky
            cache_pinky = cache
        elif map[current_y][current_x] == 7:
            new_map[current_y][current_x] = cache_clyde
            cache_clyde = cache
        elif map[current_y][current_x] == 8:
            new_map[current_y][current_x] = cache_inky
            cache_inky = cache
        elif map[current_y][current_x] == 9:
            new_map[current_y][current_x] = cache_blinky
            cache_blinky = cache
def move_ghost_random(current_x, current_y):
    global new_map
    global cache_pinky
    global cache_clyde
    global cache_inky
    global cache_blinky
    global cache
    can_move = False
    direction = random.randint(1, 4)

    if map[current_y][current_x] > 9 and new_map[current_y][current_x] != 5:
        if direction == 1:
            if map[current_y - 1][current_x] != 0 and map[current_y - 1][current_x] < 5 and new_map[current_y - 1][current_x] < 6:
                new_map[current_y - 1][current_x] = map[current_y][current_x]
                cache = map[current_y - 1][current_x]
                can_move = True
            else: cache = map[current_y][current_x]
        elif direction == 2:
            if map[current_y + 1][current_x] != 0 and map[current_y + 1][current_x] < 5 and new_map[current_y + 1][current_x] < 6:
                new_map[current_y + 1][current_x] = map[current_y][current_x]
                cache = map[current_y + 1][current_x]
                can_move = True
            else: cache = map[current_y][current_x]
        elif direction == 3 and current_x != 0:
            if map[current_y][current_x - 1] != 0 and map[current_y][current_x - 1] < 5 and new_map[current_y][current_x - 1] < 6:
                new_map[current_y][current_x - 1] = map[current_y][current_x]
                cache = map[current_y][current_x - 1]
                can_move = True
            else: cache = map[current_y][current_x]
        elif direction == 4 and current_x != 27:
            if map[current_y][current_x + 1] != 0 and map[current_y][current_x + 1] < 5 and new_map[current_y][current_x + 1] < 6:
                new_map[current_y][current_x + 1] = map[current_y][current_x]
                cache = map[current_y][current_x + 1]
                can_move = True
            else: cache = map[current_y][current_x]

        if can_move:
            if map[current_y][current_x] == 10:
                new_map[current_y][current_x] = cache_pinky
                cache_pinky = cache
            elif map[current_y][current_x] == 11:
                new_map[current_y][current_x] = cache_clyde
                cache_clyde = cache
            elif map[current_y][current_x] == 12:
                new_map[current_y][current_x] = cache_inky
                cache_inky = cache
            elif map[current_y][current_x] == 13:
                new_map[current_y][current_x] = cache_blinky
                cache_blinky = cache
def game_over_check():
    if eaten_coins >= 242:
        label1 = tk.Label(window, height=1, width=79, background="green", text='You Win!')
        label1.grid(row=0, columnspan=28)
    elif pacman_x == 0:
        label1 = tk.Label(window, height=1, width=79, background="green", text='Du hast gegen sich random bewegenden Geister verloren du Lowperformer!')
        label1.grid(row=0, columnspan=28)
    else:
        label1 = tk.Label(window, height=1, width=79, background="green", text='Score: ' + str(score))
        label1.grid(row=0, columnspan=28)
        move_pacman()
        move_ghost()
def tick():
    game_over_check()
    redraw()
    window.after(200, tick)
def change_direction(new_direction_code):
    global pacman_direction
    pacman_direction = new_direction_code

window.bind('<Up>', lambda event: change_direction(1))
window.bind('<Down>', lambda event: change_direction(2))
window.bind('<Left>', lambda event: change_direction(3))
window.bind('<Right>', lambda event: change_direction(4))

initialize_gui()
tick()
window.mainloop()