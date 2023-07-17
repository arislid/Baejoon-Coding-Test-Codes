c = int(input())
sum_score = 0
high_score = 0
percent = []

for _ in range(c):
    student = list(map(int, input().split()))
    sum_score = sum(student) - student[0]
    mean = sum_score / (len(student) -1)
    
    for j in range(1, len(student)):
        if student[j] > mean:
            high_score += 1
    percent.append(high_score / (len(student) - 1))
    high_score = 0

for i in percent:
    print(f'{i * 100:.3f}%')