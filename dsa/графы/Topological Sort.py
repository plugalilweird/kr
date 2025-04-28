class Solution:

    def topoSort(self, V, edges):
        dict1 = {i:[] for i in range(V)}
        list1 = [0]*V
        for i, j in edges:
            dict1[i].append(j)
            list1[j].append(i)