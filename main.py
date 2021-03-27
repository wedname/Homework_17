import re


class Student:

    def __init__(self, name: str, grade: int, email: str, password: str, confirm_password: str, attendance: float):
        self.name = name
        self.grade = grade
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.attendance = attendance

    regular_email = r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'
    email_regex = re.compile(regular_email)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.split()) < 3:
            self._name = value
        else:
            raise ValueError('name должен быть типом данных str и записан в формате Фамилия Имя Отчество.')

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if isinstance(value, int) and 1 <= value <= 12:
            self._grade = value
        else:
            raise ValueError('grade должен быть типом данных int.')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value, email_regex=email_regex):
        if isinstance(value, str) and email_regex.findall(value):
            self._email = value
        else:
            raise ValueError('В почте нет символов "@" и "." или email это не строка')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            has_upper = False
            has_lower = False
            has_digit = False
            has_spec_char = False
            if not len(value) > 8:
                raise ValueError("Пароль должен быть > 8 символов!")
            for char in value:
                if char.isupper():
                    has_upper = True
                if char.islower():
                    has_lower = True
                if char.isdigit():
                    has_digit = True
                if not char.isalnum():
                    has_spec_char = True
            if not has_upper:
                raise ValueError("В пароле должна быть минимум 1 большая буква!")
            if not has_lower:
                raise ValueError("В пароле должна быть минимум 1 маленькая буква!")
            if not has_digit:
                raise ValueError("В пароле должна быть минимум 1 цифра!")
            if not has_spec_char:
                raise ValueError("В пароле должен быть минимум 1 спецсимвол!")
            self._password = value
        else:
            raise ValueError('password не строка')

    @property
    def confirm_password(self):
        return self._confirm_password

    @confirm_password.setter
    def confirm_password(self, value):
        if isinstance(value, str):
            if value == self._password:
                self._confirm_password = value
            else:
                raise ValueError('Пароли не совпадают!')
        else:
            raise ValueError('confirm_password не строка')

    @property
    def attendance(self):
        return self._attendance

    @attendance.setter
    def attendance(self, value):
        if isinstance(value, float) and 0 <= value <= 100:
            self._attendance = value
        else:
            raise ValueError('name должен быть типом данных str и записан в формате Фамилия Имя Отчество.')


class StudentsGroup:

    def __init__(self):
        self.group = []

    def create_student(self, name, grade, email, password, confirm_password, attendance):
        try:
            student = Student(name, grade, email, password, confirm_password, attendance)
        except ValueError as e:
            print(e)
            return False
        if self.search_student(email) is None:
            self.group.append(student)
            return True
        else:
            print("Студент с таким email уже есть!")
            return False

    def search_student(self, mail):
        for i in range(len(self.group)):
            if mail == self.group[i]:
                return i
        print("Нет такого студента!")
        return None

    def edit_student(self, search_mail, name, grade, email, password, confirm_password, attendance):
        student_id = self.search_student(search_mail)
        if student_id is None:
            return False
        student = self.group[student_id]
        student.name = name
        student.grade = grade
        student.email = email
        student.password = password
        student.confirm_password = confirm_password
        student.attendance = attendance
        return True

    def show_students(self):
        return "\n".join([f"{x.name}\n" \
                          f"{x.grade}\n" \
                          f"{x.email}\n" \
                          f"{x.attendance}\n"
                          for x in self.group])

    def delete_students(self, search_mail):
        student = self.search_student(search_mail)
        if student is None:
            return False
        self.group.pop(student)
        return True

    def show_student(self, search_mail):
        student_id = self.search_student(search_mail)
        if student_id is None:
            return False
        student = self.group[student_id]
        return f"{student.name}" \
               f"{student.email}" \
               f"{student.grade}" \
               f"{student.attendance}" \


    def show_students_grades(self, n):
        filter_students_grades = []
        for i in range(len(self.group)):
            if self.group[i].grade >= n:
                filter_students_grades.append(f"{self.group[i].name}, {self.group[i].email}, {self.group[i].grade}, "
                                              f"{self.group[i].attendance}")
        if len(filter_students_grades) == 0:
            print("Студенты не найдены!")
        else:
            print(x for x in filter_students_grades)
            return filter_students_grades
