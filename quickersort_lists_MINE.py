from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None
    



def qsort( L ):
  def part(a, b):
    sent = Node()
    sent.next = a

    p = sent
    r = a
    q = a
    z = a

    x = a.value

    a = a.next
    while a is not b:
      if a.value < x:
        tmp = a
        q.next = a.next
        a = a.next

        p.next = tmp
        tmp.next = r

        p = p.next

      elif a.value > x:
        a = a.next
        q = q.next

      elif a.value == x:
        tmp = a
        q.next = a.next
        a = a.next

        p.next = tmp
        tmp.next = r

        r = tmp

    return sent.next, p.next, z, q

  def go(f, e):
    f, A, B, e = part(f, e)
    if f != A and f.next != A:
      tmp = A.next
      f, A = go(f, A.next)
      A.next = tmp
    if B != e and B.next != e:
      tmp = B
      B, e = go(B.next, e.next)
      tmp.next = B

    return f, e

  e = L
  while e != None: e = e.next

  L, endd = go(L, e)

  return L





def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

  
  
  

seed(12)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")

