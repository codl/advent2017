DIRECTIONS = ['n', 'ne', 'se', 's', 'sw', 'nw']

def run(_in):
    paths = _in.split('\n')
    output = ''
    for path in paths:
        path = list(map(lambda s: s.strip(), path.split(',')))
        idx = 0
        while idx < len(path):
            step = path[idx]
            diridx = DIRECTIONS.index(step)
            for jdx in range(idx+1, len(path)):
                dirjdx = DIRECTIONS.index(path[jdx])
                diff = (dirjdx - diridx) % len(DIRECTIONS)
                if diff == 3:
                    del path[jdx]
                    del path[idx]
                elif diff == 2:
                    del path[jdx]
                    path[idx] = DIRECTIONS[(diridx+1) % len(DIRECTIONS)]
                elif diff == 4:
                    del path[jdx]
                    path[idx] = DIRECTIONS[(diridx-1) % len(DIRECTIONS)]
                else:
                    continue

                idx -= 1
                break
            idx += 1
        output += repr(len(path)) + '\n'
    return output.strip()


if __name__ == '__main__':
    with open('11.example.input') as f:
        print(run(f.read().strip()))
    with open('11.input') as f:
        print(run(f.read().strip()))
