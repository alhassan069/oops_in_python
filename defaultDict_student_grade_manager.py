from collections import defaultdict


class GradeManager:
    def __init__(self) -> None:
        """
        Initialize the grade manager with appropriate defaultdict structures
        Use defaultdict to avoid key existence checks
        """

        self.grades = defaultdict(list)
        # pass

    def add_grade(self, student_name, subject, grade:float) -> None:
        """
        Add a grade for student in a specific subject
        Args:
            student_name (str): Name of the sudent
            subject (str): Subject name
            grade (float): Grade value (0-100)
        """
        # pass
        self.grades[student_name].append((subject,grade))

    def get_student_average(self, student_name) -> float:
        total_marks = 0
        total_subjects = 0
        student_numbers = self.grades[student_name]
        for i in range(len(student_numbers)):
            total_subjects += 1
            total_marks = total_marks + student_numbers[i][1]
        return total_marks/total_subjects

    def get_subject_statistics(self, subject) -> dict :
        total = 0
        highest = 0
        lowest = 0
        marks = []

        for student_name in self.grades:
            for (sub, grd) in self.grades[student_name]:
                if sub == subject:
                    total += grd
                    marks.append(grd)
        marks.sort()
        return {'average': total/len(marks), 'highest': marks[-1], 'lowest': marks[0], 'student_count': len(marks)}

    def get_top_students(self,n=3) -> list:
        """Get top N students based on their overall grade"""
        top_n_students = []
        
        for name, grades in self.grades.items():
            total_marks = 0
            subjects = len(grades)
            for (subject, mark) in grades:
                total_marks = total_marks + mark
            
            avg = total_marks/subjects
            top_n_students.append((name, round(avg,2)))
        
        top_n_students.sort(key= lambda student: student[1], reverse=True)

        return top_n_students[0:n]

    def get_failing_students(self, passing_grade=60) -> list:
        """Get students who are failing (average below passing grade)"""
        failing_students = []
        
        for name, grades in self.grades.items():
            total_marks = 0
            subjects = len(grades)
            for (subject, mark) in grades:
                total_marks = total_marks + mark
            
            avg = round(total_marks/subjects,2)
            if avg < passing_grade:
                failing_students.append((name, round(avg,2)))

        return failing_students


manager = GradeManager()

grades_data = [
    ("Alice", "Math", 85), ("Alice", "Science", 92), ("Alice", "English", 78),
    ("Bob", "Math", 75), ("Bob", "Science", 68), ("Bob", "English", 82),
    ("Charlie", "Math", 95), ("Charlie", "Science", 88), ("Charlie", "History", 91),
    ("Diana", "Math", 55), ("Diana", "Science", 62), ("Diana", "English", 70),
    ("Eve", "Math", 88), ("Eve", "Science", 94), ("Eve", "English", 86), ("Eve", "History", 89)
]

for student, subject, grade in grades_data:
    manager.add_grade(student, subject, grade)

# Test all methods
# print("Alice's average:", manager.get_student_average("Alice"))
# print("Math statistics:", manager.get_subject_statistics("Math"))
# print("Top 3 students:", manager.get_top_students(3))
print("Failing students:", manager.get_failing_students(75))
