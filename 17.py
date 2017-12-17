def run(_in):
    step = int(_in)

    buf = [0]
    pos = 0

    for i in range(1, 2018):
        pos = (pos + step) % len(buf)
        pos += 1
        buf[pos:pos] = [i]

    return buf[pos+1]


if __name__ == '__main__':
    with open('17.example.input') as f:
        print(run(f.read().strip()))
    with open('17.input') as f:
        print(run(f.read().strip()))
