

a = int(input())
b = int(input())
c = int(input())
d = int(input())

header = "\t"
for j in range(c, d + 1):
    header += str(j) + "\t"
print(header)

for i in range(a, b + 1):
    row = str(i) + "\t"
    for j in range(c, d + 1):
        row += str(i * j) + "\t"
    print(row)
