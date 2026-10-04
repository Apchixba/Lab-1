import time
import sys
import os


BLUE = '\u001b[44m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'
ERASE = '\x1B[2K'
BEGIN = '\x1B[1G'


def flag():
    pixel = ' '
    lenght = 10
    height = 10

    for i in range(height):
        for j in range(lenght):
            if (3 < i < 6 and 1 < j < 8) or (1 < i < 8 and 3 < j < 6):
                print(WHITE + pixel, end='')
            else:
                print(RED + pixel, end='')
        print(RESET)


def usor():
    pixel = ' '
    lenght = 100
    height = 30

    for i in range(height):
        for j in range(lenght):
            if abs((i - 15) ** 2 + (j - 36) ** 2 - 100) <= 35 or abs((i - 15) ** 2 + (j - 59) ** 2 - 100) <= 35:
                print(WHITE + pixel, end='')
            else:
                print(RED + pixel, end='')
        print(RESET)

def diamond():
    os.system("cls")
    pixel = ' '
    lenght = 100
    height = 27

    # center = height // 2
    # offset = height
    # step = 1
    # lenght = 1
    colors = [200, 100, 10]

    while True:
        for color in colors:
            for i in range(height):
                for j in range(lenght):
                    if abs((i - 13) ** 2 + (j - 36) ** 2 - 100) <= 35 or abs((i - 13) ** 2 + (j - 59) ** 2 - 100) <= 35:
                        print(f"\x1b[48;5;{color}m" + pixel, end='')
                    else:
                        print(RED + pixel, end='')
                # print(100 * f"\x1b[48;5;{color}m{pixel}{RESET}")
                print("\x1b[0m")
            
            print(f'\x1b[{height + 1}A', end="")
            # print(" "  * 100)
            # print(f'\x1b[{10}D')
            time.sleep(1)


def sequence():
    file = open('sequence.txt', 'r')
    odds = []
    evens = []
    for line in file:
        if -3 < float(line) <= 3:
            odds.append(float(line))
        else:
            evens.append(float(line))
    file.close()
    # print(len(odds), len(evens))
    print(f'{BLUE}{" " * int(len(odds) / 5)}{RESET} {len(odds)/(len(odds) + len(evens)) * 100}%')
    print(f'{RED}{" " * int(len(evens) / 5)}{RESET} {len(evens)/(len(odds) + len(evens)) * 100}%')

def dop():
    plot_list = [[0 for i in range(10)] for i in range(10)]
    result = [0 for i in range(10)]

    for i in range(10):
        result[i] = i / 3

    step = round(abs(result[0] - result[9]) / 9, 6)
    print(step)

    for i in range(10):
        for j in range(10):
            if j == 0:
                plot_list[i][j] = step * (8-i) + step

    for i in range(9):
        for j in range(10):
            if abs(plot_list[i][0] - result[9 - j]) < step:
                for k in range(9):
                    if 8 - k == j:
                        plot_list[i][k+1] = 1

    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += '\t' + str(round(plot_list[i][j], 2)) + '\t'
            if plot_list[i][j] == 0:
                line += '--'
            if plot_list[i][j] == 1:
                line += '!!'
        print(line)
    print('\t0\t1 2 3 4 5 6 7 8 9')

# flag() # 1
# usor() # 2
# diamond() # 3
# sequence() # 4
# dop() # dop