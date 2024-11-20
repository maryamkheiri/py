class Binary_Tree:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        self.left_height=-1
        self.right_height=-1
    def add_child(self,data):
      if self.data is None:
          self.data=data
      if data<self.data:
          if self.left:
              self.left.add_child(data)
          else:
              self.left=Binary_Tree(data)
      else:
          if self.right:
              self.right.add_child(data)
          else:
              self.right=Binary_Tree(data)

            
    def height(self):
        if self.data is None:
            return 0
        else:
            if hasattr(self.left, 'height'):
                self.left_height = self.left.height()
            if hasattr(self.right, 'height'):
                self.right_height = self.right.height()
            return 1 + max(self.left_height, self.right_height)
    def get_lvl(self,data):
        if data==self.data:
            return 0
        level=None
        if data<self.data:
            if self.left:
                level=self.left.get_lvl(data)
        else:
            if self.right:
                level=self.right.get_lvl(data)
        if level is not None:
            return level+1
                       
    def print_Tree(self,data):

            spaces="   "
            prefix="|--" if self.get_lvl(data)==0 else spaces+"|---"
            print(prefix,self.data)
            if self.left:
                self.left.print_Tree(data)
            if self.right:
                self.right.print_Tree(data)
       
        
def build_tree(elements):   
    root=Binary_Tree(elements[0])
    for i in range(1,len(elements)):
        print(elements[i])
        root.add_child(elements[i])
    return root
    
def isstrickt(root):
    if root is None:
        return True
    if root.left == None and root.right == None:
        return True
    
    if root.left and root.right:
        return isstrickt(root.left) and isstrickt(root.right)
    return False
            
def binary_sum(root):
    if root is None:
        return 0
    else:
        left=binary_sum(root.left)
        right=binary_sum(root.right)
        return root.data+left+right
                
def get_max(root):
    if root is None:
        return 0
    else:
        left=get_max(root.left)
        right=get_max(root.right)
        return max(root.data,left,right)
def reverseTree(root):
    if root is None:
        return 
    else:
        reverseTree(root.left)
        reverseTree(root.right)
        root.left,root.right=root.right,root.left
        
def searchTree(root,val):
    if root is None:
        return False
    else:
        inleft=searchTree(root.left,val)
        inright=searchTree(root.right,val)
        return root.data == val or inleft or inright
def TreeHight(root):
    if root is None:
        return -1
    else:
        lefthight=TreeHight(root.left)
        righthight=TreeHight(root.right)
        return 1+max(lefthight,righthight)
def No_nodes(root):
    if root is None:
        return 0
    return (No_nodes(root.left)+No_nodes(root.right)+1)
def iscomplete(root,index,No_nodes):
    if root is None:
        return True
    if index>=No_nodes:
        return False
    return iscomplete(root.left,2*index+1,No_nodes) and iscomplete(root.right,2*index+2,No_nodes)

#elements=["Countries","Arabs","UK","Den","Amarat"]
#elements=[9,3,10,2,4]
elements=[6,4,8,3,5]
root=build_tree(elements)
root.print_Tree((elements[0]))
no_nods=No_nodes(root)
index=0
print(iscomplete(root,index,no_nods))
if iscomplete(root,index,no_nods):
    print("is com")
else:
    print("is not")
print(root.data)
print(root.left.data)
print(root.left.left.data)
print(root.left.right.data)
print(root.right.data)
