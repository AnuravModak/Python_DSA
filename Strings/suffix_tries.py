class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.children=[]
    def construct_trie(self,val,i=0):
        if len(val)==i:
            return
        found=False
        for child in self.children:
            if child.val==val[i]:
                found=True
                child.construct_trie(val,i+1)
        if not found:
            n=node(val[i])
            self.children.append(n)
            self.next=node(val[i])
            self.children[len(self.children)-1].construct_trie(val,i+1)
    def construct_suffix_trie(self,string):
        i=0
        while i<len(string):
            self.construct_trie(string[i:])
            i+=1
    def print_trie(self,space=0):
        if self.children:
            ind=0
            for child in self.children:
                s="->"
                if child.next:
                    print(space * s + child.val,"next {}".format(child.next.val))

                else:
                    print(space * s + child.val, child.next)
                child.print_trie(space+1)


            space=0
if __name__ == '__main__':
    t1 = node("root")
    t1.construct_suffix_trie("panamabananas")
    t1.print_trie()


