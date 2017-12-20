from math import inf
from itertools import count

class Coordinate(object):
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def manhattan(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __repr__(self):
        return repr((self.x, self.y, self.z))


def run(_in):
    least_accel = inf
    solution1 = None
    for line, i in zip(_in.splitlines(), count()):
        p, v, a = map(lambda x: Coordinate(*x[3:-1].split(',')), line.split(', '))
        #print(i, p, v, a)
        if a.manhattan() < least_accel:
            least_accel = a.manhattan()
            solution1 = i

    return solution1

if __name__ == '__main__':
    with open('20.example.input') as f:
        print(run(f.read().strip()))
    with open('20.input') as f:
        print(run(f.read().strip()))
