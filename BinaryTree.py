class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        self.level=None
class Tree:
    def create_node(self,data):
            return Node(data)
    def insert(self,root,val):
        if root is None:
            return self.create_node(val)
        if val<root.data:
            root.left=self.insert(root.left,val)
        else:
            root.right=self.insert(root.right,val)
        return root
    def in_ordertravers(self,root):
        if root is not None:
            self.in_ordertravers(root.left)
            print(root.data , end=" ")
            self.in_ordertravers(root.right)
    def pre_ordertraversa(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.pre_ordertraversa(root.left)
            self.pre_ordertraversa(root.right)
    def post_ordertraversa(self,root):
        if root is not None:
            self.post_ordertraversa(root.left)
            self.post_ordertraversa(root.right)
            print(root.data,end=" ")

    def level_ordertraversa(self,root):
        q=[]
        q.append(root)
        while len(q)!=0:
            root=q.pop(0)
            print(root.data,end=" ")
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)

    def vertical_traversa(self,root):
        q=[]
        d=dict()
        q.append(root)
        root.level=0
        while len(q)!=0:
            root=q.pop(0)
            if root.level not in d:
                d[root.level]=[root.data]
            else:
                d[root.level]+=[root.data]
            if root.left:
                q.append(root.left)
                root.left.level=root.level-1
            if root.right:
                q.append(root.right)
                root.right.level=root.level+1
        
    
        sorted_by_keys = sorted(d.items(), key=lambda item: item[0])
        for i in  sorted_by_keys:
            print(sorted(i[1]),end=" ")

    def top_view(self,root):
        if root is not None:
            q=[]
            q.append(root)
            d=dict()
            root.level=0
            while len(q)!=0:
                node=q.pop(0)
                print(node.data , end="")
                if node.level not in d:
                    d[node.level]=node.data
                if node.left is not None:
                    q.append(node.left)
                    node.left.level=node.level-1
                if node.right is not None:
                    q.append(node.right)
                    node.right.level=node.level+1
            print(d)
            for i in sorted(d):
                print(d[i], end=" ")

        
    def hight(self,root):
        if root is None:
            return -1
        return max(self.hight(root.left),self.hight(root.right))+1

    def check_bst(self,root): #by inorder_traversa
        
        def in_order(root,values):
            if root is not None:
                in_order(root.left,values)
                values.append(root.data)
                in_order(root.right,values)
        values=[]
        in_order(root,values)
        for i in range(len(values)-1):
            if values[i]>=values[i+1]:
                return False
        print(values)
        return True

    def check1_bst(self,root,left_max=None,right_max=None): #by recursion
        left_max=-999999
        right_max=999999
        if root is None:
             return True
        if root.data<=left_max or root.data>=right_max:
            return False
        return self.check1_bst(root.left,root.data,right_max) and self.check1_bst(root.right,left_max,root.data)

    def iscomplete(self,root):
        if not root : return True
        q=[root]
        flag=False
        while q:
            node=q.pop(0)
            if node is None:
                flag=True
                continue
            if flag:
                return False
            q.append(node.left)
            q.append(node.right)
        return True


    def is_balanced(self,root):
        balances=[True]
        def hight(root):
            if root is None:
                return 0
            left=hight(root.left)
            right=hight(root.right)
            if abs(left-right)>1:
                balances[0]=False
                return 0
            return 1+max(left,right)
        hight(root)
        return balances[0]
        

     
         
        
tree=Tree()
root=tree.create_node(6)
tree.insert(root,4)
tree.insert(root,8)
#tree.insert(root,9)
tree.insert(root,5)
#tree.insert(root,7)
tree.insert(root,3)
#tree.insert(root,2)
#tree.insert(root,10)
#tree.insert(root,11)
#tree.insert(root,1)
#print(root.left.left.left.data)
tree.in_ordertravers(root)
print("\n***")
tree.pre_ordertraversa(root)
print("\n***")
tree.post_ordertraversa(root)
print("\n***")
tree.level_ordertraversa(root)
print("\n***","vertical_traversa-----")
tree.vertical_traversa(root)
print("\n***","top_view-----")
tree.top_view(root)
print("\n***")
print(tree.hight(root))
print("******")
print(tree.check_bst(root))
print("******")
print(tree.check1_bst(root))
print("******")
print(tree.iscomplete(root))
print("******")
print(tree.is_balanced(root))
