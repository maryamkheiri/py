from random import randint as rnd
from random import shuffle
# Import Paramiters
N=7
PS=4
M_R=0.8
M_MAX=15
EPOCH=200
objects=[(10,2),(5,3),(15,5),(7,7),(6,1),(18,4),(3,1)]
#objects=None
# Class Item
class Items:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight

# Init Function
def init_population(n,ps):
    population_list=[]
    for i in range(ps):
        member=[1 for i in range(n)]+[0 for i in range(n)]
        shuffle(member)
        member=member[:n]+[None,None]
        population_list.append(member)
    return population_list

# Cross Over Function
def cross_over(population_list,n,ps):
    n_2=n//2
    for i in range(0,ps,2):
        child1=population_list[i][:n_2]+population_list[i+1][n_2:n]+[None,None]
        child2=population_list[i+1][:n_2]+population_list[i][n_2:n]+[None,None]
        population_list.append(child1)
        population_list.append(child2)
    return population_list
# Mutation Function
def mutation(population_list,n,ps,m_r):
    chosen_ones=[i for i in range(ps,ps*2)]
    shuffle(chosen_ones)
    chosen_ones=chosen_ones[:int(ps*m_r)]
    for i in chosen_ones:
        cell=rnd(0,n-1)
        population_list[i][cell]=1 if population_list[i][cell]==0 else 0
    return population_list
# Fitness Function
def distance_weight(bag,items,m_max,n):
    length=len(bag)-2
    total_weight=0
    for i in range(length):
        if bag[i]:
            total_weight+=items[i].weight
    return abs(total_weight - m_max)

def profit(bag,items):
    length=len(bag)-2
    total_profit=0
    for i in range(length):
         if bag[i]:
                total_profit+=items[i].profit
    return total_profit
def fitness(population_list,n,ps,m_max,items):
    for i in range(ps*2):
         if population_list[i][n]==None or population_list[i][n+1]==None:
            population_list[i][n]=distance_weight(population_list[i],items,m_max,n)
            population_list[i][n+1]=profit(population_list[i],items)
    return population_list
# Sorted Function
def sort(population_list,index1,index2):
    sorted_list=sorted(population_list,key=lambda x:(x[index1],-x[index2]))
    return sorted_list
# Geter Fuunction
def geter_func(n,input_items=0,verbos=0):
    items=[]
    if input_items:
        for item in input_items:
            items.append(Items(item[0],item[1]))          
    else:
          for i in range(n):     
                profit=int(input("What's profit ?"))
                weight=int(input("What's Weight ?"))
                items.append(Items(profit,weight))
    if verbos:
        for item in items:
            print(f"Item:{items.index(item)+1} profit:{item.profit} weight:{item.weight}")
    return items
# Main
if __name__=="__main__":
    items=geter_func(N,input_items=objects,verbos=1)
    curren_population=init_population(N,PS)
    for i in curren_population:
        print(i)
    print("@@@@@@@@@@")
    curren_population=cross_over(curren_population,N,PS)
    for i in curren_population:
        print(i)
    print("@@@@@@@@@")
    curren_population=mutation(curren_population,N,PS,M_R)
    for i in curren_population:
        print(i)
    curren_population=fitness(curren_population,N,PS,M_MAX,items)
    for i in curren_population:
        print(i)
    print("@@@@@@@@@@")
    curren_population=sort(curren_population,N,N+1)
    for i in curren_population:
        print(i)
