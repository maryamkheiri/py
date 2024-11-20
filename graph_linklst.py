class Node:
    def __init__(self,val):
        self.data=val
        self.neighbors=[]
    def add_neighbors(self,vertex):
        if isinstance(vertex,Node) and vertex not in self.neighbors:
            self.neighbors.append(vertex.data)
class Graph:
    adj_dic={}
    vertecis={}
    def add_vertecis(self,vertex):
        if  isinstance(vertex,Node) and vertex.data not in self.vertecis:
            self.vertecis[vertex.data]=vertex
            return True
        else:
            return False
    def add_edge(self,start,dist):
        if start in self.vertecis and dist in self.vertecis:
            for key,val in self.vertecis.items():
                if key==start:
                        val.add_neighbors(Node(dist))
            return True
        else:
            return False
    def print_graph(self):
        for key in sorted(list(self.vertecis.keys())):
            print(f"{key}:{self.vertecis[key].neighbors}")
        
    def creat_adj_dic(self):
        for key in sorted(list(self.vertecis.keys())):
            if self.vertecis[key].neighbors:
                self.adj_dic[key]=self.vertecis[key].neighbors
    def get_path(self,start,dist,path=[]):
        path=path+[start]
        if start==dist:
            return [path]
        if start not in self.adj_dic:
            return []
        paths=[]
        for vertex in self.adj_dic[start]:
            if vertex not in path:
                new_paths=self.get_path(vertex,dist,path)
                for p in new_paths:
                    paths.append(p)
        return paths
        
    def shortest_path(self,start,dist,path=[]):
        path=path+[start]
        if start==dist:
            return path
        if start not in self.adj_dic:
            return None
        new_path=None
        for vertex in self.adj_dic[start]:
            if vertex not in path:
                np_path=self.shortest_path(vertex,dist,path)
                if np_path:
                    if new_path is None or len(np_path)<len(new_path):
                        new_path=np_path
        return new_path

nodes=["kerman","yazd","esfahan","mashhad","Tehran"]
routs=[("kerman","yazd"),
       ("kerman","esfahan"),
       ("esfahan","mashhad"),
       ("yazd","mashhad"),
       ("yazd","esfahan"),
       ("mashhad","Tehran")]
graph=Graph()
for node in nodes:
    graph.add_vertecis(Node(node))
print(graph.vertecis)
for rout in routs:
    graph.add_edge(rout[0],rout[1])

graph.print_graph()
graph.creat_adj_dic()
graph.adj_dic
print(graph.get_path("kerman","Tehran"))
print(graph.shortest_path("kerman","Tehran"))