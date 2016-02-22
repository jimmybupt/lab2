def euclidean_sparse(sparse_v1, sparse_v2):
	sum = 0.0
	return sum

from scipy.spatial import distance
#euclidean distance between one pair of vectors
def euclidean_distance(v1,v2):
	return distance.euclidean(v1,v2)

#cosine similarity between one pair of vectors
def cosine_similarity(v1,v2):
	return 1-distance.cosine(v1,v2)
	
