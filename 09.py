class Group(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.children = set()
        if parent:
            self.depth = parent.depth + 1
            parent.children.add(self)
        else:
            self.depth = 1

    def score_with_children(self):
        score = self.depth
        for child in self.children:
            score += child.score_with_children()

        return score


def run(_in):
    current = None
    top = None
    expect_garbage = False
    expect_skip = False
    garbage_count = 0
    for char in _in:
        if expect_skip:
            expect_skip = False
        elif expect_garbage:
            if char == '!':
                expect_skip = True
            elif char == '>':
                expect_garbage = False
            else:
                garbage_count += 1
        elif char == '<':
            expect_garbage = True
        elif char == '{':
            if not current:
                current = Group()
                top = current
            else:
                current = Group(current)
        elif char == '}':
            current = current.parent

    return (top.score_with_children(), garbage_count)


if __name__ == '__main__':
    with open('09.input') as f:
        print(run(f.read().strip()))
