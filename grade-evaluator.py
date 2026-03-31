import csv

formative_total = 0
summative_total = 0

formative_weight_sum = 0
summative_weight_sum = 0

failed_formative = []

try:
    with open("grades.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            score = float(row["score"])
            weight = float(row["weight"])
            assignment_type = row["group"]
            name = row["assignment"]

            # validate score
            if score < 0 or score > 100:
                print("Invalid score in", name)
                exit()

            # formative
            if assignment_type == "Formative":
                formative_total += score * weight / 100
                formative_weight_sum += weight

                if score < 50:
                    failed_formative.append((name, weight))

            # summative
            elif assignment_type == "Summative":
                summative_total += score * weight / 100
                summative_weight_sum += weight

except FileNotFoundError:
    print("grades.csv not found")
    exit()

# check weights
total_weight = formative_weight_sum + summative_weight_sum

if formative_weight_sum != 60:
    print("Formative weight must equal 60")

if summative_weight_sum != 40:
    print("Summative weight must equal 40")

if total_weight != 100:
    print("Total weight must equal 100")

# calculate total grade
total_grade = formative_total + summative_total

gpa = (total_grade / 100) * 5

# pass or fail
if formative_total >= 50 and summative_total >= 50:
    status = "PASSED"
else:
    status = "FAILED"

# resubmission logic
resubmit = []

if status == "FAILED" and failed_formative:
    highest_weight = max(failed_formative, key=lambda x: x[1])[1]

    for assignment in failed_formative:
        if assignment[1] == highest_weight:
            resubmit.append(assignment[0])

# print results
print("Final Grade:", round(total_grade,2))
print("GPA:", round(gpa,2))
print("Status:", status)

if resubmit:
    print("Resubmit:", ", ".join(resubmit))

