#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
	# to remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split()
	
	# we are looping over the words array and printing the word
	# with the count of 1 to the STDOUT
	for word in words:
		print('%s\t%s' % (word, 1))