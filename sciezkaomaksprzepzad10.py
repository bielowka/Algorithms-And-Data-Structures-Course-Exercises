#Szymon Bielówka
"""
Korzystam z odpowiednio zmodyfikowanego algorytmu Dijkstry
Modyfikacja polega na tym, że na kolejkę priorytetową odkłądam potrójne krotki postaci:
(przepływ który pójdzie daną krawędzią,nr wierzchołka, nr wierzchołka z którego prowadzi krawędź)
gdzie przepływ do kolejki wrzucam jako wartość ujemna, żeby kolejka zwracała najwięsze, nie najmniejsze wartości.
Dla każdego wierzchołka wrzucam jego sąsiadów w tej postaci
Ściągam kolejne wierzchołki i rozważam te które nie były jeszcze odwiedzone.
Ustawia parent wierchołka po ściągnięciu z kolejki, ponieważ to oznacza, że wybrana została najabrdziej optymalna krotka w któej jest dany wierzchołek
Algorytm kończy się gdy dotrzemy do szukanego wierzchołka. Jeśli ścieżka do niego nie istnieje, zwraca None.
Odtwarza wynik za pomocą tablicy parent od ostatniego wierzchołka a następnie odwaraca listę wynikową by zwrócić ją w nakazanej kolejności.
Złożoność obliczeniowa: O(E*logE)
Złożonośc pamięciowa: O(V)
"""
from copy import deepcopy


def max_extending_path( G, s, t ):
  from math import inf
  from queue import PriorityQueue
  def dijkstra(G, s, t):
    n = len(G)

    visited = [False] * n
    p = [-1] * n
    K = PriorityQueue()
    K.put((-inf, s, s))

    while not K.empty():
      u = K.get()
      p[u[1]] = u[2]
      if u[1] == t: return u[1], p
      if not visited[u[1]]:
        visited[u[1]] = True
        for v in G[u[1]]:
          if not visited[v[0]]: K.put((-min(v[1], -u[0]), v[0], u[1]))

  dist, p = dijkstra(G, s, t)
  S = [t]

  while t != s:
    S.append(p[t])
    t = p[t]

  S.reverse()
  return S
  
  
  
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3
s = 0
t = 3
C = 3  


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []: 
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)
  
if path[0] != s or path[-1] != t: 
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)

  
capacity = float("inf")
u = path[0]
  
for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")
  
