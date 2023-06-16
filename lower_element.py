class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def search(root, value):
    current = root
    l1 =  []
    while current.info != value:
        l1.append(current.info)
        if current.info > value:
            current = current.left
        else:
            current = current.right
        if current is None:
            return None
    return l1


def lca(root, v1, v2):
    l1 = search(root, v1)
    l2 = search(root, v2)
    if l1 is None or l2 is None:
        return None
    common = set(l1) & set(l2)
    if len(common) == 0:
        return None
    r = common.pop()
    print(r)
    return r

# Example usage:
# Constructing an example tree
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
# root.left.right = Node(2)
root.right.left = Node(6)
# root.right.right = Node(8)
# root.left.right.left = Node(7)
# root.left.right.right = Node(4)

# 4 2 3 1 7 6
# 1 7

v1 = 1
v2 = 7
ans = lca(root, v1, v2)
print(ans)
