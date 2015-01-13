# Enter your code here. Read input from STDIN. Print output to STDOUT

#T = input()
T = 1

from collections import namedtuple
from pprint import pprint as pp
 
 
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')
 
class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))
 
    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        #pp(neighbours)
 
        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u = [], dest
        while previous[u]:
            s.insert(0, u)
            u = previous[u]
        s.insert(0, u)
        return s
 
 


for i in xrange(T):
    #S,L  = map(int,raw_input().split(','))
    L,S = 1,4


    
    #SArr = raw_input().split()
    s = '22,54'
    LArr = s.split()
    #LArr = ['32,62', '42,68', '12,98']
    
    s = '79,17 67,7 89,25 69,23'
    SArr = s.split()
    #SArr = ['95,13', '97,25', '93,37', '79,27', '75,19', '49,47', '67,17']

    l = []
    
    for i in xrange(1,100):
        l.append((i,i+1,1))
    for ll in LArr:
        a,b = map(int,ll.split(','))
        l.append((int(a), int(b), 0))        
    for s in SArr:
        a,b = map(int,s.split(','))
        l.append((int(a), int(b), 0))        
    l = sorted(l) 
    #print l

    graph = Graph(l)
    pp(graph.dijkstra(1, 100))


