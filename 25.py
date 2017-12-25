from collections import defaultdict

def machine_step_example(state, tape, pos, step, diag):
    if state == 'A':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
        else:
            tape[pos] = 0
            pos -= 1
        state = 'B'
    else:
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
        else:
            tape[pos] = 1
            pos += 1
        state = 'A'

    step += 1

    if step == 6:
        diag = 0
        for pos in tape:
            if tape[pos]:
                diag += 1

    return state, tape, pos, step, diag


def machine_step(state, tape, pos, step, diag):
    if state == 'A':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'B'
        else:
            tape[pos] = 0
            pos -= 1
            state = 'C'
    elif state == 'B':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'A'
        else:
            tape[pos] = 1
            pos += 1
            state = 'D'
    elif state == 'C':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'A'
        else:
            tape[pos] = 0
            pos -= 1
            state = 'E'
    elif state == 'D':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'A'
        else:
            tape[pos] = 0
            pos += 1
            state = 'B'
    elif state == 'E':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'F'
        else:
            tape[pos] = 1
            pos -= 1
            state = 'C'
    elif state == 'F':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'D'
        else:
            tape[pos] = 1
            pos += 1
            state = 'A'

    step += 1

    if step == 12173597:
        diag = 0
        for pos in tape:
            if tape[pos]:
                diag += 1

    return state, tape, pos, step, diag

def run(example = False):
    state = 'A'
    tape = defaultdict(lambda: 0)
    pos = 0
    step = 0
    diag = None
    m = machine_step
    if example:
        m = machine_step_example
    while diag is None:
        state, tape, pos, step, diag = \
                m(state, tape, pos, step, diag)
    return diag



if __name__ == '__main__':
    print(run(True))
    print(run(False))
