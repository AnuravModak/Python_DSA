# if the current data is less than root.data-> append it to its left else to its right
#   and no duplicates allowed.
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

    def in_Order(self,f=[]):
        if self is None:
            return
        if self.left:
            self.left.in_Order(f)
        f.append([self,self.data])
        if self.right:
            self.right.in_Order(f)
        return f

    def search_node(self,data,l=0,r=0):
        if self.data==data:
            return data
        if self.data>data:
            if self.left is not None:
                l=self.left.search_node(data,l,r)
        if self.data<data:
            if self.right is not None:
                r=self.right.search_node(data,l,r)
        if l==data or r==data:
            return data
        else:
            return None


    def search_node_and_Delete(self,data,l=None,r=None):
        # THIS FUNCTION WILL RETURN
        if self.data==data:
            return self
        if self.data>data:
            if self.left is not None:
                l=self.left.search_node_and_Delete(data,l,r)
        if self.data<data:
            if self.right is not None:
                r=self.right.search_node_and_Delete(data,l,r)
        if l.data==data or r.data==data:
            return self
        else:
            return None

    def delete_node(self,data,y):
        if self is None:
            return
        if self.data<data:
            self.right.delete_node(data,y)
        elif self.data>data:
            self.left.delete_node(data,y)
        else:
            print(self.data,self)
            if self.left is None and self.right is None:
                if self.parent.right.data==self.data:
                    self.parent.right=None
                    self.parent=None
                elif self.parent.left.data==self.data:
                    self.parent.left=None
                    self.parent=None
            elif self.right is None or self.left is None:
                if self.parent.right.data==self.data:
                    if self.left is not None:
                        self.left.parent = self.parent
                        self.parent.right=self.left
                        del self
                    elif self.right is not None:
                        self.right.parent=self.parent
                        self.parent.right=self.right
                        del self
                elif self.parent.left.data==self.data:
                    if self.left is not None:
                        self.left.parent = self.parent
                        self.parent.right = self.left
                        del self
                    elif self.right is not None:
                        self.right.parent = self.parent
                        self.parent.right = self.right
                        self.parent = None
                        self.left = None
                        self.right = None
                        del self

            else:
                c=0
                for i in y:
                    c+=1
                    if i[1]==data:
                        break
                i=c-1
                inorder=y[i-1][0]
                print("inorder",inorder.data)

                if self.parent.left is not None:
                    if self.parent.left.data==self.data:
                        self.parent.left=inorder
                        inorder.parent=self.parent

                        if self.right is not None:
                            if self.right.data!=inorder.data:
                                inorder.right=self.right
                        if self.left is not None:
                            if self.left.data!=inorder.data:
                                inorder.left=self.left
                        del self


                if self.parent.right is not None:
                    if self.parent.right.data == self.data:
                        self.parent.right = inorder
                        inorder.parent = self.parent
                        if self.right is not None:
                            if self.right.data != inorder.data:
                                inorder.right = self.right
                                self.right.parent=inorder
                        if self.left is not None:
                            if self.left.data != inorder.data:
                                inorder.left = self.left
                                self.left.parent=inorder
                        del self


    def delete_root(self):
        y=self.in_Order([])
        c=0
        for i in y:
            c+=1
            if i[1]==self.data:
                break
        i=c-1
        inorder=y[i-1][0]
        print("inorder",inorder.data,inorder.right)
        # now here also we have 3 cases the Inorder/Successor may have 0,1,2 nodes
        # So check for every one of the case......
        if inorder.left is None and inorder.right is None:
            try:
                if inorder.parent.right.data == inorder.data:
                    inorder.parent.right = None
                if inorder.parent.left.data == inorder.data:
                    inorder.parent.left = None
            except:
                pass
            inorder.parent=inorder

            inorder.left=self.left
            self.left.parent=inorder
            inorder.right=self.right
            self.right.parent=inorder
            self=inorder
            return self

        elif inorder.left is None or inorder.right is None:
            inorder.parent=inorder
            try:
                if inorder.parent.right.data == inorder.data:
                    inorder.parent.right = None
                if inorder.parent.left.data == inorder.data:
                    inorder.parent.left = None
            except:
                pass
            if inorder.left is not None:
                n=inorder
                while n.left is not None:
                    n=n.left
                self.left.parent=n
                n.left=self.left
            elif inorder.right is not None:
                n=inorder
                while n.right is not None:
                    n=n.right
                self.right.parent=n
                n.right=self.right
            self=inorder
            return self
        else:
            try:
                if inorder.parent.right.data == inorder.data:
                    inorder.right = None
                if inorder.parent.left.data == inorder.data:
                    inorder.left = None
            except:
                pass

            l=inorder
            while l.left is not None:
                l=l.left
            self.left.parent=l
            l.left=self.left
            r=inorder
            while r.right is not None:
                r=r.right
            self.right.parent=r
            r.right=self.right
            self=inorder
            return self

    def zig_zag_traversal(self):
        curr = []
        print(root.data)
        res=[]
        fin=[]
        fin.append(self.data)
        curr.append(root)
        left_right=True
        while len(curr)>= 0:
           if left_right:
               left_right=False
           else:
               left_right=True

           if len(curr)==0 and len(res)==0:
                break
           if not left_right:
               for i in curr:
                   if i.right is not None:
                       res.append(i.right)
                       fin.append(i.right.data)
                   if i.left is not None:
                       res.append(i.left)
                       fin.append(i.left.data)

           else:
               for i in curr:
                   if i.left is not None:
                       res.append(i.left)
                       fin.append(i.left.data)
                   if i.right is not None:
                       res.append(i.right)
                       fin.append(i.right.data)

           # fin.append("N")
           curr.clear()
           curr=res.copy()
           res.clear()
        return fin









if __name__ == '__main__':
    root=TreeNode(10)
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

    y=root.search_node(4)
    if y:
        print("Found:",y)
    else:
        print("Not Found")

    print(root.in_Order([]))

    # A very dangerous delete operation....and root cant be deleted
    # y=root.in_Order([])
    # root.delete_node(8,y)
    # print(root.in_Order())
    # root.print_Tree()
    # deleting root is a difficult task...so kindly take care of it...
    # in the above node_deletion....very branched tree will throw err or return a smashed tree
    # root=root.delete_root()
    # print(root.left.data)
    # print(root.right.data)
    # print(root.parent.data)

    # root.print_Tree()
    print(root.zig_zag_traversal())
    root.inorder_succ_pred()
    print(root.return_inorder_succ_pred(11))


















