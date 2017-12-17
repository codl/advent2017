class LinkedList(object):
    def __init__(self):
        start = [0, None]
        start[1] = start

        self.current = start

    def insert(self, value):
        new = [value, self.current[1]]
        self.current[1] = new
        self.current = new

    def advance(self, steps):
        for i in range(steps):
            self.current = self.current[1]

    def find(self, value):
        while self.current[0] != value:
            self.advance(1)

def run(_in):
    step = int(_in)

    buf = LinkedList()

    for i in range(1, int(50e6)+1):
        buf.advance(step)
        buf.insert(i)
        if i == 2017:
            solution1 = buf.current[1][0]
        if i % 100000 == 0:
            print(i)

    buf.find(0)
    buf.advance(1)
    solution2 = buf.current[0]

    # let's help the reference counter
    buf.current[1] = None
    del buf.current

    return solution1, solution2


if __name__ == '__main__':
    with open('17.example.input') as f:
        print(run(f.read().strip()))
    with open('17.input') as f:
        print(run(f.read().strip()))
