# O(n)의 시간복잡도를 고려해서 for문 한 번 만으로도 경우의 수 셀 수 있도록 짤 것
def two_pointer(sequence, x):
    count = 0
    start = 0
    end = len(sequence) - 1
    sequence.sort()
    while start < end:
        if sequence[start] + sequence[end] == x:
            count += 1
            start += 1
            end -= 1
        elif sequence[start] + sequence[end] < x:
            start += 1
        else:
            end -= 1
    return count

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    x = int(input())

    result = two_pointer(sequence, x)
    print(result)

if __name__ == "__main__":
    main()