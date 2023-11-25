class Student:
        school_name="ABC school"
        def __init__(self,name,age):
            self.name=name
            self.age=age
s1=Student("Harry",20)
print("student:",s1.name,s1.age)
print("school nmae:",Student.school_name)
s1.name="jeesa"
s1.age=19
print("student name:",s1.name,s1.age)
Student.school_name="xyz school"
print("school nmae:",Student.school_name)

