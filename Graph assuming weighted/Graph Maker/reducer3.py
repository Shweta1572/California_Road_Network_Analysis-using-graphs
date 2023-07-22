#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re

current_node_key = None
source_node_id = 0  
node_key = None
node_adjacency_list = []

for line in sys.stdin:

    # filtering lines 
    if "#" in line:
        continue
    else:
        line = line.strip()
        node_key = line.split("\t")[0]
        node_value = line.split("\t")[1]
        node_dist_curr = line.split("\t")[2]

    # assigning initial distances
    if int(node_key) == 0:
        node_dist = 0
    else:
        node_dist = 200000
        
    node_tuple = ("{}:{}".format(node_value, node_dist_curr))

    if current_node_key == node_key:
        current_node_dist = node_dist
        node_adjacency_list.append(node_tuple)
        # print(node_tuple)

    else:
        if current_node_key:
            print('{}\t{}\t{}'.format(current_node_key, current_node_dist, str(node_adjacency_list)[1:-1]))
        node_adjacency_list[:] = []
        current_node_dist = node_dist
        current_node_key = node_key
        node_adjacency_list.append(node_tuple)
        # print(node_tuple)

if current_node_key:
    # print(node_tuple)
    print('{}\t{}\t{}'.format(current_node_key, node_dist, str(node_adjacency_list)[1:-1]))

