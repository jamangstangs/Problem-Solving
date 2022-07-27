n, m = map(int, input().split())

ans = 0
ans_list = []

for i in range(n):
    data = list(map(int, input().split()))
    MIN = min(data)
    ans_list.append(MIN)
print(max(ans_list))