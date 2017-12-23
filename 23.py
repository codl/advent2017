def isprime(num):
    for x in (2,) + tuple(range(3, num//2, 2)):
        if num % x == 0:
            return False
    return True


def run(_in):
    lines = _in.splitlines()

    b = None
    for line in lines:
        if line.startswith('set b'):
            b = int(line.split(' ')[2])

    solution1 = (b-2)**2

    not_prime_count = 0

    for i in range(0, 1001):
        if not isprime(i*17 + b*100 + 100000):
            not_prime_count += 1

    solution2 = not_prime_count

    return (solution1, solution2)




if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.input') as f:
        print(run(f.read().strip()))
