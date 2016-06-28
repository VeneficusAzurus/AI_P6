# AI_P6
# Forrest Cinelli and Ziyan Ding
We used Python 3 to write our project. To run our project, go to the command line and type the following:

python3 bnmain.py <network_file> <query_file> <num_samples>

where <network_file> and <query_file> should be filenames and <num_samples> should be an integer. All arguments are mandatory.

No external libraries were used. 

We chose option B for part 2. 

We chose to represent the Bayesian Network as a network of individual nodes. This was done mainly because it makes the architecture very simple, without sacrificing much power: it's very easy to recursively move through a directed graph that is modeled this way, and the nodes can even do some computations themselves. 
