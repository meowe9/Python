x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x2) - abs(x1) <= 1 and abs(y2) - abs(y1) <= 1:
    print('YES')
else:
    print('NO')