from random import randint as rnd
from random import shuffle
import matplotlib.pyplot as plt
import numpy as np
# Constances
N_cities=4
POPULATION_SIZE=4
WIGTH=500
HIEGHT=500
# Cities_Randomizer
def randomizer(n,w,h):
    offset=20
    cities_locations=[]
    for i in range(n):
        location=[rnd(offset,w-offset),rnd(offset,h-offset)]
        if location not in cities_locations:
            cities_locations.append(location)
    return cities_locations
# Initial_Population
def initial_population(n,ps):
    population_list=[]
    for i in range(ps):
        path=[i for i in range(n)]
        shuffle(path)
        path=path+[None]
        population_list.append(path) 
    return population_list
# Cross_Over
def cross_over(population_list,ps,n):
    for i in range(ps):
        path=population_list[i][:n]+[None]
        population_list.append(path)
    return population_list
# Mutation
def mutation(population_list,ps,n):
    length=ps*2
    i= ps
    while i<length:
        cell1=rnd(0,n-1)
        cell2=rnd(0,n-1)
        if cell1!=cell2:
            population_list[i][cell1],population_list[i][cell2]=population_list[i][cell2],population_list[i][cell1]
            i+=1
    return population_list     
# Convertor
def convertor(location_list,path,n):
    path_cor=[]
    for i in path[:n]:
        path_cor.append(location_list[i])
    return path_cor      
# Fitness
def fitness(population_list,n,ps,location_list):
    length=ps*2
    distaces=0
    for i in range(length):
        if population_list[i][n]==None:
            for j in range(len(location_list)-1):
                path=convertor(location_list,population_list[i],n)
                distaces+=np.sqrt((path[j][0]-path[j+1][0])**2+(path[j][1]-path[j+1][1])**2)
                population_list[i][n]=distaces
    return population_list
        
# Sorting
def sorting(population_list,k):
    population_list.sort(key=lambda x:x[k])
    return population_list
current_locations=randomizer(N_cities,WIGTH,HIEGHT)
print(current_locations)
population_list=initial_population(N_cities,POPULATION_SIZE)
print(population_list)
population_list=cross_over(population_list,POPULATION_SIZE,N_cities)
for i in population_list:
    print(i)
print("@@@@@@@@@@@")
population_list=mutation(population_list,POPULATION_SIZE,N_cities)
for i in population_list:
    print(i)
print("########")
for i in population_list:
    m= convertor(current_locations,i,N_cities)
    print(m)
    print("********")
population_list=fitness(population_list,N_cities,POPULATION_SIZE,current_locations)
for i in population_list:
    print(i)
print("+++++++")
population_list=sorting(population_list,N_cities)
population_list=population_list[:POPULATION_SIZE]
for i in population_list:
    print(i)

