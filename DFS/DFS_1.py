# https://atcoder.jp/contests/atc001/tasks/dfs_a
import sys
sys.setrecursionlimit(10**7)

def field_print(field):
    print("---------------------")
    for i in field:
        print(i)
H,W = map(int,input().split())

field = []
for l in range(H):
    low  = list(input())
    field.append(low)
    for p in range(len(low)):
        if low[p] == "s":
            s_idx = [l,p]
    
#print(H,W,field)

direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(h,w): 
    field[h][w] = "P"
    #field_print(field)
    for d in direc:
        next_h = h + d[0]
        next_w = w + d[1]
        if next_h >= H or next_w >= W:
            continue
        if next_h < 0 or next_w < 0:
            continue
        next_point = field[next_h][next_w]
        if next_point == "#":
            continue
        if next_point == "-":
            continue
        if next_point == "g":
            print("Yes")
            exit()
        field[h][w] = "-"
        dfs(next_h,next_w)
    field[h][w] = "-"
dfs(s_idx[0],s_idx[1])
print("No")
