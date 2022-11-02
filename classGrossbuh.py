from statistics import mean

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

        if len(self.grades) > 0:
            ret += f'Средняя оценка за домашние задания: {self.average_grades()}\n'
        ret += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        ret += f'Заверешенные курсы: {", ".join(self.finished_courses)}\n'
        return ret

    def average_grades(self):
        """Average of all grades"""
        for course, grades in self.grades.items():
            self.average_grades_by_course.append(round(mean(grades), 2))
            # self.average_grades_by_course.append(round(sum(grades) / len(grades), 2))
        return round(mean(self.average_grades_by_course), 2)

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

    def av(self, student, course):
        """Считаем среднии оценки по курсу"""
        if isinstance(student, Student) and course in student.grades:
            return round(mean(student.grades[course]), 2)

    def __lt__(self, other):
        if isinstance(other, Student):
            print(f"Сравнение студентов: {other.name} {other.surname} и {self.name} {self.surname}")
            for other_course, other_values in other.grades.items():
                for self_course, self_values in self.grades.items():
                    if other_course == self_course:
                        if self.av(other, other_course) > self.av(self, self_course):
                            print(f'По {other_course} {other.name} {other.surname} лучше {self.name} {self.surname}')
                        else:
                            print(f'По {other_course} {self.name} {self.surname} лучше {other.name} {other.surname}')
        else:
            return 'this is not a Student'


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

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            print(f"Сравнение лекторов: {other.name} {other.surname} и {self.name} {self.surname}")
            for other_course, other_values in other.grades.items():
                for self_course, self_values in self.grades.items():
                    if other_course == self_course:
                        if self.average_grades(other, other_course) > self.average_grades(self, self_course):
                            print(f'По {other_course} {other.name} {other.surname} лучше {self.name} {self.surname}')
                        else:
                            print(f'По {other_course} {self.name} {self.surname} лучше {other.name} {other.surname}')
        else:
            return 'this is not a Lecturer'

    def average_grades(self, lecturer, course):
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            return round(mean(lecturer.grades[course]), 2)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка: Или ревьюер не из того потока, или студент не учится на этом курсе')
