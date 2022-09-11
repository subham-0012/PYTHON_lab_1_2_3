# for i in range(1000,2001):
#     if (i%5==0 and i%8==0):
#         print(i)

# import random
# num1=random.randint(1,9)
# guess=0
# while(guess!=num1):
#     guess=int(input("Enter the number: "))

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print("\n")
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print("\n")

# a=input("Enter the string: ")
# b=""
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]
# print(b)

# rows=int(input("Enter the row: "))
# column=int(input("Enter the column: "))
# a=[]
# for i in range(rows):
#     temp=[]
#     for j in range(column):
#         temp.append(i*j)
#     a.append(temp)
# print(a)

# a=input("Enter the string")
# number=0
# char=0
# asscival=0
# for c in a:
#     if c=='0'or c=='1'or c=='2'or c=='3'or c=='4'or c=='5'or c=='6'or c=='7'or c=='8'or c=='9':
#         number+=1
#     c=c.lower()
#     asscival=ord(c)
#     if asscival>96 and asscival<123:
#         char+=1
# print(number)
# print(char)

# a=input("Enter the string")
# number=0
# Upperchar=0
# Lowerchar=0
# special=0
# for c in a:
#     if c=='0'or c=='1'or c=='2'or c=='3'or c=='4'or c=='5'or c=='6'or c=='7'or c=='8'or c=='9':
#         number+=1
#     asscival=ord(c)
#     if asscival>96 and asscival<123:
#         Lowerchar+=1
#     if asscival>64 and asscival<91:
#         Upperchar+=1
#     if (c=='$' or c=='#' or c=='@'):
#         special=1
# if(number>0 and Lowerchar>0 and Upperchar>0 and special>0):
#     print("Valid")       
# else:
#     print("Not valid")

# for i in range(100,401):
#     num=i
#     res=True
#     while(i>0):
#         if(i%2==0):
#             i=int(i/10)
#         else:
#             res=False
#             break
#     if(res):
#         print(num,", ",end="")

# a=input("Enter the month: ")
# if(a=="January" or a=="March" or a=="May" or a=="July" or a=="August" or a=="October" or a=="December"):
#     print(31)
# elif(a=='February'):
#     print("28/29")
# else:
#     print(30)

# def sum(a,b):
#     return a+b
# a=int(input("Enter the number: "))
# b=int(input("Enter the number: "))
# c=sum(a,b)
# if(c>104 and c<201):
#     print(200)
# else:
#     print(c)

# for i in range (9,0,-1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("\n")

# a=int(input("Enter the number: "))
# b=int(input("Enter the number: "))
# if(a==b or a-b==5 or a+b==5):
#     print("True")
# else:
#     print("False")

# a1=int(input("Enter x1: "))
# b1=int(input("Enter x2: "))
# a2=int(input("Enter y1: "))
# b2=int(input("Enter y2: "))
# print(((b1-a1)**2+(b2-a2)**2)**0.5)

# a=set()
# count=0
# b=0
# while(b!=-1):
#     b=int(input("Enter the number: "))
#     if(b!=-1):
#         a.add(b)
#         count+=1
# print(a)
# print(count)
# if(len(a)==count):
#     print("Yes")
# else:
#     print('No')

# x=[1,2,3,4,5,6,7,8,9,1]
# from matplotlib import pyplot as plt
# plt.hist(x)
# plt.show()

# a=input("Enter a string: ")
# b={}
# for c in a:
#     if b.get(c)!=None:
#         h=b.get(c)
#         b[c]=h+1
#     else:
#         b[c]=1
# print(b)

# a=int(input("Enter a number: "))
# while(a>0):
#     b=a
#     sum=0
#     while(b>0):
#         sum+=b%10
#         b=int(b/10)
#     a-=sum
#     print(a)
# print(a)

# a=input("Enter a number: ")
# b={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,}
# for c in a:
#     h=b.get(c)
#     b[c]=h+1
# keys=b.keys()
# for key in keys:
#     if(b[key]==0):
#         print(key)

# a=input("Enter a number: ")
# doit=True
# newmul=1
# newnum=0
# digitsum=''
# while(doit):
#     sum=0
#     for c in a:
#         c=int(c)
#         c*=newmul
#         newnum+=c
#         newmul*=10
#     sum=int(a)+newnum
#     print(sum)
#     digitsum=str(sum)
#     for i in range(int(len(digitsum)/2)):
#         if(digitsum[i]!=digitsum[len(digitsum)-1-i]):
#             break
#     else:
#         doit=False

# a=[1,2,3,4,5,6,7,8,9]
# sum=0
# print(len(a))
# for i in range(2,len(a)):
#     print(f"{a[i]} ",end="")
# print("\n")
# for i in range(len(a)-3,len(a)):
#     print(f"{a[i]} ",end="")
# print("\n")
# for i in range(len(a)):
#     sum+=a[i]
# print(sum)