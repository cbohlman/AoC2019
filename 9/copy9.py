from itertools import permutations
import time
from intcode import intcode

if __name__ == '__main__':
    with open('input.txt') as f:
        content = [int(x) for x in f.read().split(',')]
        content.extend([0] * 1000000)

print('Part 1: ')
comp = intcode(content)
start = time.time()
print(comp.calc_input(1))
end = time.time()
print(f'Calc time: {end - start}')

print('Part 2: ')
comp = intcode(content)
start = time.time()
print(comp.calc_input(2))
end = time.time()
print(f'Calc time: {end - start}')