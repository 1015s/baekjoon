# 달팽이
N = int(input())
target = int(input())

arr = [[0] * N for _ in range (N)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 시작 좌표
d = 1
r, c = N // 2, N // 2
arr[r][c] = 1
cnt = 2
answer_r, answer_c = r, c

while(1):
    if cnt > N*N:
        break
    for i in range (4):
        for j in range (d):
            if cnt > N*N:
                break
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                arr[nr][nc] = cnt
                r, c = nr, nc
                if cnt == target:
                    answer_r, answer_c = r, c
                cnt += 1

        if i % 2 == 1:
            d += 1

for i in range (N):
    for j in range (N):
        print(arr[i][j], end=" ")
    print()
print(answer_r+1, answer_c+1)