def load_orbits(content):

    data = {}
    orbs = set()
    for line in content:
        parent = line.split(')')[0]
        child = line.split(')')[1]
        data[child] = parent
        orbs.add(parent)
        orbs.add(child)
    return data, orbs

orbs = {}

def get_depth(body, parents):
    if body not in orbs:
        if body in parents:
            orbs[body] = 1 + get_depth(parents[body], parents)
        else:
            orbs[body] = 0
    return orbs[body]

path1 = []
path2 = []
def find_path(body, parents, path):
    if body in parents:
        path.append(parents[body])
        find_path(parents[body], parents, path)
    else:
        pass
    return path

if __name__ == "__main__":
    with open('input.txt') as f:
        content = f.readlines()
    content = [line.rstrip('\n') for line in content]
# test(content)
data, x = load_orbits(content)
print(sum(get_depth(p, data) for p in x))
print(orbs['YOU'])
print(orbs['SAN'])
for p in x:
    if p == 'SAN':
        san_path = find_path(p, data, path1)
    elif p == 'YOU':
        you_path = find_path(p,data, path2)

print(len(san_path))
print(len(you_path))

i = -1
lca = 0
while True:
    if (san_path[i] != you_path[i]):
        print(orbs['YOU'] + orbs['SAN'] - 2* lca)
        break
    else:
        lca += 1
        i = i - 1
        print(i)
