get_generators = __import__('15', fromlist=('get_generators',)).get_generators


def run(_in):
    gen_a, gen_b = get_generators(_in)

    gen_a = filter(lambda a: a%4 == 0, gen_a)
    gen_b = filter(lambda b: b%8 == 0, gen_b)

    count = 0
    for a, b, i in zip(gen_a, gen_b, range(int(5e6))):
        if a == b:
            count += 1

    return count


if __name__ == '__main__':
    with open('15.example.input') as f:
        print(run(f.read().strip()))
    with open('15.input') as f:
        print(run(f.read().strip()))
