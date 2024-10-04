# 부분합 - 투포인터

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
answer = 10e7
result = arr[start]
while(1):
    if end >= N: # 종료 조건
        break
    # 포인터 옮기기
    if result >= S:
        answer = min(answer, end-start+1)
        result -= arr[start]
        start += 1
    else:
        end += 1
        if end < N:
            result += arr[end]

if answer == 10e7:
    answer = 0
print(answer)