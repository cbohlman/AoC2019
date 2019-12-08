
def map_wire(wire):
    dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    dy = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

    x = 0
    y = 0
    ans = {}
    length = 0
    for i in wire:
        d = i[0]
        n = int(i[1:])
        assert d in ['L','R','U','D']
        for _ in range(n):
            x += dx[d]
            y += dy[d]
            length += 1
            if (x,y) not in ans: 
                ans[(x,y)] = length

    return ans



if __name__ == "__main__":
     A,B = open('input.txt').read().split('\n')
     A,B = [x.split(',') for x in [A,B]]

PA = map_wire(A)
PB = map_wire(B)

both = set(PA.keys())&set(PB.keys())
print(both)
ans = [abs(a) + abs(b) for (a,b) in both]
print('Part 1: ')
print(min(ans))

### Part 2
ans2 = [PA[a,b] + PB[a,b] for (a,b) in both]
print('Part 2: ')
print(min(ans2))

