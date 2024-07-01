# 상어 초등학교
# n이 3 ~ 20 으로 작음

n = int(input())

seq = []
dict = {}
classroom = [[0] * n for _ in range (n)]

for i in range (n*n):
    temp = list(map(int, input().split()))
    seq.append(temp[0])
    dict[temp[0]] = temp[1:]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def find_place(like_students):
    like_maximum = 0
    like_map = [[0] * n for _ in range (n)]
    for i in range (n):
        for j in range (n):
            if classroom[i][j] == 0:
                # 좋아하는 학생 상하좌우에 있는지 확인
                like = 0
                for k in range (4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if classroom[nr][nc] in like_students:
                            like += 1
                        like_map[i][j] = like
                        like_maximum = max(like_maximum, like)
   
    max_blank = -1
    ar, ac = 0, 0

    for i in range (n):
        for j in range (n):
            if like_map[i][j] == like_maximum and classroom[i][j] == 0:
                # 빈칸 갯수 확인
                blank = 0
                for k in range (4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if classroom[nr][nc] == 0:
                            blank += 1
                # 작은것부터 탐색 -> 자동 3번 규칙 처리
                if blank > max_blank:
                    max_blank = blank
                    ar, ac = i, j

    
    return ar, ac

score = [0, 1, 10, 100, 1000]
result = 0

for num in range (n*n):
    i, j = find_place(dict[seq[num]])
    classroom[i][j] = seq[num]

# 점수 계산
for i in range (n):
    for j in range (n):
        cnt = 0
        for k in range (4):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if classroom[nr][nc] in dict[classroom[i][j]]:
                    cnt += 1
        result += score[cnt]

print(result)
                    