class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root,key):
    while root is not None:
        if root.key == key: return root
        elif key<root.key: root=root.left
        else: root=root.right
    return None


def insert(root,key):
    Node = BSTNode(key)
    while root is not None:
        if root.key == key: return False
        elif key<root.key:
            if root.left is not None: root = root.left
            else:
                root.left=Node
                Node.parent=root
                return True
        else:
            if root.right is not None: root = root.right
            else:
                root.right=Node
                Node.parent=root
                return True

def remove(root,key):
    p=find(root,key)
    if p is None: return None

    if p.left is None and p.right is None:
        if p.parent == None:
            p.key=None
            return None
        if p.parent.left == p: p.parent.left=None
        if p.parent.right == p: p.parent.right=None

    elif p.left is None and p.right is not None:
        if p.parent.right == p:
            p.parent.right=p.right
            p.right.parent=p.parent
        elif p.parent.left == p:
            p.parent.left=p.right
            p.right.parent=p.parent

    elif p.right is None and p.left is not None:
        if p.parent.right == p:
            p.parent.right = p.left
            p.left.parent = p.parent
        elif p.parent.left == p:
            p.parent.left = p.left
            p.left.parent = p.parent

    else:
        n=prev(root,key)
        p.key=n.key
        if n.left == None and n.right == None:
            if n.parent.left == n: n.parent.left=None
            elif n.parent.right == n: n.parent.right=None

        elif n.left == None and n.right != None:
            if n.parent.right == n:
                n.parent.right = n.right
                n.right.parent = n.parent
            elif n.parent.left == n:
                n.parent.left = n.right
                n.right.parent = n.parent

        elif n.right == None and n.left != None:
            if n.parent.right == n:
                n.parent.right = n.left
                n.left.parent = n.parent
            elif n.parent.left == n:
                n.parent.left = n.left
                n.left.parent = n.parent


def min(root):
    while root.left is not None: root=root.left
    return root

def max(root):
    while root.right is not None: root=root.right
    return root

def prev(root,key):
    p=find(root,key)
    if p is None: return None

    if p.left is not None:
        p=p.left
        p=max(p)

    else:
        while p.parent is not None and p.parent.left == p: p=p.parent
        if p.parent is not None and p.parent.right == p: p = p.parent
        else: p=None

    return p


def next(root,key):
    p=find(root,key)
    if p is None: return None

    if p.right is not None:
        p=p.right
        p=min(p)

    else:
        while p.parent is not None and p.parent.right == p: p=p.parent
        if p.parent is not None and p.parent.left == p: p=p.parent
        else: p=None

    return p


#BST
root=BSTNode(21)
insert(root,15)
insert(root,37)
insert(root,5)
insert(root,7)
insert(root,13)
insert(root,8)
insert(root,20)
insert(root,25)
insert(root,40)




#
# print(root.key)
# print(root.left.key,root.right.key)
# print(root.left.left.key,root.left.right.key,root.right.left.key,root.right.right.key)
# print(root.left.left.right.key)
# print(root.left.left.right.right.key)
# print(root.left.left.right.right.left.key)
# print("..")
# print(prev(root,20).key)
# print(next(root,20).key)
#
# remove(root,15)
# print(prev(root,20).key)
#
print("....")
print(next(root,20).key)
remove(root,21)
print(next(root,20).key)
#
# print()



# remove(root,21)
# print(find(root,21).key)