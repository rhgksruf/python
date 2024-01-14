# # 학생 관리 시스템의 학생 클래스 만들기 이름 나이 전공 듣고있느 ㄴ수업
# class Student:
#     def __init__(self,a,b,c,):
#         self.name = a
#         self.grade = b
#         self.major = c
#         self.courses = []
#
#     def enroll_courses(self,course):
#         if len(self.courses) < 5:
#             self.courses.append(course)
#         else:
#             print('수업 듣는 과목이 너무 많습니다')
#
#
#     def cancel_course(self):
#         if len(self.courses) == 0:
#             print('과목이 없습니다. 뺄 수가 없어요')
#         else:
#             for index,item in enumerate(self.courses):
#                 print(f"{index}. {item}")
#             removeTarget = int(input("빼고 싶은 과목의 번호를 선택:"))
#             del self.courses[removeTarget]
#
#     def informate(self):
#         print(f"학생 이름:{self.name} 학년:{self.grade} 전공:{self.major}")
#         print("학생의 수업리스트:")
#         for i in self.courses:
#             print(f"{i}")
#
# kim = Student('김주영','3','철학과')
# kim.enroll_courses('철학의 이해')
# kim.enroll_courses('철학의 쓸모')
# kim.informate()



class Circle:
    def __init__(self,x):
        self.radius = x

    def circle_one(self):
        print(f"원의 넓이는 {self.radius ** 2 * 3.14}")
    def round(self):
        print(f"원의 둘레는 {self.radius*2*3.14}")

a = Circle(5)
a.circle_one()
a.round()
b = Circle(7)
b.circle_one()
b.round()

