class Node:
    def __init__(self,val):
        self.val=val
        self.rank=0
        self.parent=self

def find(x):
    if x!=x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y: return
    if x.rank > y.rank: y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank: y.rank += 1

def kruskal(V,E):
    A=[]
    V_n=[]
    for v in V:
        V_n.append(Node(v))

    E.sort(key = lambda pair: pair[2])

    for e in E:
        if find(V_n[e[0]])!=find(V_n[e[1]]):
            A.append(e)
            union(V_n[e[0]],V_n[e[1]])

    return A


V=[0,1,2,3,4,5]
E=[[0,5,7],[0,1,2],[1,2,5],[2,3,6],[2,4,4],[3,4,12],[4,0,8],[4,5,1],[0,3,3]]
print(kruskal(V,E))