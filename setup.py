import random

weight, height = 25, 15  # Длина должна быть больше чем ширина

food = [random.randint(0, weight - 1), random.randint(0, height - 1)]
head = [0, 5]
body = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]
max_snake = len(body)
input_controller = ["s"]
points = 0