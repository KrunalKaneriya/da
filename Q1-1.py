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
        
        for v in tamp:
    for p in range(len(v)):
        r1 = v[p] - mean[0]
        r2 = v[p] - mean[1]
        r3 = v[p] - mean[2]
        r4 = v[p] - mean[3]

        # Find the minimum difference and assign the value to the corresponding cluster
        min_diff = min(r1, r2, r3, r4)
        if min_diff == r1:
            cluster = 0
        elif min_diff == r2:
            cluster = 1
        elif min_diff == r3:
            cluster = 2
        else:
            cluster = 3

        # Print the value and its assigned cluster
        print(f"Value {v[p]} is assigned to Cluster {cluster}")

# Now, each value in the tamp list is assigned to a cluster based on its proximity to the mean of each cluster.
# Define the data points
# data_points = [12, 25, 35, 45, 60, 70, 80, 95]

# # Prompt the user to define the number of clusters
# num_clusters = int(input("Enter the number of clusters: "))

# # Initialize empty clusters
# clusters = [[] for _ in range(num_clusters)]

# # Manually assign data points to clusters
# for point in data_points:
#     valid_cluster = False
#     while not valid_cluster:
#         try:
#             cluster_num = int(input(f"Assign data point {point} to cluster (0 to {num_clusters - 1}): "))
#             if 0 <= cluster_num < num_clusters:
#                 clusters[cluster_num].append(point)
#                 valid_cluster = True
#             else:
#                 print(f"Invalid cluster number. Please enter a number between 0 and {num_clusters - 1}.")
#         except ValueError:
#             print("Invalid input. Please enter a valid cluster number.")

# # Print the clusters
# for i, cluster in enumerate(clusters):
#     print(f"Cluster {i}: {cluster}")

