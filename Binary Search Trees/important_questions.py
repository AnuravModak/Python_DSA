def isIdentical( root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root2 is None or root1 is None:
        return False
    else:
        a = root1.data == root2.data
        b = isIdentical(root1.left, root2.left)
        c = isIdentical(root1.right, root2.right)
        if a and b and c:
            return True
        else:
            return False




class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=self
    def add_node(self,data):
        if self.data<data:
            if self.right is None:
                new_node=TreeNode(data)
                self.right=new_node
                new_node.parent=self
            else:
                self.right.add_node(data)
        elif self.data>data:
            if self.left is None:
                new_node=TreeNode(data)
                self.left=new_node
                new_node.parent=self
            else:
                self.left.add_node(data)
        else:
            print("Node already exist:",self.data)
            return
    def print_Tree(self):
        n=self
        if n is None:
            return
        if n is not None:
            # print("parent:{}",self.parent.data,", child =>",self.data)
            print('parent: {}, child: {}'.format(self.parent.data,self.data))
        if n.left is not None:
            n.left.print_Tree()
        if n.right is not None:
            n.right.print_Tree()

    def in_Order(self, f=[]):
        if self is None:
            return
        if self.left:
            self.left.in_Order(f)
        f.append([self, self.data])
        if self.right:
            self.right.in_Order(f)
        return f




if __name__ == '__main__':
    root1=TreeNode(1)
    root1.add_node(3)
    root1.add_node(2)
    root1.add_node(5)
    root1.print_Tree()
    print()
    root2 = TreeNode(1)
    root2.add_node(3)
    root2.add_node(2)
    root2.add_node(5)
    root2.print_Tree()

    print(isIdentical(root1,root2))




