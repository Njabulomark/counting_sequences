#!/usr/bin/env python

import sys

def count_seqs(filename):
        line_cnts =0
	for line in filename:
		line = line.lstrip()
		if line.startswith('>'):
			line_cnts +=1
	return line_cnts






