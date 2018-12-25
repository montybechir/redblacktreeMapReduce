#!/usr/bin/env python
#reduce2.py

import string
import sys

import os
import subprocess
# counter will be number of grey nodes
# if number of grey nodes is less than 0:

# 
counter = 1
firstCommand = True
firstCommand = "hadoop jar \
						/home/instructor/hadoop-streaming/hadoop-streaming-2.7.3.jar \
						-D stream.map.output.field.separator=. \
						-D stream.num.map.output.key.fields=2 \
						-files q2mapper2.py,q2reducer2.py \
						-mapper q2mapper2.py -reducer q2reducer2.py \
						-input /user/mbechirn/a2q2input/q2input.txt \
						-output /user/mbechirn/a2q2.1"

inputFile = "/user/mbechirn/a2q2input/q2input.txt"
outputPath = "/user/mbechirn/a2q2.1/"
outputP = "/user/mbechirn/a2q2.1"
outputFile = "part*"
numO = 1
inputPath = "/user/mbechirn/"
constantCommand = "hadoop jar \
						/home/instructor/hadoop-streaming/hadoop-streaming-2.7.3.jar \
						-D stream.map.output.field.separator=. \
						-D stream.num.map.output.key.fields=2 \
						-files q2mapper2.py,q2reducer2.py \
						-mapper q2mapper2.py -reducer q2reducer2.py \\"
						# sub process library - can fork commands , get a handle and read stderr 
# call first map reduce job
sp = subprocess.Popen([firstCommand], stdout=subprocess.PIPE, stderr =subprocess.PIPE, shell=True)
out, err = sp.communicate()
countG = 1

while(countG > 0):
	countG = 0
	if err == None:
		system.exit()


	print(err)


	count = err.split("numgreynodes=")[1].split("\n")[0].rstrip()

	countG = int(count)
	inputFile = outputFile
	
	filesWanted = "hdfs dfs -ls " + outputPath + "part*"
	
	sp = subprocess.Popen([filesWanted], shell=True, stdout=subprocess.PIPE)
	out = sp.communicate()
	
	out = list(out)

	print(out)
	
	out2 = out[0].split(" /")[1]

	out3 = out2.split(" ")[0]
	inputPre = "-input " + outputPath
	num = 0
	numstr = "0000"
	inputString = ""

	print(out)
	inputCurr = ""
	for i in range(len(out)/2):
		inputCurr = inputPre + "part-" + numstr + str(num)+ " "
		inputString = inputString + inputCurr
		 
	numO +=1 

	outputPath = outputP + str(numO) 

	newCommand = constantCommand + inputString + "-output " + outputPath

	outputPath = outputPath + "/" 


	sp = subprocess.Popen([newCommand], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	out, err = sp.communicate()
