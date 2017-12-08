import sys
def run(_in):
    valid_count = 0
    phrases = _in.strip().split('\n')
    for phrase in phrases:
        words = phrase.split()
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
    print(run(sys.stdin.read()))
