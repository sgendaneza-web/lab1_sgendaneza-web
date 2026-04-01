Grade-evaluator.py is a python application that calculates a student's final academic standing based
on a pre-existing CSV file of course grades. Organizer.sh is a bash shell script that acts as an
"organizer" to find your CSV files.

#For it to properly function, you need to have a csv file.

How to run grade-evaluator.py
> Type *python3 grade-evaluator.py*
This script reads the grades.csv file, checks that scores and weights are valid, calculates the final grade and GPA,
determines whether the student has passed or failed based on formative and summative performance,
and identifies any formative assignment eligible for resubmission if the student fails.

How to run organizer.sh
> Type *bash organizer.sh*
This script automatically organizes grade files by renaming the existing csv file with a timestamp, 
moving it into an archive folder, creating a new empty csv file, and recording the action in a log file.
