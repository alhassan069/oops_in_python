from collections import defaultdict


class GradeManager:
    def __init__(self) -> None:
        """
        Initialize the grade manager with appropriate defaultdict structures
        Use defaultdict top avoid key existence checks
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
        print(self.grades)
        total = 0
        highest = 0
        lowest = 0
        marks = []

        for student_name in self.grades:
            for marks_tuple in self.grades[student_name]:
                if marks_tuple[0] == subject:
                    marks.append(marks_tuple[1])
        marks = marks.sort()
        print(marks)
        return {'average': 0.00, 'highest': 0.00, 'lowest': 0.00, 'student_count': 0}

    def get_top_students(self,n=3) -> list:
        """Get top N students based on their overall grade"""
        return [('student_name', 'average_grade')]

    def get_failing_students(self, passing_grade=60) -> list:
        """Get students who are failing (average below passing grade)"""
        return [('student_name', 'average_grade')]



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
print("Math statistics:", manager.get_subject_statistics("Math"))
# print("Top 3 students:", manager.get_top_students(3))
# print("Failing students:", manager.get_failing_students(75))
