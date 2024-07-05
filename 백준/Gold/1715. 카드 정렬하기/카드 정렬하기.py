# 카드 정렬하기
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한가
import heapq

N = int(input())
arr = [int(input()) for _ in range (N)]
arr.sort()

heap = arr

answer = 0
for i in range (N-1):
    if len(heap) >= 2:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        answer += (first + second)
        heapq.heappush(heap, first+second)

print(answer)