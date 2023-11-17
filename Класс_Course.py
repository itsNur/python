class Course():
    """описание курса"""
    def __init__(self, name, max_students) -> None:
        """атрибуты курса"""
        self.name = name
        self.students = []
        self.max_students = max_students
        self.teacher = ''
        

    def add_student(self, student_name):
        """добавляет студента на курс"""
        if len(self.students) <= self.max_students:
            self.students.append(student_name)
            print(f"{student_name} добавлен(a) на курс {self.name}")
        else:
            print("Курс уже полон, невозможно добавить")


    def remove_student(self, student_name):
        """удаляет студента"""
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} удален(a) из курса {self.name}")


    def get_student_list(self):
        """список студентов"""
        return self.students
    

    def set_teacher(self, teacher_name):
        """назначение преподавателя"""
        self.teacher = teacher_name
        print(f"Преподаватель {teacher_name} назначен(a) на курс {self.name}")

python_course = Course('Поколение Python', 10)
math_course = Course('Математика', 5)

python_course.set_teacher('Тимур')
python_course.set_teacher('Татьяна')

python_course.add_student('Нурсултан')
python_course.add_student('Нурислам')
python_course.add_student('Кундуз')
python_course.add_student('Асел')
python_course.add_student('Денис')
python_course.add_student('Алексей')
python_course.add_student('Комрон')
python_course.add_student('Барри')
python_course.add_student('Крис')
python_course.add_student('Анастасия')
python_course.add_student('Гулжан')
python_course.add_student('Вейн')

math_course.add_student('Нурсултан')
math_course.add_student('Нурислам')
math_course.add_student('Кундуз')
math_course.add_student('Асел')
math_course.add_student('Денис')
math_course.add_student('Алексей')
math_course.add_student('Комрон')

print("Список студентов на курсе 'Python': ", python_course.get_student_list())
print("Список студентов на курсе 'Математика': ", math_course.get_student_list())

python_course.remove_student('Нурсултан')
math_course.remove_student('Нурсултан')

print("Список студентов на курсе 'Python': ", python_course.get_student_list())
print("Список студентов на курсе 'Математика': ", math_course.get_student_list())