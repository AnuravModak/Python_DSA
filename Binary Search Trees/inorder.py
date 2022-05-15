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

    def in_Order(self,f=[]):
        if self is None:
            return
        if self.left:
            self.left.in_Order(f)
        f.append([self.data,self.inorder_pred,self.inorder_suc])
        if self.right:
            self.right.in_Order(f)
        return f

    def inorder_succ_pred(self):
        if self is None:
            return
        if self.right is None:
            if self.parent.data>self.data:
                self.inorder_suc= self.parent.data
        if self.left is None:
            if self.data>self.parent.data:
                self.inorder_pred = self.parent.data

        if self.right is None and self.left is None:
            if self.parent.data>self.data:
                self.inorder_suc = self.parent.data
        if self.left is not None:
            self.inorder_pred = self.left.data
            self.left.inorder_succ_pred()
        if self.right is not None:
            self.inorder_suc = self.right.data
            self.right.inorder_succ_pred()


    def return_inorder_succ_pred(self, key):
        if self == None:
            return
        if self.data == key:
            return self.inorder_pred, self.inorder_suc
        if self.left is not None:
            if key < self.data:
                y = self.left.return_inorder_succ_pred(key)
                return y
        if self.right is not None:
            if key > self.data:
                y = self.right.return_inorder_succ_pred(key)
                return y



if __name__ == '__main__':
    root = TreeNode(50)
    root.add_node(30)
    root.add_node(20)
    root.add_node(60)
    root.add_node(70)
    root.print_Tree()
    root.inorder_succ_pred()
    print(root.in_Order([]))
