# 마법사 상어와 비바라기
# 비바라기 -> (N, 1) (N, 2) (N-1, 1) (N-1, 2) -> 이동 M번

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range (N)]
move = [list(map(int, input().split())) for _ in range (M)]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 초기 비구름 생성
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for m in range (M):
    # 구름 이동
    visited = [[0] * N for _ in range(N)]
    d, s = move[m]
    for i in range (len(cloud)):
        r, c = cloud[i]
        nr = (r + dr[d-1] * s + N) % N
        nc = (c + dc[d-1] * s + N) % N
        cloud[i] = [nr, nc]

    # 물의 양 증가
    for r, c in cloud:
        visited[r][c] = 1
        A[r][c] += 1

    for r, c in cloud:
        # 물이 증가한 칸에 물복사버그 마법
        cnt = 0
        for k in range (1, 8, 2):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if A[nr][nc] > 0:
                    cnt += 1
        A[r][c] += cnt

    new_cloud = []
    for i in range (N):
        for j in range (N):
            if A[i][j] >= 2 and not visited[i][j]:
                new_cloud.append([i, j])
                A[i][j] -= 2

    cloud = new_cloud

answer = 0
for i in range (N):
    for j in range (N):
        answer += A[i][j]
print(answer)