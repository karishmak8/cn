import socket            
s = socket.socket()        
print ("Socket successfully created")
port = 34439            
s.bind(('', port))        
print ("socket binded to %s" %(port))
s.listen(5)    
print ("socket is listening")           
c, addr = s.accept()  
print ('Got connection from', addr )
y=''
while True:
    x=c.recv(1024).decode()
    print("received char",x)
    y='sending acknowledgement '+x
    print(y)
    c.send(y.encode())
    if y=='sending acknowledgement ;':
        print('yes')
        break
c.close()
