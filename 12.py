def run(_in):
    lines = _in.split('\n')
    groups = set()
    for line in lines:
        args = line.split()
        program = args[0]
        piped = map(lambda a: a.rstrip(','), args[2:])
        group = frozenset(map(lambda a: int(a), (program, *piped)))
        for other in set(groups):
            if other & group:
                group = group | other
                groups.remove(other)
        groups.add(group)

    zero_group = [s for s in groups if 0 in s][0]

    return (len(zero_group), len(groups))


if __name__ == '__main__':
    with open('12.example.input') as f:
        print(run(f.read().strip()))
    with open('12.input') as f:
        print(run(f.read().strip()))
