class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
        #self.level=1
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
        #child.level=child.parent.level+1
    def get_lvl(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        spaces="  "*self.get_lvl()
        #spaces="  "*self.level
        prefix=spaces+"|--" if self.parent else "|--"
        print(prefix,self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree()
    def isempty(self):
        return len(self.children)==0
        
    def search_tree(self,key):
        key=str(key)
        key=''.join(key.split())
        if self.data==key:
            return True
        if not self.isempty():
            for child in self.children:
                val=child.search_tree(key)
                if val==True:
                    return True
            return False
    def isbinary(self):
        if len(self.children)==0:
            return True
        if len(self.children)>2:
            return False
        for child in self.children:
            if child.isbinary():
                return True
        return False

    def hight(self):
        if len(self.children)==0:
            return 0
        max_hight=-1
        for child in self.children:
            max_hight= max(max_hight,child.hight())
        return 1+max_hight

def create_product_tree():
    root=TreeNode("Electronic")
    
    laptop=TreeNode("laptop ")
    root.add_child(laptop)
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Asus"))
    root.children[0].children[0].add_child(TreeNode("Latest Version"))
    root.children[0].children[0].add_child(TreeNode("OLd Version"))
    #root.children[0].children[0].add_child(TreeNode("Out Version"))
    #laptop.add_child(TreeNode("Hp"))
    phone=TreeNode("phones")
    root.add_child(phone)
    phone.add_child(TreeNode("Iphone"))
    phone.add_child(TreeNode("LG"))
    #phone.add_child(TreeNode("Sony"))
    #phone.add_child(TreeNode("Samsung"))
    #tv=TreeNode("televisions")
    #root.add_child(tv)
    #tv.add_child(TreeNode("LG"))
    #tv.add_child(TreeNode("Sony"))
    return root

if __name__=="__main__":
    root=create_product_tree()
    root.print_tree()
    
    print(root.search_tree("LG"))
    print(root.isempty())
    print(root.isbinary())
    print(root.hight())
    