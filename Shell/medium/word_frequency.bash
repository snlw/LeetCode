#!/bin/bash
# Example of words.txt :
# the day is sunny the the
# the sunny is is

cat words.txt | 
# Replace whitespaces with newlines to get all words in separate lines
tr -s '[:space:]' '\n' | 
# Sort words
sort | 
# Get unique occurrences
uniq -c |
# Sort by occurrences
sort -nr | 
# Print to stdout
awk '{print $2 " " $1}'

