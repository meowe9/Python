x = int(input())
if x % 100 == 11:
    print("грибов")
elif 2 <= x % 10 <= 4:
    print("гриба")
elif x % 10 == 1:
    print("гриб")
else:
    print("грибов")