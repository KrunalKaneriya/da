import operator
from builtins import print
from collections import Counter


import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
df = pd.read_csv('D:\\test.csv', names = ['products'], sep = ',')
f = list(df["products"].apply(lambda x:x.split(",") ))
# f=[['a','c','d'],['b','c','e'],['a','b','c','e'],['b','e'],['a','f','g'],['b','d','e']]
# f=[['MILK', 'BREAD', 'BISCUIT'], ['BREAD', 'MILK', 'BISCUIT', 'CORNFLAKES'], ['BREAD', 'TEA', 'BOURNVITA'], ['JAM', 'MAGGI', 'BREAD', 'MILK'], ['MAGGI', 'TEA', 'BISCUIT'], ['BREAD', 'TEA', 'BOURNVITA'], ['MAGGI', 'TEA', 'CORNFLAKES'], ['MAGGI', 'BREAD', 'TEA', 'BISCUIT'], ['JAM', 'MAGGI', 'BREAD', 'TEA'], ['BREAD', 'MILK'], ['COFFEE', 'COCK', 'BISCUIT', 'CORNFLAKES'], ['COFFEE', 'COCK', 'BISCUIT', 'CORNFLAKES'], ['COFFEE', 'SUGER', 'BOURNVITA'], ['BREAD', 'COFFEE', 'COCK'], ['BREAD', 'SUGER', 'BISCUIT'], ['COFFEE', 'SUGER', 'CORNFLAKES'], ['BREAD', 'SUGER', 'BOURNVITA'], ['BREAD', 'COFFEE', 'SUGER'], ['BREAD', 'COFFEE', 'SUGER'], ['TEA', 'MILK', 'COFFEE', 'CORNFLAKES']]
# f=[['l', 't', 'p', 'h'],['p', 'm', 't'], ['l', 'p', 't', 'h'],['l', 'm', 't', 'h'], ['p', 'm', 't', 'h'],['p', 't', 'h'],['m', 'h'],['l', 'p', 'm'],['l', 't', 'h'],['p', 't']]
# for i in range(n):
#     p=[]
#     f.append(p)
#     t = int(input("how many element inside list"))
#     for y in range(t):
#         r=input("enter your first element")
#         p.append(r)
#

# print(f)
p=()
d1={}
for x in f:
    p+=tuple(i for i in x)
    d1=dict(Counter(p))
apryori=[]
l2=[]
l3=[]
sorted_d = sorted(d1.items(), key=operator.itemgetter(1))
sorted_d = dict( sorted(d1.items(), key=operator.itemgetter(1),reverse=True))
# print(sorted_d)

for k,v in sorted_d.items():
    if (v>1):
        support=v/len(f)
        l2.append(k)
        a=[k,v,support]
        apryori.append(a)

for a in range(0,len(l2)):
    s1=l2[a]
    for b in range(a+1,len(l2)):
        a=[s1,l2[b]]
        l3.append(a)
count=0
second_le={}
# print(l2)
# print(l3)
con=[]
for i in l3:
    w=tuple(i)
    mf=w[0]
    for z in f:
        if(mf in z):
            if(w[1] in z):
                count=count+1
    if(count>1):
        bb=d1[w[0]]
        second_le_key=w[0]+w[1]
        second_le[second_le_key]=count
        config=count/bb
        cose=[w[0]+w[1],count,config]
        con.append(cose)
    count=0
# print(con)
main_third_le=tuple(l3[0])
l7=[]
# print(sorted_d)
# print(second_le)
for x in range(1,len(l3)):
    w=tuple(l3[x])
    if(main_third_le[0] in w[0]):
        ap=[main_third_le[0],main_third_le[1],w[1]]
        l7.append(ap)
        if(main_third_le[1] in w[0]):
            dp = [main_third_le[0], main_third_le[1], w[0]]
            l7.append(dp)

tc=0
third_le={}
for ax in l7:
    dd=tuple(ax)
    for z in f:
        if (dd[0] in z):
            if (dd[1] in z):
                if (dd[2]in z):
                    tc=tc+1
    if(tc>1):
        third_le_key=dd[0]+dd[1]+dd[2]
        third_le[third_le_key]=tc
    tc=0

print(sorted_d)
print(second_le)
print(apryori)
print(con)
print(third_le)

# The code you provided is implementing the Apriori algorithm for association rule mining from scratch, without using any specialized library for association rule mining. The Apriori algorithm is a classic algorithm used to discover frequent itemsets in a transaction dataset and then generate association rules from these itemsets. The code identifies frequent itemsets and calculates support, confidence, and lift values for association rules.

# Here's a breakdown of the key steps in the code:

# 1. Read a CSV file named 'test.csv' into a Pandas DataFrame, assuming it contains transaction data with a single column named 'products'.

# 2. Split the 'products' column into lists of items and store them in a list called `f`.

# 3. Create an empty tuple `p` and an empty dictionary `d1` to count the occurrences of individual items.

# 4. Loop through the lists in `f`, update `p` and `d1` with the count of each item.

# 5. Sort the items in `d1` by their counts in descending order, resulting in a dictionary named `sorted_d`.

# 6. Create an empty list `apryori` to store frequent itemsets, an empty list `l2` to store item names, and an empty list `l3` to store pairs of items.

# 7. Iterate through `sorted_d` and identify frequent itemsets with a count greater than 1. Calculate the support for each itemset.

# 8. Create an empty dictionary `second_le` to store counts of pairs of items.

# 9. Generate pairs of items from `l2` and count their occurrences in the transactions. Store pairs with counts greater than 1 in `second_le`.

# 10. Calculate confidence for the pairs of items in `second_le` and store them in the `con` list.

# 11. Generate triples of items from pairs in `l7` and count their occurrences in the transactions. Store triples with counts greater than 1 in the `third_le` dictionary.

# 12. Finally, the code prints various dictionaries and lists that contain information about frequent itemsets, support, confidence, and triplets of items.

# In summary, this code is a custom implementation of the Apriori algorithm for finding frequent itemsets and generating association rules from a transaction dataset. It calculates support, confidence, and lift values to identify association rules based on item co-occurrence.












