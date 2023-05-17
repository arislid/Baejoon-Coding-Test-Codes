def sum_bewteen_two(sequence, n, k):
    sub_list = [sum(sequence[:k])]
    for i in range(n-k):
        sub_sum = sub_list[i] - sequence[i] + sequence[i+k]
        sub_list.append(sub_sum)
    return max(sub_list)

def main():
    import sys
    n, k = map(int, input().split())
    sequence = list(map(int, sys.stdin.readline().split()))
    result = sum_bewteen_two(sequence, n, k)
    print(result)
    
main()