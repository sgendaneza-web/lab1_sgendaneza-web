#!/bin/bash

# create an archive folder if it doesn't exist
mkdir -p archive
# create a timestamp
timestamp=$(date +"%Y%m%d-%H%M%S")

# rename the file
new_name="grades_$timestamp.csv"
mv grades.csv archive/$new_name

# created a new empty grades.csv
touch grades.csv

# log the action
echo "$timestamp | grades.csv -> archive/$new_name" >> organizer.log

echo "Archive complete"