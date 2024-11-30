class Node:
    def __init__(self,data,level,fscore,parent):
        self.data=data
        if parent==None:
            self.level=level
        else:
            self.level=level+1
        self.fscore=fscore
        self.parent=parent
    
    def find_index(self,num):
        index=self.data.index(num)
        i=index//3
        j=index-(i*3)
        return i,j    
    
    def possible_moves(self):
        i,j=self.find_index("0")
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        direction_names=["up","down","left","right"]
        all_directions={directions[i]:direction_names[i] for i in range(4)}
        possible_moves=[]
        for k in directions:
            if not ((i+k[0]<0) or (i+k[0]>2) or (j+k[1]<0) or (j+k[1]>2)):
                possible_moves.append(all_directions[k])
        return possible_moves
    
    def generate_chilren(self):
        i,j=self.find_index("0")
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        direction_names=["up","down","left","right"]
        all_directions={direction_names[i]:directions[i] for i in range(4)}
        possible_directions=self.possible_moves()
        move_to=[]
        for k in possible_directions:
            move_to.append((all_directions[k][0]+i,all_directions[k][1]+j))
        children=[]
        for p in move_to:
            puzzle=list(self.data)
            zero_index=j+(i*3)
            des_index=p[1]+p[0]*3
            puzzle[zero_index],puzzle[des_index]=puzzle[des_index],puzzle[zero_index]
            children.append("".join(puzzle))
        chilren_obj=[]
        for i in children:
            chilren_obj.append(Node(i,self.level+1,0,self))
        return chilren_obj

class Puzzle:
    def __init__(self,curren):
        self.puzzle=curren
        self.open=[]
        self.colsed=[]
        self.visited={}
    
    def find_index(self,cur,num):
        index=cur.find(num)
        i=index//3
        j=index-(i*3)
        return i,j
    def f_score(self,curr,goal):
            return self.h_score(curr.data,goal)+curr.level
    def h_score(self,current,goal):
        total=0
        for i in range(len(current)):
            i,j=self.find_index(current,str(i))
            x,y=self.find_index(goal,str(i))
            total+=abs(i-x)+abs(j-y)
        for i in range(len(current)):
            if int(current[i]!=i+1 ):
                if int(current[i]==0 and i==8):
                    pass
                else:
                    total+=1
        return total
    
    def prosess(self):
        start=Node(self.puzzle,0,0,Node)
        goal="123456780"
        self.open.append(start)
        while True:
            cur=self.open[0]
            if cur.data==goal:
                _list=[]
                _list.append(cur)
                while cur.parent == None:
                    _list.append(cur.parent)
                    cur=cur.parent
                    
                else:
                    _list.append(cur.parent)
                _list=_list[::-1]
                t=0
                for i in _list:
                    if i!=None:
                        for j in range(0,9,3):
                            print(i.data[j] , "  " , i.data[j+1] , "  ", i.data[j+2])
                            print("********")
                    t+=1
                print("total step is :" , t)
                break
            
            
            for i in cur. generate_chilren():
                i.f_score=self.f_score(i,goal)
                if i.data not in self.visited or self.visited[i.data]>i.f_score:
                    self.open.append(i)
                    self.visited[i.data]=i.f_score
            self.colsed.append(cur)
            self.visited[cur.data]=self.h_score(cur.data,goal)
            with open("log.txt" , "w") as f:
                f.write(str(self.visited)+"\n")
            del self.open[0]
            self.open.sort(key=lambda x:x.f_score , reverse=False)
                    
        
puz=Puzzle("123450678")
puz.prosess()