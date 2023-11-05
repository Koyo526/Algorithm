#Atcoder
#https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a

N,K = map(int,input().split())
A = list(map(int,input().split()))
#print(N,K,A)

high = N-1
low = 0

if K > A[high]:
    print(-1)
    exit()

while low+1 < high:
    mid = (high + low)//2
    if A[mid] >= K:
        high = mid
    else:
        low = mid 
print(high)