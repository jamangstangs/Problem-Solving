n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(row, col):
    if row<0 or row>=n or col<0 or col>=m:
        return False
    if graph[row][col] == 0:
        graph[row][col] = 1
        dfs(row-1, col)
        dfs(row, col-1)
        dfs(row+1, col)
        dfs(row, col+1)
        return True
    return False

ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            ans+=1

print(ans)     
        