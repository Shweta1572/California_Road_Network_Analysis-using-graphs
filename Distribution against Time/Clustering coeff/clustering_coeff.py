from csv import writer
import time

time_in = time.time()

dist=[]
source_node = None
k = None
num_edges = 0
with open('test_rec.txt','r') as f:
    file_content = f.readlines()
    for i in range(len(file_content)):
        node = int(file_content[i].strip().split("\t")[0])
        adjacency_list = file_content[i].strip().split("\t")[2]
        neighbours = adjacency_list.strip().split(",")
        if i == 0:
            source_node = node
            k = len(neighbours)
            for neighbour in neighbours:
                dist.append(int(neighbour.strip().split(":")[0]))
        elif node in dist:
            common_node_adjacency_list = adjacency_list
            for neighbour in neighbours:
                if int(neighbour.strip().split(":")[0]) in dist:
                    num_edges += 1

time_out = time.time()
time_taken = time_out - time_in

if k < 2:
    clustering_coef = 0
    print('The local clustering coefficient for {} is {}.'.format(str(source_node), str(clustering_coef)))
else:
    clustering_coef_den = k*(k-1)
    clustering_coef = num_edges/clustering_coef_den
    print('The local clustering coefficient for {} is {}.'.format(str(source_node), str(clustering_coef)))

List = [source_node, clustering_coef, time_taken]
with open('clustering_coeff.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(List)
    f_object.close()
