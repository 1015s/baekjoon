# 게리맨더링2
# 인구가 가장 많은 선거구 - 가장 적은 선거구가 min

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
total = 0
for matrix in board:
    total += sum(matrix)

def calc_people(i, j, d1, d2):
    global total
    people = [0] * 5
    visited = [[False] * N for _ in range (N)]

    # 1번
    col1 = j+1
    for k in range (i+d1):
        if k >= i:
            col1 -= 1
        people[0] += sum(board[k][:col1])

    # 2번
    col2 = j+1
    for k in range (i+d2+1):
        if k > i:
            col2 += 1
        people[1] += sum(board[k][col2:])


    # 3번
    col3 = j-d1
    for k in range (i+d1, N):
        people[2] += sum(board[k][:col3])
        if k < i+d1+d2:
            col3 += 1

    # 4번
    col4 = j+d2
    for k in range (i+d2+1, N):
        people[3] += sum(board[k][col4:])
        if k <= i+d1+d2:
            col4 -= 1

    # 5번
    people[4] = total - (people[0] + people[1] + people[2] + people[3])

    # 모든 선거 구는 구역을 적어도 하나는 포함해야 함
    if people.count(0) > 0:
        return -1

    max_gu = max(people)
    min_gu = min(people)

    return abs(max_gu - min_gu)


answer = []
# 기준점, 경계 길이 정해서 brute force
for i in range (N-2):
    for j in range (1, N-1):
        for d1 in range (1, N-1):
            for d2 in range (1, N-1):
                if 0 <= i+d1-1 < N and 0 <= i+d2-1 < N and 0 <= j-d1+d2-1 < N:
                    if i+d1+d2 < N and j>=d1 and j+d2<N:
                        # 각 선거구 별로 인원 세기
                        result = calc_people(i, j, d1, d2)
                        if result >= 0 :
                            answer.append(result)

print(min(answer))