#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys

source_node_id = 0

for line in sys.stdin:

    if "#" in line:
        continue
    else:
        node_id = int(line.split("\t", 1)[0])
        node_value = int(line.split("\t",1)[1])
        node_dist = (((node_id + node_value)%20) + 1)

    #if node_id == source_node_id:
    #    node_dist = 0
    #else:
    #    node_dist = 2000000

    print('{}\t{}\t{}'.format(node_id, node_value, node_dist))