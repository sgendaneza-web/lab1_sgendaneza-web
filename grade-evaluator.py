import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    formative_total = 0
    summative_total = 0

    failed_formatives = []

    # a) Check if scores are between 0 and 100
    for item in data:
        if not (0 <= item["score"] <= 100):
            print(f"Invalid score found in {item['assignment']}")
            sys.exit(1)

    # b) Validate weights
    for item in data:
        total_weight += item["weight"]

        if item["group"] == "Formative":
            formative_weight += item["weight"]
            formative_total += (item["score"] * item["weight"]) / 100

            # e) check failed formative assignments
            if item["score"] < 50:
                failed_formatives.append(item)

        elif item["group"] == "Summative":
            summative_weight += item["weight"]
            summative_total += (item["score"] * item["weight"]) / 100

    if total_weight != 100:
        print("Error: Total weight must equal 100")
        sys.exit(1)

    if formative_weight != 60:
        print("Error: Formative weight must equal 60")
        sys.exit(1)

    if summative_weight != 40:
        print("Error: Summative weight must equal 40")
        sys.exit(1)

    # c) Calculate final grade
    final_grade = formative_total + summative_total

    # GPA conversion
    if final_grade >= 80:
        gpa = 4.0
    elif final_grade >= 70:
        gpa = 3.0
    elif final_grade >= 60:
        gpa = 2.0
    elif final_grade >= 50:
        gpa = 1.0
    else:
        gpa = 0.0

    # d) Pass condition
    formative_percent = formative_total / 60 * 100
    summative_percent = summative_total / 40 * 100

    passed = formative_percent >= 50 and summative_percent >= 50

    # f) Print results
    print(f"Final Grade: {final_grade:.2f}%")
    print(f"GPA: {gpa}")

    if passed:
        print("FINAL DECISION: PASSED!")
    else:
        print("FINAL DECISION: FAILED!")

    # resubmission suggestion
    if failed_formatives:
        highest_weight = max(failed_formatives, key=lambda x: x["weight"])

        print("\nResubmission recommended for:")
        for item in failed_formatives:
            print(f"- {item['assignment']} ({item['score']}%)")

        print(
            f"\nPriority resubmission: {highest_weight['assignment']} "
            f"(highest weight = {highest_weight['weight']})"
        )
    else:
        print("\nNo formative resubmissions needed!")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)