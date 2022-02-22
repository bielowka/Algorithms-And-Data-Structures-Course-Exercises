def bellmanford(G,s,t):
    from math import inf
    n=len(G)
    d=[inf]*n
    p=[None]*n
    d[s]=0

    for i in range(n):
        for u in range(n):
            for v in G[u]:
                if d[v[0]] > d[u] + v[1]:
                    d[v[0]] = d[u] + v[1]
                    p[v[0]] = u

    for u in range(n):
        for v in G[u]:
            if d[v[0]]>d[u]+v[1]: return "Cykl ujemny"

    return d[t]



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
# #
# G=[
#     [(1,4)],
#     [],
#     []
# ]

print(bellmanford(G,0,7))



