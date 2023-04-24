def fibo(n: int) -> int:
    fibo_list = [0] * (n+1)
    for i in range(n+1):
        if i == 0:
            fibo_list[i] = 0
        elif i == 1:
            fibo_list[i] = 1
        else:
            fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list[i]


n = int(input())
print(fibo(n))