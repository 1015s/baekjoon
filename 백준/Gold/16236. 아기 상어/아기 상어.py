# 아기 상어
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

s_size = 2
s_r, s_c = -1, -1
for i in range (N):
    for j in range (N):
        if board[i][j] == 9:
            s_r, s_c = i, j
            board[i][j] = 0

time = 0

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

k = 0

while(1):
    # 상어 이동
    visited = [[-1] * N for _ in range (N)]
    cand = []
    q = deque()
    q.append([s_r, s_c])
    visited[s_r][s_c] = 0

    while q:
        r, c = q.popleft()
        for i in range (4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                if board[nr][nc] <= s_size: # 지나갈 수 있는 물고기
                    visited[nr][nc] = visited[r][c] + 1
                    q.append([nr, nc])
                    if 0 < board[nr][nc] < s_size:
                        cand.append([visited[nr][nc], nr, nc])

    if not cand: # 더 이상 이동 불가
        break

    cand.sort()
    dist, s_r, s_c = cand[0]

    # 상어 이동시키기
    time += dist
    k += 1
    board[s_r][s_c] = 0

    # 상어 크기
    if k == s_size:
        s_size += 1
        k = 0

print(time)
