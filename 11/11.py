from itertools import permutations
import time
import matplotlib.pyplot as plt


class intcode:
    def __init__(self, content):
        self.content = content.copy()
        self.input_count = 0
        self.i = 0
        self.r_base = 0

    def get_address(self, index, mode):
        if mode == 0 or mode == 1:
            return index
        elif mode == 2:
            return index + self.r_base

    def get_param(self, index, mode):
        content = self.content
        if mode == 0:
            return content[content[index]]
        elif mode == 1:
            return content[index]
        elif mode == 2:
            return content[content[index] + self.r_base]
    

    def calc_input(self, phase, in_signal):
        while self.i < len(self.content):
            op_code = self.content[self.i]
            # print(f'Opcde is {op_code}')
            if op_code > 100: 
                op_code = int(str(self.content[self.i])[-1])
                if len(str(self.content[self.i])) > 2:
                    p1m = int(str(self.content[self.i])[-3])
                if len(str(self.content[self.i])) > 3:
                    p2m = int(str(self.content[self.i])[-4])
                if len(str(self.content[self.i])) > 4: 
                    p3m = int(str(self.content[self.i])[-5])
                elif len(str(self.content[self.i])) <= 2:
                    p1m = 0 
                    p2m = 0
                    p3m = 0
                elif len(str(self.content[self.i])) == 3:
                    p2m = 0
                    p3m = 0
                elif len(str(self.content[self.i])) == 4:
                    p3m = 0
            elif op_code < 100:
                p1m = 0
                p2m = 0
            if (op_code == 99):
                raise StopIteration
            elif (op_code == 1):
                in1 = self.get_param(self.i+1, p1m)
                in2 = self.get_param(self.i+2, p2m)
                save = self.get_address(content[self.i+3], p3m)
                self.content[save] = in1 + in2
                self.i = self.i + 4
            elif (op_code == 2):
                in1 = self.get_param(self.i+1, p1m)
                in2 = self.get_param(self.i+2, p2m)
                save = self.get_address(content[self.i+3], p3m)
                self.content[save] = in1 * in2
                self.i = self.i + 4
            elif (op_code == 3):
                if self.input_count == 0:
                    num = phase
                    # print("phase")
                    self.input_count += 1
                elif self.input_count == 1:
                    num = in_signal
                    # print("signal")
                save = self.get_address(self.content[self.i+1],p1m)
                self.content[save] = num
                self.i += 2
            elif (op_code == 4):
                output = self.get_param(self.i+1, p1m)
                # print(output)
                self.i += 2
                return(output)
            elif (op_code == 5):
                if self.get_param(self.i+1, p1m) != 0:
                    self.i = self.get_param(self.i+2, p2m)
                else:
                    self.i += 3
            elif (op_code == 6):
                if self.get_param(self.i+1, p1m) == 0:
                    self.i = self.get_param(self.i+2, p2m)
                else:
                    self.i += 3
            elif (op_code == 7):
                save = self.get_address(content[self.i+3], p3m)
                if (self.get_param(self.i+1, p1m) < self.get_param(self.i+2, p2m)):
                    self.content[save] = 1
                    self.i += 4
                else:
                    self.content[save] = 0
                    self.i += 4
            elif (op_code == 8):
                save = self.get_address(content[self.i+3], p3m)
                if (self.get_param(self.i+1, p1m) == self.get_param(self.i+2, p2m)):
                    self.content[save] = 1
                    self.i += 4
                else:
                    self.content[save] = 0
                    self.i += 4
            elif (op_code == 9):
                    self.r_base = self.r_base + self.get_param(self.i+1, p1m)
                    self.i += 2
            else:
                print('Error', self.content[self.i])

def run_amplifiers(first, phase):
    halt = False
    outs = [first]
    comps = [intcode(content) for _ in range(5)]
    while not halt:
        try:
            for i in range(0,len(comps)):
                outs.append(comps[i].calc_input(phase[i],outs[-1]))
        except StopIteration:
            halt = True
            return outs[-1]


def robot_step(comp, in_signal):
    paint = comp.calc_input(in_signal,in_signal)
    direction = comp.calc_input(in_signal,in_signal)
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
        content.extend([0] * 1000000)


def run_robot(content, initial):
    robot_pos = (0,0)
    painted = set()
    direction = 'U'
    canvas = {robot_pos: initial}
    print('Part 1: ')
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
print(len(run_robot(content,0)[1]))
# Part 2
canvas = run_robot(content,1)[0]
coords = canvas.keys()
white = []
for coord in coords:
    if canvas[coord] == 1:
        white.append(coord)
xs,ys = zip(*white)

# plt.scatter(xs,ys)
# plt.show()
out = [[' ']*40]*10
graphic = [[' '] * 40 for i in range(10)]
print(f'Are these arrays the same? {out == graphic}')



# def print_panels(white_panels, output_array):
#     for x, y in white_panels:
#         output_array[y][x] = '#'
    
#     for line in out:
#         print(''.join(c*2 for c in line))

# print('out array')
# print_panels(white, out)
# print('graphic array')
# print_panels(white, graphic)


for x, y in white:
    out[2-y][x] = '█'


for ll in out:
    print(''.join(c*2 for c in ll))

for x, y in white:
    graphic[2-y][x] = '█'

for ll in graphic:
    print(''.join(c*2 for c in ll))

