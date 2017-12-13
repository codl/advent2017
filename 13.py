def run(_in):
    lines = _in.split('\n')
    layers = list()
    for line in lines:
        args = line.split()
        layer = int(args[0].rstrip(":"))
        depth = int(args[1])
        layers.append((layer, depth))

    severity = 0
    for layer, depth in layers:
        t = layer
        # scandepth = abs(((t+2) % (2 * (depth-1)))-2)
        # lol this isnt necessary at all
        if t % ((depth-1)*2) == 0:
            severity += depth * layer

    return severity


if __name__ == '__main__':
    with open('13.example.input') as f:
        print(run(f.read().strip()))
    with open('13.input') as f:
        print(run(f.read().strip()))
