from operator import methodcaller
class Group:
    def __init__(self,*students):
        if all(isinstance(student,Student) for student in students):
            if len(students)<=20:
                self.students=students
            else:
                raise ValueError
        else:
            raise TypeError
    def highest_score(self):
        top=sorted(self.students,key=methodcaller('average_score'),reverse=True)
        return top[:5]


class Student:
    surname_name=[]
    def __init__(self,name,surname,record_book,grades):
        if type(name)==str and type(surname)==str and type(record_book)==int and type(grades)==list:
            if name.isalpha() and surname.isalpha() and record_book>0 and all(0<=grade<=100 for grade in grades) and not f'{surname} {name}' in Student.surname_name:
                Student.surname_name.append(f'{surname} {name}')
                self.name=name
                self.surname=surname
                self.record_book=record_book
                self.grades=grades
            else:
                raise ValueError
        else:
            raise TypeError
    def average_score(self):
        return sum(self.grades)/len(self.grades)
    def __str__(self):
        return f'Surname:{self.surname}, Record book number:{self.record_book}, grade:{self.average_score()}'
try:
    one=Student("Valera","Bubkinov",1,[11,11,100])
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