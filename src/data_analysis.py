"""Basic student data analysis script."""

def load_students(filename):
    # Load student data from CSV file.
    with open('filename', 'r') as file:
        student_data = file.readlines()
    students = []
    for line in student_data:
        students.append(line.split(","))
    return students


def calculate_average_grade(students):
    # Calculate average grade from student data.
    total = 0
    for student in students:
        total += student[2]
    return total/len(students)


def count_math_students(students):
    # Count students in Math.
    math = students.count("Math")
    return math


def generate_report(students):
    # Generate formatted report.
    total = len(students)
    avg_grade = calculate_average_grade(students)
    count_math = count_math_students(students)

    return ("Number of students: ", total,
             "\nAverage grade: ", avg_grade,
             "\nNumber of math students: ", count_math)
    

def save_report(report, filename):
    # Save report to file.
    with open(filename, 'w') as file:
        file.write(report)

def main():
    # Main execution function.
    students = load_students('data/students.csv')
    report = generate_report(students)
    save_report(report, 'output/analysis_report.txt)')
    
