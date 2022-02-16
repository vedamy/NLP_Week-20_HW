#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import string
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
	# to remove leading and trailing whitespace
	line = line.strip()
	# Convert the characters in line to lowercase to avoid case mismatch
	line = line.lower()
	# Remove the punctuation marks from the line
	new_line = line.translate(line.maketrans("", "", string.punctuation))
	# split the line into words
	words = new_line.split()
	for i in line:
		if i in string.punctuation:
			print(i)
			# we are looping over the words array and printing the word
			# with the count of 1 to the STDOUT
			for word in words:
				# write the results to STDOUT (standard output);
				# what we output here will be the input for the
				# Reduce step, i.e. the input for reducer.py
				print('%s\t%s' % (word, 1))