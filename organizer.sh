#!/bin/bash

# create archive folder if it doesn't exist
mkdir -p archive

# create timestamp
timestamp=$(date +"%Y%m%d-%H%M%S")

# rename file
new_name="grades_$timestamp.csv"

# move file to archive
mv grades.csv archive/$new_name

# create new empty grades.csv
touch grades.csv

# log the action
echo "$timestamp | grades.csv -> archive/$new_name" >> organizer.log

echo "Archive complete"