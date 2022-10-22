def sort_num(N):
    num_list = []
    for i in range(N):
        n = int(input())
        num_list.append(n)

    num_list.sort()

    for i in num_list:
        print(i)

if __name__ == '__main__':
    N = int(input())
    sort_num(N)