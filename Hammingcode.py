div=list(map(int,input().split())) 
data=list(map(int,input().split()))
n=len(div)
data1=data+[0]*(n-1)
def xor(top,down,n):
    ret=[]
    for i in range(n):
        if(top[i]==down[i]):
            ret.insert(i,0)
        else:
            ret.insert(i,1)
    return ret[1:]        
def division(data1):
    r=data1[0:n]
    while(len(data1)>=n):
        if(r[0]==1):
            r=xor(r,div,n)
            if(len(data1)>n):
                r=r+[data1[n]]
                data1.pop(n)
            else:
                break
            
           
        if(r[0]==0):
            r=xor(r,[0]*n,n) 
            if(len(data1)>n):
                r=r+[data1[n]]
                data1.pop(n)
            else:
                break
    return r 
result=division(data1)
sender_data=data+result 
print("Data from sender: ",sender_data)
result=division(sender_data) 
print("resultant from reciever: ",result)
if(1 not in result):
    print("no error") 
else:
    print("error")
