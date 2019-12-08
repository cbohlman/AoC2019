from itertools import permutations

class intcode:
    def __init__(self, content):
        self.content = content.copy()
        self.input_count = 0
        self.i = 0

    def get_param(self, index, mode):
        content = self.content
        if mode == 0:
            return content[content[index]]
        elif mode == 1:
            return content[index]

    def calc_input(self, phase, in_signal):
        while self.i < len(self.content):
            op_code = self.content[self.i]
            if op_code > 100: 
                op_code = int(str(self.content[self.i])[-1])
                if len(str(self.content[self.i])) > 2:
                    p1m = int(str(self.content[self.i])[-3])
                if len(str(self.content[self.i])) > 3:
                    p2m = int(str(self.content[self.i])[-4])
                elif len(str(self.content[self.i])) <= 2:
                    p1m = 0 
                    p2m = 0
                elif len(str(self.content[self.i])) == 3:
                    p2m = 0
            elif op_code < 100:
                p1m = 0
                p2m = 0
            if (op_code == 99):
                raise StopIteration
            elif (op_code == 1):
                in1 = self.get_param(self.i+1, p1m)
                in2 = self.get_param(self.i+2, p2m)
                save = self.content[self.i+3]
                self.content[save] = in1 + in2
                self.i = self.i + 4
            elif (op_code == 2):
                in1 = self.get_param(self.i+1, p1m)
                in2 = self.get_param(self.i+2, p2m)
                save = self.content[self.i+3]
                self.content[save] = in1 * in2
                self.i = self.i + 4
            elif (op_code == 3):
                if self.input_count == 0:
                    num = phase
                    print("phase")
                    self.input_count += 1
                elif self.input_count == 1:
                    num = in_signal
                    print("signal")
                save = self.content[self.i+1]
                self.content[save] = num
                self.i += 2
            elif (op_code == 4):
                output = self.get_param(self.i+1, p1m)
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
                if (self.get_param(self.i+1, p1m) < self.get_param(self.i+2, p2m)):
                    self.content[self.content[self.i+3]] = 1
                    self.i += 4
                else:
                    self.content[self.content[self.i+3]] = 0
                    self.i += 4
            elif (op_code == 8):
                if (self.get_param(self.i+1, p1m) == self.get_param(self.i+2, p2m)):
                    self.content[self.content[self.i+3]] = 1
                    self.i += 4
                else:
                    self.content[self.content[self.i+3]] = 0
                    self.i += 4
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
print(content)
phases = permutations([5,6,7,8,9])
outputs = []

phases = permutations([5,6,7,8,9])
for i in phases:
    outputs.append(run_amplifiers(0, i))





print(max(outputs))
