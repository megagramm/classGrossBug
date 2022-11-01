from classGrossbuh import *
from service import *

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


