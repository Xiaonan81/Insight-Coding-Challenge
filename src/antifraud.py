from collections import defaultdict;

def build_initial_network_state(fpath = 'paymo_input/batch_payment.txt'):
	"""
	Description:
		Builds the initial state of the user network from the batch_payment.txt file.
	
	Input : fpath [string] - Filepath for batch_payment.txt
	
	Output: graph [defaultdict(set)] - Graph of the initial state of the user netwrok
	"""
	print('Building the initial state of the user network...');
	graph = defaultdict(set);
	with open(fpath, 'r') as infile:
		hdr = infile.readline();
		for line in infile:
			nodes = [[x.strip() for x in line.split(',')][i] for i in [1, 2]]
			if (nodes[0].isdigit() * nodes[1].isdigit()):
				sender = int(nodes[0]); receiver = int(nodes[1]);
				graph[sender].add(receiver); graph[receiver].add(sender);
	infile.close();
	print('\t Done');
	return graph

def stream_payments(graph, fpath = 'paymo_input/stream_payment.txt'):
	"""
	Description:
		Streams payments from the stream_payment.txt file and writes the appropriate
		string to output files depending on the connection distance returned from 
		the paymo_bfs function.
	
	Input : graph [defaultdict(set)] - Graph of the initial state of the user network
			fpath [string] - Filepath for stream_payment.txt
			
	Output: [defaultdict(set)] Graph of the final state of the user network
	"""
	print('Streaming payments...');
	switcher = { 1     : ('trusted\n'   , 'trusted\n'   , 'trusted\n'   ),
				 2     : ('unverified\n', 'trusted\n'   , 'trusted\n'   ),
				 3     : ('unverified\n', 'unverified\n', 'trusted\n'   ),
				 4     : ('unverified\n', 'unverified\n', 'trusted\n'   ),
				 False : ('unverified\n', 'unverified\n', 'unverified\n')}
	out1 = open('paymo_output/output1.txt', 'w');
	out2 = open('paymo_output/output2.txt', 'w');
	out3 = open('paymo_output/output3.txt', 'w');
	with open(fpath, 'r') as infile:
		hdr = infile.readline();
		for line in infile:				
			nodes = [[x.strip() for x in line.split(',')][i] for i in [1, 2]];
			if (nodes[0].isdigit()*nodes[1].isdigit()):
				sender = int(nodes[0]); receiver = int(nodes[1]);
				conn_lev = paymo_bfs(graph, sender, receiver, diameter = 4);
				out1.write(switcher[conn_lev][0]);
				out2.write(switcher[conn_lev][1]);
				out3.write(switcher[conn_lev][2]);
				graph[sender].add(receiver); graph[receiver].add(sender);
	infile.close(); out1.close(); out2.close(); out3.close();
	print('\tDone')
	return graph

def paymo_bfs(graph, start, goal, diameter = float('inf')):
	"""
	Description:
		Breadth-First Search for the connection level of the sender and receiver. This
		function also has a diameter input to specify the maximum connection distance
		desired before False is returned.
		
	Input: graph    [defaultdict(set)] - Graph of the current state of the user network
		   start    [int] - userID who is sending the money using paymo
		   goal     [int] - userID who is receiving the money using paymo
		   diameter [int or float] - maximum number of connections before False is returned
		   
	Output: len(path) - 1 [int] - connections distance
			OR
			False [Bool] - if the connection is greater than the diameter
	"""
	queue = [(start, [start])];
	disc = set([start]);
	while queue:
		(vertex, path) = queue.pop(0);
		if len(path) - 1 > diameter:
			return False;
		elif goal == vertex:
			return len(path) - 1;
		for next in graph[vertex] - set(path) - disc:
			if next not in disc:
				queue.append((next, path + [next]));
				disc.add(next);
	return False;

stream_payments(build_initial_network_state());