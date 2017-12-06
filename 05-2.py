def run(_in):
    instructions = list(map(lambda s: int(s), _in.strip().split()))
    pos = 0
    steps = 0
    while pos >= 0 and pos < len(instructions):
        steps += 1
        instruction = instructions[pos]
        instructions[pos] += -1 if instruction >= 3 else 1
        pos += instruction

    return steps

if __name__ == '__main__':
    import sys
    print(run(sys.stdin.read()))
