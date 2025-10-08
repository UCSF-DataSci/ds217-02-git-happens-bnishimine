"""Basic student data analysis script."""
import os

def load_students(filename):
    # Load student data from CSV file.
    with open(filename, 'r') as file:
        student_data = file.readlines()
    students = []
    for line in student_data:
        students.append(line.split(","))
    return students

def calculate_average_grade(students):
    # Calculate average grade from student data.
    total = 0
    for student in students:
        total += int(student[2])
    return total/len(students)


def count_math_students(students):
    # Count students in Math.
    math = students[3].count("Math")
    return math


def generate_report(students):
    # Generate formatted report.
    total = len(students)
    avg_grade = calculate_average_grade(students)
    count_math = count_math_students(students)

    report = (
        f"Number of students: {total}\n"
        f"Average grade: {avg_grade:.1f}\n"
        f"Number of math students: {count_math}\n"
    )
    return report
    

def save_report(report, filename):
    # Save report to file.
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        file.write(report)

def main():
    # Main execution function.
    students = load_students('data/students.csv')
    report = generate_report(students)
    save_report(report, 'output/analysis_report.txt')
    
