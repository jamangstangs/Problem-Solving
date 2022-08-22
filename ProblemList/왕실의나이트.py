location = input()
row = int(location[1])
col = int(ord(location[0]))-int(ord('a'))+1

drow = [2,2,-2,-2,1,1,-1,-1]
dcol = [1,-1,1,-1,2,-2,2,-2]

ans = 8

for i in range(8):
    if (row+drow[i]) < 1 or (row+drow[i]) > 8 or (col+dcol[i]) < 1 or (col+dcol[i]) > 8 :
        ans -=1
print(ans)

