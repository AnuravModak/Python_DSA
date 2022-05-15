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


    def max_Path_Sum_Of_Tree(self,l=0,r=0):
        if self.left is None and self.right is None:
            return self.data
        if self.left is not None:
            l=self.left.max_Path_Sum_Of_Tree(l,r)
            l+=self.data
        if self.right is not None:
            r=self.right.max_Path_Sum_Of_Tree(l,r)
            r+=self.data
        # print(l,r,self.data,l+r)
        if self.data==0:
            # this will be my output..i.e "root" will always come last in recursion stack...
            # so the last one to execute will have the ans in its parameters.so return or modify it...
            return max(l,r,self.data,l+r)
        return max(l,r,self.data)

       # NOTE: in binary trees or in trees in general...max path sum between two nodes is not a practically feasible question....
       # because u can only approach a node from its parent node only...so the path from node1 to node2 is an unique and only
       # possible path...so that will be the max path sum between node1 and node2.



if __name__ == '__main__':
    root = TreeNode(0)
    # way1
    # root.add_node(1)
    # root.add_node(2)
    # root.add_node(3)
    # root.add_node(4)
    # root.add_node(5)
    # root.add_node(6)
    # root.add_node(7)
    # root.add_node(8)
    # root.add_node(9)

    #way1 ends here----------------------------------

    #Either use way 1 or way2 below-----------------
    node1=TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(-5)
    node6 = TreeNode(6)
    node7 = TreeNode(-7)
    node8 = TreeNode(8)
    node9 = TreeNode(-9)

    root.left=node1
    root.right=node2
    node1.parent=root
    node2.parent=root

    node1.left=node3
    node1.right=node4
    node3.parent=node1
    node4.parent=node1

    node2.left=node5
    node5.parent=node2

    node3.left=node6
    node3.right=node7
    node7.parent=node3
    node6.parent=node3

    node4.left=node8
    node4.right=node9
    node8.parent=node4
    node9.parent=node4
    # way2 ends here-----------------------------------------
    root.print_Tree()

    print("max path sum in a given tree is:",root.max_Path_Sum_Of_Tree())
    print(root.vertical_order_recursive(root))
