knothash = __import__("10-2", fromlist=('densehash',)).densehash
import random


def knothashb(_in):
    bytes_ = knothash(_in)
    out = list()
    for idx in range(len(bytes_)):
        for jdx in range(8):
            if(bytes_[idx] & 2**(7-jdx)):
                out.append(idx*8 + jdx)
    return tuple(out)


def neighbours(coord):
    x, y = coord
    return {
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1)
        }


def run(_in):
    squares = set()
    groups = set()

    def _debug():
        CHARS="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        groupchars = dict()
        for row in range(128):
            for column in range(128):
                square = (column, row)
                if square in squares:
                    char = '#'
                    for group in groups:
                        if square in group:
                            if char != "#":
                                raise Exception()
                            if group not in groupchars.keys():
                                groupchars[group] = random.choice(CHARS)
                            char = groupchars[group]
                            break
                    print(char, end='')
                else:
                    print('.', end='')
            print('')
        print('')

    for row in range(128):
        for column in knothashb('{}-{}'.format(_in, row)):
            squares.add((column, row))

    for square in squares:
        group = set((square,))
        group |= squares & neighbours(square)
        for other in set(groups):
            if other & group:
                group |= other
                groups.remove(other)
        groups.add(frozenset(group))

    return len(squares), len(groups)


if __name__ == '__main__':
    with open('14.example.input') as f:
        print(run(f.read().strip()))
    with open('14.input') as f:
        print(run(f.read().strip()))
