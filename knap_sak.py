from random import randint as rnd
import copy
# Constances
N=7
M_MAX=15
objects=[(10,2),(5,3),(15,5),(7,7),(6,1),(18,4),(3,1)]
#objects=None
EPOCH=200
# Class Item
class Items:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight
        self.profit_by_weight=profit/weight
        self.portion=0.0
# Geter Input Function
def geter_item(n,input_items=0,verbos=0):
    items=[]
    if not input_items:
        for i in range(n):
            profit=int(input("What's profit ?"))
            weight=int(input("What's Weight ?"))
            items.append(Items(profit,weight))
    else:
        for item in input_items:
            items.append(Items(item[0],item[1]))
    if verbos:
        for item in items:
            print(f"Item:{items.index(item)+1} profit: {item.profit} weight: {item.weight} profit_by_weight:{item.profit_by_weight} ")
                  
    return items
# Picking item
def pick_item(items):
    best_item=None
    items=sorted(items,key=lambda x:x.profit_by_weight, reverse=True)
    for item in items:
        if best_item:
            if best_item.profit_by_weight<item.profit_by_weight and item.portion<1:
                 best_item=item
        else:
            if item.portion<1:
                best_item=item
    return best_item
# Main
items=geter_item(N,input_items=objects,verbos=1)
print("@@@@@@@@@")

bag=[]
offset=M_MAX
while offset>0:
    best_items=pick_item(items)
    if best_items:
        if best_items.weight<=offset :
            best_items.portion=1
            bag.append(best_items)
            offset-=best_items.weight
        else:
            best_items.portion=((offset*100)/best_items.weight)/100
            bag.append(best_items)
            offset=0
    else:
        break
total_profit=0
total_weight=0
total_weight1=""
profit=""
portion=""
for i in bag:
    total_profit+=(i.portion)*(i.profit)
    total_weight+=i.weight*i.portion
    total_weight1+=f"{i.weight*i.portion} + "
    profit+=f"{i.profit} + "
    portion+=f"{i.portion} + "
print("total_profit:",total_profit)
print(f"total weight:{total_weight}")
print(f"total weight {total_weight1[:-2]}")
print(f"profit: {profit[:-2]}")
print(f"portion:{portion[:-2]}")
    
        


         



                