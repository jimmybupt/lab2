print 'CSE 5243 Clustering Analysis by Kun Liu & Zhe Dong'

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--file", dest="in_file",
		 help="the input vector",metavar="FILE"
		 default="vector1.txt")
parser.add_option("-o", "--output", dest="out_file",
		  help="the output matrix file", metavar="FILE")
parser.add_option("-m", "--metric", dest="metric",
		  metavar="[Euclidean|Other]",
		 default="Euclidean", help="Type of similarity")
parser.add_option("-a", "--algorithm", dest="algorithm",
		  metavar="[DBSCAN|Other]",
		  default="DBSCAN")
parser.add_option("-e", "--eps", dest="epsilon", metavar="<Epsilon>",
		  type="float", default=0.5)
parser.add_option("-M", "--min-sample", dest="min_sample", metavar="<Min samples>",
		  type="int", default=5)
parser.add_option("-t", "--test", dest="small_data",
		  action="store_true", default=False)
parser.add_option("-k", dest="cluster", metavar="<Cluster>", type="int",
		  default=10)
(options, args) = parser.parse_args()


#### put a vector file definition here

#open vector file
vector_file = open(options.in_file, 'r')
label_file = open('label.txt', 'r')

#read vector into classes
import ast
import sys
from scipy.sparse import *
info = open("info.txt",'r');
rdim = int(info.readline())
cdim = int(info.readline())


if options.small_data:
	rdim = 5000;
	print 'small test set selected, only loading 5000 rows'

S = lil_matrix((rdim, cdim))

print "Reading vectors... ",
sys.stdout.flush()
i = 0
for line in vector_file:
	data = ast.literal_eval(line);
	for D in data:
		S[i, int(D[0])] = float(D[1])
	i=i+1
	if i==rdim:
		break
label = []
i = 0
for line in label_file:
	label.append(ast.literal_eval(line))
	if i==rdim:
		break

print "done"
S = S.tocsr()


#choose cluster method
import cluster
prediction = []
if options.algorithm.lower()=="dbscan":
	prediction=cluster.DBSCAN_clustering(options.epsilon, options.min_sample,S,options.metric.lower())
elif options.algorithm.lower()=="kmeans":
	prediction=cluster.kmeans_clustering(options.cluster, S)

print len(prediction)


#print cluster result
hist = {}
for item in prediction:
	if item in hist:
		hist[item] += 1
	else:
		hist[item] = 1

for key in hist:
	print key," ", hist[key]

#evaluate result
import quality

quality.quality_evaluation(prediction, S.toarray(), label)
	


#TODO:
#1. measure time
#2. put paser code into another file



