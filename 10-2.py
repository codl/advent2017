from functools import reduce

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

def run(_in):
    inputs = _in.split('\n')
    output = ''
    for _in2 in inputs:
        steps = list(_in2.encode('ASCII'))
        steps += [17, 31, 73, 47, 23]

        sparse = CircularList(256)
        skip = 0
        idx = 0

        for _ in range(64):
            for step in steps:
                sparse[idx:idx+step] = sparse[idx+step-1:idx-1:-1]
                idx += step
                idx += skip
                skip += 1

        dense = list()
        for i in range(16):
            block = sparse[i*16:(i+1)*16]
            byte = reduce(lambda x, y: x ^ y, block)
            dense.append(byte)

        digest = ''
        for byte in dense:
            hexbyte = format(byte, '02x')
            digest += hexbyte

        output += digest + '\n'

    return output



if __name__ == '__main__':
    with open('10-2.example.input') as f:
        print(run(f.read().rstrip()))
    with open('10.input') as f:
        print(run(f.read().strip()))
