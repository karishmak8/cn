import string
INF=999
str1=string.ascii_uppercase
adj=[]
v=int(input("enter no.of vertices "))
adj=[[0 for i in range(v)]for i in range(v)]
e=int(input("enter no.of edges "))
for k in range(e):
  v1,v2=int(input("enter the vertex1 ")),int(input("enter the vertex1 "))
  adj[v1][v2]=int(input("enter the weight of the edge "))
  adj[v2][v1]=adj[v1][v2]
print("adj =",adj)
for i in range(v):
    u=list(str1[0:v])
    s=int(input("enter source vertex "))
    d=[]
    visited=[]
    for i in range(v):
        if(i==s):
            visited.append(True)
            d.append(0)
        else:
            d.append(INF)
            visited.append(False)
    k=s
    for i in range(v):
        for j in range(v):
            if(adj[k][j]!=0 and visited[j]==False):
                if(d[j]>d[k]+adj[k][j]):
                    d[j]=d[k]+adj[k][j]
                    u[j]=str1[k]
        visited[k]=True
        min=999999
        for m in range(v):
            if(visited[m]==False and d[m]<min):
                min=d[m]
                k=m
    print("for the vertex ",str1[s])
    for i in range(v):
        print(str1[i],end=" ")
        print(d[i],end=" ")
        print(u[i])
