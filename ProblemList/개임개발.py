n, m = map(int, input().split())
row, col, direction = map(int, input().split())

# 방문 위치 초기화해준다. 
passed = [[0] * m for _ in range(n)]
passed[row][col] = 1
# 맵 초기화 해준다. 
earth = []

# 육지 바다 초기화 해준다. 
for i in range(n):
    earth.append(list(map(int,input().split())))


# direction 맞춰서 세팅
drow = [1,0,-1,0]
dcol = [0,1,0,-1]

# 회전하는 함수
def rotate_anti_clock(direction):
    if(direction == 0):
        direction = 3
    else:
        direction -= 1 
    return direction

# 해당 방향 이동 가능한지 여부 리턴
def able_to_move(row, col, direction):
    wrow = row + drow[direction]
    wcol = col + dcol[direction]
    # 벗어남
    if wrow < 0 or wrow > n or wcol < 0 or wcol >m:
        return False
    # 방문했었음
    if passed[wrow][wcol] == 1:
        return False
    # 바다임
    if earth[wrow][wcol] == 1:
        return False
    return True

# 뒤가 바다면 false, 뒤가 육지면 true:
def able_to_back_step(row, col, direction):
    back_direction = (direction+2)%4
    wrow = row + drow[back_direction]
    wcol = col + dcol[back_direction]
    if earth[wrow][wcol] == 1:
        return False
    return True

# 시뮬레이션 시작하는 함수
def simulation(row, col, direction):
    result = 1
    passed[row][col] = 1
    while True:
        # 동서남북 체크하고 이동 가능한지 체크한. 만약 for문 다 돌았으면 전부다 못가는 것이다. 뒤로 간다. 
        crow = row
        ccol = col
        turn_time = 0
        for i in range(4):
            turn_time+=1
            direction = rotate_anti_clock(direction)
            if able_to_move(row, col, direction):
                row = row + drow[direction]
                col = col + dcol[direction]
                passed[row][col] = 1
                result+=1
                break
        # 4회전 한 경우
        if turn_time == 4 : 
            if able_to_back_step(row,col,direction):
                back_direction = (direction+2)%4
                row = row + drow[back_direction]
                col = col + dcol[back_direction]
            # 백스텝 불가
            else:
                break
    print(result)
        
simulation(row,col,direction)