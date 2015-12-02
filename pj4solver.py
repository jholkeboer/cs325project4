#!/usr/bin/python

# Oregon State CS325 Project 4 - TSP
# Project Group 4
# Michael Loo
# Susan Eldridge
# Jack Holkeboer

# Adapted from: https://gist.github.com/mlalevic/6222750

import sys, os
from math import sqrt
import itertools
import datetime

def node_distance(node1, node2):
	# each node is an array [x,y]
	distance = int(round(sqrt( (node1[0]-node2[0])**2 + (node1[1]-node2[1])**2 )))
	return distance

def import_problem(inputfile):
	# nodes = {}
	nodes = []
	with open(inputfile) as f:
		for line in f:
			parsed_line = line.strip().split(" ")
			# nodes[int(parsed_line[0])] = [int(parsed_line[1]), int(parsed_line[2])]
			nodes.append([int(parsed_line[1]), int(parsed_line[2])])
	return nodes

def export_solution(tour, outputfile):
	with open(outputfile, 'w+') as f:
		f.write(str(tour['length']) + "\n")
		for node in tour['path']:
			f.write(str(node) + "\n")

def tsp(nodes):
	tour = {'length': 0, 'path': []}
	node_count = len(nodes)

	# all_distances = [[node_distance(nodes[x], nodes[y]) for y in sorted(nodes)] for x in sorted(nodes)]
	# A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
	
	# for node in range(2, node_count):
	# 	print "Node ", node
	# 	B = {}
	# 	for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, node_count), node)]:
	# 		for j in S - {0}:
	# 			B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])
	# 	A = B

	# res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
	# tour['path'] = res[1]
	# tour['length'] = res[0]
	return tour


if len(sys.argv) == 2:
	inputfile = sys.argv[1]
	outputfile = inputfile + ".tour"
	nodes = import_problem(inputfile)

	start = datetime.datetime.now()
	tour = tsp(nodes)
	end = datetime.datetime.now()
	print tour
	print "Time elapsed: ", (end - start)
	# export_solution(tour, outputfile)
	
	
else:
	print "Usage: pj4solver.py [inputfile]"