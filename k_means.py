from builtins import map
from itertools import takewhile
import random

number=int(input("entyer your element"))
main_list=[]
for i in range(number):
    input_num=int(input("entyer your element"))
    main_list.append(input_num)
print(main_list)
tmp_list=main_list
tamp=[]
k=int(input("entyer your element"))
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



