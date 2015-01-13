class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)
 
class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
 
    def add_vertex(self, vertex):
        self.adj[vertex] = []
 
    def get_edges(self, v):
        return self.adj[v]
 
    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge  #redge is not defined in Edge class
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0
 
    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge,residual) in path:
                result = self.find_path( edge.sink, sink, path + [(edge,residual)] ) 
                if result != None:
                    return result
 
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            flow = min(res for edge,res in path)
            for edge,res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))

def hcf( n1, n2 ):
  while n1*n2:
    if n1 > n2:
      n1 %= n2
    else:
      n2 %= n1
  return max( n1, n2 )

def coprime( n1, n2 ):
  return hcf( n1, n2 ) == 1


g=FlowNetwork()

#N = input()
N = 5
#A = map(int,raw_input().split())
A = [2,5,7,11,13]
B = [14,2,3,26,14]
#B = map(int,raw_input().split())


map(g.add_vertex, list(range(2*N+2)))


for i in xrange(N):
    g.add_edge(0,i+2,1)
    g.add_edge(N+i+2,1,1)

for i in xrange(N):
    for j in xrange(N):
        
        if coprime(A[i],B[j]):
            pass
        else:
            g.add_edge(i+2,N+j+2,1)
            


print g.max_flow(0,1)    
