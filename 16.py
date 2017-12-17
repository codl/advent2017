from functools import reduce
from textwrap import indent, dedent
from itertools import count

def compile_instructions(instructions, length):
    code = ''
    for instruction in instructions:
        if instruction[0] == 's':
            spin = int(instruction[1:])
            nips = length - spin
            code += f'''
            programs += programs[:{nips}]
            programs[:{-length}] = []
            '''
        elif instruction[0] == 'x':
            a, b = map(lambda n: int(n), instruction[1:].split('/'))
            code += f'''
            temp = programs[{a}]
            programs[{a}] = programs[{b}]
            programs[{b}] = temp
            '''
        elif instruction[0] == 'p':
            a, b = instruction[1:].split('/')
            code += f'''
            apos = programs.index('{a}')
            bpos = programs.index('{b}')
            programs[apos] = '{b}'
            programs[bpos] = '{a}'
            '''

    code = 'def dance(programs):\n{}'.format(indent(dedent(code), ' '))

    scope = dict()

    exec(code, scope)

    return scope['dance']

def run(_in, length=16):
    instructions = _in.split(',')
    programs = list("abcdefghijklmnop")[:length]
    seen = list()
    seen.append(tuple(programs))

    dance = compile_instructions(instructions, length)

    for i in count():
        dance(programs)
        if i == 0:
            solution1 = ''.join(programs)
        tprograms = tuple(programs)
        if tprograms not in seen:
            seen.append(tprograms)
        else:
            intro_len = seen.index(tprograms)
            cycle_len = i + 1 - intro_len
            break

    solution2 = seen[intro_len + (int(1e9) - intro_len) % cycle_len]

    solution2 = ''.join(solution2)

    return (solution1, solution2)



if __name__ == '__main__':
    with open('16.example.input') as f:
        print(run(f.read().strip(), 5))
    with open('16.input') as f:
        print(run(f.read().strip()))
