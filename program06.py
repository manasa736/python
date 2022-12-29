

m=[[1,2],[3,4],[5,6],[7,8]]
##ans=[]
##for row in range(len(m[0])):#row=0,1
##    temp=[]
##    for col in range(len(m)):#col=0,1,2,3
##        temp.append(m[col][row])
##    ans.append(temp)
##print(ans)


ans=[[m[col][row]for col in range(len(m))]for row in range(len(m[0]))] 
print(ans)
