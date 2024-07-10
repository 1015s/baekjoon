# 마법사 상어와 파이어스톰

from collections import deque

N, Q = map(int, input().split())
N = 1 << N
A = [list(map(int, input().split())) for _ in range (N)]
levels = list(map(int, input().split()))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for level in levels:
    # 격자 나누기 -> 시계 방향 회전
    size = 1 << level
    _A = [[0] * N for _ in range (N)]
    for i in range (N // size):
        for j in range (N // size):
            sr, sc = i*size, j*size
            for r in range (size):
                for c in range (size):
                    _A[sr+r][sc+c] = A[sr+size-c-1][sc+r]
    A = _A
    # 얼음 양 줄이기 - 얼음이 있는 칸이 3개이상 인접하지 않으면 얼음양 1 줄이기
    melt = []
    for i in range (N):
        for j in range (N):
            cnt = 0
            for k in range (4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0:
                    cnt += 1
            if cnt < 3 and A[i][j] > 0:
                melt.append([i, j])
    for r, c in melt:
        A[r][c] -= 1

def bfs(i, j):
    ice_size = 0
    visited = [[False] * N for _ in range (N) ]
    q = deque()
    q.append([i, j])
    while q:
        r, c = q.popleft()
        for k in range (4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append([nr, nc])
                ice_size += 1

    return ice_size


# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 - bfs

max_ice = 0
sum = 0
for i in range (N):
    for j in range (N):
        sum += A[i][j]
        if A[i][j] > 0:
            max_ice = max(max_ice, bfs(i, j))

print(sum)
print(max_ice)