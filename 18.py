from collections import defaultdict
from threading import Thread, Event, Semaphore
from queue import Queue

def run_program(instructions, part, pid=None, qin=None, qout=None, evt=None, sem=None):
    registers = defaultdict(lambda: 0)
    if part == 1:
        playing = None
    elif part == 2:
        sent_count = 0
        registers['p'] = pid
    idx = 0

    while True:
        instruction, *args = instructions[idx]
        values = list()
        for arg in args:
            if arg.isalpha():
                values.append(registers[arg])
            else:
                values.append(int(arg))

        #print(instruction, args, values, pid)

        if instruction == 'set':
            registers[args[0]] = values[1]
        elif instruction == 'add':
            registers[args[0]] += values[1]
        elif instruction == 'mul':
            registers[args[0]] *= values[1]
        elif instruction == 'mod':
            registers[args[0]] %= values[1]
        elif instruction == 'jgz':
            if values[0] > 0:
                idx += values[1]
                continue
        elif instruction == 'snd':
            if part == 1:
                playing = values[0]
            else:
                qout.put(values[0])
                sent_count += 1
        elif instruction == 'rcv':
            if part == 1:
                if values[0] != 0:
                    return playing
            else:
                with sem:
                    evt.set()
                    val = qin.get()
                    if val:
                        registers[args[0]] = val
                    else:
                        break

        idx += 1

    # part 2
    qout.put(sent_count)

def run(_in):
    instructions = _in.split('\n')
    instructions = tuple(map(lambda i: tuple(i.split(' ')), instructions))

    solution1 = run_program(instructions, 1)

    evt = Event()
    sem = Semaphore(2)
    q12 = Queue()
    q21 = Queue()
    t1 = Thread(target = run_program, args = (instructions, 2, 0, q21, q12, evt, sem))
    t2 = Thread(target = run_program, args = (instructions, 2, 1, q12, q21, evt, sem))
    t1.start()
    t2.start()
    while True:
        if sem.acquire(timeout=1):
            sem.release()
        else:
            q12.put(None)
            q21.put(None)
            t1.join()
            t2.join()
            solution2 = q21.get()
            break

    return (solution1, solution2)


if __name__ == '__main__':
    with open('18.example.input') as f:
        print(run(f.read().strip()))
    with open('18.input') as f:
        print(run(f.read().strip()))
