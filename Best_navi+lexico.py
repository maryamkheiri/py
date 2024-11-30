import numpy as np
from random import randint as rnd
from random import shuffle
import matplotlib.pyplot  as plt
from copy import copy
import cv2
NCITIES=4
WIGHT=500
HIGHT=500
OFFSET=20
def radomizer(n,w,h,offset):
    city_collections=[]

    for i in range(n):
        x= rnd(offset,w-offset)
        y= rnd(offset,h-offset)
        city_collections.append([x,y])
    return city_collections
def draw_cities(img,locations):
    for x,y in locations:
        img=cv2.circle(img,(x,y),6,(0,0,255),-1)
    return img


def all_lexicopath(n):
    loc=[i for i in range(n)]
    all_path=[]
    length=len(loc)
    cpy=loc.copy()
    all_path.append(cpy)
    while True:
        larges_i=-1
        
        for i in range(length-1):
            if loc[i]<loc[i+1]:
                larges_i=i
        if larges_i==-1:
            break

        laegest_j=0
        for j in range(length):
            if loc[larges_i]<loc[j]:
                laegest_j=j

        loc[larges_i],loc[laegest_j]=loc[laegest_j],loc[larges_i]
        loc_left=loc[:larges_i+1]
        loc_right=loc[larges_i+1:]
        loc_right.reverse()
        loc=loc_left+loc_right
        cpy=loc.copy()
        all_path.append(cpy)
    return all_path


def convertor_path(locations,path):
    coverted_loc=[]
    for i in path:
        coverted_loc.append(locations[i])
    return coverted_loc


def draw_path(img,path,color):
    length=len(path)
    for i in range(length-1):
        img=cv2.line(img,path[i],path[i+1],color,3)
    return img
def euclidian_distace(path):
    length=len(path)
    distace=0
    for i in range(length-1):
        distace+=np.sqrt((path[i][0]-path[i+1][0])**2 +(path[i][1]-path[i+1][1])**2)
        return distace
#Main
area=np.full(( WIGHT,HIGHT,3),255,np.int16)
locations=radomizer(NCITIES,WIGHT,HIGHT,OFFSET)
area=draw_cities(area,locations)
all_path=all_lexicopath(NCITIES)

for path in all_path:
    best_path=[]
    best_ditace=None
    area=np.full(( WIGHT,HIGHT,3),255,np.int16)
    path_core=convertor_path(locations,path)
    area=draw_path(area,path_core,(0,255,0))
    distances=euclidian_distace(path_core)
    if best_ditace is not None:
        if distances < best_ditace:
            best_ditace = distances
            best_path=path_core.copy()       
    else:
        best_ditace=distances
        best_path=path_core.copy() 
        
    area=draw_path(area, best_path,(0,255,0))
    plt.imshow(area)
    plt.title(f"the distace so far is: {best_ditace}")
    plt.grid()
    plt.show()
