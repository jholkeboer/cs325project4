#!/usr/bin/python

# Oregon State CS325 Project 4 - TSP
# Project Group 4
# Michael Loo
# Susan Eldridge
# Jack Holkeboer

import sys, os
from math import sqrt, round

def node_distance(node1, node2):
	# each node is an array [x,y]
	distance = int(round(sqrt( (node1[0]-node2[0])^2 + (node1[1]-node2[1])^2 )))
	return distance

def import_problem(inputfile):
	nodes = {}
	with open(inputfile) as f:
		for line in f:
			parsed_line = line.strip().split(" ")
			nodes[parsed_line[0]] = [parsed_line[1], parsed_line[2]]
	return nodes

def export_solution(tour, outputfile):
	with open(outputfile, 'w+') as f:
		f.write(str(tour['length']) + "\n")
		for node in tour['path']:
			f.write(str(node) + "\n")

def tsp(nodes):
	tour = {'length': 0, 'path': [1,2,3]}
	
	# algorithm goes here
	
	return tour

if len(sys.argv) == 2:
	inputfile = sys.argv[1]
	outputfile = inputfile + ".tour"
	nodes = import_problem(inputfile)
	tour = tsp(nodes)
	export_solution(tour, outputfile)
else:
	print "Usage: pj4solver.py [inputfile]"