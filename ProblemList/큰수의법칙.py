n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 입력받은 수 정렬해서 제일 큰수와 제일 작은 수를 추출해낸다. 
data.sort()
first = data[n-1]
second = data[n-2]

# k+1의 나머지가 0인경우 두번째를 더해준다. 
# m/(k+1) 횟수 만큼 (first * k + second)
# m%(k+1) 횟수만큼 first
# 더 정리하면 아래와 같다. 
# (m//(k+1)) * first + (m%(k+1)) * second
print((m//(k+1)) * (first * k + second) + (m%(k+1)) * first)