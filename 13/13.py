from utils.intcode import intcode

if __name__ == '__main__':
    with open('input.txt') as f:
        content = [int(x) for x in f.read().split(',')]

def print_field(field):
    for line in field:
        print(line)

def draw(field, instruction):
    field[instruction[1]][instruction[0]] = instruction[2]

def get_ball_pos(field):
    for y in range(0,len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 4:
                return(x,y)

def get_joy_pos(field):
    for y in range(0,len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 3:
                return(x,y)

def update_joy(field):
    ball_pos = get_ball_pos(field)
    joy_pos = get_joy_pos(field)
    if ball_pos and joy_pos:
        if ball_pos[0] < joy_pos[0]:
            return -1
        elif ball_pos[0] == joy_pos[0]:
            return 0
        elif ball_pos[0] > joy_pos[0]:
            return 1

def count_blocks(content):
    comp = intcode(content)
    output = []
    block_count = 0
    while True:
        try:
            output.append(comp.calc_input(0))
            if len(output) == 3:
                if output[2] == 2:
                    block_count += 1
                output = []
        except StopIteration:
            break
    return block_count
    


def run_game(content):
    content[0] = 2
    comp = intcode(content)
    xmax = 41
    ymax = 22
    output = []
    field = [[0] * (xmax+1) for y in range(0,(ymax+1))]
    joy = 0
    while True:
        try:
            output.append(comp.calc_input(joy))
            if len(output) == 3:
                draw(field, output)
                output = []
                joy = update_joy(field)
        except StopIteration:
            break
    return field

print('Part 1:')
print(count_blocks(content))
print('Part 2: ')
field = run_game(content)
print(field[0][-1])


