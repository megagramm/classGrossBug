from classGrossbuh import *
from service import *

rprint("Создали студентов")

stud1 = Student('Иван', 'Иванов', 'male')
stud1.courses_in_progress += ['Python', 'Java', 'Git']
stud1.finished_courses += ('Введение в программирование', 'Английский для программистов')

stud2 = Student('Пётр', 'Петров', 'male')
stud2.courses_in_progress += ['Python', 'Git']
stud2.finished_courses.append('Введение в программирование')

stud3 = Student('Татьяна', 'Татьянова', 'female')
stud3.courses_in_progress += ['Java']
stud3.finished_courses += ("Введение в программирование", "Git")

print(stud1, stud2, stud3, sep="\n")


rprint('Создали Лекторов')
lect1 = Lecturer('Виктор', 'Викторов')
lect1.courses_attached += ['Python', 'Git', 'Введение в программирование']

lect2 = Lecturer('Марина', 'Мариновна')
lect2.courses_attached += ['Java', 'Git', 'Введение в программирование']

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


rprint("Студенты оценили лекторов")
stud1.rate_lecturer(lect1, 'Python', 8)
stud2.rate_lecturer(lect1, 'Python', 9)
stud1.rate_lecturer(lect1, 'Java', 10)
stud2.rate_lecturer(lect1, 'Java', 9)
stud1.rate_lecturer(lect1, 'Git', 5)
stud2.rate_lecturer(lect1, 'Git', 4)

stud1.rate_lecturer(lect2, 'Python', 1)
stud2.rate_lecturer(lect2, 'Python', 1)
stud1.rate_lecturer(lect2, 'Java', 7)
stud2.rate_lecturer(lect2, 'Java', 9)
stud1.rate_lecturer(lect2, 'Git', 8)
stud2.rate_lecturer(lect2, 'Git', 10)

print(lect1, lect2, sep="\n")

rprint('Выводим студентов')
print(stud1, stud2, stud3, sep="\n")



#  эксперименты


rprint("Сравниваю лекторов")

lect1 > lect2

rprint("Сравниваю студентов")
stud1 > stud2

# print(123)
# obj_stud = dict()
# for i in range(len(students)):
#     obj_stud.update({'stud'+str(i+1): Student(students[i][0], students[i][1], students[i][2])})
# print(obj_stud['stud1'].name)

# 4
"""
1. для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса 
(в качестве аргументов принимаем список студентов и название курса);
2. для подсчета средней оценки за лекции всех лекторов в рамках курса 
(в качестве аргумента принимаем список лекторов и название курса).
"""


def students_average_grades_by_course(students, course):
    av = []
    for student in students:
        av.append(mean(student.grades[course]))
    return round(mean(av), 2)


def lecturers_average_grades_by_course(lecturers, course):
    av = []
    for lecturer in lecturers:
        av.append(mean(lecturer.grades[course]))
    return round(mean(av), 2)


students = [stud1, stud2]
course = "Python"
print(f'Средняя оценка у студентов по {course} = {students_average_grades_by_course(students, course)}')
lecturers = [lect1, lect2]
course = "Git"
print(f'Средняя оценка у лекторов по {course} = {lecturers_average_grades_by_course(lecturers, course)}')
