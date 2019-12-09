if __name__ == '__main__':
    with open('input.txt') as f:
        content = [int(x) for x in f.read().split(',')]
content.extend([0] * 1000000)


print(content[1016])