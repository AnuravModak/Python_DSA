# So we can only create a binary search tree from post-order/pre-Order traversal
# We can also create a BST from inorder or....whatever BST u have..
# inorder traversal will always give u elements in ascending order......
# so whatever BST tree u create is correct...as all the possoble combination is possible
# That is why we say its not possible because it doesnt make any sense....






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
            self.left.post_Order()
        if self.right:
            self.right.post_Order()
        print('{}'.format(self.data),end=" ")
    def inOrder(self):
        if self is None:
            return
        if self.left:
            self.left.inOrder()
        print('{}'.format(self.data),end=" ")
        if self.right:
            self.right.inOrder()

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




    def postOrder_to_Tree(self,s):
        root=TreeNode(s[-1])
        s.reverse()
        s.pop(0)
        for i in s:
            root.add_node(i)
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


    # root.post_Order()
    # PO=[1, 4, 7 ,9 ,8, 6 ,3, 2 ,13 ,12, 11, 10 ]
    # y=root.postOrder_to_Tree(PO)
    # y.print_Tree()


    root.inOrder()







