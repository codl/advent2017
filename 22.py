from collections import defaultdict
from itertools import count
Coordinate = __import__('19', fromlist=('Coordinate')).Coordinate

def run(_in):
    width = None
    grid = defaultdict(lambda: 0)
    for line, i in zip(_in.splitlines(), count()):
        width = len(line)
        for char, j in zip(line, count()):
            grid[Coordinate(j, i)] = 2 if (char == '#') else 0
    startgrid = grid.copy()

    pos = Coordinate(width//2, width//2)
    direction = Coordinate(0, -1)

    infected = 0

    for _ in range(10000):
        if grid[pos]:
            direction = direction.rot(-1)
        else:
            direction = direction.rot(+1)
            infected += 1

        grid[pos] = not grid[pos]
        pos = pos + direction

    solution1 = infected

    grid = startgrid.copy()
    pos = Coordinate(width//2, width//2)
    direction = Coordinate(0, -1)

    infected = 0

    for _ in range(10000000):
        if grid[pos] == 0:
            direction = direction.rot(+1)
        elif grid[pos] == 1:
            infected += 1
        elif grid[pos] == 2:
            direction = direction.rot(-1)
        else:
            direction = -direction

        grid[pos] = (grid[pos]+1)%4
        pos = pos + direction


    return (solution1, infected)



if __name__ == '__main__':
    with open('22.example.input') as f:
        print(run(f.read().strip()))
    with open('22.input') as f:
        print(run(f.read().strip()))
