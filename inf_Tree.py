class TreeNode:
    def __init__(self,data):
        self.val=data
        self.child=[]
    def print_child(self,root):
        if root is None:
            return
        print(root.val)
        for i in root.child:
            self.print_child(i)


if __name__ == '__main__':
    root=TreeNode(0)
    root.child.append(TreeNode(1))
    root.child.append(TreeNode(2))
    root.child.append(TreeNode(3))
    root.child[1].child.append(TreeNode(4))
    root.print_child(root)

