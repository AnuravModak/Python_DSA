
class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=self
        self.sum=-1
        self.right_height=-1
        self.left_height=-1

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
            
    def max_Height(self,l=0,r=0):
        if self is not None:
            if self.left is not None:
                l=1+self.left.max_Height(l)
                return l
            if self.right is not None:
                r=1+self.right.max_Height(r)
                return r
            if self.left is None and self.right is None:
                return max(r,l)

    def Height(self,root):
        if root is None:
            return 0
        else:
            return  1+max(self.Height(root.left), self.Height(root.right))



    def diameter_Of_Tree(self,root):
        if root is None:
            return 0
        lheight=self.Height(root.left)
        rheight=self.Height(root.right)

        ldiameter=self.diameter_Of_Tree(root.left)
        rdiameter=self.diameter_Of_Tree(root.right)
        return max(lheight+rheight,max(ldiameter,rdiameter))













    # def diameter_Of_Tree(self,left_subtree=0,right_subtree=0,left_diameter =0,right_diameter=0):
        


        


if __name__ == '__main__':
    root=TreeNode("Root")
    root.add_node(1)
    root.add_node(2)
    root.add_node(3)
    root.add_node(4)
    root.add_node(5)
    root.add_node(6)
    root.add_node(7)
    root.add_node(8)
    root.add_node(9)

    root.print_Tree()

    print("Height of the tree",root.max_Height())
    # the reason i am passing 1 as "l" because i am jumping one node from root to node.left
    # print("Height of the left subtree",root.left.max_Height(1,0))
    # the reason i am passing 1 as "r" because i am jumping one node from root to node.right
    # print("Height of the right subtree", root.right.max_Height(0,1))


    #use max_height() to calulate height
    # and use Height(_) to calculate diameter of binary tree
    print("Diameter of binary Tree",root.diameter_Of_Tree(root))







