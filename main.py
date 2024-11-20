import os
import keyboard
import time
import colorama
import random

print(colorama.Fore.GREEN +"\tSnakeInTerminal!\n" + colorama.Style.RESET_ALL + colorama.Fore.CYAN + """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠙⣻⣷⣶⣤⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡿⠋⠀⠀⠀⠀⢹⣿⣿⡟⠉⠉⠉⢻⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⠀⠀⠀⠈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠉⠛⠿⣷⣤⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⣀⣀⡀⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣧⠀⠀
⠀⠀⣿⣿⣿⠁⠀⠈⠙⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠀⠀
⠀⠀⢿⣿⣿⣆⠀⠀⠀⠀⠈⠛⠿⣿⣶⣦⡤⠴⠀⠀⠀⠀⠀⣸⣿⣿⣿⡿⠀⠀
⠀⠀⠈⢿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣶⣦⣤⣀⣀⡀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀""" + colorama.Style.RESET_ALL)

time.sleep(2)
weight, height = 25, 15  # Длина должна быть больше чем ширина

food = [random.randint(0, weight - 1), random.randint(0, height - 1)]
head = [0, 5]
body = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]
max_snake = len(body)

def draw():
    os.system("cls" if os.name == "nt" else "clear")
    print(("0" * weight) + ("0"))
    for h in range(height):
        line = ""
        for w in range(weight + 1):
           if h == head[1] and w == head[0]:
               line += colorama.Back.BLACK + " " + colorama.Style.RESET_ALL
           elif [w, h] in body:
               line += colorama.Back.BLACK + " " + colorama.Style.RESET_ALL
           elif [w, h] == food:
               line += colorama.Back.RED + " " + colorama.Style.RESET_ALL
           else:
               line += colorama.Back.GREEN + " "
        print(line)

while True:
    draw()
    print(("0" * weight) + ("0"))
    body[0] = head.copy()
    
    for i in reversed(range(max_snake)):  
            body[i] = body[i - 1]

    if keyboard.is_pressed("w") and head[1] > 0:
        head[1] -= 1
    elif keyboard.is_pressed("s") and head[1] < height - 1:
        head[1] += 1
    elif keyboard.is_pressed("a") and head[0] > 0:
        head[0] -= 1
    elif keyboard.is_pressed("d") and head[0] < weight - 1:
        head[0] += 1

    if len(body) > max_snake:
        del body[-1]

    for b in body:
        if (head[0] == food[0] and head[1] == food[1]):
            food = [random.randint(0, weight - 1), random.randint(0, height - 1)]
            max_snake += 1
            body.insert(0, head.copy())

            break

    time.sleep(0.1)