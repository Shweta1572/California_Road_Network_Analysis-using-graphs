dist=[]
dist_1=[]
sum=0
avg=0
with open('result.txt','r') as f:
    for line in f:
        dist.append(int(line.split()[1]))

for i in range(0,len(dist)):
    if dist[i]!=200000 and dist[i]!=200001:
        dist_1.append(dist[i])

for ele in dist_1:
    sum=sum+ele
avg=(sum/(len(dist_1)+1))
print('The average is:',avg)

  
