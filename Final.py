"""
Metrics testing on Karate Club clusterings (known ground truth) based on this paper : https://arxiv.org/pdf/1907.12581.pdf
Sander Schulhoff                                                             
Aug 13 2019

The clusterings in paper 21 (https://arxiv.org/pdf/1008.3926.pdf) were assumed to be the same as Zachary's as the paper did not specify the 
person that its algorithm clustered incorrectly or its mutual info score but it did say it got the same result as many other algorithms. 
Also, I could not find source code to replicate it. This paper finds 2 groupings.
The clusterings in paper 22 (https://www.pnas.org/content/pnas/103/23/8577.full.pdf) were recreatable by means of this Github repository
(https://github.com/zhiyzuo/python-modularity-maximization) that replicates the results. This paper finds 4 groupings.

Only mutual_info_score and homogeneity_score give the 4 cluster result a higher score. I tried finding the reduced mutual information (RMI)
function in scikit but only found adjusted_mutual_info_score and normalized_mutual_info_score. Both give the 2 cluster result a higher 
score which RMI would agree with.

note:
Get4KarateGroupings.py is runnable as a Jupyter Notebook
"""

from sklearn import metrics
labels_true =           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
labels_predZachary =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
labels_pred22 =         [5, 5, 5, 5, 6, 6, 6, 5, 4, 5, 6, 5, 5, 5, 4, 4, 6, 5, 4, 5, 4, 5, 4, 3, 3, 3, 4, 3, 3, 4, 4, 3, 4, 4]
#pretty sure labels_pred21 same as labels_predZachary
labels_pred21 =         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 


print("mutual_info_score:")
print("Statistical Inference (2 clusters): " + str(metrics.mutual_info_score(labels_true, labels_pred21))) #paper 21
print("Maximizing Modularity (4 clusters): " + str(metrics.mutual_info_score(labels_true, labels_pred22))) #paper 22
print("adjusted_mutual_info_score:")
print("Statistical Inference (2 clusters): " + str(metrics.adjusted_mutual_info_score(labels_true, labels_pred21)))
print("Maximizing Modularity (4 clusters): " + str(metrics.adjusted_mutual_info_score(labels_true, labels_pred22))) 
print("normalized_mutual_info_score:")
print("Statistical Inference (2 clusters): " + str(metrics.normalized_mutual_info_score(labels_true, labels_pred21))) 
print("Maximizing Modularity (4 clusters): " + str(metrics.normalized_mutual_info_score(labels_true, labels_pred22))) 
print("adjusted_rand_score:")
print("Statistical Inference (2 clusters): " + str(metrics.adjusted_rand_score(labels_true, labels_pred21))) 
print("Maximizing Modularity (4 clusters): " + str(metrics.adjusted_rand_score(labels_true, labels_pred22))) 
print("homogeneity_score:")
print("Statistical Inference (2 clusters): " + str(metrics.homogeneity_score(labels_true, labels_pred21))) 
print("Maximizing Modularity (4 clusters): " + str(metrics.homogeneity_score(labels_true, labels_pred22))) 
print("fowlkes_mallows_score:")
print("Statistical Inference (2 clusters): " + str(metrics.fowlkes_mallows_score(labels_true, labels_pred21))) 
print("Maximizing Modularity (4 clusters): " + str(metrics.fowlkes_mallows_score(labels_true, labels_pred22))) 

