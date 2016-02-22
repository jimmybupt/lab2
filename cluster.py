from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

#KMeans clustering function
def kmeans_clustering(n_clusters,word_vector):
  model=KMeans(n_clusters)
  prediction=model.fit_predict(word_vector)
  return prediction
  
#Hierarchical clustering function
def hierarchical_clustering(n_clusters,word_vector):
  model=AgglomerativeClustering(n_clusters)
  prediction=model.fit_predict(word_vector)
  return prediction

