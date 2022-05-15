class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=self

    # By default i will add the node to left child
    def add_node(self,data):
        if not self.left:
            new_node=TreeNode(data)
            new_node.parent = self
            self.left=new_node

        elif not self.right:
            new_node = TreeNode(data)
            new_node.parent = self
            self.right = new_node

        else:
            self.left.add_node(data)

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
    def pre_Order(self):
        if self is None:
            return
        print('parent: {}, child: {}'.format(self.parent.data, self.data))
        if self.left:
            self.left.pre_Order()
        if self.right:
            self.right.pre_Order()
    def post_Order(self):
        if self is None:
            return
        if self.left:
            self.left.pre_Order()
        if self.right:
            self.right.pre_Order()
        print('parent: {}, child: {}'.format(self.parent.data, self.data))
    def inOreder(self):
        if self is None:
            return
        if self.left:
            self.left.pre_Order()
        print('parent: {}, child: {}'.format(self.parent.data, self.data))
        if self.right:
            self.right.pre_Order()

    def levelOrder(self,root):
        queue=[]
        print(root.data)
        queue.append(root)
        while len(queue)>0:
            i=queue[0]

            if i.left is not None:
                print("parent: {}, child: {}".format(i.left.parent.data,i.left.data))
                queue.append(i.left)
            if i.right is not None:
                print("parent: {}, child: {}".format(i.right.parent.data,i.right.data))
                queue.append(i.right)
            queue.pop(0)










if __name__ == '__main__':
    root=TreeNode("Root")
    root.add_node(1)
    root.add_node(2)
    root.add_node(3)
    root.add_node(4)
    root.print_Tree()

    print()
    print("Pre-Order Traversal")
    root.pre_Order()

    print()
    print("Post-Order Traversal")
    root.post_Order()

    print()
    print("Inorder Traversal")
    root.inOreder()

    print()
    print("LevelOrder Traversal")
    root.levelOrder(root)








