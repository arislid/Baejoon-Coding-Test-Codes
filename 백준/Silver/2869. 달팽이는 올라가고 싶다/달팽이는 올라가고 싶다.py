from math import ceil

def snail_up(a, b, v):
    if a == v:
        return 1
    else:
        return ceil((v-a) / (a-b) + 1)

if __name__ == '__main__':
    a, b, v = map(int, input().split())
    print(snail_up(a, b, v))