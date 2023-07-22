First of all our data in in unusable format. We have to convert it into usable form by making a file with adjacency list.
So we form the final file using a mapper and reducer and convert the original file into a file with adjacency list, which is named as road.txt.
We have considered the weight of each edge to be 1 for this part.
We use the mapper1.py and reducer1.py in Graph Generator folder to process the original data into useful data.


We have not only calculated the distance from the source node but also the path that is followed by the edges to reach the destination using the minimum distance!!
Output.txt contains multiple columns. The first column conatins the destination node. 
We consider 0 to be the source node for this part. 
The second column is the shortest distance from 0 to the destination node. Or in other words, the second number in a line is the minumum distance from 0 to the node which is the first number of the line.
Further some columns contain the adjacency list of the node in column 1 separated by commas.
The last column shows the path that is followed to calculate the minimum distance.
So, we have also calculated an extra metric, the path!

ALGORITHM:
We have considered the distance between nodes that are not in the adjacency list of 0 to be at a distance of 2000000, which is the representation of infinite.
And all the nodes connected to 0 are considered to be at a distance 1.
We use parallel BFS and Dijkstra to calculate the distance. When some node is discovered using parallel BFS, we update it's distance from 2000000 to it's calculated current distance.
We iteratively compute each node's distance to the source node (0 in this case) and we stop when all the nodes are visited.
We update the distance of each children from 0 with parent distance + parent-child distance.
The node is selected according to the lowest distance of previous node.

If some line is showing it's second number to be 2000000, it means that this node has still not been discovered in the parallel BFS.


Following is the command that was used to execute the operations:
chmod a+x launch_local.sh
./launch_local.sh road.txt [-v]


I terminated the operation after the program ran for 6 hours and was showing for no signs of stopping.
The output is stored in output.txt0 and we have the intial 8 or 9 lakhs of lines. We can continue this on a stronger computer or EMR.


