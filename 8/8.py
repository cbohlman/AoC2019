if __name__ == '__main__':
    with open('input.txt') as f:
        content = str(f.read())

print("Part 1:")
height = 6
width = 25
content = [int(i) for i in content]

layer = []
layers = []
for i in range(len(content)):
    layer.append(content[i])
    if len(layer) == height*width:
        layers.append(layer)
        layer = []

min = height*width
min_layer = []
for layer in layers:
    num_zeros = layer.count(0)
    if num_zeros < min:
        min = num_zeros
        min_layer = layer

print(min_layer.count(1) * min_layer.count(2))

# Part 2
print("Part 2: ")
final = layers[0]
for layer in layers:
    for i in range(len(layer)):
        if final[i] == 2:
            final[i] = layer[i]

final = [str(i) for i in final]
final = ['1' if x == '1' else ' ' for x in final]
image = []
i = 0 
while i < len(final):
    row = ''.join(final[i:i+width])
    image.append(row)
    i += width
    print(row)

