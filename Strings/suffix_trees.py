class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=self
        self.id=0
        self.children=[]

    def build_suffix_trees(self,string,i):
        found=False
        for child in self.children:
            if child.val[0]==string[0]:
                found=True


