import heapq
import random
from collections import deque

class Grid:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.grid=[['.' for _ in range(w)] for _ in range(h)]
        self.start=None
        self.goal=None
        self.dynamic=[]

    @staticmethod
    def from_map_string(s):
        lines=s.strip().split('\n')
        h=len(lines)
        w=len(lines[0])
        g=Grid(w,h)
        for y in range(h):
            for x in range(w):
                c=lines[y][x]
                g.grid[y][x]=c
                if c=='S': g.start=(x,y)
                if c=='G': g.goal=(x,y)
                if c=='D': g.dynamic.append([x,y,0])
        return g

    def blocked(self,x,y):
        if x<0 or y<0 or x>=self.w or y>=self.h: return True
        if self.grid[y][x]=='#': return True
        for d in self.dynamic:
            if d[0]==x and d[1]==y: return True
        return False

    def neigh(self,x,y):
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        r=[]
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if not self.blocked(nx,ny):
                r.append((nx,ny))
        return r

    def move_dyn(self):
        p=[(0,1),(0,-1),(1,0),(-1,0)]
        for d in self.dynamic:
            dx,dy=p[d[2]]
            d[0]=max(0,min(self.w-1,d[0]+dx))
            d[1]=max(0,min(self.h-1,d[1]+dy))
            d[2]=(d[2]+1)%4


class Node:
    def __init__(self,p,c,par=None):
        self.p=p
        self.c=c
        self.par=par
    def __lt__(self,o): return self.c<o.c


def path(n):
    r=[]
    while n:
        r.append(n.p)
        n=n.par
    return r[::-1]


def bfs(g,s,t):
    q=deque([Node(s,0)])
    vis={s}
    while q:
        n=q.popleft()
        if n.p==t: return path(n)
        for nb in g.neigh(*n.p):
            if nb not in vis:
                vis.add(nb)
                q.append(Node(nb,n.c+1,n))
    return None


def astar(g,s,t):
    pq=[(0,Node(s,0))]
    gc={s:0}
    while pq:
        _,n=heapq.heappop(pq)
        if n.p==t: return path(n)
        for nb in g.neigh(*n.p):
            ng=gc[n.p]+1
            if nb not in gc or ng<gc[nb]:
                gc[nb]=ng
                f=ng+abs(nb[0]-t[0])+abs(nb[1]-t[1])
                heapq.heappush(pq,(f,Node(nb,ng,n)))
    return None


class Sim:
    def __init__(self,g):
        self.g=g
        self.pos=g.start
        self.path=[]
        self.i=0

    def plan(self):
        self.path=astar(self.g,self.pos,self.g.goal)
        self.i=0

    def step(self):
        self.g.move_dyn()
        if not self.path or self.i>=len(self.path)-1:
            self.plan()
            if not self.path: return False
        nxt=self.path[self.i+1]
        if self.g.blocked(*nxt):
            self.plan()
            return True
        self.pos=nxt
        self.i+=1
        print("Agent:",self.pos)
        if self.pos==self.g.goal:
            print("Done")
            return False
        return True


if __name__=="__main__":
    m="""S..
.D.
..G"""
    g=Grid.from_map_string(m)
    sim=Sim(g)
    for _ in range(20):
        if not sim.step():
            break
