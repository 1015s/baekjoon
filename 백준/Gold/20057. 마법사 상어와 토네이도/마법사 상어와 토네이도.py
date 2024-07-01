# 마법사 상어와 토네이도

N = int(input())

A = []
for i in range (N):
    A.append(list(map(int, input().split())))

sr = sc = N // 2

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
p = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]

# 배열을 90도 반시계 방향으로 회전
def rotate_90(proportion):
    new_proportion = list(reversed(list(zip(*proportion))))
    return new_proportion

p1 = rotate_90(p)
p2 = rotate_90(p1)
p3 = rotate_90(p2)

proportions = [p, p1, p2, p3]
alphas = [[2, 1], [3, 2], [2, 3], [1, 2]]

answer = 0

tr = sr
tc = sc

curl = 0
turn = 2
now = 0
proportion = proportions[0]

while not (tr == 0 and tc == 0):

    # 토네이도 이동
    tr += dr[curl]
    tc += dc[curl]
    now += 1
    sand = A[tr][tc]
    A[tr][tc] = 0
    left = sand

    # 모래 정보 갱신
    for r in range (5):
        for c in range (5):
            now_sand = int (sand * proportion[r][c])
            left -= now_sand

            if 0 <= tr + r - 2 < N and 0 <= tc + c -2 < N:
                A[tr + r -2][tc + c - 2] += now_sand
            else:
                answer += now_sand
    # alpha 위치에 남은 모래 두기
    if 0 <= tr + alphas[curl][0] - 2 < N and 0 <= tc + alphas[curl][1] - 2 < N:
        A[tr + alphas[curl][0] - 2][tc + alphas[curl][1] - 2] += left
    else:
        answer += left
    
    # 토네이도 방향 바꾸기
    if now == turn or now == turn // 2:
        curl = (curl + 1) % 4
        proportion = proportions[curl]

        if now == turn:
            now = 0
            turn += 2

print(answer)


