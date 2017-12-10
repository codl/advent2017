def sign(n):
    return 1 if n >= 0 else -1

class CircularList(object):
    def __init__(self, length):
        self.items = list(range(length))

    def __getitem__(self, key):
        if isinstance(key, slice):
            step = key.step
            if step is None:
                step = 1

            idx = key.start
            bleh = list()
            while idx * sign(step) < key.stop * sign(step):
                bleh.append(self[idx])
                idx += step
            return bleh

        else:
            key = key % len(self.items)
            return self.items[key]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            step = key.step
            if step is None:
                step = 1

            idx = key.start
            idxv = 0
            while idx * sign(step) < key.stop * sign(step):
                self[idx] = value[idxv]
                idx += step
                idxv += 1

        else:
            key = key % len(self.items)
            self.items[key] = value

    def __repr__(self):
        return repr(self.items)

def run(_in, length=256):
    steps = map(lambda n: int(n.strip()), _in.split(','))

    clist = CircularList(length)
    skip = 0
    idx = 0

    for step in steps:
        if step > 0:
            clist[idx:idx+step] = clist[idx+step-1:idx-1:-1]
        idx += step
        idx += skip
        skip += 1

    return clist[0] * clist[1]


if __name__ == '__main__':
    with open('10-1.example.input') as f:
        print(run(f.read().strip(), 5))
    with open('10.input') as f:
        print(run(f.read().strip()))
