from collections import Counter

def find_pairs(sequence, x):
    count = 0
    counter = Counter(sequence)

    for num in counter:
        complement = x - num
        if complement in counter and complement != num:
            count += counter[num] * counter[complement]

    return count // 2

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    x = int(input())

    result = find_pairs(sequence, x)
    print(result)

if __name__ == "__main__":
    main()