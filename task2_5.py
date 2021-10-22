from operator import methodcaller
class Group:
    surname_name=[]
    def __init__(self,*students):
        if not all(isinstance(student,Student) for student in students):
            raise TypeError
        if not len(students)<=20:
            raise ValueError
        for student in students:
            if f'{student.surname} {student.name}' in Group.surname_name:
                raise ValueError
            Group.surname_name.append(f'{student.surname} {student.name}')
        self.students=students            
    def highest_score(self):
        top=sorted(self.students,key=methodcaller('average_score'),reverse=True)
        return top[:5]


class Student:
    def __init__(self,name,surname,record_book,grades):
        self.name=name
        self.surname=surname
        self.record_book=record_book
        self.grades=grades
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise TypeError
        if not name.isalpha():
            raise ValueError
        self.__name=name
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self,surname):
        if not isinstance(surname,str):
            raise TypeError
        if not surname.isalpha():
            raise ValueError
        self.__surname=surname
    @property
    def record_book(self):
        return self.__record_book
    @record_book.setter
    def record_book(self,record_book):
        if not isinstance(record_book,int):
            raise TypeError
        if not record_book>0:
            raise ValueError
        self.__record_book=record_book
    @property
    def grades(self):
        return self.__grades
    @grades.setter
    def grades(self,grades):
        if not isinstance(grades,list):
            raise TypeError
        if not all(0<=grade<=100 for grade in grades):
            raise ValueError
        self.__grades=grades
    def average_score(self):
        return sum(self.grades)/len(self.grades)
    def __str__(self):
        return f'Surname:{self.surname}, Record book number:{self.record_book}, grade:{self.average_score()}'
try:
    one=Student("Valera","Bubkinov",1,[11,11,98])
    two=Student("John","Spilberg",2,[1,1,1])
    three=Student("Ivan","Marmeladov",3,[3,3,3])
    four=Student("Dmytro","Vodoleyv",4,[1,1,1])
    five=Student("Arseniy","Ivanov",5,[1,1,1])
    six=Student("Vasya","Pupkin",6,[1,1,1])
    seven=Student("Kolya","Morgun",7,[1,1,1])
    eight=Student("Misha","Berezhko",8,[1,1,1])
    nine=Student("Sasha","Fedchenko",9,[1,1,1])
    ten=Student("Pavlo","Nedashkivskiy",10,[1,1,1])
    ti_01=Group(one,two,three,four,five,six,seven,eight,nine,ten)
    for student in ti_01.highest_score():
        print(student)
except ValueError:
    print("Enter correct values")
except NameError:
    print("Name error")
except TypeError:
    print("Type error")