from classGrossbuh import *
from service import *

rprint("Создали студентов")

stud1 = Student('Иван', 'Иванов', 'male')
stud1.courses_in_progress += ['Python', 'Java', 'Git']
stud1.finished_courses += ('Введение в программирование', 'Английский для программистов')

stud2 = Student('Пётр', 'Петров', 'male')
stud2.courses_in_progress += ['Python', 'Git']
stud2.finished_courses.append('Введение в программирование')

print(stud1, stud2, sep="\n")


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

print(rev1, rev2, sep="\n")

rprint('Ревьюеры оценили работы студентов')
rev1.rate_hw(stud1, 'Python', 1)
rev1.rate_hw(stud1, 'Python', 7)
rev1.rate_hw(stud1, 'Python', 9)
rev1.rate_hw(stud1, 'Python', 4)
rev1.rate_hw(stud1, 'Git', 10)
rev1.rate_hw(stud1, 'Git', 10)
rev1.rate_hw(stud1, 'Git', 9)

rev2.rate_hw(stud2, 'Python', 1)
rev2.rate_hw(stud2, 'Python', 10)
rev2.rate_hw(stud2, 'Python', 4)
rev2.rate_hw(stud2, 'Python', 7)


rprint("Студенты оценили лекции лекторов")
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

rprint('Выводим студентов')
print(stud1, stud2, sep="\n")

stud1 > stud2
stud2 > stud1

rprint('Выводим лекторов')
print(lect1, lect2, sep="\n")

rprint('Сравниваем лекторов')
lect1 > lect2
lect2 > lect1


rprint('Четвертое задание')


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


course = "Python"
print(f'Средняя оценка у студентов по {course} = {students_average_grades_by_course(Student.student_list, course)}')
course = "Git"
print(f'Средняя оценка у лекторов по {course} = {lecturers_average_grades_by_course(Lecturer.lecturer_list, course)}')
