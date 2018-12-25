#!/usr/bin/env python
#mapper.py

import sys


for line in sys.stdin:
	line = line.rstrip()
	line = line.lower()

	node_id, info = line.split('\t')
	info = info.split('|')
	adjList = info[0].split(',')
	value = info[1]
	color = info[2]
	parent = info[3]

	if color != "gray":
		print("%s"%(line)) # if what we received wasn't grey just pass it
		continue # skip remainder of what's in this loop iteration 
	# here we have a grey node, first make this node B 
	# and pass it 
	blackNode = "" + node_id + "\t"  + info[0] + "|" + value + "|" + "BLACK" + "|" + parent
	print("%s"%(blackNode))
	# now go through each child of this node, and add 1 to its value 
	newValue = int(value) +1
	newValue = str(newValue)
	for child_id in adjList:
		gray = "" + child_id  + "\t" + "0null|" + newValue + "|GRAY|" + parent + "," + node_id
		print("%s"%(gray))