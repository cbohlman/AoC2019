class intcode:
    def __init__(self, content):
        self.content = content.copy()
        # self.content = self.content.extend([0] * 1000000)
        self.input_count = 0
        self.i = 0
        self.r_base = 0
    
    def increment(self, i):
        self.i += i

    def jump(self, i):
        self.i = i

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
    
    def parse_instr(self, instruction):
            op_code = self.content[self.i]
            p1, p2, p3 = self.i+1, self.i+2, self.i+3
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
                p3m = 0
            return op_code, p1, p1m, p2, p2m, p3, p3m

    def op_add(self, p1, p1m, p2, p2m, p3, p3m):
        in1 = self.get_param(p1, p1m)
        in2 = self.get_param(p2, p2m)
        save = self.get_address(self.content[p3], p3m)
        self.content[save] = in1 + in2
        self.increment(4)

    def op_mul(self, p1, p1m, p2, p2m, p3, p3m):
        in1 = self.get_param(p1, p1m)
        in2 = self.get_param(p2, p2m)
        save = self.get_address(self.content[p3], p3m)
        self.content[save] = in1 * in2
        self.increment(4)

    def op_in(self,p1,p1m, in_signal):
        save = self.get_address(self.content[p1], p1m)
        self.content[save] = in_signal
        self.increment(2)

    def op_out(self, p1, p1m):
        output = self.get_param(p1, p1m)
        return(output)

    def op_jump_true(self, p1, p1m, p2, p2m):
        if self.get_param(p1, p1m) != 0:
            self.jump(self.get_param(p2,p2m))
        else:
            self.increment(3)

    def op_jump_false(self, p1, p1m, p2, p2m):
        if self.get_param(p1, p1m) == 0:
            self.jump(self.get_param(p2,p2m))
        else:
            self.increment(3)
        
    def op_lt(self, p1, p1m, p2, p2m, p3, p3m):
        save = self.get_address(self.content[p3], p3m)
        if (self.get_param(p1, p1m) < self.get_param(p2, p2m)):
            self.content[save] = 1
            self.increment(4)
        else:
            self.content[save] = 0
            self.increment(4)

    def op_eq(self, p1, p1m, p2, p2m, p3, p3m):
        save = self.get_address(self.content[p3], p3m)
        if (self.get_param(p1, p1m) == self.get_param(p2, p2m)):
            self.content[save] = 1
            self.increment(4)
        else:
            self.content[save] = 0
            self.increment(4)

    def op_rb_adjust(self, p1, p1m):
        self.r_base += self.get_param(p1,p1m)
        self.increment(2)
    

    def calc_input(self, in_signal):
        while self.i < len(self.content):
            instruction = self.content[self.i]
            # print(f'Opcde is {op_code}')
            op_code, p1, p1m, p2, p2m, p3, p3m = self.parse_instr(instruction)
            if (op_code == 99):
                raise StopIteration
            elif (op_code == 1):
                self.op_add(p1, p1m, p2, p2m, p3, p3m)
            elif (op_code == 2):
                self.op_mul(p1, p1m, p2, p2m, p3, p3m)
            elif (op_code == 3):
                self.op_in(p1,p1m, in_signal)
            elif (op_code == 4):
                return(self.op_out(p1,p1m))
            elif (op_code == 5):
                self.op_jump_true(p1, p1m, p2, p2m)
            elif (op_code == 6):
                self.op_jump_false(p1, p1m, p2, p2m)
            elif (op_code == 7):
                self.op_lt(p1, p1m, p2, p2m, p3, p3m)
            elif (op_code == 8):
                self.op_eq(p1, p1m, p2, p2m, p3, p3m)
            elif (op_code == 9):
                self.op_rb_adjust(p1, p1m)
            else:
                print('Error', op_code)

