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

print(stud1 > stud2)
print(stud2 > stud1)


#  эксперименты
students = [
    ['Андрей', 'Андреев', 'male'],
    ['Сергей', 'Сергеев', 'male'],
    ['Петр', 'Петров', 'male']
]

# print(lect1.grades)
# print(lect2.grades)
# print(lect1.grades['Python'])
# exit()ч
rprint("Сравниваю лекторов")
# print(lect1.name)
lect1 > lect2

obj_stud = dict()
for i in range(len(students)):
    obj_stud.update({'stud'+str(i+1): Student(students[i][0], students[i][1], students[i][2])})
# print(obj_stud['stud1'].name)
