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
        next(file)  # Skip header line
        student_data = file.readlines()
    students = []
    for line in student_data:
        students.append(line.split(","))
    return students


def analyze_data(students):
    # Calculate multiple statistics
    max_grade = max([s[2] for s in students])

    min_grade = min([s[2] for s in students])
    
    avg_grade = sum([int(s[2]) for s in students]) / len(students)
            
    
    return {
        "Total students": len(students),
        "Maximum grade": max_grade,
        "Minimum grade": min_grade,
        "Average grade": avg_grade,
        "Distribution": analyze_grade_distribution(students)
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
    report = (f"Number of students: {results[["Total students"]]}"
              f"\nAverage grade: {results["Average grade"]}"
              f"\nHighest grade: {results["Maximum grade"]}"
              f"\nLowest grade: {results["Minimum grade"]}"
              f"\nGrade distribution: {results["Distribution"]}")
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