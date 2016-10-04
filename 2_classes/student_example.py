# coding=utf-8

class Human:
    city = 'Хабаровск'
    name = surname = None

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return '{name} {surname}'.format(name=self.name, surname=self.surname)

    @staticmethod
    def get_city():
        return Human.city

    def __eq__(self, other):
        return False


# vasya = Human('Вася', "Пупкин")
# Human.get_city()
# print(Human.fullname())


class Student(Human):
    def __init__(self, name, surname, course, speciality):
        super(Student, self).__init__(name, surname)
        self.course = course
        self.speciality = speciality

    def get_speciality(self):
        return self.speciality or 'Специальность не указана'


class LazyMan(Human):
    lazyness = 95


class Worker(Student, LazyMan):
    """
    класс
    ого
    работника
    """
    lazyness = 15

    def get_hours(self):
        result = None
        if 1:
            pass
        elif 2 :
            pass



Worker.__get_private_info = None

print(Worker.__get_private_info)
student_katya = Student('Катя', "Иванова", 4, 'Marketing')
