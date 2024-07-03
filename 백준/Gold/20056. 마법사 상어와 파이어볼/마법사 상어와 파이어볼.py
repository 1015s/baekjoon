# 마법사 상어와 파이어볼
# 이동 k번 후, 남아있는 파이어볼 질량의 합
import copy

N, M, K = map(int, input().split())
arr = [[[] for _ in range (N)] for _ in range (N)]

for i in range (M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

def duplicate_fireball(r, c, fireballs):
    total_amount, total_velocity = 0, 0
    mod = (fireballs[0][2] + 2) % 2
    flag = True

    for fireball in fireballs:
        total_amount += fireball[0]
        total_velocity += fireball[1]
        if (fireball[2] % 2) != mod:
            flag = False

    m = total_amount // 5
    s = total_velocity // len(fireballs)

    return m, s, flag

for round in range (K):
    after_move = set()
    move_arr = [[[] for _ in range (N+1)] for _ in range (N+1)]
    # 파이어볼 이동 (모두 d의 방향으로 s칸)
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range (N):
        for j in range (N):
            if arr[i][j] != []:
                for m, s, d in arr[i][j]:
                    nr = (i + dr[d] * s + N) % N
                    nc = (j + dc[d] * s + N) % N
                    move_arr[nr][nc].append([m, s, d])
                    after_move.add((nr, nc))

    for r, c in after_move:
        if len(move_arr[r][c]) > 1:
            m, s, d = duplicate_fireball(r, c, move_arr[r][c])

            move_arr[r][c] = []
            if m != 0:
                if d:
                    move_arr[r][c].append([m, s, 0])
                    move_arr[r][c].append([m, s, 2])
                    move_arr[r][c].append([m, s, 4])
                    move_arr[r][c].append([m, s, 6])
                else:
                    move_arr[r][c].append([m, s, 1])
                    move_arr[r][c].append([m, s, 3])
                    move_arr[r][c].append([m, s, 5])
                    move_arr[r][c].append([m, s, 7])


    arr = copy.deepcopy(move_arr)

# 남아있는 파이어볼 질량의 합
answer = 0
for i in range (N):
    for j in range (N):
        if arr[i][j] != []:
            for m, s, d in arr[i][j]:
                answer += m
print(answer)
