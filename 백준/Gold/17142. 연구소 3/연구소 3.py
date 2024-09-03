# 연구소 3
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 10e5

# 바이러스 퍼뜨리기 - bfs
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def virus(virus_combination):
    global answer

    time = 0
    virus_blank = 0

    q = deque()
    tmp_board = [[-1] * N for _ in range (N)]
    visited = [[False] * N for _ in range (N)]

    for r, c in virus_combination:
        tmp_board[r][c] = 0
        q.append([r, c])
        visited[r][c] = True

    while q:
        r, c = q.popleft()
        for k in range (4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if board[nr][nc] != 1: # 벽이 아닌 경우
                    tmp_board[nr][nc] = tmp_board[r][c] + 1
                    q.append([nr, nc])
                    if board[nr][nc] == 0:
                        time = max(time, tmp_board[nr][nc])
                        virus_blank += 1
                    visited[nr][nc] = True

    if blank != virus_blank: # 바이러스 다 안퍼짐
        return

    # answer 값 업데이트
    answer = min(answer, time)

# 빈 칸 갯수, 전체 바이러스 위치 저장
blank = 0
virus_pos = []
for i in range (N):
    for j in range (N):
        if board[i][j] == 0:
            blank += 1
        elif board[i][j] == 2:
            virus_pos.append([i, j])

# 바이러스 조합 고르기
virus_combinations = combinations(virus_pos, M)

# 바이러스 퍼뜨리기
for virus_combination in virus_combinations:
    virus(virus_combination)

if answer == 10e5:
    answer = -1
print(answer)