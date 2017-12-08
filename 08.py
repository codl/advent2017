from collections import defaultdict
from math import inf

CMPFUNCS = {
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
    '>=': lambda a, b: a >= b,
    '<=': lambda a, b: a <= b,
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b
}


def run(_in):
    regs = defaultdict(lambda: 0)

    _max = -inf

    instructions = _in.split('\n')
    for instruction in instructions:
        reg, action, value,\
            _if, cmpreg, cmptype, cmpvalue = instruction.split()

        value = int(value)
        cmpvalue = int(cmpvalue)

        if action == 'dec':
            value = -value

        if CMPFUNCS[cmptype](regs[cmpreg], cmpvalue):
            regs[reg] += value

            _max = max(_max, regs[reg])

    return (max(regs.values()), _max)


if __name__ == '__main__':
    import sys
    print(run(sys.stdin.read().strip()))
