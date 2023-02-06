

class Course:
    def __init__(self, name, start_date, number_of_lectures, teacher):
        self.name = name
        self.start_date = start_date
        self.number_of_lectures = number_of_lectures
        self.teacher = teacher
        self.students = []
        self.home_tasks = []
        self.lectures = [Lecture(f'Lecture {i-1}', i-1, teacher) for i in range(1, self.number_of_lectures+1)]

    def __str__(self):
        return f'{self.name} ({self.start_date})'

    # додати студента до  self.students = [] через enroll
    def enrolled_by(self):
        return self.students

    def get_lecture(self, x):
        if len(self.lectures) > 16:
            raise AssertionError('error')
        for i in range(1, len(self.lectures)+1):
            if i == x:
                _ = self.lectures[i]
                return _

    @property
    def lecture_name(self):
        return self.name

    @lecture_name.setter
    def lecture_name(self, value):
        self.name = value

    def get_homeworks(self):
        ht = [self.lectures[i].home_w for i in range(0, len(self.lectures))
              if self.lectures[i].home_w is not None]
        return ht


class Lecture:
    def __init__(self, name, number, teacher):  # teacher == Teacher
        self.name = name
        self.number = number
        self.teacher = teacher
        teacher.add_lecture(self)
        self.home_w = None

    def get_homework(self):
        return self.home_w

    def set_homework(self, new_homework):  # Homework
        self.home_w = new_homework

    # def ht(self):  # Course
    #     return Course.self.home_w.append(self)


class Homework:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    # студентів, що виконали домашнє завдання.

class Teacher:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.list = []

    def __str__(self):
        return f'Teacher: {self.first_name} {self.last_name}'

    def teaching_lectures(self):
        return self.list

    def add_lecture(self, lecture: Lecture):
        return self.list.append(lecture)


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.assigned_homeworks = []

    def enroll(self, course):  # Course
        return course.students.append(self)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

    # назначені домашні завдання.
    def add_homework(self):
        print(Homework('Functions', 'what to do here'))
        return self.assigned_homeworks.append(Homework('Functions', 'what to do here'))

    # # назначені домашні завдання.
    # def add_homework1(self):
    #     Course.get_homeworks()
    #     # ht = [Course.lectures[i].home_w for i in range(0, len(Course.lectures))
    #     #       if Course.lectures[i].home_w is not None]
    #     return ht



if __name__ == '__main__':

    main_teacher = Teacher('Thomas', 'Anderson')
    assert str(main_teacher) == f'Teacher: {main_teacher.first_name} {main_teacher.last_name}'

    python_basic = Course('Python basic', '31.10.2022', 16, main_teacher)

    assert len(python_basic.lectures) == python_basic.number_of_lectures
    assert str(python_basic) == 'Python basic (31.10.2022)'

    assert python_basic.teacher == main_teacher
    assert python_basic.enrolled_by() == []
    assert main_teacher.teaching_lectures() == python_basic.lectures  # !!!!!!

    students = [Student('John', 'Doe'), Student('Jane', 'Doe')]
    for student in students:
        assert str(student) == f'Student: {student.first_name} {student.last_name}'
        student.enroll(python_basic)

    assert python_basic.enrolled_by() == students # список студентів що записалися

    third_lecture = python_basic.get_lecture(3)

    assert third_lecture.name == 'Lecture 3'
    assert third_lecture.number == 3
    assert third_lecture.teacher == main_teacher
    try:
        python_basic.get_lecture(17)
    except AssertionError as error:
        assert error.args == ('Invalid lecture number',)

    third_lecture.name = 'Logic separation. Functions'
    assert third_lecture.name == 'Logic separation. Functions'

    assert python_basic.get_homeworks() == []
    assert third_lecture.get_homework() is None
    functions_homework = Homework('Functions', 'what to do here')
    assert str(functions_homework) == 'Functions: what to do here'
    third_lecture.set_homework(functions_homework)

    assert python_basic.get_homeworks() == [functions_homework]
    assert third_lecture.get_homework() == functions_homework

    # for student in students:
    #     assert student.assigned_homeworks == [functions_homework]
    #
    # assert main_teacher.homeworks_to_check == []
    # students[0].do_homework(functions_homework)
    # assert students[0].assigned_homeworks == []
    # assert students[1].assigned_homeworks == [functions_homework]

    # assert functions_homework.done_by() == {students[0]: None}
    # assert main_teacher.homeworks_to_check == [functions_homework]

    # for mark in (-1, 101):
    #     try:
    #         main_teacher.check_homework(functions_homework, students[0], mark)
    #     except AssertionError as error:
    #         assert error.args == ('Invalid mark',)
    #
    # main_teacher.check_homework(functions_homework, students[0], 100)
    # assert main_teacher.homeworks_to_check == []
    # assert functions_homework.done_by() == {students[0]: 100}
    #
    # try:
    #     main_teacher.check_homework(functions_homework, students[0], 100)
    # except ValueError as error:
    #     assert error.args == ('You already checked that homework',)
    #
    # try:
    #     main_teacher.check_homework(functions_homework, students[1], 100)
    # except ValueError as error:
    #     assert error.args == ('Student never did that homework',)
    #
    # substitute_teacher = Teacher('Agent', 'Smith')
    # fourth_lecture = python_basic.get_lecture(4)
    # assert fourth_lecture.teacher == main_teacher
    #
    # fourth_lecture.new_teacher(substitute_teacher)
    # assert fourth_lecture.teacher == substitute_teacher # зміна вчителя
    # assert len(main_teacher.teaching_lectures()) == python_basic.number_of_lectures - 1  # мінус для основного
    # assert substitute_teacher.teaching_lectures() == [fourth_lecture] # додалась +1 лекція для змінного
    # assert substitute_teacher.homeworks_to_check == []
