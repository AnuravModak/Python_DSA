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
            self.right.add_node(data)

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

    def l_Order(self,root):
        queue=[]
        queue.append(root)
        l_order=[]
        l_order.append(root.data)
        while len(queue)>0:
            i=queue[0]

            if i.left is not None:
                l_order.append(i.left.data)
                queue.append(i.left)
            if i.right is not None:
                l_order.append(i.right.data)
                queue.append(i.right)
            queue.pop(0)
            l_order.append("next")
        return l_order
    def r_Order(self,root):
        queue=[]
        queue.append(root)
        r_order=[]
        r_order.append(root.data)
        while len(queue)>0:
            i=queue[0]
            if i.right is not None:
                r_order.append(i.right.data)
                queue.append(i.right)
            if i.left is not None:
                r_order.append(i.left.data)
                queue.append(i.left)

            queue.pop(0)
            r_order.append("next")
        return r_order




if __name__ == '__main__':
    root=TreeNode("Root")
    root.add_node(1)
    # root.add_node(2)
    # root.add_node(3)
    # root.add_node(4)
    # root.add_node(5)
    # root.add_node(6)
    # root.add_node(7)
    # root.add_node(8)
    # root.add_node(9)

    root.print_Tree()
    left_order=root.l_Order(root)
    # print(left_order)
    print()
    print("left View of the subtree")
    for i in range(len(left_order)):
        if left_order[i]=="Root":
            print(left_order[i])
            if i+1<len(left_order):
                print(left_order[i+1])
        if left_order[i]=='next':
            if i+1<len(left_order) :
                if not left_order[i+1]=="next":
                    print(left_order[i+1])

    right_order=root.r_Order(root)
    print()
    print("right View of the subtree")
    for i in range(len(right_order)):
        if right_order[i] == "Root":
            print(right_order[i])
            if i + 1 < len(right_order):
                print(right_order[i + 1])
        if right_order[i] == 'next':
            if i + 1 < len(right_order):
                if not right_order[i + 1] == "next":
                    print(right_order[i + 1])



