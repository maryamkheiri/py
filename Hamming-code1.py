import numpy as np
alphabet=list(map(lambda i:i,
        "abcdefghijklmnopqrstuxwyzABCDEFGHIJKLMNOPQRSTUXWYZ1234567890!@#$%^&*()_+= {}[]|\?><.,:;''"))
print(alphabet)
_str="Hello World!"
binary_rep=[]
for i in _str:
    binary_rep.append(bin(alphabet.index(i)))
print(binary_rep)
def block_creator(binary_code):
    binary_code=binary_code[2:]
    length=len(binary_code)
    for i in range(length,11):
        binary_code="0"+binary_code
    places=[[0,3],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
    block=np.zeros((4,4),np.int8)
    for index,val in enumerate(binary_code):
        row,col=places[index]
        block[row][col]=val
    if (np.count_nonzero(block[:,1])+np.count_nonzero(block[:,3]))%2:
        block[0][1]=1
    if (np.count_nonzero(block[:,2])+np.count_nonzero(block[:,3]))%2:
        block[0][2]=1
    if (np.count_nonzero(block[1])+np.count_nonzero(block[3]))%2:
        block[1][0]=1
    if (np.count_nonzero(block[2])+np.count_nonzero(block[3]))%2:
        block[2][0]=1
    print(block)    
    return block
output=""
for i in range(len(binary_rep)):
    binary_rep[i]=list(block_creator(binary_rep[i]).flatten(order="F"))
    #binary_rep=binary_rep.tolist()
    output+="".join([str(i) for i in binary_rep[i]])
with open("data.txt","w") as fi:
    fi.write(output)
print(output)
