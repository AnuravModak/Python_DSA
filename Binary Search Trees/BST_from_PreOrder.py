class TreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.parent=self

    def add_node(self, data):
        if self.data < data:
            if self.right is None:
                new_node = TreeNode(data)
                self.right = new_node
                new_node.parent = self
            else:
                self.right.add_node(data)
        elif self.data > data:
            if self.left is None:
                new_node = TreeNode(data)
                self.left = new_node
                new_node.parent = self
            else:
                self.left.add_node(data)
        else:
            print("Node already exist:", self.data)
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




    def preOrder_to_Tree(self,s):
        root=TreeNode(s[0])
        for i in range(1,len(s)):
            root.add_node(s[i])
        return root

if __name__ == '__main__':
    root = TreeNode(10)
    root.add_node(2)
    root.add_node(3)
    root.add_node(6)
    root.add_node(8)
    root.add_node(1)
    root.add_node(11)
    root.add_node(12)
    root.add_node(13)
    root.add_node(4)
    root.add_node(9)
    root.add_node(7)


    root.print_Tree()
    y=root.preOrder_to_Tree([7,5,4,6,8,9])
    print()
    y.print_Tree()






