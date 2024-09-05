# 스타트와 링크
# 능력치 차이 최소

N = int(input())
board = [list(map(int, input().split())) for _ in range (N)]
team_number = N//2

# 모든 경우의 수 탐색 - backtracking
start = []
link = []
answer = []

def dfs(n, start, link):
    if n  == N:
        # 능력치 계산
        start_score = 0
        for i in range (team_number):
            for j in range (team_number):
                start_score += board[start[i]][start[j]]

        link_score = 0
        for i in range (team_number):
            for j in range (team_number):
                link_score += board[link[i]][link[j]]
        answer.append(abs(start_score - link_score))
        return

    # 팀 나누기
    # 스타트 팀
    if len(start) < team_number:
        start.append(n)
        dfs(n+1, start, link)
        start.pop()

    # 링크 팀
    if len(link) < team_number:
        link.append(n)
        dfs(n+1, start, link)
        link.pop()


dfs(0, start, link)
print(min(answer))