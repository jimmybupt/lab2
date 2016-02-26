print 'CSE 5243 Similarity Matrix by Kun Liu & Zhe Dong'

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--file", dest="in_file",
		 help="the input vector",metavar="FILE")
parser.add_option("-o", "--output", dest="out_file",
		  help="the output matrix file", metavar="FILE")
parser.add_option("-m", "--metric", dest="metric",
		  metavar="[Euclidean|Other]",
		 default="Euclidean", help="Type of similarity")
parser.add_option("-a", "--algorithm", dest="algorithm",
		  metavar="[DBSCAN|Other]",
		  default="DBSCAN")
parser.add_option("-e", "--eps", dest="epsilon", metavar="<Epsilon>",
		  default=10.0)
parser.add_option("-M", "--min-sample", dest="min_sample", metavar="<Min samples>",
		  default=10)
parser.add_option("-t", "--test", dest="small_data",
		  action="store_true", default=False)
(options, args) = parser.parse_args()


#### put a vector file definition here

#open vector file
vector_file = open(options.in_file, 'r')

#read vector into classes
import ast
import sys
from scipy.sparse import *
info = open("info.txt",'r');
cdim = 0
rdim = 21578
for line in info:
	cdim = int(line)
cdim = 20778	
S = lil_matrix((rdim, cdim))


if options.small_data:
	rdim = 1000;
	print 'small test set selected, only loading 1000 rows'

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
	
print "done"
S = S.tocsr()


#compute the pairwise distance
import distance
#dist_func = {
#	'euclidean':distance.euclidean_sparse
#}
#func = dist_func[(options.metric.lower())]
#D_Matrix = []
#for i in range(0, len(L)-1):
#	v = []
#	for j in range(0, i):
#		d = func(L[i], L[j])
#		v.append(d)
#	D_Matrix.append(v)

#encode the matrix and save

#out = open("result.txt",'w')
#for row in D_Matrix:
#	print >>out, row


#choose cluster method
import cluster
if options.algorithm.lower()=="dbscan":
	prediction=cluster.DBSCAN_clustering(options.epsilon, options.min_sample,S,options.metric.lower())
	print prediction
elif options.algorithm.lower()=="hierarchical":
	print "a"

#TODO:
#1. measure time
#2. put paser code into another file



