class Graph:#adjacacy matrix
    def __init__(self,nodes,edges):
        self.nodes=nodes
        self.edges=edges
        self.adj_dict=self.create_adj_dict()
        self.adj_matrix=self.create_adj_matrix()

    def create_adj_dict(self):
        adj_dict={}
        for start,dist,_ in self.edges:
            if start not in adj_dict:
                adj_dict[start]=[dist]
            else:
                adj_dict[start].append(dist)
        return adj_dict

    def create_adj_matrix(self):
        adj_matrix=[[0 for _ in self.nodes]for _ in self.nodes]
        for rout in self.edges:
            start=self.nodes.index(rout[0])
            dist=self.nodes.index(rout[1])
            adj_matrix[start][dist]=rout[2]          
        return adj_matrix

    def get_path(self,start,dist,paths=[]):
        paths=paths+[start]
        if start==dist:
            return[paths]
        if start not in self.adj_dict:
            return []
        new_paths=[]
        for vertex in self.adj_dict[start]:
            if vertex not in paths:
                np_paths=self.get_path(vertex,dist,paths)
                for p in np_paths:
                    new_paths.append(p)
        return new_paths

    def get_path_cost(self,start,dist):
        paths=self.get_path(start,dist)
        paths=self.get_distance(paths)
        return paths
        
    def get_distance(self,paths):
        distance=0
        for i in range(len(paths)):
            for j in range (len(paths[i])-1):
                s_i=self.nodes.index(paths[i][j])
                s_j=self.nodes.index(paths[i][j+1])
                distance+=self.adj_matrix[s_i][s_j]
            paths[i].append(distance)
            distance=0
        return paths

nodes=["kerman","yazd","esfahan","mashhad","Tehran"]
routs=[("kerman","yazd",8),
       ("kerman","esfahan",7),
       ("esfahan","mashhad",20),
       ("yazd","mashhad",22),
       ("yazd","esfahan",5),
       ("mashhad","Tehran",26)]
my_gepgh=Graph(nodes,routs)

print(my_gepgh.adj_matrix)
print(my_gepgh.adj_dict)
print(my_gepgh.get_path("kerman","Tehran"))
print(my_gepgh.get_path_cost("kerman","Tehran"))