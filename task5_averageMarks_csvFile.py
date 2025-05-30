# Program to read from CSV file of student marks and calculate average marks

import csv

# Open the file in read mode
with open("student.csv", "r") as file:
    total_marks = 0
    student_count = 0

    data = csv.reader(file)

    # Skip and save the header row
    header = next(data)

    rows = []

    # Read each row of data
    for row in data:
        name = row[0]
        marks = float(row[1])  # Convert marks to float
        rows.append((name, marks))  # Store name and marks as a tuple
        total_marks += marks
        student_count += 1

    # Display student details
    print("Student Marks Detail:\n")
    print(f"{header[0]:<10}{header[1]:<10}")
    print('-' * 20)
    for name, marks in rows:
        print(f"{name:<10}{marks:<10}")

    # Calculate and display average
    if student_count > 0:
        average_marks = total_marks / student_count
        print("\nTotal Students:", student_count)
        print(f"Average Marks: {average_marks:.2f}")
    else:
        print("No student data found.")
