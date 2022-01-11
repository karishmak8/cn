import random 
import copy
data=list(map(int,input().split()))
n=len(data)
plist=[]

p=0
for p in range(n):
    if(2**p>=p+n+1):
        break 
    
for i in range(p):
    arr=[]
    for j in range(2*i,n+p+1,2*(i+1)):
        for k in range(j,j+2**i):
            if k>n+p:
                break
            arr.append(k)
    plist.append(arr) 

for i in range(p):
    data.insert(2**i-1,0)

p_cpy = copy.deepcopy(plist)

for i in range(p):
    for j in range(len(plist[i])):
        plist[i][j] = data[plist[i][j]-1] 
    if sum(plist[i])%2==0:
        data[2**i-1]=0        
    else:
        data[2**i-1]=1
    
print("Hamming code generated is ",data)
rand=int(input("enter the position:"))
print("Changing position",rand+1,'to 0')

data[rand]=0
pos="" 
for i in range(p):
    for j in range(len(p_cpy[i])):
        p_cpy[i][j] = data[p_cpy[i][j]-1]     
    
    if sum(p_cpy[i])%2==0:
        pos='0'+pos
    else:
        pos='1'+pos 


if '1' not in pos:
    print("No Error")
else:
    print("Binary position to be corrected is ",pos)
