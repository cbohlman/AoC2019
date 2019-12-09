from itertools import permutations

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
                # raise StopIteration
                return
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
                print(output)
                self.i += 2
                # return(output)
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




if __name__ == '__main__':
    with open('input.txt') as f:
        content = [int(x) for x in f.read().split(',')]
content.extend([0] * 1000000)

print('Part 1: ')
comp = intcode(content)
comp.calc_input(1,1)

print('Part 2: ')
comp = intcode(content)
comp.calc_input(2,1)