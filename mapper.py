#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    
    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    
    
    stopword = set(['the', 'and', '.',',',':',';','-','\'','?','!', '\"'])

    for word in words:
        if word not in  stopword:
          print '%s\t%s' % (word, "1")
