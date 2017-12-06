import sys
_in = sys.stdin.read().strip()

rows = _in.split('\n')
rows = map(lambda row: row.split(), rows)

def dink(row):
    for idx in range(len(row)):
        for idx2 in range(len(row)):
            if idx == idx2:
                continue
            a = row[idx]
            b = row[idx2]
            if a % b == 0:
                return a // b

checksum = 0

for row in rows:
    row = list(map(lambda number: int(number), row))
    checksum += dink(row)

print(checksum)
