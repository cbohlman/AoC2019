from itertools import permutations
import time
import matplotlib.pyplot as plt
from utils.intcode import intcode


def robot_step(comp, in_signal):
    paint = comp.calc_input(in_signal)
    direction = comp.calc_input(in_signal)
    return paint, direction

def turn(current_dir, rotation):
    if rotation == 0:
        current_dir -= 90
    elif rotation == 1:
        current_dir += 90
    return current_dir

def update_pos(cur_pos, cur_dir, turn_dir):
    new_dir = ''
    #up and 0 move left
    if cur_dir == 'U' and turn_dir == 0:
        new_dir = 'L'
        new_pos = (cur_pos[0] - 1, cur_pos[1])
    #up and 1 move right
    elif cur_dir == 'U' and turn_dir == 1:
        new_dir = 'R'
        new_pos = (cur_pos[0] + 1, cur_pos[1])
    #left and 0 move down
    elif cur_dir == 'L' and turn_dir == 0:
        new_dir = 'D'
        new_pos = (cur_pos[0], cur_pos[1] - 1)
    #left and 1 move up
    elif cur_dir == 'L' and turn_dir == 1:
        new_dir = 'U'
        new_pos = (cur_pos[0], cur_pos[1] + 1)
    #down and 0 move right
    elif cur_dir == 'D' and turn_dir == 0:
        new_dir = 'R'
        new_pos = (cur_pos[0] + 1, cur_pos[1])
    #down and 1 move left
    elif cur_dir == 'D' and turn_dir == 1:
        new_dir = 'L'
        new_pos = (cur_pos[0] - 1, cur_pos[1])
    #right and 0 move up
    elif cur_dir == 'R' and turn_dir == 0:
        new_dir = 'U'
        new_pos = (cur_pos[0], cur_pos[1] + 1)
    #right and 1 move down
    elif cur_dir == 'R' and turn_dir == 1:
        new_dir = 'D'
        new_pos = (cur_pos[0], cur_pos[1] - 1)
    else:
        print("ERROR")
    return new_pos, new_dir


if __name__ == '__main__':
    with open('input.txt') as f:
        content = [int(x) for x in f.read().split(',')]


def run_robot(content, initial):
    robot_pos = (0,0)
    painted = set()
    direction = 'U'
    canvas = {robot_pos: initial}
    visited = []
    visited.append(robot_pos)
    instructions = []
    comp = intcode(content)


    while True:
        try:
            if robot_pos in canvas.keys():
                cur_col = canvas[robot_pos]
            else:
                cur_col = 0
            output = robot_step(comp, cur_col)
            instructions.append(output)
            canvas[robot_pos] = output[0]
            robot_pos, direction = update_pos(robot_pos, direction, output[1])
            painted.add(robot_pos)
            visited.append(robot_pos)
        except StopIteration:
            break

    return canvas, painted
print('Part 1: ')
print(len(run_robot(content,0)[1]))
# Part 2
print('Part 2: ')
canvas = run_robot(content,1)[0]
coords = canvas.keys()
white = []
for coord in coords:
    if canvas[coord] == 1:
        white.append(coord)
xs, ys = zip(*white)
print(len(xs))
out = [[' '] * (len(xs)) for i in range(10)]

for x, y in white:
    # print(x,y)
    out[2-y][x] = '█'


for line in out:
    print(''.join(c*2 for c in line))
