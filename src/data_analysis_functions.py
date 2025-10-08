"""Advanced student data analysis script."""
import os
def load_data(filename):
    # Check if file is CSV
    if filename.endswith('.csv'):
        return load_csv(filename)
    else:
        return "Unsupported file format"
    

def load_csv(filename):
    # Load student data from CSV file.
    with open(filename, 'r') as file:
        student_data = file.readlines()
    students = []
    for line in student_data:
        students.append(line.split(","))
    return students

def analyze_data(students):
    # Calculate multiple statistics
    max_grade = max(int(student[2]) for student in students)
    min_grade = min(int(student[2]) for student in students)
    avg_grade = sum(int(student[2]) for student in students) / len(students)
    return {
        "Maximum grade": max_grade,
        "Minimum grade": min_grade,
        "Average grade": avg_grade
    }
    

def analyze_grade_distribution(students):
    # Count grades by letter grading, calculate and display percentage of distribution with '.1f' formatting.
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    total = len(students)

    for student in students:
        grade = int(student[2])
        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1
    
    percent_distribution = { percent: (count / total) * 100 for percent, count in distribution.items()}

    return { 'Grades': distribution , 'Grade breakdown': percent_distribution}


def save_results(results, filename):
    # Generate formatted report.
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    total = len(results)
    data_analysis = analyze_data(results)
    analysis_grade_dist = analyze_grade_distribution(results)
    report = (f"Number of students: {total}\n"
              f"\nData analysis: {data_analysis:.1f}\n"
              f"\nGrade distribution: {analysis_grade_dist}\n")
    with open(filename, 'w') as file:
        file.write(report)

def main():
    """Main execution function."""
    students = load_data('data/students.csv')

    results = analyze_data(students)

    save_results(results, 'output/analysis_report.txt')

    print(results)



if __name__ == "__main__":
    main()