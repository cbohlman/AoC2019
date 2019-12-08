def calc_fuel(mass):
    fuel = int(int(mass) / 3) - 2
    print(fuel)
    if (fuel <= 0):
        return 0
    else:
        return fuel + calc_fuel(fuel)


def test_input(content):
    fuel = 0
    for line in content:
        fuel = fuel + calc_fuel(line)
    print(fuel)


if __name__ == '__main__':
    with open('input.txt') as f:
        content = f.readlines()
    content = [line.rstrip('\n') for line in content]
    test_input(content)