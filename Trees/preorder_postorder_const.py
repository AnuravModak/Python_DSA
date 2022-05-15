class Treenode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1



def buildtree(preorder,inorder,start,end):
    global idx
    idx=0
    curr=preorder[idx]
    if start > end:
        return None
    idx+=1
    n1=Treenode(curr)
    if start==end:
        return n1
    pos=search(inorder,curr)
    n1.left=buildtree(preorder,inorder,start,pos-1)
    n1.right=buildtree(preorder,inorder,pos+1,end)
    return n1

def printInorder(node):
    printInorder(node.left)
    print(node.data)
    printInorder(node.right)

if __name__ == '__main__':
    preorder=[1,2,4,3,5]
    inorder=[4,2,1,5,3]
    print(buildtree(preorder,inorder,0,4))
