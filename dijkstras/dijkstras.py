f = open("input.txt")

n = int(f.readline().strip())
start, end = f.readline().strip().split(" ")

nodes = []

for i in range(n):
    x,y,z = f.readline().strip().split(" ")
    z = int(z)
    nodes.append([x,y,z])

wt = 0
curr = start
seen = [start]

while curr != end:
    wts = {}
    for node in nodes:
        if node[0] == curr:
            if node[1] not in seen:
                wts[node[1]] = wt + node[2]
            if node[2] > wt + node[2]:
                node[2] = wt + node[2]

    curr = min(wts, key=wts.get)
    wt = wts[curr]
    seen.append(curr)

print "->".join(seen) + ": " + str(wt)
