#!/bin/bash
echo "creating project structure..."

mkdir -p src data output
echo "created directories src, data, output"


cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,15,90,Math
Andrew,16,92,Math
Frank,15,3,Math
Dan,15,65,Math
Franklin,16,25,Math
Crash,17,77,Math
Beatrice,17,89,Math
Aaron,15,100,Math
Bean,15,80,Math
Cat,16,71,math
EOF

echo "created students.csv file"

cat > src/data_analysis.py << 'EOF'
"""Basic student data analysis script."""

def load_students(filename):
    """Load student data from CSV file."""
    # TODO: Implement CSV loading
    pass

def calculate_average_grade(students):
    """Calculate average grade from student data."""
    # TODO: Implement average calculation
    pass

def count_math_students(students):
    """Count students in Math."""
    # TODO: Implement counting
    pass

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
EOF

echo "create src/data_analysis.py with initialized functions"

cat > src/data_analysis_functions.py << 'EOF'
"""Advanced student data analysis script."""

def load_data(filename):
    """Check if file is CSV"""
    # TODO: Implement file checker
    pass

def load_csv(filename):
    """Load student data from CSV file."""
    # TODO: Implement csv file reader
    pass

def analyze_data(students):
    """Calculate multiple statistics"""
    # TODO: Implement statistic dictionary
    pass

def analyze_grade_distribution(students):
    """Count grades by letter grading"""
    # TODO: Implement counting of letter grades
    pass

def save_results(results, filename):
    """Generate formatted report."""
    # TODO: Implement report generation
    pass

def main():
    """Main execution function."""
    # TODO: Orchestrate the analysis
    pass

if __name__ == "__main__":
    main()
EOF

echo "create src/data_analysis_functions.py with initialized functions"


cat > .gitignore << 'EOF'
# Python cache files
__pycache__/
*.pyc
EOF

echo "created .gitignore"

cat > requirements.txt << 'EOF'
EOF

echo "no external packages required, created requirements.txt"
