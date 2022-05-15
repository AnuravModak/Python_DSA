# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def print_Tree(self):
        n=self
        if n is None:
            return
        if n is not None:
            # print("parent:{}",self.parent.data,", child =>",self.data)
            print(self.val)
        if n.left is not None:
            n.left.print_Tree()
        if n.right is not None:
            n.right.print_Tree()


    def hasPathSum(self, A, B):
        ans=0
        if B == 0 and (self.right is None and self.left is None):
            return 1

        if self.right is not None:
            ans = ans or self.right.hasPathSum(A, B - self.val)

        if self.left is not None:
            ans = ans or self.left.hasPathSum(A, B - self.val)

        if ans:
            return 1
        else:
            return 0

    def pathsum(self,A,B,curr_sum,path=[]):
        c=curr_sum+A.val
        if c==B and (A.left is None and A.right is None):
            path.append(A.val)
            return path
        if A.left is not None and curr_sum!=B :
            path.append(A.val)
            path=self.pathsum(A.left,B,c,path)
        if A.right is not None and curr_sum!=B:
            path.append(A.val)
            path=self.pathsum(A.right,B,c,path)
        return path

    def get_path(self,A,B,left_path=None,right_path=None):
        if A.left is not None:
            left_path=self.pathsum(A.left,B,A.val,[A.val])
        if A.right is not None:
            right_path=self.pathsum(A.right,B,A.val,[A.val])
        ans=list(list())
        if left_path:
            if sum(left_path)==B:
                ans.append(left_path)
        if right_path:
            if sum(right_path)== B:
                ans.append(right_path)

        return ans
    def path_to_leaf(self,A,root,temp=[0]):
        if A is not None:
            temp.append(A.val)
        if A.left is None and A.right is None:

            temp.append(0)
            temp.append(root.val)
            return temp
        if A.right is not None:
            temp=self.path_to_leaf(A.right,root,temp)
        if A.left is not None:
            temp=self.path_to_leaf(A.left,root,temp)
        return temp

    def sumNumbers(self,A):
        y=self.path_to_leaf(root,root)
        list_string = list(map(str, y))
        sum=0
        l="".join(map(str,list_string))
        Split=l.split("0")
        print(Split)
        for i in range(len(Split)):
            if Split[i]!="" and Split[i]!=str(root.val):
                sum+=int(Split[i])
        print(sum)
        return sum%1003

    def dfs(self, root, num=0):
        if root.left == None and root.right == None:
            num = (num * 10 + root.val) % 1003
            self.ans = (self.ans + num) % 1003
            return
        num = (num * 10 + root.val) % 1003
        if root.left: self.dfs(root.left, num)
        if root.right: self.dfs(root.right, num)

    def SumNumbers(self, root):
        ans = 0
        self.dfs(root)
        return self.ans
    def preOrder(self,root):
        if root is not None:
            print(root.val)
        if root.left is not None:
            self.preOrder(root.left)
        if root.right is not None:
            self.preOrder(root.right)

    def iterative_preorderTraversal(self,root):
        ans=[]
        stack=[root]
        i=0
        while len(stack)>0:
            node=stack.pop(len(stack)-1)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            ans.append(node.val)
        return ans

    def vertical_order_recursive(self, root, line_no=0,l=0, vertical=dict()):
        if root is None:
            return vertical
        if line_no not in vertical:
            vertical[line_no] = [[root.val,l]]
        elif line_no in vertical:
            if root.val not in vertical[line_no]:
                vertical[line_no].append([root.val,l])
            else:
                return vertical
        if root.left is not None:
            y=line_no-1
            # line_no-=1 .... dont do this
            vertical = self.vertical_order_recursive(root.left,y,l+1, vertical)
        if root.right is not None:
            y=line_no +1
            #line_no+=1 .... dont do this
            vertical = self.vertical_order_recursive(root.right,y,l+1, vertical)


        return vertical

    def get_path_Interview_bit(self, root, v):
        self.arr = []
        y = self.get_path_func(root, v)
        if y:
            self.arr.reverse()
            return self.arr
        else:
            return -1

    def get_path_func(self, root, v):
        if root is None:
            return False
        if root.val== v:
            self.arr.append(root.val)
            return True
        l = self.get_path_func(root.left, v)
        r = self.get_path_func(root.right, v)
        if l:
            self.arr.append(root.val)
        if r:
            self.arr.append(root.val)
        return l or r








if __name__ == '__main__':
    # TREE-1
    # root =TreeNode(1)
    # root.left=TreeNode(3)
    # root.right=TreeNode(2)
    # root.right.left=TreeNode(4)
    # root.right.left.right=TreeNode(5)

    # TREE-2
    root = TreeNode(1)
    root.right=TreeNode(6)
    root.right.left=TreeNode(3)
    root.left=TreeNode(2)
    root.left.right=TreeNode(7)
    root.left.right.left=TreeNode(4)
    root.left.right.right=TreeNode(5)
    root.left.right.right.left=TreeNode(8)



    # print(root.hasPathSum(root,-1)
    # print(root.pathsum(root,4))
    # root.print_Tree()
    # print(root.get_path(root,-4))
    print(root.sumNumbers(root))
    root.preOrder(root)
    print(root.vertical_order_recursive(root))
    print(root.get_path_Interview_bit(root,8))


    




