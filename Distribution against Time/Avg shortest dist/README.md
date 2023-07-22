We take the file road.txt, which we originally generated from the given file in the question.
We will now take the forst 100000 lines from the beginning and then operate on it.
We use the following command to do it:
sed -n '1,100000p' road.txt > reduced_road.txt
We also introduce some random values, just to make the process more random!

MODUS OPERANDI:

the shell script q3a.py executes the orders as listed.
The python file average.py computes the average distance of nodes from the source node.

Since we have altered the original file, it is possible the some of the nodes may be 'stand alone', which may mean that no adjacent node exits for
that particular node. In that case our script returns 0 as the average sum.
Now, the shell script runs the instructions 100 times  and each tiem one new node is selected as the source node.

Our original script is set in such a way that the first node in first line is set as the source node.
So, by using q3a.sh, we regularly delete the first line after each iteration and because of that we get a new source node each time.

COMMANDS:
chmod a+x q3a.sh
./q3a.sh

We have plotted the graph using scatter function of matplotlib.
By observing the graph, we observe that there is a positive correlation between the average distance and the time taken in seconds as it is a positive slope.




