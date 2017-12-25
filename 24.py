def bridgemaker_3000(elements, starter = 0, keys=None):
    if keys == None:
        keys = (lambda e: e[0] + e[1],)
    candidates = list()
    candidates.append(([], *((0,)*len(keys))))
    for element in elements:
        others = elements.copy()
        others.remove(element)
        if element[0] == starter or element[1] == starter:
            ender = None
            if element[0] == starter:
                ender = bridgemaker_3000(others, element[1], keys)
            else:
                ender = bridgemaker_3000(others, element[0], keys)
            if ender:
                keyss = []
                for i in range(len(keys)):
                    keypos = i+1
                    keyss.append(keys[i](element) + ender[keypos])
                candidates.append(([element,]+ender[0], *keyss))
    for i in range(len(keys)):
        keypos = i+1
        maxkey = max(candidates, key=lambda e: e[keypos])[keypos]
        candidates = list(filter(lambda c: c[keypos] == maxkey, candidates))
    return candidates[0]

def run(_in):
    elements = map(lambda e: e.split('/'), _in.splitlines())
    elements = list(map(lambda e: (int(e[0]), int(e[1])), elements))
    solution1 = bridgemaker_3000(elements)
    solution2 = bridgemaker_3000(elements, keys=(lambda e:1, lambda e: e[0]+e[1]))
    return solution1, solution2

if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.example.input') as f:
        print(run(f.read().strip()))
    with open(day + '.input') as f:
        print(run(f.read().strip()))
