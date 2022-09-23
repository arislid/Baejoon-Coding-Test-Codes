# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

chess_list = [1, 1, 2, 2, 2, 8]

input_list = list(map(int, input().split()))
output_list = [chess_list[i] - input_list[i] for i in range(len(chess_list))]

for i in output_list:
    print(i, end=" ")