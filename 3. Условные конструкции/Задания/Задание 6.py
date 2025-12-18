a = int(input())
b = int(input())
c = int(input())
d = max(a,b,c)
i = min(a,b,c)
k = (a + b + c) - d - i
if i + k <= d:
    print('Не существует')
elif c**2==a**2+b**2:
    print('Прямоугольный')
elif d **2 > (i **2 + k **2):
    print('Тупоугольный')
elif c**2 < (a**2+b**2):
    print('Остроугольный')