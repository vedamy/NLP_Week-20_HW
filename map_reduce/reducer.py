#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None

# read the entire line from STDIN

for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
    # splitting the data on the basis of tab we have provided in mapper.py
	word, count = line.split('\t', 1)
	count = int(count)
	if current_word == word:
		current_count += count
		
	else:
		if current_word:
			print(str(current_count)+ "\t" + current_word)
		current_count = count
		current_word = word

				
if current_word == word:
	print(str(current_count)+ "\t" + current_word)
