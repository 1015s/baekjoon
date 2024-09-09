# 주사위 굴리기
# 주사위 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면으로, 아니면 반대
# 주사위가 이동했을 때 마다 상단에 쓰여 있는 값 구하기

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range (N)]
move = list(map(int, input().split()))
dice = [0] * 6

# 동
dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]


# 초기 상태
dice[0] = board[x][y]
board[x][y] = 0

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

# 이동
for d in range (K):
    # 지도 내부로 이동 가능한지 먼저 확인
    nx = x + dr[move[d]]
    ny = y + dc[move[d]]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    # 좌표 이동
    x, y = nx, ny

    # 굴리기
    if move[d] == 1: # 동
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif move[d] == 2:  # 서
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif move[d] == 3: # 북
        dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]
    else: # 남
        dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]

    if board[x][y] == 0:
        board[x][y] = dice[0]
    else:
        dice[0] = board[x][y]
        board[x][y] = 0

    # 주사위 상단에 있는 수 출력
    print(dice[5])