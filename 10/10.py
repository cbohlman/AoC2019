import math
from operator import attrgetter

from collections import defaultdict

class asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.count = 0
        self.vectors = defaultdict(list)


def sort_distance(points, x, y):
    points.sort(key = lambda p: math.sqrt((p[0]-x)**2 + (p[1] -y)**2))
    return points


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
            r = math.atan2(xd,yd)*(180/math.pi)
            r = (r + 360) % 360
            r_vals.add(r)
            asteroid.vectors[r].append((search.x, search.y))
    asteroid.count = len(r_vals)
    counts.append(asteroid.count)

print("Part 1:")
print(max(counts))

print("Part 2")
obj = max(asteroids, key=attrgetter('count'))
print(obj.x,obj.y)
# print(obj.vectors)
sort_list = []
destroyed = set()
laser = sorted (obj.vectors.items())
laser.reverse()
laser.insert(0, laser.pop())
for i in laser:
    i = sort_distance(i[1], obj.x, obj.y)
for i in laser:
    print(i)
lased = []
for i in range(8):
    for r, coords in laser: 
        if i < len(coords):
            lased.append(coords[i])
print(lased[199][0]*100 + lased[199][1])
    





    
