# Atcoder
# https://atcoder.jp/contests/abc146/tasks/abc146_c

A,B,N = map(int,input().split())

def result(A,B,x):
    return A*int(x)+B*len(x)

if result(A,B,str(10**19)) <= N:
    print(10**19)
    exit()

high = 10**19
low = 0
mid = (low+high)//2

while low+1 < high:
    mid_price = result(A,B,str(mid))
    print(high,low,mid,mid_price)
    if mid_price > N:
        high = mid
    else:
        low = mid
    mid = (low+high)//2
print(mid)
