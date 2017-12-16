from functools import reduce, lru_cache
from itertools import count

def scramble(_in, positions):
    out = list()
    for position in positions:
        out.append(_in[position])
    return tuple(out)

@lru_cache()
def compile_positions(instructions, n=1):
    programs = list("abcdefghijklmnop")
    inprograms = list(programs)

    if n == 1:
        for instruction in instructions:
            if instruction[0] == 's':
                spin = int(instruction[1:])
                programs[0:0] = programs[-spin:]
                programs = programs[:16]
            elif instruction[0] == 'x':
                a, b = map(lambda n: int(n), instruction[1:].split('/'))
                temp = programs[a]
                programs[a] = programs[b]
                programs[b] = temp
            elif instruction[0] == 'p':
                a, b = instruction[1:].split('/')
                apos = programs.index(a)
                bpos = programs.index(b)
                programs[apos] = b
                programs[bpos] = a

        inpositions = list()
        for program in programs:
            inpositions.append(inprograms.index(program))

        return tuple(inpositions)


    else:
        n1 = n//2
        if n % 2 == 0:
            n2 = n//2
        else:
            n2 = n//2 + 1
        positions1 = compile_positions(instructions, n1)
        positions2 = compile_positions(instructions, n2)
        positions = scramble(positions2, positions1)
        print(n, n1, n2)
        print(positions, positions1, positions2)
        return tuple(positions)

def run(_in):
    instructions = tuple(_in.split(','))
    programs = list("abcdefghijklmnop")

    positions_one = compile_positions(instructions, 1)

    positions_billion = compile_positions(instructions, int(1e9))

    one = scramble(programs, positions_one)
    billion = scramble(programs, positions_billion)

    return (''.join(one), ''.join(billion))



if __name__ == '__main__':
    with open('16.input') as f:
        print(run(f.read().strip()))
