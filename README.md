## Analyzing California Road Network Using Graph Theory

**Graph with Unit Distance:**
- In this analysis, we assume that the distance between all nodes (locations) in the California road network is the same and equal to 1.
- We use parallel Breadth-First Search (BFS) starting from a source node to find the shortest distance to all other nodes in the network.

**Graph with Weights:**
- In this part of the analysis, the distance between node i and node j is determined using the formula (((i+j)%20)+1).
- Again, we employ parallel BFS from a source node to find the shortest distance to all other nodes in the network.

**Distribution Against Time:**
- For the average shortest distance, we randomly select 1000 nodes and run BFS with equal weights (1).
- We calculate the average shortest distance from each of these nodes to all other nodes and plot it against the time taken to run the code.
- Additionally, we calculate the clustering coefficient for another set of 1000 random nodes using BFS with equal weights (1) and plot it against the corresponding time taken.

**Average Shortest Distance vs. Time Taken:**
- In this section, we repeat the process described in the "Distribution Against Time" section, and we also print out the shortest paths obtained during the computation.

## Sample Run
The shell scripts required for the analysis are provided in their respective folders.

