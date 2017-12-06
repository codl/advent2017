from math import inf
def wheremax(banks):
    _max = -inf
    idx = 0
    for i in range(len(banks)):
        if banks[i] > _max:
            idx = i
            _max = banks[i]

    return idx

def run(_in):
    banks = _in.strip().split()
    banks = list(map(lambda i: int(i), banks))
    seen = []
    while tuple(banks) not in seen:
        seen.append(tuple(banks))

        idxmax = wheremax(banks)
        blocks = banks[idxmax]
        banks[idxmax] = 0
        for i in range(blocks):
            banks[(i+idxmax+1) % len(banks)] += 1

    return (len(seen), len(seen) - seen.index(tuple(banks)))

if __name__ == '__main__':
    import sys
    print(run(sys.stdin.read()))
