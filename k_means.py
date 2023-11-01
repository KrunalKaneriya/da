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

# The code you provided is a Python script that generates a list of random numbers, then repeatedly selects random values from the list to create sublists, and finally calculates the average of each sublist. Here's a breakdown of the code:

# 1. The user is prompted to enter the number of elements in the list.

# 2. A list named `main_list` is created, and the user is prompted to enter `number` elements, which are appended to this list.

# 3. The original `main_list` is printed to show its content.

# 4. The user is prompted to enter a value `k`.

# 5. The code initializes an empty list `tamp` to store sublists.

# 6. A loop runs `k` times to create `k` sublists. In each iteration, it selects elements from the `tmp_list` (which is initially a copy of `main_list`) at even indexes (0, 2, 4, etc.) and appends them to a sublist called `num`. The selected elements are removed from `tmp_list`.

# 7. The `num` sublist is appended to the `tamp` list, creating a list of sublists.

# 8. The code then calculates the average (mean) of each sublist in `tamp`. It iterates through each sublist, calculates the sum of its elements, divides the sum by the number of elements in the sublist, and appends the result to the `mean` list.

# 9. Finally, the code prints the `mean` list, which contains the average values for each sublist.

# The code does not implement a specific algorithm; rather, it's a script for generating random sublists, calculating their averages, and storing the results in a new list.

