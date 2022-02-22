from queue import PriorityQueue

def BFS_bipartiness(G,s):
    w=True
    Q=[]
    visited=[False for i in range(len(G))]
    d=[None for i in range(len(G))]
    parent=[None for i in range(len(G))]

    d[s]=False
    visited[s]=True
    Q.append(s)

    while len(Q)!=0:
        u=Q.pop(0)
        for v in range(1,len(G[u])):
            if visited[G[u][v]]==False:
                visited[G[u][v]] = True
                d[G[u][v]]=not d[u]
                parent[G[u][v]]=u
                Q.append(G[u][v])
            else:
                if d[G[u][v]]==d[u]: w=False

    return w






G=[
    [0,3,4,5,6],
    [1,4],
    [2,3,4],
    [3,0,2],
    [4,0,1,2],
    [5,0],
    [6,0],
]

print(BFS_bipartiness(G,0))