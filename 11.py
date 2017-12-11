DIRECTIONS = ['n', 'ne', 'se', 's', 'sw', 'nw']

def run(_in):
    paths = _in.split('\n')
    output = ''
    for path in paths:
        path = list(map(lambda s: s.strip(), path.split(',')))
        steps = list()
        maxsteps = 0
        for step in path:
            diridx = DIRECTIONS.index(step)
            found = False

            cancel = DIRECTIONS[(diridx + 3) % 6]
            cancelright = DIRECTIONS[(diridx + 2) % 6]
            cancelleft = DIRECTIONS[(diridx - 2) % 6]
            if cancel in steps:
                steps.remove(cancel)
            elif cancelright in steps:
                steps[steps.index(cancelright)] = DIRECTIONS[(diridx+1) % 6]
            elif cancelleft in steps:
                steps[steps.index(cancelleft)] = DIRECTIONS[(diridx-1) % 6]
            else:
                steps.append(step)

            maxsteps = max(maxsteps, len(steps))
        output += '{} steps, max {}\n'.format(len(steps), maxsteps)
    return output.strip()


if __name__ == '__main__':
    with open('11.example.input') as f:
        print(run(f.read().strip()))
    with open('11.input') as f:
        print(run(f.read().strip()))
