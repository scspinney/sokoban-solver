#!/bin/bash

# point to the directory containing the 1000 levels per file
# not .sok files (that's what this script produces)
input_dir="sokobanLevels/Sokoban-small-v0"

# set the path to the header file
header_file="header_file.txt"

# change to the input directory
cd "$input_dir"

# loop over all .txt files in the current directory
for file in *.txt; do

    # get the file's number by removing all non-numeric characters from the filename
    number=$(echo "$file" | tr -dc '0-9')

    # create the new filename with .sok extension
    new_name="$number.sok"

    # add the header to the file
    cat "$header_file" "$file" > temp && mv temp "$file"

    # rename the file
    mv "$file" sokobanLevels/sok_files/"$new_name"

done
