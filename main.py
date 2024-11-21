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
input_controller = ["s"]

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
               line += colorama.Back.LIGHTGREEN_EX + " "
        print(line)

while True:
    draw()
    print(("0" * weight) + ("0"))
    body[0] = head.copy()
    
    for i in reversed(range(max_snake)):  
            body[i] = body[i - 1]

    if keyboard.is_pressed("w"):
        head[1] -= 1
        input_controller.append("w")
    elif keyboard.is_pressed("s"):
        head[1] += 1
        input_controller.append("s")
    elif keyboard.is_pressed("a"):
        head[0] -= 1
        input_controller.append("a")
    elif keyboard.is_pressed("d"):
        head[0] += 1
        input_controller.append("d")
    else:
        if input_controller[-1] == "w":
            head[1] -= 1
            input_controller.append("w")
        elif input_controller[-1] == "s":
            head[1] += 1
            input_controller.append("s")
        elif input_controller[-1] == "a":
            head[0] -= 1
            input_controller.append("a")
        elif input_controller[-1] == "d":
            head[0] += 1
            input_controller.append("d")

        if body[0][0] < 0 or body[0][0] >= weight or body[0][1] < 0 or body[0][1] >= height:
            food = [random.randint(0, weight - 1), random.randint(0, height - 1)]
            head = [0, 5]
            body = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]
            max_snake = len(body)
            input_controller = ["s"]
        else:
            pass

        if head in body:
            food = [random.randint(0, weight - 1), random.randint(0, height - 1)]
            head = [0, 5]
            body = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]
            max_snake = len(body)
            input_controller = ["s"]
        else:
            pass


    for b in body:
        if (head[0] == food[0] and head[1] == food[1]):
            food = [random.randint(0, weight - 1), random.randint(0, height - 1)]
            max_snake += 1
            body.append(head.copy())

            break

    if len(body) > max_snake:
        del body[-1]

    time.sleep(0.1)