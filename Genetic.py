from random import randint as rnd
from random import shuffle
import matplotlib.pyplot as plt
from random import sample
#IMPORTING DEPENDENCIES
N=4
PS=6
MR=0.8
EPOCH=200
#INITIAL POPULATION FUNCTION
def init_function(n,ps):
    population_list=[]
    for i in range(ps):
        member=[]
        for j in range(n): 
            member.append(rnd(0,n-1))
        population_list.append(member+[None])
    return population_list
# CROSSOVER FUNCTION
def cross_over(population_list,n,ps):
    for i in range(0,ps,2):
        child1=population_list[i][:n//2]+population_list[i+1][n//2:n]+[None]
        child2=population_list[i][n//2:n]+population_list[i+1][:n//2]+[None]
        population_list.append(child1)
        population_list.append(child2)
    return population_list
#MUTATION
def mutation(population_list,ps,n,mr):
    chosen_ones=list(range(ps,ps*2))
    shuffle(chosen_ones)
    chosen_ones=chosen_ones[:int(ps*mr)]

    for i in chosen_ones:
        cell=rnd(0,n-1)
        val=rnd(0,n-1)
        population_list[i][cell]=val
    
    return population_list
#FITNESS
def fitness(population_list,n):
    
    length=len(population_list)
    for i in range(length):
        confilict=0
        for j in range(n):
            for k in range (j+1,n):
                if population_list[i][j]==population_list[i][k]:
                    confilict+=1
                if abs(population_list[i][j]-population_list[i][k])==abs(k-j):
                    confilict+=1
        population_list[i][-1]=confilict
    return population_list
#SHOW _OUTCOME
def show_func(soloution,n):
    for i in range(n+1):
        plt.plot([0,n*2],[i*2,i*2])
        plt.plot([i*2,i*2],[0,n*2])
    for i in range(n):
        plt.scatter([i*2+1],soloution[i]*2+1)
    plt.show()
#MAIN
current_population=init_function(N,PS)
current_population=fitness(current_population,N)
current_population=sorted(current_population,key=lambda x:x[-1])
if current_population[0][-1]==0:
    print("best solution is found in initial population",current_population[0])
    show_func(current_population[0],N)
else:
    for i in range(EPOCH):        
        current_population=cross_over(current_population,N,PS)
        current_population=mutation(current_population,PS,N,MR)
        current_population=fitness(current_population,N)
        current_population=sorted(current_population,key=lambda x:x[-1])
        current_population=current_population[:PS]
        if current_population[0][-1]==0:
            print(i+1 ,"best solution is found",current_population[0])
            show_func(current_population[0],N)
            break
        else:
            print(i+1 ,"best solution so far",current_population[0])
    else:
        print("soory we couldnt fid a solution")



