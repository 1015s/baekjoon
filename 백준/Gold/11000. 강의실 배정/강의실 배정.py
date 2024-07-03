# 강의실 배정 - 우선순위큐 사용
import heapq
import sys

n = int(input())
info = []
for i in range(n):
    info.append(list(map(int, sys.stdin.readline().split())))

# 빨리 시작 - 빨리 끝나는 대로 정렬
info = sorted(info, key=lambda x: x[0])

# 강의실 최소 1개는 있어야 함
heap = [info[0][1]]

for i in range (1, n):
    if info[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, info[i][1])


print(len(heap))