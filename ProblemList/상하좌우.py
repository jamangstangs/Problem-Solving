n = int(input())
plans = input().split()
x,y = 1, 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_types = ['U', 'D', 'L', 'R']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:

            nx=x+dx[i]
            ny=y+dy[i]
            break
    if nx > n or nx < 1 or ny > n or ny < 1:
        continue
    x = nx
    y = ny

print(x, y)



