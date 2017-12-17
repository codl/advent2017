from functools import reduce

def run(_in):
    instructions = _in.split(',')
    programs = list("abcdefghijklmnop")

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

    return reduce(lambda a, b: a+b, programs)



if __name__ == '__main__':
    with open('16.input') as f:
        print(run(f.read().strip()))
