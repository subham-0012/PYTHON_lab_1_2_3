# question 1
# class SRMIST:
#     def __init__(self,school,dept1,dept2,dept3,dept4):
#         self.school=school
#         self.dept1=dept1
#         self.dept2=dept2
#         self.dept3=dept3
#         self.dept4=dept4
#     def newspec(self,spec):
#         self.spec=spec
#     def printall(self):
#         print(self.school)
#         print(self.dept1)
#         print(self.dept2)
#         print(self.dept3)
#         print(self.dept4)
#         print(self.spec)
# srmist=SRMIST("SCHOOL OF ENGINEERING","BLOCKCHAIN","AI-ML","CYBER-SEC","MECHANICAL")
# srmist.newspec("ELECTRICAL")
# srmist.printall()
# del srmist.dept1
# del srmist.dept2
# attrs= vars(srmist)
# print(attrs)

# question 2
# class CTECH:
#     pass
# class CINTEL:
#     pass
# class NWC:
#     pass
# class DSBS:
#     pass
# ctech1=CTECH()
# cintel1=CINTEL()
# nwc1=NWC()
# dsbs1=DSBS()
# print(isinstance(ctech1,CTECH))
# print(ctech1.__class__.__base__)

# question 3
# class Dept:
#     def __init__(self,dept=None):
#         if dept is None:
#             self.dept="SCO"
#         else:
#             self.dept=dept
#         print(f"The department is {self.dept}")
# dept1=Dept("dept")
# dept1=Dept()

# question 4
# class Rectangle:
#     def __init__(self,length=None,breadth=None):
#         if (length is None) and (breadth is None):
#             self.length=0
#             self.breadth=0
#         if length is None:
#             self.length=0
#             self.breadth=breadth
#         if breadth is None:
#             self.length=length
#             self.breadth=0
#         else:
#             self.length=length
#             self.breadth=breadth
#     # def __init__(self,length,breadth):
#     #     self.length=length
#     #     self.breadth=breadth
#     # def __init__(self,number):
#     #     self.length=number
#     #     self.breadth=number
#     def area(self):
#         print((self.length)*(self.breadth))
# rec1=Rectangle()
# rec2=Rectangle(2,3)
# rec3=Rectangle(3)
# print(rec1.area())
# print(rec2.area())
# print(rec3.area())

# question 4
# class Rectangle:
#     def _init_(self,length=0,breadth=0):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         print(self.length*self.breadth)
# t1=Rectangle()
# t1.area()
# t2=Rectangle(4,5)
# t2.area()
# t3=Rectangle(3,3)
# t3.area()

# question 5
# class PrintDT:
#     def python__data(self,list1=None):
#         if list1 is None:
#             list1=[]
#         print(list1)
#     # def python__data(self,tuple1=()):
#     #     if tuple1 is None:
#     #         tuple1=()
#     #     print(tuple1)
#     # def python__data(self,string1=""):
#     #     if string1 is None:
#     #         string1 =""
#     #     print(string1)
# d1=PrintDT()
# d2=PrintDT()
# d3=PrintDT()
# d1.python__data([1,2,3])
# d2.python__data((4,5,6))
# d3.python__data("7,8,9")

# question 6
# class Banks_SRMIST:
#     def __init__(self):
#         self.Balance=0
#     def getBalance(self):
#         print(self.Balance)
# class CUB(Banks_SRMIST):
#     def __init__(self,balance):
#         super().__init__()
#         self.Balance=balance
#     def getBalance(self):
#         print(self.Balance)
# class HDFC(Banks_SRMIST):
#     def __init__(self,balance):
#         super().__init__()
#         self.Balance=balance
#     def getBalance(self):
#         print(self.Balance)
# class Indian_Bank(Banks_SRMIST):
#     def __init__(self,balance):
#         super().__init__()
#         self.Balance=balance
#     def getBalance(self):
#         print(self.Balance)
# b2=CUB(15000)
# b2.getBalance()
# b3=HDFC(30000)
# b3.getBalance()
# b4=Indian_Bank(40000)
# b4.getBalance()

# question 7
# class Time:
#     def __init__(self,hours,minutes):
#         self.hours=hours
#         self.minutes=minutes
#     def addTime(self,other):
#         print(f"The sum time is {self.hours+other.hours}:{self.minutes+other.minutes}")
#     def displayTime(self):
#         print(f"The time is {self.hours}:{self.minutes}")
#     def displayMinutes(self):
#         print(f"The time in minutes is {self.hours*60 + self.minutes}")
# t1=Time(1,5)
# t2=Time(2,10)
# t1.addTime(t2)
# t1.displayTime()
# t2.displayMinutes()

# question 8
# class triangle:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.s=(self.a+self.b+self.c)/2
#     def perimeter(self):
#         print(self.a+self.b+self.c)
#     def area(self):
#         self.area=self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c)
#         print(self.area)
# t1=triangle(4,5,6)
# t1.perimeter()
# t1.area()