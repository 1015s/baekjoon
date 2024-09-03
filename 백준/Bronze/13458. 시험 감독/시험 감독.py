# 시험 감독
# 필요한 감독관 수의 최솟값 -> 부감독관을 몇 명 배치하느냐

N = int(input())
A = list(map(int, input().split()))

B, C = map(int, input().split())

answer = 0

# 총 감독관 1명씩 배정
answer += N
for i in range (N):
    answer += max(0, (A[i] - B + C - 1) // C)

print(answer)