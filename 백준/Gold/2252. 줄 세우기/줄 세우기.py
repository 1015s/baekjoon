# 줄 세우기 - 위상정렬 (순서 존재)
from collections import deque

N, M = map(int, input().split())
board = [[] for _ in range (N+1)]
in_node = [0] * (N+1)
for i in range (M):
    s, e = map(int, input().split())
    board[s].append(e)
    in_node[e] += 1

q = deque()
result = []

for i in range (1, N+1):
    if in_node[i] == 0: # 진입 0 이면 q에 넣기
        q.append(i)

while q:
    cur = q.popleft()
    result.append(cur)

    # 현재에서 나가는 간선 제거
    for n in board[cur]:
        in_node[n] -= 1
        if in_node[n] == 0:
            q.append(n)

for i in range (N):
    print(result[i], end=" ")