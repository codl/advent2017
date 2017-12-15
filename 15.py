class Generator(object):
    def __init__(self, factor, seed):
        self.factor = factor
        self.state = seed

    def __iter__(self):
        return self

    def __next__(self):
        self.state = (self.state * self.factor) % 2147483647
        return self.state % (2 ** 16)

def run(_in):
    args = _in.split('\n')
    gen_a = Generator(16807, int(args[0]))
    gen_b = Generator(48271, int(args[1]))

    count = 0
    count2 = 0
    for a, b, i in zip(gen_a, gen_b, range(int(40e6))):
        if a == b:
            count += 1

    return count


if __name__ == '__main__':
    with open('15.example.input') as f:
        print(run(f.read().strip()))
    with open('15.input') as f:
        print(run(f.read().strip()))
