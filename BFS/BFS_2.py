#幅優先探索
#参考資料
# BFS (幅優先探索) 超入門！ 〜 キューを鮮やかに使いこなす 〜
# https://qiita.com/drken/items/996d80bcae64649a6580

from collections import deque
N, M = map(int,input().split())
li = [[] for _ in range(N)]
for m in range(M):
    a,b = map(int,input().split())
    li[a].append(b)
    li[b].append(a)
print(li)

d = deque([0])
print(d)
dist = [-1]*N
dist[0] = 0
while d:
    print("-----------")
    x = d.popleft()
    for i in li[x]:
        print(x,i,d)
        if dist[i] == -1:
            dist[i] = dist[x]+1
            d.append(i)
print(dist,li)

print("===============")
print("Distance from point 0")
for i in range(N):
    print("{}: {}".format(i,dist[i]))