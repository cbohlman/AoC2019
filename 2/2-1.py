
def calc_input(content, noun, verb):
    input = content.copy()
    i = 0
    input[1] = noun
    input[2] = verb
    while i < len(input):
        if (input[i] == 99):
            return(input)
        elif (input[i] == 1):
            in1 = input[input[i+1]]
            in2 = input[input[i+2]]
            save = input[i+3]
            input[save] = in1 + in2
            #print(f"Saving {in1 + in2} to {save}")
            i = i + 4
        elif (input[i] == 2):
            in1 = input[input[i+1]]
            in2 = input[input[i+2]]
            save = input[i+3]
            input[save] = in1 * in2
            #print(f"Saving {in1 * in2} to {save}")
            i = i + 4
        else:
            print('Error', input[i])



if __name__ == '__main__':
    with open('input1.txt') as f:
        content = [int(x) for x in f.read().split(',')]
print("Part 1:")
print(calc_input(content,12,2)[0])  

print("Part 2:")
for i in range(0,99):
    for j in range(0,99):
        #print(i,j)
        out = calc_input(content,i,j)[0]
        if(out == 19690720):
            print(100 * i + j)
