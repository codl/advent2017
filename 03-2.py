from collections import defaultdict


class Coordinates(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    """
    def rot(self, direction):
        if direction > 0:
            return Coordinates(-self.y, self.x)
        else:
            return Coordinates(self.y, -self.x)
    """

    def rot(self):
        return Coordinates(-self.y, self.x)

    def neighbours(self):
        return (self + Coordinates(x, y) for x, y in
                ((1, 1), (1, 0), (1, -1), (0, -1), (-1, -1),
                 (-1, 0), (-1, 1), (0, 1)))

    def __repr__(self):
        return '<Coordinates {}, {}>'.format(self.x, self.y)


C = Coordinates


def run(_in):
    threshold = int(_in)
    grid = defaultdict(lambda: None)
    direction = C(1, 0)
    current = C(0, 0)
    grid[current] = 1


    while threshold > grid[current]:
        current = current + direction
        grid[current] = 0
        for neighbour in current.neighbours():
            if neighbour in grid:
                grid[current] += grid[neighbour]

        if current + direction.rot() not in grid:
            direction = direction.rot()

    return grid[current]


if __name__ == '__main__':
    import sys
    print(run(int(sys.stdin.read().strip())))
