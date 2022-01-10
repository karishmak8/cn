import socket            
port = 34439              
s = socket.socket()        
s.connect(('127.0.0.1', port))
data=input("enter the data to send ")
i=0
while(i!=len(data)):
        print("sending char",data[i])
        s.send(data[i].encode())
        y=s.recv(1024).decode()
        print(y)
        if(y=='sending acknowledgement '+data[i]):
            print("char",data[i],"sent")
            i+=1
        else:
            print("resending char",data[i])
s.close()    
