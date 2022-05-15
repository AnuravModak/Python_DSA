# QUESTIONS:
# Sum Replacement problem(inplace) without using any additional data structure.
# Max Height of the binary tree.
# Get path from root to node.
# Check if the tree is balanced.
# Lowest Common ancestor (LCA).
# Shortest Path between two nodes.
# Flatten the binary tree (inplace) without using additional data strutures.
# Children of a node at Kth distance.
# Ancestor of a node at Kth distance.
# Find all Nodes at Kth distance from a given node.

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
            self.left.in_Order()
        print('parent: {}, child: {}'.format(self.parent.data, self.data))
        if self.right:
            self.right.in_Order()

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

    def sum_Replacement(self):
        # as i am traversing left and right nodes seperately i need to return values after each recursion
        if self.right is None and self.left is None:
            return self.data
        if self.right is None :
            self.data+=self.left.sum_Replacement()
            return self.data
        if self.left is None :
            self.data+=self.right.sum_Replacement()
            return self.data
        if self.right is not None and self.left is not None:
            self.data=self.right.sum_Replacement()+self.left.sum_Replacement()
            return self.data

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

    def minDepth(self,root):
        # Corner Case.Should never be hit unless the code is
        # called on root = NULL
        if root is None:
            return 0

        # Base Case : Leaf node.This acoounts for height = 1
        if root.left is None and root.right is None:
            return 1

        # If left subtree is Null, recur for right subtree
        if root.left is None:
            return self.minDepth(root.right) + 1

        # If right subtree is Null , recur for left subtree
        if root.right is None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def Height(self,root):
        if root is None:
            return 0
        else:
            return  1+max(self.Height(root.left), self.Height(root.right))

    def isHeightBalanced(self, root, isBalanced=True):

        # base case: tree is empty or not balanced
        if root is None or not isBalanced:
            return 0, isBalanced

        # get the height of the left subtree
        left_height, isBalanced = self.isHeightBalanced(root.left, isBalanced)

        # get the height of the right subtree
        right_height, isBalanced = self.isHeightBalanced(root.right, isBalanced)

        # tree is unbalanced if the absolute difference between the height of
        # its left and right subtree is more than 1
        if abs(left_height - right_height) > 1:
            isBalanced = False

        # return height of subtree rooted at the current node
        return max(left_height, right_height) + 1, isBalanced





    def get_path_from_root_to_node(self,n_data,found=False):
        n=self
        queue=[]
        path=[0]
        traverse=[]
        queue.append(n)
        while not found and len(queue)>0 :
            i=queue[0]
            if i.data==n_data:
                found=True
                traverse.append([i.data,i])
                break
            if i.left is not None:
                queue.append(i.left)
                traverse.append([i.left.data,i.left])
                if i.left.data==n_data:
                    found=True
                    break
            if i.right is not None:
                queue.append(i.right)
                traverse.append([i.right.data,i.right])
                if i.right.data==n_data:
                    found=True
                    break
            queue.pop(0)
        # print(traverse)
        if found :
            c=len(traverse)
            n=traverse[c-1][1]
            while n.data!=0:
                path.insert(1,n.data)
                n=n.parent
            return path,True

        else:
            return path,False

    def LCA(self,n1,n2):
        p1, p1_exist=self.get_path_from_root_to_node(n1)
        p2, p2_exist = self.get_path_from_root_to_node(n2)
        if p1_exist and p2_exist:
            if len(p1)>=len(p2):
                for i in range(len(p2)):
                    if p2[i]!=p1[i]:
                        return p1,p2,p2[i-1]
                return p1,p2,p2[len(p2)-1]
            else:
                for i in range(len(p1)):
                    if p1[i]!=p2[i]:
                        return p1,p2,p1[i-1]
                return p1,p2,p1[len(p1)-1]
        else:
            return [],[],-1

    def get_Shortest_path(self,n1,n2):
        p1,p2,lca=self.LCA(n1,n2)
        print(lca,p1,p2)
        if lca!=-1:
            i1 = p1.index(n1)
            j1 = p1.index(lca)
            u = i1 - j1

            i2 = p2.index(n2)
            j2 = p2.index(lca)
            v = i2 - j2

            shortest_path = []
            for i in range(i1, -1, -1):
                shortest_path.append(p1[i])
                if p1[i] == lca:
                    break
            for i in range(p2.index(lca), len(p2)):
                shortest_path.append(p2[i])
                if p2[i] == n2:
                    break
            shortest_path = list(dict.fromkeys(shortest_path))

            print("length of shortest path: {} and path is: {}".format((u+v),shortest_path))
            # return u+v
        else:
            print("Node doesnt exist")


    def search_element(self,root,val):
        if root is None:
            return False
        if root.data==val:
            return True
        l=self.search_element(root.left,val)
        r=self.search_element(root.right,val)
        return l or r



    def flatten_Tree(self):
        if self ==None or (self.left is None and self.right is None ):
            return
        if self.left is not None:
            self.left.flatten_Tree()
            self.temp=self.right
            self.right=self.left
            self.left=None

            self.tail=self.right
            # another temporary variable...which actually stores root.left
            # now this tail's last node will be left node which we kept "None"....i.e at last i will append the right node
            while self.tail.right is not None:
                self.tail=self.tail.right
            self.tail.right=self.temp
        self.right.flatten_Tree()


    def nodesAt_Kth_distance_child(self,node,k,np):
        if k==0:
            np.append(self.data)
            return np
        if self.left is not None:
            self.left.nodesAt_Kth_distance_child(node,k-1,np)
        if self.right is not None:
            self.right.nodesAt_Kth_distance_child(node,k-1,np)
        return np

    def nodesAt_Kth_distance_ancestor(self,node,k,np):
        if self.parent.left.data==self.data:
            p=self.parent.right.nodesAt_Kth_distance_child(node,k-2,np)
            np=np+p
            np=list(dict.fromkeys(np))
            return np
        if self.parent.right.data==self.data:
            p=self.parent.left.nodesAt_Kth_distance_child(node,k-2,np)
            np = np + p
            np = list(dict.fromkeys(np))
            return np

    def nodesAt_Kth_distance(self,node,k,mp):
        if self.parent.data!=self.data:# means if its not the root node
            child=self.nodesAt_Kth_distance_child(node,k,[])
            ancestor=self.nodesAt_Kth_distance_ancestor(node,k,[])
            mp=child+ancestor
            mp=list(dict.fromkeys(mp))
            return mp
        else:
            np=self.nodesAt_Kth_distance_child(node,k,[])
            return np




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
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

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

    # the next 3 lines will change the tree to sum_replaced tree...so be carefull before uncommenting
    # root.sum_Replacement()
    # print()
    # root.print_Tree()

    t1=root
    p=[]
    # print(root.is_Balanced())
    y1,h=root.get_path_from_root_to_node(-1)
    print(y1,h)
    print(root.get_path_from_root_to_node(8))

    root.get_Shortest_path(1,9)

    # this will flatten the tree inplace
    # root.flatten_Tree()
    # root.inOreder()
    # n=root
    # while n is not None:
    #     print(n.data)
    #     n=n.right
    #

    m=2
    print('children at distance {}:'.format(m),root.left.nodesAt_Kth_distance_child(1,m,[]))
    print("ancestor at distance {}:".format(m+1),root.left.nodesAt_Kth_distance_ancestor(1,m+1,[]))
    print("nodes at Kth distance {}:".format(m),root.left.nodesAt_Kth_distance(1,m,[]))
    print(root.search_element(root,7))











