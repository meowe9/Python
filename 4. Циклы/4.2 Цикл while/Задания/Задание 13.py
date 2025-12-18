start_sum = int(input())
target_sum = int(input())
percent = int(input())
a = (percent + 100)/100
while start_sum <  target_sum :
    start_sum *= a
    print(start_sum)