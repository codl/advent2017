def run(_in):
    lines = _in.split('\n')

    parents = dict()

    for line in lines:
        args = line.split()
        if len(args) > 2:
            children = set(map(lambda a: a.strip(','), args[3:]))
            for child in children:
                parents[child] = args[0]

    current = lines[0].split()[0]
    while current in parents:
        current = parents[current]

    return current


if __name__ == '__main__':
    import sys
    print(run(sys.stdin.read().strip()))
