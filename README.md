# Table of Contents

1. [Python Version] (README.md#python-version)
2. [Required Packages] (README.md#required-packages)
3. [Details of Implementation] (README.md#details-of-implementation)
4. [Testing and Timing] (README.md#testing-and-timing)
5. [Repo directory structure] (README.md#repo-directory-structure)

##Python Version

This code was written to use Python 2.7. Please make sure that you do not attempt to run it using Python 3.x.

##Required Packages

This code doesn't use any third party packages. It does, however, use the difaultdict data type available from the collections package that should come standard with Python 2.7.


##Details of Implementation

[Back to Table of Contents] (README.md#table-of-contents)

This coding challenge is a classic example of a problem appropriate for graph theory. The user network is represented by a simple undirected graph (no multi-edges or self-loops). It is assumed that the users are not all connected to each other; i.e, |E|<<|V|^2, where |E| is the number of edges (connections) and |V| is the number of vertices (users). As a result of the sparse nature of the graph, an adjacency list was used to store the graph rather than an adjacency matrix. Furthermore, a defaultdict of sets was used to store the adjacency list as it offers many benefits over the standard dict data type in Python. The defaultdict contained sets which streamlined the edge representation as there was no need to check for redundant connections. Finally, because the batch_payment.txt and stream_payent.txt files contained millions of transions each, the file was read line by line in order to avoid loading the entire transaction history and stream into memory.

##Testing and Timing

[Back to Table of Contents] (README.md#table-of-contents)

In addition to the simple test provided by Insight in the insight_testsuite directory, I also made a more slightly more sophisticated test in the my-test-paymo-trans directory. This test checked that the new streaming transactions were in fact added to the graph and that all three output files contained the correct string ('trusted' or 'unverified') for the various transitions. I also ran the run_tests.sh to ensure that I passed the default test provided by Insight.

As far as the time it takes this code to determine the whether or not a tranaction is verified or unverified, I allowed the code to process the first 1000 tranactions in the stream_payment.txt file provided by insight. On average, it takes 0.7 sec per transaction with the most connected users maxing out at 3.5-4.5 sec/transaction. It should be noted that these tests were run on a 2008 MacBook with a 2.4 GHz Intel Core 2 Duo Processor and 8 GB of 1067 MHz RAM. I anticipate that most modern servers that would typically run this code would far outperform my machine. 

##Repo directory structure
[Back to Table of Contents] (README.md#table-of-contents)

My Repo Structure

	├── README.md 
	├── run.sh
	├── src
	│  	└── antifraud.py
	├── paymo_input
	│   └── batch_payment.txt
	|   └── stream_payment.txt
	├── paymo_output
	│   └── output1.txt
	|   └── output2.txt
	|   └── output3.txt
	└── insight_testsuite
	 	   ├── run_tests.sh
		   └── tests
	        	└── test-1-paymo-trans
        		│   ├── paymo_input
        		│   │   └── batch_payment.txt
        		│   │   └── stream_payment.txt
        		│   └── paymo_output
        		│       └── output1.txt
        		│       └── output2.txt
        		│       └── output3.txt
        		└── my-test-paymo-trans
            		 ├── paymo_input
        		     │   └── batch_payment.txt
        		     │   └── stream_payment.txt
        		     └── paymo_output
        		         └── output1.txt
        		         └── output2.txt
        		         └── output3.txt