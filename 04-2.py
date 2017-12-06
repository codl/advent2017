def sorted(string: str):
    output = ""
    while string:
        _min = min(string)
        minidx = string.index(_min)
        string = string[:minidx] + string[minidx+1:]
        output += _min

    return output
def run(_in):
    valid_count = 0
    phrases = _in.strip().split('\n')
    for phrase in phrases:
        words = phrase.split()
        words = list(map(sorted, words))
        invalid = False
        while words:
            word = words.pop()
            if word in words:
                invalid = True
                break

        if not invalid:
            valid_count += 1

    return valid_count

if __name__ == '__main__':
    import sys
    print(run(sys.stdin.read()))
