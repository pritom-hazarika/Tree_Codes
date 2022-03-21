class Node:
    def __init__(self,cargo,left=None,right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.cargo)

def insert(root,key):
    if root is None:
        return Node(key)
    if root.cargo>key:
        if root.left is None:
            root.left = Node(key)
        else:
            insert(root.left,key)
    else:
        if root.right is None:
            root.right = Node(key)
        else:
            insert(root.right,key)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root,end=' ')
        inorder(root.right)


if __name__ =='__main__':
    tree = Node(5)
    insert(tree,2)
    insert(tree,8)
    insert(tree,9)
    insert(tree,6)
    insert(tree,4)
    insert(tree,3)
    inorder(tree)