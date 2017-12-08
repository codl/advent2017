_in = input().strip()

total = 0

for i in range(len(_in)):
    ii = (i+1) % len(_in)
    if _in[i] == _in[ii]:
        total += int(_in[i])

print(total)
