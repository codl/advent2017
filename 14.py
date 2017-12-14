knothash = __import__("10-2", fromlist=('densehash',)).densehash


def knothashb(_in):
    bytes_ = knothash(_in)
    out = list()
    for byte in bytes_:
        for i in range(7, -1, -1):
            out.append(bool(byte & 2**i))
    return tuple(out)


def run(_in):
    rows = map(lambda i: knothashb('{}-{}'.format(_in, i)), range(128))
    rows = tuple(rows)

    count = 0
    for row in rows:
        for square in row:
            if square:
                count += 1

    return count


if __name__ == '__main__':
    with open('14.example.input') as f:
        print(run(f.read().strip()))
    with open('14.input') as f:
        print(run(f.read().strip()))
