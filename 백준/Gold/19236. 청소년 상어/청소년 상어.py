# 청소년 상어
# 상어 물고기 먹고 -> 물고기 이동 (45도 반시계) -> 상어 이동 (물고기 있는 칸으로만)
# 최댓값
import copy

fish = [[] for _ in range (4)]

for i in range (4):
    info = list(map(int, input().split()))
    temp = []
    for j in range (4):
        temp.append([info[2*j], info[2*j+1]-1])
    fish[i] = temp

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0

# brute force

def move_shark(shark, shark_score, fish):
    global answer

    shark_score += fish[shark[0]][shark[1]][0]
    answer = max(answer, shark_score)
    fish[shark[0]][shark[1]][0] = 0
    
    # 물고기 이동 (번호 작은거 부터)
    visited = [False] * 17
    for f in range(1, 17):
        for i in range(4):
            for j in range(4):
                # f번 물고기 움직이기
                if fish[i][j][0] == f and not visited[f]:
                    before_dir = fish[i][j][1]

                    for k in range(8):
                        n_dir = (before_dir + k) % 8
                        nr = i + dr[n_dir]
                        nc = j + dc[n_dir]
                        if 0 <= nr < 4 and 0 <= nc < 4 and [nr, nc] != shark:
                            # 이동
                            fish[i][j][1] = n_dir
                            fish[nr][nc], fish[i][j] = fish[i][j], fish[nr][nc]
                            visited[f] = True
                            break

    shark_dir = fish[shark[0]][shark[1]][1]
    for i in range (1, 5):
        nr = shark[0] + dr[shark_dir] * i
        nc = shark[1] + dc[shark_dir] * i
        if 0 <= nr < 4 and 0 <= nc < 4 and fish[nr][nc][0] > 0:
            move_shark([nr, nc], shark_score, copy.deepcopy(fish))


move_shark([0, 0], 0, fish)
print(answer)