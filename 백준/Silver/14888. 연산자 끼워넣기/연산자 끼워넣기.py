N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # 덧 뺄 곱 나

# backtracking으로 완전탐색
answers = set()
def dfs(round, sum, add, sub, mul, div):
    if round == N:
        answers.add(sum)
        return

    if add > 0:
        dfs(round+1, sum+numbers[round], add-1, sub, mul, div) # 덧셈
    if sub > 0:
        dfs(round+1, sum-numbers[round], add, sub-1, mul, div) # 뺄셈
    if mul > 0:
        dfs(round+1, sum*numbers[round], add, sub, mul-1, div) # 곱셈
    if div > 0: # 나눗셈
        dfs(round+1, int(sum/numbers[round]), add, sub, mul, div-1)


dfs(1, numbers[0], add, sub, mul, div)
print(max(answers))
print(min(answers))
