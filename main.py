import time
import random
import heapq
from collections import deque

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
        res=[]
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if not self.block(nx,ny):
                res.append((nx,ny))
        return res


def gen(w,h,d):
    g=Grid(w,h)
    for _ in range(int(w*h*d)):
        x=random.randint(0,w-1)
        y=random.randint(0,h-1)
        g.g[y][x]='#'
    return g


def bfs(g):
    q=deque([(g.s,0)])
    vis=set([g.s])
    count=0
    while q:
        n,c=q.popleft()
        count+=1
        if n==g.t:
            return count
        for nb in g.neigh(n[0],n[1]):
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
        if n==g.t:
            return count
        if n in vis:
            continue
        vis.add(n)
        for nb in g.neigh(n[0],n[1]):
            h=abs(nb[0]-g.t[0])+abs(nb[1]-g.t[1])
            heapq.heappush(pq,(h,nb))
    return count


maps=[("small",gen(5,5,0.1)),("medium",gen(15,15,0.2)),("large",gen(25,25,0.25))]
algorithms=[("BFS",bfs),("A*",astar)]

print("\nResults:\n")

for mname,g in maps:
    print("Map:",mname)
    for aname,algo in algorithms:
        t1=time.time()
        nodes=algo(g)
        t2=time.time()
        print("  ",aname,"| time(ms):",round((t2-t1)*1000,3),"| nodes:",nodes)
    print()
