import time
import random
import heapq
from collections import deque
import pandas as pd
import matplotlib.pyplot as plt

class Grid:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.g=[['.' for _ in range(w)] for _ in range(h)]
        self.s=(0,0)
        self.t=(w-1,h-1)

    def block(self,x,y):
        return x<0 or y<0 or x>=self.w or y>=self.h or self.g[y][x]=='#'

    def neigh(self,x,y):
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        return [(x+dx,y+dy) for dx,dy in d if not self.block(x+dx,y+dy)]


def gen(w,h,d):
    g=Grid(w,h)
    for _ in range(int(w*h*d)):
        x=random.randint(0,w-1)
        y=random.randint(0,h-1)
        g.g[y][x]='#'
    return g


def bfs(g):
    q=deque([(g.s,0)])
    vis={g.s}
    count=0
    while q:
        n,c=q.popleft()
        count+=1
        if n==g.t: return count
        for nb in g.neigh(*n):
            if nb not in vis:
                vis.add(nb)
                q.append((nb,c+1))
    return count


def astar(g):
    pq=[(0,g.s)]
    vis=set()
    count=0
    while pq:
        _,n=heapq.heappop(pq)
        count+=1
        if n==g.t: return count
        if n in vis: continue
        vis.add(n)
        for nb in g.neigh(*n):
            h=abs(nb[0]-g.t[0])+abs(nb[1]-g.t[1])
            heapq.heappush(pq,(h,nb))
    return count


maps=[("small",gen(5,5,0.1)),("med",gen(15,15,0.2)),("large",gen(25,25,0.25))]
alg=[("bfs",bfs),("astar",astar)]

rows=[]
for mname,g in maps:
    for aname,a in alg:
        t1=time.time()
        nodes=a(g)
        t2=time.time()
        rows.append({"map":mname,"algo":aname,"time":(t2-t1)*1000,"nodes":nodes})

df=pd.DataFrame(rows)
print(df)

plt.figure()
for a in df["algo"].unique():
    d=df[df["algo"]==a]
    plt.plot(d["map"],d["time"],label=a)
plt.legend()
plt.show()
