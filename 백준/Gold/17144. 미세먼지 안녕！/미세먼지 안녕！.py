# 미세먼지 안녕!
# 시간 초과 -> 최적화 짧은 for문 여러개로

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def clean_air(start, dir):
    if dir == -1: # 반시계
        for i in range (start-1, 0, -1):
            A[i][0] = A[i-1][0]
        for i in range (0, C-1):
            A[0][i] = A[0][i+1]
        for i in range (0, start):
            A[i][C-1] = A[i+1][C-1]
        for i in range (C-1, 0, -1):
            A[start][i] = max(A[start][i-1], 0)
    else: # 시계
        for i in range (start+1, R-1):
            A[i][0] = A[i+1][0]
        for i in range (0, C-1):
            A[R-1][i] = A[R-1][i+1]
        for i in range (R-1, start, -1):
            A[i][C-1] = A[i-1][C-1]
        for i in range (C-1, 0, -1):
            A[start][i] = max(A[start][i-1], 0)


for t in range (T):
    # 미세먼지 확산 (동시에)
    _A = [[0] * C for _ in range(R)]

    for i in range (R):
        for j in range (C):
            if A[i][j] > 0:
                _A[i][j] += A[i][j]
                if A[i][j] >= 5:
                    # 미세먼지 확산
                    amount = A[i][j] // 5
                    for k in range(4):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                            _A[nr][nc] += amount
                            _A[i][j] -= amount
            elif A[i][j] == -1:
                _A[i][j] = -1

    A = _A

    # 공기 청정기 작동 (한 칸씩 이동)
    # 위쪽 - 반시계, 아래쪽 - 시계
    cleaner = []
    for i in range (R):
        if A[i][0] == -1:
            cleaner.append(i)
            cleaner.append(i+1)
            break
    clean_air(cleaner[0], -1)
    clean_air(cleaner[1], 1)


# 남은 미세먼지 양 출력
answer = 0
for i in range (R):
    for j in range (C):
        if A[i][j] > 0:
            answer += A[i][j]
print(answer)
