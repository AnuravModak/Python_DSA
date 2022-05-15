class student:
    def __init__(self,sno,sname,cgpa):
        self.sno=sno
        self.sname=sname
        self.cgpa=cgpa
class Class:
    def __init__(self):
        self.students=[]

    def add_stduents(self,student_details):
        self.students.append(student_details)
    def sort_students_on_cgpa(self):
        self.students.sort(key=lambda i:i.cgpa,reverse=True)
        return self.students

c1=Class()
c1.add_stduents(student(1,"Anurav",8.1))
c1.add_stduents(student(11, "Amit", 6.1))
c1.add_stduents(student(12, "Rajesh", 8.7))
c1.add_stduents(student(13, "Varun", 9.1))
y=c1.sort_students_on_cgpa()
for i in y:
    print(i.cgpa,i.sname,i.sno)
# if __name__ == '__main__':
#     c1=Class()
#     c1.add_stduents(student(1,"Anurav",8.1))
#     c1.add_stduents(student(11, "Amit", 6.1))
#     c1.add_stduents(student(12, "Rajesh", 8.7))
#     c1.add_stduents(student(13, "Varun", 9.1))
#     y=c1.sort_students_on_cgpa()
#     for i in y:
#         print(i.cgpa,i.sname,i.sno)

