# 인구 이동
# 국경선 열기 -> 인구 이동
from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

day = 0

while(1):
    unions = []
    # 국경선 열기 - bfs
    visited = [[0] * N for _ in range (N)]
    for i in range (N):
        for j in range (N):
            if visited[i][j] == 0:
                # bfs
                union = set()
                q = deque()
                q.append([i, j])
                union.add((i, j))
                while q:
                    r, c = q.popleft()
                    for k in range (4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                            if L <= abs(board[nr][nc] - board[r][c]) <= R:
                                q.append([nr, nc])
                                union.add((nr, nc))
                                visited[nr][nc] = 1
                if len(union) > 1:
                    unions.append(union)

    if len(unions) == 0: # 인구이동 끝
        break

    # 인구이동
    for u in unions:
        num = len(u)
        total = 0
        for r, c in u:
            total += board[r][c]
        amount = total // num
        for r, c in u:
            board[r][c] = amount

    day += 1
print(day)
