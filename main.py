import os
import keyboard
import time
import colorama

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

head = [0, 5]
body = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]
max_snake = len(body)

weight, height = 25, 15  # Длина должна быть больше чем ширина
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
           else:
               line += colorama.Back.GREEN + " "
        print(line)

while True:
    draw()
    print(("0" * weight) + ("0"))
    if keyboard.is_pressed("w") and head[1] > 0:
        body[0] = head.copy()
        head[1] -= 1
        for i in reversed(range(max_snake)):
            body[i] = body[i - 1]
    elif keyboard.is_pressed("s") and head[1] < height - 1:
        body[0] = head.copy()
        head[1] += 1
        for i in reversed(range(max_snake)):  
            body[i] = body[i - 1]
    elif keyboard.is_pressed("a") and head[0] > 0:
        body[0] = head.copy()
        head[0] -= 1
        for i in reversed(range(max_snake)):  
            body[i] = body[i - 1]
    elif keyboard.is_pressed("d") and head[0] < weight - 1:
        body[0] = head.copy()
        head[0] += 1
        for i in reversed(range(max_snake)):  
            body[i] = body[i - 1]

    if len(body) > max_snake:
        del body[-1]

    time.sleep(0.1)