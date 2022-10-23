import sys
def input():
    return sys.stdin.readline().rstrip()

def sort_num(N):
    num_list = []
    for i in range(N):
        n = int(input())
        num_list.append(n)

    num_list.sort()
    def print_list(num_list):
        for i in num_list:
            print(i)
    return num_list

def statistic(N):
    num_list = sort_num(N)
    def mean(num_list):
        return round(sum(num_list) / len(num_list))
    def mid(num_list):
        return num_list[int(N/2) - 1] if N % 2 == 0 else num_list[int(N / 2)]
    def most_value(num_list):
        set_list = set(num_list)
        dict_list = {}
        for i in num_list:
            if i not in dict_list.keys():
                dict_list[i] = 1
            else:
                dict_list[i] += 1
            # count_list = num_list.count(i)
            # dict_list[i] = count_list
        # sort_dict_list = dict(sorted(dict_list.items(), key=lambda item: item[1], reverse=True))
        max_value = max(dict_list.values())
        count_list = [n for n in dict_list.keys() if dict_list[n] == max_value]
        return count_list[0] if len(count_list) == 1 else count_list[1]

    def list_range(num_list):
        if N == 1:
            return 0
        else:
            return abs(max(num_list) - min(num_list))

    print(mean(num_list))
    print(mid(num_list))
    print(most_value(num_list))
    print(list_range(num_list))

if __name__ == '__main__':
    N = int(input())
    statistic(N)