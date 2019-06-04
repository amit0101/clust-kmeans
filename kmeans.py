import numpy as np
import random
from matplotlib import pyplot as plt


class Clustering:
    """Class to cluster a list of 2-D points into a given number of clusters.
    Class method kmeans is used for clustering by k-means method. It prints and plots output clusters by default.
    """

    def __init__(self, tuples, k):
        self.tuples = tuples
        self.k = k
    
    @staticmethod
    def rmsdist(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    
    @classmethod
    def kmeans(cls, tuples, k, verbose=True, plot=True):

        clusters = [0]*len(tuples)
        centroids = random.sample(tuples, k=k)

        prev_centroids = []

        while prev_centroids!=centroids:

            prev_centroids = centroids

            for index in range(len(tuples)):
                mindist = np.inf
                for i in range(k):
                    dist = Clustering.rmsdist(tuples[index], centroids[i])
                    if dist < mindist:
                        mindist = dist
                        clusters[index] = i

            for i in range(k):
                indices = [x for x, cluster in enumerate(clusters) if cluster==i]
                cluster_tuples = [tuples[index] for index in indices]
                centroid = tuple([sum(p)/len(p) for p in zip(*cluster_tuples)])
                centroids[i] = centroid
        
        # Printing output
        if verbose:
            for i in range(k):
                print("Cluster " + str(i) + ":")
                indices = [x for x, cluster in enumerate(clusters) if cluster==i]
                cluster_tuples = [tuples[index] for index in indices]
                print(cluster_tuples)
                print("Cluster centroid: " + str(centroids[i]) + '\n')
                
        # Plotting clusters
        if plot:
            colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
            for i in range(len(tuples)):
                plt.plot(tuples[i][0], tuples[i][1], marker='o', c=colors[clusters[i]])
            plt.title('Color-coded clusters')
            plt.show()

        return clusters, centroids


# Test case

k = 3
tuples = [(1, 2), (2, 1), (2, 3), (3, 2), (11, 12), (12, 11), (12, 13), (13, 12), (20, 21), (21, 20), (21, 22), (22, 21)]

clusters, centroids = Clustering.kmeans(tuples, k)
