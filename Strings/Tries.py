class node:
    def __init__(self,val):
        self.val=val
        self.next=False
        self.children=[]

    def add_nodes(self,string,ind=0):
        if ind==len(string):
            return
        found=False
        for child in self.children:
            if child.val==string[ind]:
                child.add_nodes(string,ind+1)
                found=True
        if not found:
            self.children.append(node(string[ind]))
            self.next = node(string[ind])
            self.children[len(self.children)-1].add_nodes(string,ind+1)


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
    def print(self,space=0):
        if self.children:
            ind = 0
            for child in self.children:
                s = "->"
                print(space * s + child.val)
                print(child.next)
                child.print(space + 1)

    def prefix_triematching(self,text,i=0,arr=[]):
        if i==len(text):
            return arr
        if self.next==False:
            if self.next==text[0]:
                arr.append(self.val)
            return arr
        y=None
        for child in self.children:
            if child.val==text[0]:
                arr.append(child.val)
                y=child.prefix_triematching(text[i+1:],i,arr)
        if y:
            return arr
        # return arr

    def trie_matching(self,text):
        i=0
        true_self=self
        res=list(list())
        arr=list(list())
        while i < len(text):
            y=self.prefix_triematching(text[i:],0,[])
            if y:
                arr.append(list(y))
            i+=1
        return arr


if __name__ == '__main__':
    t1=node("root")
    t1.add_nodes("banana")
    t1.add_nodes("pan")
    t1.add_nodes("and")
    t1.add_nodes("nab")
    t1.add_nodes("bandana")
    t1.add_nodes("ananas")
    t1.add_nodes("antennas")

    t1.add_nodes("nana")
    # t1.add_nodes("anu")


    t1.print_trie()
    print(t1.trie_matching("panamabananas"))


