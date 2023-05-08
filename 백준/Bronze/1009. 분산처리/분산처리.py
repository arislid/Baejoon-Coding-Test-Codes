n = int(input())
res = []
for i in range(n):
    a, b = map(int, input().split())
    a = a % 10
    if a in [1, 5, 6]:
        res.append(a)
    elif a == 2:
        check = [6, 2, 4, 8]
        res.append(check[b%4])
    elif a == 3:
        check = [1, 3, 9, 7]
        res.append(check[b%4])
    elif a == 4:
        check = [6, 4]
        res.append(check[b%2])
    elif a == 7:
        check = [1, 7, 9, 3]
        res.append(check[b%4])
    elif a == 8:
        check = [6, 8, 4, 2]
        res.append(check[b%4])
    elif a == 9:
        check = [1, 9]
        res.append(check[b%2])
    else:
        res.append(10)
for _ in res:
    print(_)