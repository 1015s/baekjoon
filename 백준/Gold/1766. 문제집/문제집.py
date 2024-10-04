# 문제집 - 위상정렬 (우선순위 큐)
import heapq

N, M = map(int, input().split())
board = [[] for _ in range (N+1)]
inbound = [0] * (N+1)

for _ in range (M):
    s, e = map(int, input().split())
    board[s].append(e)
    inbound[e] += 1

result = []
q = []
for i in range (1, N+1):
    if inbound[i] == 0:
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    result.append(cur)
    for n in board[cur]:
        inbound[n] -= 1
        if inbound[n] == 0:
            heapq.heappush(q, n)

for i in result:
    print(i, end=" ")