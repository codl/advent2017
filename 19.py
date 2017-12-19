from collections import defaultdict
from itertools import count
from string import ascii_letters


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def rot(self, direction):
        if direction >= 0:
            return Coordinate(-self.y, self.x)
        else:
            return Coordinate(self.y, -self.x)


def run(_in):
    lines = _in.splitlines()

    diagram = defaultdict(lambda: None)
    start = None

    for line, y in zip(lines, count()):
        for char, x in zip(line, count()):
            if char in '|-+' + ascii_letters:
                diagram[Coordinate(x, y)] = char
                if y == 0:
                    start = Coordinate(x, y)

    del lines

    current = start
    direction = Coordinate(0, 1)
    seen = str()
    steps = 1

    while True:
        if diagram[current + direction]:
            pass
        elif diagram[current + direction.rot(1)]:
            direction = direction.rot(1)
        elif diagram[current + direction.rot(-1)]:
            direction = direction.rot(-1)
        else:
            break

        current += direction

        steps += 1

        if diagram[current] in ascii_letters:
            seen += diagram[current]

    return (seen, steps)



if __name__ == '__main__':
    with open('19.example.input') as f:
        print(run(f.read()))
    with open('19.input') as f:
        print(run(f.read()))
