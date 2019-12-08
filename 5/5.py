
def get_param(content, index, mode):
    if mode == 0:
        return content[content[index]]
    elif mode == 1:
        return content[index]

def calc_input(content, noun, verb):
    input = content.copy()
    i = 0
    # input[1] = noun
    # input[2] = verb
    while i < len(input):
        op_code = input[i]
        if op_code > 100: 
            op_code = int(str(input[i])[-1])
            if len(str(input[i])) > 2:
                p1m = int(str(input[i])[-3])
            if len(str(input[i])) > 3:
                p2m = int(str(input[i])[-4])
            elif len(str(input[i])) <= 2:
                p1m = 0 
                p2m = 0
            elif len(str(input[i])) == 3:
                p2m = 0
        elif op_code < 100:
            p1m = 0
            p2m = 0
        if (op_code == 99):
            return(input)
        elif (op_code == 1):
            in1 = get_param(input, i+1, p1m)
            in2 = get_param(input, i+2, p2m)
            save = input[i+3]
            input[save] = in1 + in2
            #print(f"Saving {in1 + in2} to {save}")
            i = i + 4
        elif (op_code == 2):
            in1 = get_param(input, i+1, p1m)
            in2 = get_param(input, i+2, p2m)
            save = input[i+3]
            input[save] = in1 * in2
            #print(f"Saving {in1 * in2} to {save}")
            i = i + 4
        elif (op_code == 3):
            print("input")
            num = 5
            save = input[i+1]
            input[save] = num
            i += 2
        elif (op_code == 4):
            print('Output:')
            print(get_param(input, i+1, p1m))
            i += 2
        elif (op_code == 5):
            if get_param(input, i+1, p1m) != 0:
                i = get_param(input, i+2, p2m)
            else:
                i += 3
        elif (op_code == 6):
            if get_param(input, i+1, p1m) == 0:
                i = get_param(input, i+2, p2m)
            else:
                i += 3
        elif (op_code == 7):
            if (get_param(input, i+1, p1m) < get_param(input, i+2, p2m)):
                input[input[i+3]] = 1
                i += 4
            else:
                input[input[i+3]] = 0
                i += 4
        elif (op_code == 8):
            if (get_param(input, i+1, p1m) == get_param(input, i+2, p2m)):
                input[input[i+3]] = 1
                i += 4
            else:
                input[input[i+3]] = 0
                i += 4
        else:
            print('Error', input[i])



if __name__ == '__main__':
    with open('input.txt') as f:
        content = [int(x) for x in f.read().split(',')]
print("Part 1:")
calc_input(content,0,0)
