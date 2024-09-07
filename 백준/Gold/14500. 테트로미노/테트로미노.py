# 테트로미노
# 테트로미노 하나 -> 칸 수 합 최대로

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# brute force - dfs
def dfs(r, c, n, sum):
    global answer
    if n == 4: # 4개
        answer = max(answer, sum)
        return

    for i in range (4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, n+1, sum + board[nr][nc])
            visited[nr][nc] = False


visited = [[False] * M for _ in range(N)]
for i in range (N):
    for j in range (M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])

        # ㅗ 모양 따로 체크 필요
        block = []
        for t in range (4):
            ni = i + dr[t]
            nj = j + dc[t]
            if 0 <= ni < N and 0 <= nj < M:
                block.append(board[ni][nj])

        if len(block) == 4:
            block.sort(reverse=True)
            block.pop()
            answer = max(answer, sum(block)+board[i][j])
        elif len(block) == 3:
            answer = max(answer, sum(block)+board[i][j])

        visited[i][j] = False

print(answer)
