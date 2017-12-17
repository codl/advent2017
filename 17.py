from blist import blist

def run(_in):
    step = int(_in)

    buf = blist([0])
    index = 0

    for i in range(1, int(50e6)+1):
        index = (index + step) % len(buf)
        buf.insert(index+1, i)
        index += 1
        if i == 2017:
            solution1 = buf[index+1]

    solution2 = buf[buf.index(0)+1]

    return solution1, solution2


if __name__ == '__main__':
    with open('17.example.input') as f:
        print(run(f.read().strip()))
    with open('17.input') as f:
        print(run(f.read().strip()))
