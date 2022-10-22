from math import ceil

def acm_hotel(T):
    res = []
    for i in range(T):
        h, w, n = map(int, input().split())
        a = ceil(n / h)
        b = n % h
        ans = ''
        if b == 0:
            if a < 10:
                ans = str(h) + '0' + str(a)
            else:
                ans = str(h) + str(a)
        else:
            if a < 10:
                ans = str(b) + '0' + str(a)
            else:
                ans = str(b) + str(a)
        res += [ans]
    return res

if __name__ == '__main__':
    T = int(input())
    res = acm_hotel(T)
    for i in res:
        print(i)