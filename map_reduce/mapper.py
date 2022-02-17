#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
	#remove leading and trailing whitespaces
	line=line.strip()
	#split words into lines
	words=line.split()

	for word in words:
		word=re.findall(r"[\w]+|[^\s\w]", word)
		for word in word:
			if word=='':
				pass
			else:
				print(word.lower() + "\t" + '1')
				