class Program(object):
    def __init__(self, name, weight):
        self.name = name
        self.parent = None
        self.children = set()
        self.weight = weight
        self._weight_with_children = None

    def weight_with_children(self):
        if self._weight_with_children is not None:
            return self._weight_with_children

        weight = self.weight
        for child in self.children:
            weight += child.weight_with_children()

        self._weight_with_children = weight

        return weight

    def odd_one_out(self):
        children = list(self.children)
        for _ in range(len(children)):
            child = children.pop()
            if all((child.weight_with_children() != other.weight_with_children() for other in children)):
                return child
            children.insert(0, child)


def run(_in):
    lines = _in.split('\n')

    programs = dict()
    parents = dict()

    for line in lines:
        args = line.split()
        name = args[0]
        weight = int(args[1].strip('()'))

        if len(args) > 2:
            children = set(map(lambda a: a.strip(','), args[3:]))
            for child in children:
                parents[child] = name

        programs[name] = Program(name, weight)

    current = lines[0].split()[0]
    while current in parents:
        current = parents[current]

    top = programs[current]

    for child_name in parents:
        parent = programs[parents[child_name]]
        child = programs[child_name]

        child.parent = parent
        parent.children.add(child)

    current = top
    _next = current
    while _next:
        current = _next
        _next = current.odd_one_out()

    wrong = current

    current = wrong.parent
    right = next((child for child in current.children if child is not wrong))
    diff = right.weight_with_children() - wrong.weight_with_children()

    return (top.name, wrong.weight + diff)


if __name__ == '__main__':
    import sys
    print(run(sys.stdin.read().strip()))
