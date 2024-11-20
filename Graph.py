class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.adj_dict=self.create_dict()
        self.adj_list=self.create_list()
    def create_dict(self):
        adj_dict={}
        for edge in self.edges:
            pointA,pointB=edge
            if pointA not in adj_dict:
                adj_dict[pointA]=[]
            if pointB not in adj_dict:
                adj_dict[pointB]=[]
            adj_dict[pointA].append(pointB)
        return adj_dict
    def create_list(self):
        adj_list=dict()
        for edge in self.edges:
            pointA,pointB=edge
            if pointA not in adj_list:
                adj_list[pointA]=[]
            if pointB not in adj_list:
                adj_list[pointB]=[]
            adj_list[pointA].append(pointB)
            adj_list[pointB].append(pointA)
        return adj_list


        
    def dfs_Itr(self,start):
        stack=[start]
        while stack:
            cur=stack.pop()
            print(cur,end=" ")
            for val in self.adj_dict[cur]:
                stack.append(val)
    
    def dfs_recursion(self,start):
        print(start,end=" ")
        if len(self.adj_dict[start])==0:
            return
        for val in self.adj_dict[start]:
            self.dfs_recursion(val)
        
    def bfs_Itr(self,start):#directed
        queue=[start]
        while queue:
            cur=queue.pop(0)
            print(cur,end=" ")
            for val in self.adj_dict[cur]:
                queue.append(val)

    def bfs_Itr1(self,start):#indirected
        visited=[start]
        queue=[start]
        while queue:
            cur=queue.pop(0)
            if cur not in visited:
                visited.append(cur)
            print(cur,end=" ")
            for val in self.adj_list[cur]:
                if val not in visited:
                    queue.append(val)
                
    def has_pass_dfs(self,srs,des,visited=[]):
        visited=visited+[srs]
        if srs == des:
            return True
        if srs not in self.adj_list:
            return False
        for val in self.adj_list[srs]:
            if val not in visited:
                if (self.has_pass_dfs(val,des,visited)==True):
                    return True
        return False
                
routes=[(10,30),(10,40),(10,50),(10,70),(30,100),(50,60),(70,80),(80,90),(20,25)]
my_graph=Graph(routes)
print(my_graph.adj_dict)
print(my_graph.dfs_Itr(10))
print(my_graph.dfs_recursion(10))
print(my_graph.bfs_Itr(10))
print(my_graph.adj_list)
print(my_graph.bfs_Itr1(10))
print(my_graph.has_pass_dfs(10,100))