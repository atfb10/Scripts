#!/bin/bash

# Count number of word occurrences on a single page

# Function that handles search functionality
word_search() {
    echo "The term $1 is found the following number of times on $2: " 
    curl --silent $2 | grep -c -i $1
}

# Print instructions
echo "Welcome to the string search program. Enter String and webpage arguments to count word occurences on a page!"
echo 

# Gather input
echo "Enter word to search for: "
read WORD 
echo 
echo "Enter webpage to search on: "
read SITE

# Show results
word_search $WORD $SITE