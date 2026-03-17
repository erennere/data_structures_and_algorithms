"""
Graph data structure and algorithms implementation.

This module provides a comprehensive Graph class that supports:
- Weighted and unweighted graphs
- Adjacency list representation
- Multiple graph traversal algorithms (BFS, DFS)
- Shortest path algorithms (Dijkstra, Bellman-Ford, SSSP)
- Topological sorting

Classes:
    Graph: Represents a graph with vertices and edges

Supported Operations:
    - add_vertex/remove_vertex: Manage vertices
    - add_edge/remove_edge/update_edge: Manage edges
    - bfs/dfs: Graph traversals
    - dijkstra/bellman_ford: Shortest path algorithms
    - topologicalSort: Topological ordering for DAGs

Complexity varies by algorithm: Most operations O(V + E) where V is vertices, E is edges.
"""

from collections import deque 
import heapq
class Graph:
    def __init__(self, g_dict = {}):
        self.adjacency_list = {}
        for node, info in g_dict.items():
            self.add_vertex(node)
            if isinstance(info, dict):
                for vertex, weight in info.items():
                    self.add_vertex(vertex)
                    self.add_edge(node, vertex, weight)
            elif isinstance(info, list):
                for vertex in info:
                    self.add_vertex(vertex)
                    self.add_edge(node, vertex)
                        
    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            return False
        self.adjacency_list[vertex] = {}
        return True

    def add_edge(self, v1, v2, weight=1):
        if v1 not in self.adjacency_list:
            return False
        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1][v2] = weight
        return True
    
    def update_edge(self, v1, v2, weight):
        return self.add_edge(v1, v2, weight)

    def remove_edge(self, v1, v2):
        if v1 not in self.adjacency_list or v2 not in self.adjacency_list:
            return False
        if v2 in self.adjacency_list[v1]:
            del self.adjacency_list[v1][v2]
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return False
        for neighbor in self.adjacency_list[vertex]:
            del self.adjacency_list[neighbor][vertex]
        del self.adjacency_list[vertex]
        return True
    
    def bfs(self, start):
        """Perform breadth-first search (BFS) graph traversal.
        
        Traversal is achieved by exploring vertices level by level: the starting vertex
        is enqueued, then for each dequeued vertex, all unvisited adjacent vertices are
        visited and enqueued consecutively. This ensures all vertices at distance k are
        visited before any vertex at distance k+1, exploring in breadth across levels.
        
            raise ValueError(f'{start} not in the graph')

        visited = {start}
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            yield vertex

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start):
        """Perform depth-first search (DFS) graph traversal.
        
        Traversal is achieved by exploring as far as possible along each branch before
        backtracking: the starting vertex is pushed on a stack, then for each popped
        vertex, unvisited adjacent vertices are pushed consecutively. This ensures each
        branch is fully explored from root to leaf before exploring the next branch.
        
            raise ValueError(f'{start} not in the graph')

        visited = {start}
        stack = [start]

        while stack:
            vertex = stack.pop()
            yield vertex

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    def topologicalSort(self):
        """Perform topological sorting of a directed acyclic graph (DAG).
        
        Sorting is achieved by performing depth-first search on all unvisited vertices,
        adding each vertex to a result stack after exploring all its neighbors. Vertices
        with no outgoing edges are added first, progressively building a topological
        order where every edge u->v has u appearing before v in the final ordering.
        
        stack = []
        for vertex in self.adjacency_list:
            if vertex not in visited:
                self.topologicalSortUtil(vertex, visited, stack)
        while stack:
            yield stack.pop()

    def topologicalSortUtil(self, v, visited, stack):
        visited.add(v)
        for nxt in self.adjacency_list[v]:
            if nxt not in visited:
                self.topologicalSortUtil(nxt, visited, stack)
        stack.append(v)

    def sssp(self, v_start, v_end):
        if v_end not in self.adjacency_list:
            raise Exception(f'{v_end} is not in the graph')
        
        dists = {v_start: 0}
        parents = {v_start: None}
        queue = deque([v_start])
        while queue:
            current_vertex = queue.popleft()
            if current_vertex == v_end:
                return dists, parents
            
            for neighbor, dist in self.adjacency_list[current_vertex].items():
                if dist != 1:
                    print('graph is a weighted one, thus changing to dijkstra')
                    return self.dijkstra_pq(v_start, v_end)
                
                if neighbor not in dists:
                    dists[neighbor] = dists[current_vertex] + 1
                    parents[neighbor] = current_vertex
                    queue.append(neighbor)
    
    def dijkstra(self, v_start, v_end):
        if v_end not in self.adjacency_list:
            raise Exception(f'{v_end} is not in the graph')
        
        dists = {k:float('inf') for k in self.adjacency_list}
        explored = {k:False for k in self.adjacency_list}

        current = v_start
        dists[current] = 0
        parents = {current:None}

        while current is not None:
            for nxt, dist in self.adjacency_list[current].items():
                if dist < 0:
                    print('negative edge has been found, changing to Bellman-Ford')
                    return self.bellman_ford(v_start, v_end)

                if explored[nxt]:
                    continue

                new_dist = dists[current] + dist
                if new_dist < dists[nxt]:
                    dists[nxt] = new_dist
                    parents[nxt] = current

            explored[current] = True
            unexplored = [k for k, v in explored.items() if not v]
            min_dist = float('inf')
            min_node = None
            for node in unexplored:
                dist = dists[node]
                if not explored[node] and dists[node] < min_dist:
                    min_dist = dists[node]
                    min_node = node
            current = min_node
        return dists, parents
    
    def dijkstra_pq(self, v_start, v_end):
        if v_end not in self.adjacency_list:
            raise Exception(f'{v_end} is not in the graph')
        
        dists = {k:float('inf') for k in self.adjacency_list}
        explored = set()
        current = v_start

        parents = {current:None}
        dists[current] = 0
        pq = [(0, current)]  # (distance, vertex)
        while pq:
            current_dist, node = heapq.heappop(pq)
            if node in explored:
                continue
            if node == v_end:
                break

            for nxt, dist in self.adjacency_list[node].items():
                if dist < 0:
                    print('negative edge has been found, changing to Bellman-Ford')
                    return self.bellman_ford(v_start, v_end)

                if nxt in explored:
                    continue

                new_dist = dist + current_dist
                if new_dist < dists[nxt]:
                    dists[nxt] = new_dist
                    parents[nxt] = node
                    heapq.heappush(pq, (new_dist, nxt))

            explored.add(node)
        return dists, parents
    
    def bellman_ford(self, v_start, v_end):
        if v_end not in self.adjacency_list:
            raise Exception(f'{v_end} is not in the graph')
        
        dists = {v:float('inf') for v in self.adjacency_list}
        parents = {v_start:None}
        dists[v_start] = 0
        is_premature = False

        def run_cycle():
            is_modified = False
            for source_v, info in self.adjacency_list.items():
                source_dist = dists[source_v]
                if source_dist == float('inf'):
                    continue

                for dest_v, dist in info.items():
                    new_dist = source_dist + dist
                    if new_dist < dists[dest_v]:
                        dists[dest_v] = new_dist
                        parents[dest_v] = source_v
                        is_modified = True
            return is_modified

        for _ in range(len(self.adjacency_list)-1):
            if not run_cycle():
                is_premature = True
                break
        
        if not is_premature and run_cycle():
                raise Exception('Negative cycle found')
        return dists, parents

    def floyd_warshall(self):
        n = len(self.adjacency_list)
        dists = [[float('inf')] * n for _ in range(n)]
        sources = [[None] * n for _ in range(n)]
        vertices = list(self.adjacency_list.keys())

        for i, v in enumerate(vertices):
            dists[i][i] = 0
            for j, d in enumerate(vertices):
                if d in self.adjacency_list[v]:
                    dists[i][j] = self.adjacency_list[v][d]
                    sources[i][j] = d

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    new_dist = dists[j][i] + dists[i][k]
                    if new_dist < dists[j][k]:
                        dists[j][k] = new_dist
                        sources[j][k] = sources[j][i]
        return dists, sources
              
my_dict = {
    'A' : ['B', 'C', 'E', 'F'],
    'B' : ['A', 'E'],
    'C' : ['B', 'A', 'F'],
    'E' : ['A', 'B'],
    'F' : ['A', 'C']
}

my_dict = {
    'A' : ['C'],
    'B' : ['C', 'D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : ['H', 'F'],
    'F' : ['G'],
    'G' : [],
    'H' : []
}

my_dict = {
    'A' : ['B', 'C', 'D'],
    'B' : ['J'],
    'J' : ['K'],
    'K' : [],
    'C': ['G'],
    'G': ['H', 'I'],
    'H' : ['K'],
    'I' : [],
    'D': ['G']}

my_graph = Graph(my_dict)
bfs_order = my_graph.bfs('A')
dfs_order = my_graph.dfs('A')

for vertex in bfs_order:
   print(vertex)
print('-----------------')
for vertex in dfs_order:
   print(vertex)

print('>>>>>>>>>>>>>>>>>>>>>>')
source = 'A'
target = 'H'
dists, parents = my_graph.sssp(source, target)
child = target
while child is not None:
    child = parents[child]
    print(child)


print(dists)
print(parents)

print('>>>>>>>>>>>>>>>>>>>>>>>>')
my_dict = {
    'A' : {'B':6, 'D':9, 'C':10},
    'B' : {'E':16, 'F':13, 'D':5},
    'D' : {'F':8, 'H':7},
    'C' : {'D':6, 'H':7, 'G':21},
    'E' : {'G':10},
    'F' : {'E':4, 'G':12},
    'H' : {'F':2, 'G':14},
    'G' : {}
}
my_graph = Graph(my_dict)
source = 'A'
target = 'G'

dists, parents = my_graph.dijkstra(source, target)
child = target
while child is not None:
    child = parents[child]
    print(child)

print(dists)
print(parents)

print('>>>>>>>>>>>>>>>>>>>>>>>>')
source = 'A'
target = 'G'

dists, parents = my_graph.dijkstra_pq(source, target)
child = target
while child is not None:
    child = parents[child]
    print(child)

print(dists)
print(parents)


print('>>>>>>>>>>>>>>>>>>>>>>>>')
source = 'A'
target = 'G'

dists, parents = my_graph.floyd_warshall()
print(dists)
print(parents)



class DisjointSet:
    def __init__(self, n):
        # parent[i] = parent of i
        # initially each element is its own parent (root)
        self.parent = list(range(n))
        # rank[i] = approximate tree height
        self.rank = [0] * n

    def find(self, x):
        # find the root with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False  # already in same set

        # union by rank
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True
    
def kruskal(graph):
    ds = DisjointSet(len(graph.adjacency_list))
    pq = []
    id_ = {v: i for i, v in enumerate(graph.adjacency_list)}

    for v, info in graph.adjacency_list.items():
        for d, w in info.items():
            heapq.heappush(pq, (w, v, d))

    mst = Graph()
    for v in graph.adjacency_list:
        mst.add_vertex(v)
    cost = 0
    edges_added = 0
    n = len(graph.adjacency_list)

    while pq and edges_added < n - 1:
        w, v, d = heapq.heappop(pq)
        if ds.find(id_[v]) != ds.find(id_[d]):
            ds.union(id_[v], id_[d])
            mst.add_edge(v, d, w)
            cost += w
            edges_added += 1

    if edges_added != n - 1:
        raise ValueError("Graph is disconnected; MST does not exist")
    return mst, cost

def prims(graph, v_start):
    if v_start not in graph.adjacency_list:
        raise ValueError(f'{v_start} not in graph')
    
    explored = set()
    pq = []
    for d, w in graph.adjacency_list[v_start]:
        pq.append((w, v_start, d))

    mst = Graph()
    for v in graph.adjacency_list:
        mst.add_vertex(v)

    while pq:
        cost, start, end = heapq.heappop(pq)
        if start in explored:
            continue
        mst.add_edge(start, end, cost)
        explored.add(start)
        explored.add(end)
        for d, w2 in graph.adjacency_list[start]:
            if d not in explored:
                heapq.heappush(pq, (w2, v, d))
        




    

    
















