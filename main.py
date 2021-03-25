"""
Задание: Написать класс студент.
В студенте должны быть следующие поля:
1) Фио - DONE
 - Проверить, что в ФИО содержится более 3-х слов
 - Проверить, что ФИО - строка
2) Оценка - DONE
 - Проверить, что оценка - число
 - Проверить, что оценка находится в диапазоне от 1 до 12 (Включительно)
3) Почта - DONE
 - Проверить, что почта - строка
 - Сделать валидацию для почты (Можно использовать regex или метод find в Python)
4) Пароль - DONE
 - Проверить, что пароль - строка
 - Длина пароля >= 8
 - Есть спец. символ в пароле
 - Есть большая и маленькая буква
 - Есть число
5) Подтверждение пароля - DONE
 - Проверить, что значение - строка
 - Подтверждение пароля должно совпадать с паролем
6) Посещаемость пар - DONE
 - Проверить, что значение - число
 - Посещаемость должна задаваться в процентах, в диапазоне от 0 до 100%
Все поля в классе должны быть реализованы через property
В качестве выполненного ДЗ отправить ссылку на репозиторий на GitHub
"""
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
