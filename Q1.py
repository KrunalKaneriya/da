import random

main_list=[34,25,76,54,88,99,11,46,67,73,22,44]
tmp_list=main_list
tamp=[]
k=4
for i in range(k):
    num=[]
    for x in range(0,len(tmp_list),2):
        random_val=random.choice(tmp_list)
        tmp_list.remove(random_val)
        num.append(random_val)

    tamp.append(num)
print(tamp)
sum=0
mean=[]
for z in tamp:
    for r in z:
        sum=sum+r
    avg=int(sum/len(z))
    mean.append(avg)
    sum=0
print(mean)
for v in tamp:
    for p in range(len(v)):
        r1=v[p]-mean[0]
        r2=v[p]-mean[1]
        r3 = v[p] - mean[2]
        r4 = v[p] - mean[3]
        if(r1<r2 and r1<r3 and r1<r4):
            
