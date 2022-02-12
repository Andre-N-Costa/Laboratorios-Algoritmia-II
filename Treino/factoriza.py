import math

def factoriza(n):
    i = 1
    suml = []
    sum = 0
    for m in range(n + 1):
        suml.append(-1)
    if n % 2 == 0:
        suml[2] = 1
        n = n/2
    while n % 2 == 0:
        n = n/2
    for i in range(3,int(math.sqrt(n)) + 1,2):
        print(i)
        while n % i == 0:
            n = n/i
            suml[i] = 1
    suml[int(n)] = 1
    for n in suml:
        if n == 1:
            i = suml.index(n)
            sum = sum + i
            suml[i] = -1
    return sum
