from statistics import mean 


def rprint(string):
    """Формирует вывод текста на экран по правому краю"""
    eq_symb_len = 79-len(string)-1
    if eq_symb_len > 0:
        print(f'\n{"="*eq_symb_len} {string}\n')
    else:
        print(f'\n{string}\n')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades_by_course = list()

    def __str__(self):
        ret = f'Имя: {self.name}\nФамилия: {self.surname}\n'

        # считаем среднюю оценку по всем предметам
        if len(self.grades) > 0:
            ret += f'Средняя оценка за домашние задания: {self.average_grades()}\n'
        ret += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        ret += f'Заверешенные курсы: {", ".join(self.finished_courses)}\n'
        return ret

    def average_grades(self):
        print(self.average_grades_by_course)
        for course, grades in stud1.grades.items():
            # avg_by_course.append(round(mean(grades), 2))
            self.average_grades_by_course.append(round(sum(grades) / len(grades), 2))
            print(course)
        # print(self.average_grades_by_course)
        # return round(mean(self.avg_by_course),2)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('Ошибка: Либо студент не учится на этом курсе, либо лектор этот курс не ведет')

    def average_rate_hw(self):
        ...


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        ret = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        if hasattr(self, 'courses_attached') and len(self.courses_attached) > 0:
            ret += f'Ведёт следующие курсы: {",  ".join(self.courses_attached)}\n'
        return ret


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка: Или ревьюер не из того потока, или студент не учится на этом курсе')


rprint("Создали студентов")

stud1 = Student('Иван', 'Иванов', 'male')
stud1.courses_in_progress += ['Python', 'Java', 'Git']
stud1.finished_courses.append('Введение в программирование')
stud1.finished_courses.append('Английский для программистов')

stud2 = Student('Пётр', 'Петров', 'male')
stud2.courses_in_progress += ['Python', 'Git']
stud2.finished_courses.append('Введение в программирование')

stud3 = Student('Татьяна', 'Татьянова', 'female')
stud3.courses_in_progress += ['Java']
stud3.finished_courses.append("Введение в программирование")
stud3.finished_courses.append("Git")

print(stud1, stud2, stud3, sep="\n")



rprint('Создали Лекторов')
lect1 = Lecturer('Виктор', 'Викторов')
lect1.courses_attached += ['Python']
lect2 = Lecturer('Марина', 'Мариновна')
lect2.courses_attached += ['Java']
print(lect1, lect2, sep="\n")


rprint('Создали Ревьюеров')
rev1 = Reviewer('Альберт', 'Альбертов')
rev1.courses_attached += ['Python', 'Git']

rev2 = Reviewer('Илларион', 'Илларионов')
rev2.courses_attached += ['Python']

rev3 = Reviewer('Варлам', 'Варламов')
rev3.courses_attached += ['Java', ' Английский для программистов']

print(rev1, rev2, rev3, sep="\n")

rprint('Оценили работы студентов')
rev1.rate_hw(stud1, 'Python', 1)
rev1.rate_hw(stud1, 'Python', 7)
rev1.rate_hw(stud1, 'Python', 9)
rev1.rate_hw(stud1, 'Python', 4)
rev1.rate_hw(stud1, 'Git', 10)
rev1.rate_hw(stud1, 'Git', 10)
rev1.rate_hw(stud1, 'Git', 9)
rev3.rate_hw(stud1, 'Java', 10)
rev3.rate_hw(stud1, 'Java', 9)


rev2.rate_hw(stud2, 'Python', 1)
rev2.rate_hw(stud2, 'Python', 10)
rev2.rate_hw(stud2, 'Python', 4)
rev2.rate_hw(stud2, 'Python', 7)

rev3.rate_hw(stud3, 'Java', 10)
rev3.rate_hw(stud3, 'Java', 8)
rev3.rate_hw(stud3, 'Java', 4)
rev3.rate_hw(stud3, 'Java', 7)


# print(mean(stud1.grades))
# print(stud1.grades)

# exit()

rprint("Студенты оценили лекторов")
stud1.rate_lecturer(lect1, 'Python', 8)
stud2.rate_lecturer(lect1, 'Python', 9)
stud3.rate_lecturer(lect1, 'Python', 1)

stud1.rate_lecturer(lect2, 'Java', 1)
stud2.rate_lecturer(lect2, 'Java', 1)
stud3.rate_lecturer(lect2, 'Java', 10)

print(lect1, lect2, sep="\n")

rprint('Выводим студентов')
print(stud1, stud2, stud3, sep="\n")



#####
obj_stud = set()
for i in range(4):
    obj_stud.update({'stud'+str(i): []})

print(obj_stud)


