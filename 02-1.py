import sys
_in = sys.stdin.read().strip()

rows = _in.split('\n')
rows = map(lambda row: row.split(), rows)

checksum = 0

for row in rows:
    row = list(map(lambda number: int(number), row))
    checksum += max(row) - min(row)

print(checksum)
