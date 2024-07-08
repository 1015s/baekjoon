# 톱니바퀴
# 맞닿는 곳 -> 회전 시 rotate -> queue 사용

from collections import deque


t1 = deque(input())
t2 = deque(input())
t3 = deque(input())
t4 = deque(input())

status = [0, t1, t2, t3, t4]

K = int(input())
info = [list(map(int, input().split())) for _ in range (K)]

dx = [1, -1]
# 1 -> 시계, -1 -> 반시계
for n, d in info:
    # 맞닿는 곳 확인 (총 3개)
    is_rotate = [0] * 4
    for i in range (1, 4):
        if status[i][2] != status[i+1][6]: # 다른 경우 -> 회전 가능
            is_rotate[i] = 1

    # 오른쪽
    qr = deque()
    qr.append([n, d])
    while qr:
        cur, dir = qr.popleft()
        status[cur].rotate(dir)
        next = cur + 1
        if 1 <= next <= 4 and is_rotate[cur]:
            qr.append([next, -dir])

    # 왼쪽
    ql = deque()
    ql.append([n, d])
    while ql:
        cur, dir = ql.popleft()
        status[cur].rotate(dir)
        next = cur - 1
        if 1 <= next <= 4 and is_rotate[next]:
            ql.append([next, -dir])

    status[n].rotate(-d)

score = [0, 1, 2, 4, 8]
answer = 0
for i in range (1, 5):
    if status[i][0] == '1':
        answer += score[i]
print(answer)
