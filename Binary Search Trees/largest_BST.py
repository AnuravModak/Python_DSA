class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=self
        self.min=self.data
        self.max=self.data
        self.subTreeSize=1
        self.isBST=True
        self.sizeOfLargestBST=0
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

    def print_Tree_With_Attributes(self):
        n = self
        if n is None:
            return
        if n is not None:
            # print("parent:{}",self.parent.data,", child =>",self.data)
            print('parent: {}, current node: {}, max: {}, min: {}, subtree size: {}, isBST: {}'
                  .format(self.parent.data, self.data,self.max,self.min,self.subTreeSize,self.isBST))
        if n.left is not None:
            n.left.print_Tree_With_Attributes()
        if n.right is not None:
            n.right.print_Tree_With_Attributes()



    def largest_BST(self):
        if self is None:
            return
        if self.left is None and self.right is None:
            return
        if self.left :
            self.left.largest_BST()
        if self.right:
            self.right.largest_BST()
        # now here the placement is very important....here i need to use "Bottom to Up" approach...
        # thats why i am first traversing to the lowest level in the function...and then comes
        
        if self.left is not None and self.right is not None:
            self.isBST = True if self.data<self.right.data and self.data>self.left.data else False
            self.min = min(self.left.min, self.right.min, self.min)
            self.max = max(self.left.max, self.right.max, self.max)
            self.subTreeSize += self.left.subTreeSize + self.right.subTreeSize
        if self.left is not None and self.right is None:
            self.isBST = True if self.data>self.left.data else False
            self.min = min(self.left.min, self.min)
            self.max = max(self.left.max, self.max)
            self.subTreeSize += self.left.subTreeSize
        if self.right is not None and self.left is None:
            self.isBST =  True if self.data<self.right.data else False
            self.min = min( self.right.min, self.min)
            self.max = max( self.right.max, self.max)
            self.subTreeSize +=  self.right.subTreeSize











if __name__ == '__main__':
    root=TreeNode(5)
    # root.left=TreeNode(14)
    # root.left.parent=root
    # root.right=TreeNode(6)
    # root.right.parent=root
    root.add_node(3)
    root.add_node(6)
    root.add_node(2)
    root.add_node(4)
    root.add_node(7)
    root.print_Tree()
    root.largest_BST()
    root.print_Tree_With_Attributes()

