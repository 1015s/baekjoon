# 뱀
# 사과 -> 뱀 길이 증가, 벽/자기 몸과 충돌 -> 게임 끝
# 초기 : (0, 0), 오른쪽, 길이 1
# 게임이 몇 초에 끝나는지 계산

# 보드
N = int(input())
board = [[0] * (N) for _ in range (N)]

# 사과
K = int(input())
for i in range (K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2

# 뱀 방향 전환 (L : 왼쪽 90도, R : 오른쪽 90도)
info = []
L = int(input())
for i in range (L):
    temp = input().split()
    info.append([int(temp[0]), temp[1]])

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 초기
snake = [[0, 0]]
board[0][0] = 1
dir = 0
t = 0

while(1):
    # 새로운 머리 위치
    head = snake[-1]
    tail = snake[0]

    n_head_r = head[0] + d[dir][0]
    n_head_c = head[1] + d[dir][1]

    # 종료 조건 - 머리만으로 계산 가능
    if n_head_r < 0 or n_head_r >= N or n_head_c < 0 or n_head_c >= N or board[n_head_r][n_head_c] == 1:
        t += 1
        break

    # 꼬리 이동 -> 새로운 머리 위치에 사과 없을 때만
    if board[n_head_r][n_head_c] == 0:
        board[tail[0]][tail[1]] = 0
        snake.pop(0)

    # 머리 이동
    board[n_head_r][n_head_c] = 1
    snake.append([n_head_r, n_head_c])

    t += 1

    # 방향 전환
    if len(info) > 0 and t == info[0][0]:
        if info[0][1] == 'L': # 왼쪽 90 도
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4
        info.pop(0)

print(t)