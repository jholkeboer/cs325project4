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
	node_dict = {}
	nodes = []
	with open(inputfile) as f:
		for line in f:
			parsed_line = line.strip().split(" ")
			while '' in parsed_line:
				parsed_line.remove('')
			node_dict[parsed_line[1] + "-" + parsed_line[2]] = int(parsed_line[0])
			nodes.append([int(parsed_line[1]), int(parsed_line[2])])
	return nodes, node_dict

def export_solution(tour, outputfile):
	with open(outputfile, 'w+') as f:
		f.write(str(tour['length']) + "\n")
		for node in tour['path']:
			f.write(str(node) + "\n")

def tsp(points, node_dict):
	start = points[0]
	must_visit = points
	path = [start]
	must_visit.remove(start)
	while must_visit:
		nearest = min(must_visit, key=lambda x: node_distance(path[-1], x))
		path.append(nearest)
		must_visit.remove(nearest)
	
	tour = {'length': 0, 'path': []}
	
	# get node indices
	for n in path:
		node_key = str(n[0]) + "-" + str(n[1])
		tour['path'].append(node_dict[node_key])
	
	# calculate path length
	for i in range(len(path)):
		tour['length'] += node_distance(path[i], path[i-1])

	return tour


if len(sys.argv) == 2:
	inputfile = sys.argv[1]
	outputfile = inputfile + ".tour"
	nodes, node_dict = import_problem(inputfile)

	start = datetime.datetime.now()
	tour = tsp(nodes, node_dict)
	end = datetime.datetime.now()

	print "Time elapsed: ", (end - start)
	export_solution(tour, outputfile)
	
else:
	print "Usage: pj4solver.py [inputfile]"
