# 퇴사
# 상담으로 얻을 수 있는 최대 수익 - 백트래킹

N = int(input())
arr = [list(map(int, input().split())) for _ in range (N)]

def dfs(n, sm):
    global answer

    if n == N: # 종료 조건
        answer = max(answer, sm)
        return

    if n + arr[n][0] <= N: # 상담 O
        dfs(n + arr[n][0], sm+arr[n][1])
    dfs(n+1, sm)  # 상담 X

answer = 0
dfs(0, 0)
print(answer)