# class V:
#     def __init__(self, name, age):
#         print('init')
#         self._age = age
#         self._name = name
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self, age):
#         print(f'set age. Age = {age}')
#         if age < 200:
#             self._age = age
#
#     def __repr__(self):
#         return f'class V: name = {self._name}, age = {self._age}'
#
#     age = property(get_age, set_age)
#
#
# alina = V('Alina', 455)
#
# print(alina)
#
# alina.age = 455
# print(alina)

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self._email = f'{self.first}.{self.last}@email.com'

    def get_email(self): # геттер
        return self._email

    def set_email(self, email): # сеттер
        self._email = email
        