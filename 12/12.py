from itertools import combinations
import math

class Moon:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x, self.y, self.z = int(x), int(y), int(z)
        self.vx, self.vy, self.vz = int(vx), int(vy), int(vz)

    def get_pos(self):
        return self.x, self.y, self.z

    def get_vel(self):
        return self.vx, self.vy, self.vz

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_kin(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def get_pot(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_total(self):
        return self.get_kin() * self.get_pot()

    def get_x_state(self):
        return str(self.x)+str(self.vx)

    def get_y_state(self):
        return str(self.y)+str(self.vy)

    def get_z_state(self):
        return str(self.z)+str(self.vz)

    def get_state(self):
        return str(self.x)+str(self.y)+str(self.z)+str(self.vx)+str(self.vy)+str(self.vz)

def gravity(p1, p2):
    if p1 > p2:
        return -1, 1
    elif p1 < p2:
        return 1, -1
    elif p1 == p2:
        return 0, 0 


def apply_gravity(moon1, moon2):
    dx1, dx2 = gravity(moon1.x, moon2.x)
    dy1, dy2 = gravity(moon1.y, moon2.y)
    dz1, dz2 = gravity(moon1.z, moon2.z)
    moon1.vx += dx1
    moon1.vy += dy1
    moon1.vz += dz1
    moon2.vx += dx2
    moon2.vy += dy2
    moon2.vz += dz2

def sim1(content, timestep):
    v_in = [0,0,0]
    moons = []
    for line in content:
        line = line.replace('>','').replace('<','').replace('x','').replace('y','').replace('z','').replace('=','')
        line = line.split(',')
        moon = Moon(*line, *v_in)
        moons.append(moon)

    for i in range(len(moons)):
        moons[i].id = i

    moons_comb = list(combinations(moons,2))

    for i in range(timestep):
        for pair in moons_comb:
            apply_gravity(pair[0], pair[1])
            # print(pair[0].id, pair[0].get_pos(), pair[0].get_vel())
            # print(pair[1].id, pair[1].get_pos(), pair[1].get_vel())
        for moon in moons:
            moon.apply_velocity()

    energy = [x.get_total() for x in moons]
    state = [x.get_state() for x in moons]
    state = ''.join(state)
    print(state)
    return(sum(energy))
if __name__ == "__main__":
    with open('input.txt') as f:
        content = [x.rstrip() for x in f.readlines()]

print('Part 1: ')
#print(sim1(content, 1000))

print('Part 2: ')
v_in = [0,0,0]
moons = []
for line in content:
    line = line.replace('>','').replace('<','').replace('x','').replace('y','').replace('z','').replace('=','')
    line = line.split(',')
    moon = Moon(*line, *v_in)
    moons.append(moon)

for i in range(len(moons)):
    moons[i].id = i


moons_comb = list(combinations(moons,2))
count = 0 
x_states = set()
y_states = set()
z_states = set()

x_found = False
y_found = False 
z_found = False
while not (x_found and y_found and z_found):
    x_state = []
    y_state = []
    z_state = []
    for pair in moons_comb:
        apply_gravity(pair[0], pair[1])
    for moon in moons:
        moon.apply_velocity()
    for moon in moons:
        x_state.append(moon.get_x_state())
        y_state.append(moon.get_y_state())
        z_state.append(moon.get_z_state())
    x_state = ''.join(x_state)
    y_state = ''.join(y_state)
    z_state = ''.join(z_state)
    
    if x_state in x_states:
        x_found = True 
    if y_state in y_states:
        y_found = True 
    if z_state in z_states:
        z_found = True 

    if not x_found:    
        x_states.add(x_state)
    if not y_found:
        y_states.add(y_state)
    if not z_found:
        z_states.add(z_state)
    
    print(x_found,y_found,z_found)
    
x_count = len(x_states)
y_count = len(y_states)
z_count = len(z_states)
print(x_count, y_count, z_count)

lcm = int(abs(x_count * y_count) / math.gcd(x_count, y_count))
print(lcm)
lcm = int(abs(z_count * lcm) / math.gcd(z_count, lcm))

print(lcm)
# energy = [x.get_total() for x in moons]
# return(sum(energy))