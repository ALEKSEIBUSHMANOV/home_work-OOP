# создем класс Студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# создаем метод добавления курсов в завершенные курсы
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

# создаем метод выставления оценок лекторам за лекции
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# создаем перегрузку метода для вызова конкретных данных о студентах
    def __str__(self):
        return f'Имя: {self.name}'\
               f'\nФамилия: {self.surname}'\
               f'\nСредняя оценка за домашние задания: {self.average_rating_homework()}'\
               f'\nКурсы в процесс изучения: {",".join(self.courses_in_progress)}'\
               f'\nЗавершенные курсы: {",".join(self.finished_courses)}'

# создаем метод вычисления средней оценки за домашние задания
    def average_rating_homework(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        return sum(map(sum, self.grades.values())) / grades_count

# создаем метод для сравнения студентов
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
            return
        return self.average_rating_homework() < other.average_rating_homework()

# создаем класс преподаватлей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# создаем класс лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []

# создаем метод вычисления средней оценки за лекции
    def average_rating_lection(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        return sum(map(sum, self.grades.values())) / grades_count

# создаем метод перегрузки для вывода конкретных данных о лекторах
    def __str__(self):
        return f'Имя: {self.name}'\
               f'\nФамилия: {self.surname}'\
               f'\nСредняя оценка за лекции: {self.average_rating_lection()}'

# создаем метод для сравнения лекторов
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer")
            return
        return self.average_rating_lection() < other.average_rating_lection()

# создаем класс проверяющих преподавателей
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# создаем метод выставления оценок студентам за домашние задания
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# создаем метод перегрузки для вывода данных о проверяющих преподавателей
    def __str__(self):
        return f'Имя: {self.name}'f'\nФамилия: {self.surname}'


# создаем экземпляр класса Студент и добавляем ему курсы в процессе изучения и завершенные курсы
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python','Java']
best_student.add_courses('Введение в программирование')

# создаем экземпляр класса Студент и добавляем ему курсы в процессе изучения и завершенные курсы
best_student_second = Student('Pol', 'Jones', 'your_gender')
best_student_second.courses_in_progress += ['Python','Java']
best_student_second.add_courses('Гит')

# создаем экземпляр класса Лектор и добавляем ему курсы, которые он ведет
cool_lecturer = Lecturer('Kris', 'Simpson')
cool_lecturer.courses_attached += ['Python', 'Java']

# создаем экземпляр класса Лектор и добавляем ему курсы, которые он ведет
cool_lecturer_second = Lecturer('Jina', 'Smit')
cool_lecturer_second.courses_attached += ['Python', 'Java']

# создаем экземпляр класса Проверяющий и добавляем ему курсы, которые он ведет
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# создаем экземпляр класса Проверяющий и добавляем ему курсы, которые он ведет
cool_reviewer_second = Reviewer('Mark', 'Woutny')
cool_reviewer_second.courses_attached += ['Python']

# выставляем оценки студенту
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# выставляем оценки другому студенту
cool_reviewer.rate_hw(best_student_second, 'Python', 9)
cool_reviewer.rate_hw(best_student_second, 'Python', 8)
cool_reviewer.rate_hw(best_student_second, 'Python', 10)

# выставляем оценки лектору по курсу Ява
best_student.rate_hw(cool_lecturer, 'Java', 10)
best_student.rate_hw(cool_lecturer, 'Java', 10)
best_student.rate_hw(cool_lecturer, 'Java', 10)

# выставляем оценки второму лектору по курсу Ява
best_student.rate_hw(cool_lecturer_second, 'Java', 8)
best_student.rate_hw(cool_lecturer_second, 'Java', 9)
best_student.rate_hw(cool_lecturer_second, 'Java', 9)

# выставляем оценки лектору по курсу Питон
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 6)
best_student.rate_hw(cool_lecturer, 'Python', 5)

# выставляем оценки второму летору по курсу Питон
best_student.rate_hw(cool_lecturer_second, 'Python', 8)
best_student.rate_hw(cool_lecturer_second, 'Python', 9)
best_student.rate_hw(cool_lecturer_second, 'Python', 9)

# вывод информации
print(best_student.grades)
print(best_student_second.grades)
print(cool_lecturer.grades)
print(cool_lecturer_second.grades)
print(cool_reviewer)
print(cool_reviewer_second)
print(cool_lecturer)
print(cool_lecturer_second)
print(best_student)
print(best_student_second)
print(cool_lecturer < cool_lecturer_second)
print(best_student < best_student_second)

# создаем списки студентов и лекторов
student_list = [best_student, best_student_second]
lecturer_list = [cool_lecturer, cool_lecturer_second]

# создаем функцию выставления средней оценки студентам по одному курсу
def student_rating(student_list, course_name):

    sum_all = 0
    count_all = 0
    for stud in student_list:
        if course_name in stud.courses_in_progress:
            sum_all += stud.average_rating_homework()
            count_all += 1
        average_for_all = sum_all / count_all
    return average_for_all

# создаем функцию выставления средней оценки лекторам по одному курсу
def lecturer_rating(lecturer_list, course_name):

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if course_name in lect.courses_attached:
            sum_all += lect.average_rating_lection()
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# вывод информации о средних оценках студентов и лекторов за один курс
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")





