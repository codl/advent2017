from math import inf
from itertools import count
import random

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return random.choice((1, -1))


class Coordinate(object):
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def manhattan(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __repr__(self):
        return repr((self.x, self.y, self.z))

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and\
                self.z == other.z

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y, self.z + other.z)


class Particle(object):
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def __repr__(self):
        return "<Particle {} {} {}>".format(self.p, self.v, self.a)

    def step(self):
        self.v += self.a
        self.p += self.v

    def resolved(self):
        """is this particle in, going towards, and accelerating towards
        the same... sextant.. like octant but theres only six of them

        heres a real bad ascii art diagram of the equivalent in 2D space

        \   ^   /
         \  |  /  a particle
          \ | /    o ->
           \|/
        ____|__________>
           /|\ 
          / | \ 
         /  |  \ 
        """
        return \
            sign(self.p.x - self.p.y) == sign(self.v.x - self.v.y) and\
            sign(self.p.x - self.p.z) == sign(self.v.x - self.v.z) and\
            sign(self.p.y - self.p.z) == sign(self.v.y - self.v.z) and\
            sign(self.p.x - self.p.y) == sign(self.a.x - self.a.y) and\
            sign(self.p.x - self.p.z) == sign(self.a.x - self.a.z) and\
            sign(self.p.y - self.p.z) == sign(self.a.y - self.a.z)

def run(_in):
    least_accel = inf
    solution1 = None
    particles = list()
    for line, i in zip(_in.splitlines(), count()):
        p, v, a = map(lambda x: Coordinate(*x[3:-1].split(',')), line.split(', '))
        #print(i, p, v, a)
        if a.manhattan() < least_accel:
            least_accel = a.manhattan()
            solution1 = i

        particle = Particle(p, v, a)
        particles.append(particle)

    resolved = 0
    while len(particles):
        #print(len(particles), resolved)
        random.shuffle(particles)
        furthest = max(particles, key=lambda e: e.p.manhattan())
        fastest = max(particles, key=lambda e: e.v.manhattan())
        accelerationest = max(particles, key=lambda e: e.a.manhattan())
        if furthest is fastest and fastest is accelerationest:
            #print('candidate', furthest)
            if furthest.resolved():
                #print('resolved')
                resolved += 1
                particles.remove(furthest)

        for particle in particles:
            particle.step()

        destroyed = set()
        for particle, i in zip(particles, count()):
            collisions = filter(lambda other: other.p == particle.p, particles[i+1:])

            for collision in collisions:
                destroyed.add(collision)
                destroyed.add(particle)
                #print('whammo')

        for particle in destroyed:
            particles.remove(particle)

    solution2 = resolved

    return solution1, solution2

if __name__ == '__main__':
    with open('20.example.input') as f:
        print(run(f.read().strip()))
    with open('20.input') as f:
        print(run(f.read().strip()))
