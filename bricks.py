n = int(input())
m = int(input())

matrix = []
startIndex = 1
def convertoint(vals):
    toint = []
    for i in vals:
        toint.append(int(i))
    return toint


for i in range(n):
    vals = convertoint(input().split())
    if len(vals) != m:
        print("-1")
        break
    matrix.append(vals)
    print(matrix)

empty_matrix = []
for i in range(n):
    empty_list = []
    for y in range(m):
        empty_list.append(0)
    empty_matrix.append(empty_list)
    print(empty_matrix)

if (n * m) % 2 == 0 and n < 100 or m < 100:

    for i in range(n):
        for y in range(m - 1):
            if empty_matrix[i][y] == 0:
                if matrix[i][y] != matrix[i][y + 1]:
                    empty_matrix[i][y] = startIndex
                    empty_matrix[i][y + 1] = startIndex
                    startIndex += 1

    for i in range(n - 1):
        for y in range(m):
            if empty_matrix[i][y] == 0:
                if matrix[i][y] != matrix[i + 1][y]:
                    empty_matrix[i][y] = startIndex
                    empty_matrix[i + 1][y] = startIndex
                    startIndex += 1
else:
    print("-1")

print(empty_matrix)
