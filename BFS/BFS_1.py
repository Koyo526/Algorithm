#幅優先探索
#AtcoderABC209Dより出題

N, Q = map(int,input().split())
li  =[[] for _ in range(N)] 
for i in range(N-1):
    a, b = map(int,input().split())
    li[a-1].append(b-1)
    li[b-1].append(a-1)
print(li)

from collections import deque
d = deque([0])
print(d)
dist = [-1]* N
dist[0] = 0
while d:
    print("---------")
    x = d.popleft()
    for i in li[x]:
        print(x,i,d)
        if dist[i] == -1:
            dist[i] = dist[x] + 1
            d.append(i)
print(dist,li)

for _ in range(Q):
    a,b = map(int,input().split())
    a = dist[a-1]%2
    b = dist[b-1]%2
    if a!=b:
        print("Road")
    else:
        print("Town")