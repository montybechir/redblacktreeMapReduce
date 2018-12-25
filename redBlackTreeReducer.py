#!/usr/bin/env python
#reduce2.py

import string
import sys

prevValue = None
prevColor = None
prevParent = None 
prev_Node = None 
countGrey = 0
for line in sys.stdin:
	line = line.rstrip()
	line = line.lower()

	node_id, content = line.split('\t\t')
	node_id = node_id.split('.')[0]
	info = content.split('|')
	adjList = info[0].split(',')
	value = info[1]
	color = info[2]
	parent = info[3]
	key = node_id
	val = content

	# if the node read wasn't gray just print the line
	if(color == "black"):
		print("%s\t%s"%(key,val)) # if what we received wasn't grey just pass it
		continue # skip remainder of what's in this loop iteration 
	elif(color == "gray"):
		# store this node's information, next node will be a white node containing its children's info 
		# in case we get two gray nodes with the same value, we need to keep the darkest color, and min value 
		if(prev_Node == node_id):
			value = min(value, prevValue) # take the minimum value between the two 
		prev_Node = node_id
		prevColor = color
		prevParent = parent
		prevValue = value
		# increment num of greynodes read by 1 everytime 
		print >> sys.stderr, "reporter:counter: CUSTOM, numgreynodes,1" 

	else:
		# here we have a white node
		# if the previous node is the same as this node, then it was a grey node
		# we should take that grey Node's value, and parent and use this white node's adj list to pass back to mapper
		if(prev_Node == node_id):
			updatedNode = "" + node_id + "\t"  + info[0] + "|" + prevValue + "|" + prevColor + "|" + prevParent
			print("%s"%(updatedNode))
		else:
			print("%s\t%s"%(key,val))


countgreystr = "count:" + str(countGrey)
sys.stderr.write(countgreystr)
