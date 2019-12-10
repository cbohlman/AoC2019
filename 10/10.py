import math

class asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.count = 0




with open('input.txt') as f:
    content = f.readlines()

asteroids = []
for y in range(0, len(content)):
    for x in range(0, len(content[y])):
        if content[y][x] == '#':
            asteroids.append(asteroid(x,y))

counts = []
for asteroid in asteroids:
    r_vals = set()
    x,y = asteroid.x, asteroid.y
    for search in asteroids:
        xd = asteroid.x - search.x
        yd = asteroid.y - search.y
        if (xd == 0) and (yd == 0):
            pass
        else: 
            r = math.atan2(yd,xd)
            r_vals.add(r)
    asteroid.count = len(r_vals)
    counts.append(asteroid.count)

print("Part 1:")
print(max(counts))