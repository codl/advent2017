import math

def arthsum(z):
    return (z * (z+1)) // 2

def invarthsum(z):
    _sum = 0
    x = 0
    while _sum <= z:
        x += 1
        _sum = arthsum(x)

    return x - 1

def run(z: int):
    dist1 = invarthsum((z-2)/8) + 1
    z -= arthsum(dist1-1) * 8 + 1
    z2 = (z-1) % (2 * dist1)
    z3 = z2 - dist1 + 1
    z4 = abs(z3)
    dist = dist1 + z4

    #print(dist1)
    #print(z)
    #print(z2)
    #print(z3)
    #print(z4)

    return dist


print(run(int(input())))
