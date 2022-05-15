class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=self
        self.inorder_suc=None
        self.inorder_pred=None
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
    def preOrder(self):
        if self.left is not None:
            self.left.preOrder()
        print(self.data)
        if self.right is not None:
            self.right.preOrder()

    def in_Order(self,f=[]):
        if self is None:
            return
        if self.left:
            self.left.in_Order(f)
        f.append(self.data)
        if self.right:
            self.right.in_Order(f)
        return f

        # for every node: for left subtree, left child must be less than root node and its parent or null
        # for every node: for right subtree, right child must be more than root node and its parent or null
    def is_BST(self,root,min=None,max=None):
        if root is None:

            return True
        if self is None:
            return

        if min is not None and root.data<=min.data:
            return False
        if max is not None and root.data>=max.data:
            return False

        l=self.is_BST(root.left,min,root)

        r=self.is_BST(root.right,root,max)

        return l and r

    def build_BST(self,arr,start,end):
        if start>end:
            return None
        mid=(start+end)//2
        root=TreeNode(arr[mid])
        root.left=self.build_BST(arr,start,mid-1)
        root.right=self.build_BST(arr,mid+1,end)
        return root

























if __name__ == '__main__':

    # Test-Case-1
    # root=TreeNode(12)
    # root.left=TreeNode(6)
    # root.left.parent=root
    # root.right = TreeNode(4)
    # root.right.parent=root
    #
    # root.left.right=TreeNode(14)
    # root.left.right.parent=root.left
    #
    #
    # root=TreeNode(4)
    # root.left=TreeNode(2)
    # root.left.parent=root
    #
    # root.left.left=TreeNode(1)
    # root.left.parent=root.left
    # root.left.left.parent=root.left
    #
    # root.right=TreeNode(7)
    # root.right.parent=root
    #
    # root.right.left=TreeNode(3)
    # root.right.left.parent=root.right
    # root.right.right=TreeNode(8)
    # root.right.right.parent=root.right

    # Test-Case-2
    # root=TreeNode(12)
    # root.add_node(6)
    # root.add_node(0)
    # root.add_node(7)
    # root.add_node(5)
    # root.add_node(8)
    # root.add_node(14)
    # root.add_node(16)
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
    print(root.is_BST(root))
    # arr=[10,20,30,40,50,60,70]
    # y=root.build_BST(arr,0,len(arr)-1)
    # y.preOrder()
    # print(y.in_Order([]))
    # print(y.data,y.left.data,y.right.data)
    print(root.in_Order([]))


