#!/bin/bash

# point to the directory containing the 1000 levels per file
# not .sok files (that's what this script produces)
input_dir="/home/spinney/scratch/sokoban-solver/sokobanLevels/Sokoban-v0"

# Extract the dataset name from the input_dir
dataset_name=$(basename "$input_dir")

# set the path to the header file
header_file="/home/spinney/scratch/sokoban-solver/header_file.txt"

# change to the input directory
cd "$input_dir"

# Create the subdirectory in sok_files with the dataset name
output_dir="/home/spinney/scratch/sokoban-solver/sokobanLevels/sok_files/$dataset_name"
echo "Dataset: $dataset_name"

mkdir -p "$output_dir"

# loop over all .txt files in the current directory
for file in *.txt; do
    
    # get the file's number by removing all non-numeric characters from the filename
    number=$(echo "$file" | tr -dc '0-9')

    # create the new filename with .sok extension
    new_name="$number.sok"

    # print the filename being processed
    echo "Processing: $file"

    # add the header to the file
    cat "$header_file" "$file" > temp && mv temp "$file"

    # move the processed file to the subdirectory
    mv "$file" "$output_dir/$new_name"
done
