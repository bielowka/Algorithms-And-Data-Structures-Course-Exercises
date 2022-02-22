def edmondskarp(G,s,t):
    from collections import deque
    from math import inf
    n=len(G)
    fmax = 0
    CFP = [-1] * n
    L=[[] for i in range(n)]
    for i in range(n):
        for j in G[i]:
            L[i].append([j[0],j[1],0])

    for u in range(n):
        for x in L[u]:
            p=False
            for v in L[x[0]]:
                if v[0]==u: p=True
            if p==False: L[x[0]].append([u,0,0])

    while(True):
        p=[-1]*n

        p[s]=-2
        CFP[s]=inf

        Q=deque()
        Q.clear()
        Q.append(s)

        finish=True
        while len(Q)!=0:
            u=Q.pop()
            for x in L[u]:
                cp=x[1]-x[2]
                if cp==0 or p[x[0]]!=-1: continue
                p[x[0]]=u
                CFP[x[0]]=min(CFP[u],cp)
                if x[0]==t:
                    finish=False
                    break
                Q.append(x[0])
        if finish==True: return fmax

        fmax+=CFP[t]

        v=t

        while v!=s:
            u=p[v]
            for z in L[u]:
                if z[0]==v: z[2]+=CFP[t]
            for z in L[v]:
                if z[0]==u: z[2]-=CFP[t]
            v=u



G=[
    [(1,5),(2,4)],
    [(3,6)],
    [(3,3),(4,2)],
    [(4,1),(5,2)],
    [(5,4)],
    [],
]

print(edmondskarp(G,0,5))