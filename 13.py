from itertools import count


def run(_in):
    lines = _in.split('\n')
    layers = list()
    for line in lines:
        args = line.split()
        layer = int(args[0].rstrip(":"))
        depth = int(args[1])
        layers.append((layer, depth))

    def have_a_go(delay):
        severity = 0
        caught = False
        for layer, depth in layers:
            t = layer + delay
            if t % ((depth-1)*2) == 0:
                caught = True
                severity += depth * layer

        if not caught:
            return True

        return severity

    def delay_needed():
        for delay in count():
            severity = have_a_go(delay)
            if severity is True:
                return delay

    return (have_a_go(0), delay_needed())


if __name__ == '__main__':
    with open('13.example.input') as f:
        print(run(f.read().strip()))
    with open('13.input') as f:
        print(run(f.read().strip()))
