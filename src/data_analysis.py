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
    

def generate_report(students):
    """Generate formatted report."""
    # TODO: Implement report generation
    pass

def save_report(report, filename):
    """Save report to file."""
    # TODO: Implement file saving
    pass

def main():
    """Main execution function."""
    # TODO: Orchestrate the analysis
    pass

if __name__ == "__main__":
    main()
