from math import sqrt

def spins(pattern):
    patterns = set()
    if len(pattern) == 4:
        p0, p1, p2, p3 = pattern
        patterns.add(p0 + p1 +
                     p2 + p3)
        patterns.add(p3 + p0 +
                     p2 + p1)  # rotated cw
        patterns.add(p1 + p0 +
                     p3 + p2)  # flipped
        patterns.add(p0 + p2 +
                     p1 + p3)  # rotated cw and flipped
    else:
        p0, p1, p2, p3, p4, p5, p6, p7, p8 = pattern
        patterns.add(p0 + p1 + p2 +
                     p3 + p4 + p5 +
                     p6 + p7 + p8)
        patterns.add(p6 + p3 + p0 +
                     p7 + p4 + p1 +
                     p8 + p5 + p2)  # rotated cw
        patterns.add(p2 + p1 + p0 +
                     p5 + p4 + p3 +
                     p8 + p7 + p6)  # flipped
        patterns.add(p0 + p3 + p6 +
                     p1 + p4 + p7 +
                     p2 + p5 + p8)  # rotated cw and flipped
    for pattern in patterns.copy():
        patterns.add(pattern[::-1])  # this gives us the other four patterns!

    return patterns


def iterate(state, patterns):
    size = int(sqrt(len(state)))
    newstate = None
    if size % 2 == 0:
        newsize = (size * 3) // 2
        newstate = [None] * (newsize**2)
        for x in range(0, size, 2):
            for y in range(0, size, 2):
                pattern = state[x + size*y:x + size*y + 2]
                pattern += state[x + size*(y+1):x + size*(y+1) + 2]


                newpattern = patterns[pattern]
                p0, p1, p2, p3, p4, p5, p6, p7, p8 = newpattern

                xx = (x * 3) // 2
                yy = (y * 3) // 2

                newstate[xx+0 + (yy+0)*newsize] = p0
                newstate[xx+1 + (yy+0)*newsize] = p1
                newstate[xx+2 + (yy+0)*newsize] = p2

                newstate[xx+0 + (yy+1)*newsize] = p3
                newstate[xx+1 + (yy+1)*newsize] = p4
                newstate[xx+2 + (yy+1)*newsize] = p5

                newstate[xx+0 + (yy+2)*newsize] = p6
                newstate[xx+1 + (yy+2)*newsize] = p7
                newstate[xx+2 + (yy+2)*newsize] = p8
    else:
        newsize = (size * 4) // 3
        newstate = [None] * (newsize**2)
        for x in range(0, size, 3):
            for y in range(0, size, 3):
                pattern = state[x + size*y:x + size*y + 3]
                pattern += state[x + size*(y+1):x + size*(y+1) + 3]
                pattern += state[x + size*(y+2):x + size*(y+2) + 3]


                newpattern = patterns[pattern]
                p0, p1, p2, p3, p4, p5, p6, p7, p8,\
                    p9, p10, p11, p12, p13, p14, p15 = newpattern

                xx = (x * 4) // 3
                yy = (y * 4) // 3

                newstate[xx+0 + (yy+0)*newsize] = p0
                newstate[xx+1 + (yy+0)*newsize] = p1
                newstate[xx+2 + (yy+0)*newsize] = p2
                newstate[xx+3 + (yy+0)*newsize] = p3

                newstate[xx+0 + (yy+1)*newsize] = p4
                newstate[xx+1 + (yy+1)*newsize] = p5
                newstate[xx+2 + (yy+1)*newsize] = p6
                newstate[xx+3 + (yy+1)*newsize] = p7

                newstate[xx+0 + (yy+2)*newsize] = p8
                newstate[xx+1 + (yy+2)*newsize] = p9
                newstate[xx+2 + (yy+2)*newsize] = p10
                newstate[xx+3 + (yy+2)*newsize] = p11

                newstate[xx+0 + (yy+3)*newsize] = p12
                newstate[xx+1 + (yy+3)*newsize] = p13
                newstate[xx+2 + (yy+3)*newsize] = p14
                newstate[xx+3 + (yy+3)*newsize] = p15

    return "".join(newstate)


def run(_in, example=False):
    patterns = dict()
    for line in _in.splitlines():
        line = line.replace('/', '')
        input_pattern, _, output_pattern = line.split(' ')
        patterns[input_pattern] = output_pattern
        for pattern in spins(input_pattern):
            if pattern not in patterns:
                patterns[pattern] = output_pattern

    state = (".#." +
             "..#" +
             "###")

    state = iterate(state, patterns)
    state = iterate(state, patterns)

    if example:
        solution1 = state.count('#')
        return solution1

    state = iterate(state, patterns)
    state = iterate(state, patterns)
    state = iterate(state, patterns)
    solution1 = state.count('#')

    for _ in range(13):
        state = iterate(state, patterns)

    solution2 = state.count('#')

    return (solution1, solution2)



if __name__ == '__main__':
    with open('21.example.input') as f:
        print(run(f.read().strip(), True))
    with open('21.input') as f:
        print(run(f.read().strip()))
