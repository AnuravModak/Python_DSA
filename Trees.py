class TreeNode:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
    def preorder_printing(self):
        if self is None:
            return
        print("parent: {}, child: {}".format(self.parent.val,self.val))
        if self.right:
            self.right.preorder_printing()
        if self.left:
            self.left.preorder_printing()
    def check(self,root,data):
        if root is None:
            return False
        if root.val==data:
            self.arr.append(root.val)
            return True
        l=self.check(root.left,data)
        r=self.check(root.right,data)
        if l:
            self.arr.append(root.val)
        if r:
            self.arr.append(root.val)
        return (l or r)
    def path_root_to_node(self,root,val):
        self.arr=[]
        y=self.check(root,val)
        if y:
            # self.arr.reverse()
            print(self.arr)

    def search_parent(self, root, B, height=0):
        if root is None:
            return False
        if root.val == B:
            self.arr.append([root.val,root])
            return True
        l = self.search_parent(root.left, B, height)
        r = self.search_parent(root.right, B, height)
        if l:

            self.arr.append([root.val,root])
        if r:
            self.arr.append([root.val,root])

        return l or r

    def print_elements(self, root, h1, h2=0):
        if root is None:
            return
        h2 += 1
        if h2 == h1:
            self.ele_height.append(root)
        if root.left:
            self.print_elements(root.left, h1, h2)
        if root.right:
            self.print_elements(root.right, h1, h2)

    def solve(self, A, B):
        self.arr = []
        res = []
        self.ele_height = []
        y = self.search_parent(A, B)
        self.print_elements(A, len(self.arr))
        # print(self.arr)
        # print(self.ele_height)
        if len(self.arr)>1:
            parent = self.arr[1][1]
            # print(parent)
            for i in self.ele_height:
                if parent.left and parent.right:
                    if parent.left.val != i.val and parent.right.val != i.val:
                        res.append(i.val)
                if parent.left and not parent.right:
                    if parent.left.val!=i.val:
                        res.append(i.val)
                if parent.right and not parent.left:
                    if parent.right.val!=i.val:
                        res.append(i.val)


            print(res)
        else:
            print([])

















if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(5)
    root.left.right.right.left = TreeNode(8)
    # root.preorder_printing()
    # root.path_root_to_node(root,8)
    root.solve(root,6)
    # root.preorder_printing()
    # root.left=TreeNode(1)
    # root.left=TreeNode(1)
    # root.left=TreeNode(1)
    # root.left=TreeNode(1)



