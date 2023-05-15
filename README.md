# PART 2: USER GUIDE
# Experimental Evaluation of Optimal Distance Oracles for Planar Graphs
Welcome to our project on evaluating and improving the distance oracle developed by Das, Kipouridis, Gutenberg, and Wulff-Nilsen for planar graphs. In this README guide, we will provide you with all the necessary information to understand and use our code and resources effectively.
Resources
To understand the context of our project, it is recommended to familiarize yourself with the following concepts and resources:
1. Planar Graphs: Planar graphs are an important class of graphs that have applications in various fields. Familiarize yourself with the properties and characteristics of planar graphs.
2. Klein's Distance Oracle: Klein developed a complex distance oracle using a highly advanced dynamic tree structure. You can refer to Klein's original paper to understand the intricacies of his approach.
https://dl.acm.org/doi/pdf/10.5555/1070432.1070454
3. Das, Kipouridis, Gutenberg, and Wulff-Nilsen's Distance Oracle: This alternative distance oracle offers comparable performance to Klein's approach but is easier to maintain and implement. Refer to their paper for a detailed description of their preprocessing and query procedures.
https://epubs.siam.org/doi/epdf/10.1137/1.9781611977066.1


# Evaluation
Our project involves evaluating the distance oracle developed by Das, Kipouridis, Gutenberg, and Wulff-Nilsen. The main components of our evaluation include:

1. Preprocessing Procedure: We preprocess the graph using a divide-and-conquer algorithm. The graph is divided into sub-graphs, and the shortest path trees are formed from the edges of the end points of each subgraph. The intersecting area is contracted since all the shortest path trees from the subgraph must contain the contracted area. Recursive calls on the subproblems result in a graph with only contracted nodes.
2. Query Procedure: Once the graph is processed, a query finds the distance to a contracted node and sums up the distance when the desired node is found. The contraction of nodes is done by updating the weight of outgoing edges and removing incoming edges of the contracted node.
3. Space and Runtime Analysis: We analyze the space and runtime complexity of the algorithm. The space required by all subproblems is at most 12n - 24, where n is the number of vertices. The total data structure size becomes O(n log h), and the total construction time is O(S(n) log h), where S(n) is equivalent to O(nlog(n)).
# Future Work
Experimental Evaluation: The algorithm should be implemented using Python and tested on extensive road networks or planar graphs. Compare the practical results against the theoretical runtimes to assess the algorithm's effectiveness.
# Code
We provide you with the following code and resources to help you get started:
Codebase: The codebase below contains the implementation of the distance oracle algorithm. We use list and priority queue data structures. 
