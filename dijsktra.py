from queue import PriorityQueue
from math import inf

def dijkstra(G,v,f):

    n=len(G)

    d = [inf] * n
    d[v] = 0
    K=PriorityQueue()

    K.put((d[v],v))

    p = [None] * n


    while not K.empty():
        u=K.get()
        for v in G[u[1]]:
            if d[v[0]]>d[u[1]]+v[1]:
                d[v[0]]=d[u[1]]+v[1]
                p[v[0]]=u[1]
                K.put((d[v[0]],v[0]))

    return d[f],d


# def mind(d,QS):
#     min_=inf
#     res=-1
#     for i in range(len(d)):
#         if not QS[i]:
#             if d[i]<min_:
#                 min_=d[i]
#                 res=i
#     return res
#
#
# def dijkstra(G,v,f):
#
#     n=len(G)
#     QS = [False] * n
#     d = [inf] * n
#     d[v] = 0
#     p = [-1] * n
#
#     for i in range(n):
#         u=mind(d,QS)
#         QS[u]=True
#         for w in G[u]:
#             if not QS[w[0]] and d[w[0]]>d[u]+w[1]:
#                 d[w[0]]=d[u]+w[1]
#                 p[w[0]]=u
#
#     return d[f]



G=[
    [(1,3),(4,3)],
    [(2,1)],
    [(3,3),(5,1)],
    [(1,3)],
    [(5,2)],
    [(0,6),(3,1)]
]

G=[
    [(1,4),(2,4)],
    [(2,1),(3,100)],
    [(4,100)],
    [(5,5)],
    [(5,5)],
    []
]

G=[
    [(1,1),(2,10),(3,3)],
    [(0,1),(2,1),(3,1)],
    [(0,1),(1,1),(3,1),(4,10)],
    [(0,1),(1,1),(2,1)],
    [(2,10),(5,10)],
    [(4,10),(6,10)],
    [(5,10),(7,10)],
    [(6,10)]
]


#
# G=[
#     [(1,5)],
#     [(2,7)],
#     [],
# ]
#
# G=[
#     [(1,4),(2,7)],
#     [(2,1)],
#     [],
# ]
#
# G=[
#     [(1,4)],
#     [],
#     []
# ]
##0,2

print(dijkstra(G,0,7))