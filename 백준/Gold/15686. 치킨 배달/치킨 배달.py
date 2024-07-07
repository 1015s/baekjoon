# 치킨 배달
# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
# 치킨집 최대 M개 -> 도시의 치킨 거리 가장 작게 되도록
from itertools import combinations

N, M = map(int, input().split())
city = []
for i in range (N):
    city.append(list(map(int, input().split())))

answer = 10e9

# 치킨 거리 계산 -> 집마다 bfs 각각 돌리기 (시간 초과), 그냥 계산
def calc_chicken_distance(candidates):
    global answer
    for chickens in candidates:
        total_distance = 0
        for home in homes:
            dist = 10e9
            for chicken in chickens:
                dist = min(dist, (abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])))
            total_distance += dist
        answer = min(total_distance, answer)

# 치킨 집 M개 고르기
chickens = []
homes = []
for i in range (N):
    for j in range (N):
        if city[i][j] == 1:
            homes.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

candidates = list(combinations(chickens, M))
calc_chicken_distance(candidates)
print(answer)


