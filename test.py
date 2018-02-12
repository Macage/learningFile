def count():
    fs = []
    for i in range(1,4):
        def f(j):
            def g():
                return j * j
            return g
        r = f(i)
        fs.append(i)
    return fs
#f1, f2, f3 = count()
#print(f1,f2,f3)
"""
class Person(object):
    pass

xiaoming = Person()
xiaoming.name = "Xiao Ming"
xiaoming.gender = "Male"
xiaoming.birth = "1990-1-1"
xiaohong = Person()
xiaohong.name = "Xiao Hong"
xiaohong.school = "No.1 high school"
xiaohong.grade = 2
print (xiaoming)
print ("\n")
print (xiaohong)
"""
"""
class Person(object):
    address = "Earth"
    def __init__(self,name,gender,birth,**kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k,v in kw.items():
            setattr(self,k,v)

xiaoming = Person('Xiao Ming','Male','2019-01-01',job="student")
print(xiaoming)
print(xiaoming.job)
print(xiaoming.name)
print(Person.address)
Person.address = "Shanghai"
p1 = Person("HuHu","Female","2010-1-1",school="shanghai university")
"""
class Person(object):
    address = "China"
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

class Student(Person):
    birth = "2018-1-1"
    def __init__(self,name,gender,school,score):
        super(Student,self).__init__(name,gender)
        self.school = school
        self.score = score

p1 = Student("xiaoming",'male','SHU',90)
print(p1)
Student.address
Person.birth

