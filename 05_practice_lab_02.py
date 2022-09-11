# a=input("Enter a string: ")
# b=""
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]
# print(b)

# a=input("Enter a string: ")
# b=input("Enter another string: ")
# c=b
# result=False
# while(c!=a):
#     k=c[0:1]
#     c=c[1:len(c)]
#     c+=k
#     if(c==a):
#         result=True
#     if(c==b):
#         break
# if(result):
#     print("yes")
# else:
#     print("no")

# import random
# a=int(input("Enter the length: "))
# c=""
# count=0
# while(count!=a):
#     b=random.randint(0,1)
#     c+=str(b)
#     count+=1
# print(c)

# a=input("Enter a string: ")
# b=""
# for i in range(0,len(a)):
#     if((ord(a[i])>64 and ord(a[i])<91) or (ord(a[i])>96 and ord(a[i])<123)):
#         b+=a[i]
# print(b)

# a=[(11,2,3,14),(13,5,22,10),(12,2,3,10)]
# b=[]
# length=len(a[0])
# for i in range(0,length):
#     sum=0
#     for j in range(0,len(a)):
#         sum+=a[j][i]
#     b.append(sum)
# b=tuple(b)
# print(b)

# a=[(11,2,3,14),(13,5,22,10),(12,2,3,10),(10,),(),()]
# b=len(a)
# c=[]
# print(b)
# for i in range(b):
#     if(len(a[i])!=0):
#         c.append(a[i])
# print(c)

# a=[10,15,23,48,[48,12],{12,45},(11,2,3,14),(13,5,22,10),(12,2,3,10),(10,),(),()]
# count=0
# for i in range(len(a)):
#     if(isinstance(a[i],tuple)==False):
#         count+=1
#     else:
#         break
# print(count)

# a=[[(9, 51), (7, 9)], [(11, 1), (22, 19)]]
# b=[]
# c=[]
# length=len(a[0][0])
# length1=len(a[0])
# length2=len(a)
# for i in range(length):
#     c=[]
#     for j in range(length2):
#         for k in range(length1):
#             c.append(a[j][k][i])
#     b.append(tuple(c))
#     print(b)

# a=[15,14,15,13,1,23,1]
# b={}
# for c in a:
#     h=b.get(c)
#     if(h==None):
#         b[c]=1
#     else:
#         b[c]=h+1
# for key, value in b.items():
#     if(value==1):
#         print(key)

# a=input("Enter a three digit number: ")
# d=[]
# c=a[2]
# b=a[1]
# a=a[0]
# d.append(a)
# d.append(b)
# d.append(c)
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if(i!=j and j!=k and k!=i):
#                 print(d[i],d[j],d[k])

# def printEven(a):
#     for i in a:
#         if(i%2==0):
#             print(i)
# a=[1,4,6,5,8,9]
# printEven(a)

# def checkPalindrome(a):
#     for c in range(int(len(a)/2)):
#         if(a[c]!=a[len(a)-1-c]):
#             print("It is not a palindrome")
#             break
#     else:
#         print("It is a palindrome")
# a=input("enter a string: ")
# checkPalindrome(a)

# def checkprime(a):
#     for j in range(2,a):
#         if(a%j==0):
#             print("It is not a prime number")
#             break
#     else:
#         print("It is a prime number")
# a=int(input("Enter a number: "))
# checkprime(a)


'''
# An athelete trainer wants to train an extra session for the best two students for 100m running having timing from 12 to 13 seconds. The number of students is N. And he is given an array P, which has N timing entries one for every athlete. The best two atheletes are the ones who have minimum difference in their timings. Output would be the athlete's with least timings and with min timing difference
athlete1=0
athlete2=0
a=[12.71, 12.70, 12.31, 12.56, 12.33, 12.81]
b=[0,0,0,0,0,0]
for i in range(6):
    b[i]=a[i]
b.sort()
print(b)
# print(a)
for i in range(6):
    if(a[i]==b[0]):
        athlete1=i
for i in range(6):
    if(a[i]==b[1]):
        athlete2=i
difference=a[athlete2]-a[athlete1]
print(athlete1,athlete2,difference)
'''
'''
# A DNA sequence has four characters/bases A,T,G and C. Find count of the substrings that start and end with the same base. Get the DNA string and base character from user
required =input("enter the string: ")
char=input("enter the required character: ")
count=0
for i in range(len(required)):
    if(required[i]==char):
        for j in range(i+1,len(required)):
            if(required[i]==required[j]):
                count+=1
print(count)
'''
'''
# The minimum attendance required for a training workshop is 75 percentage. The workshop is hosted for 20 days. Already N days have passed in the workshop (N<=20). A student wants to find how many days he should further attend the workshop to complete it successfully. He constructs a string as input to algorithm that has N bits indicating the attendance for the past N days. Bit 1 in the string is present and 0 is absent. Output he number of days he has to yet attend. If he cannot make it up, display "you are already very short of attendance".
s1=input("Enter the string: ")
count=0
length=len(s1)
for i in range(length):
    if s1[i]=='1':
        count+=1
result=15-count
if(result<=20-length):
    print(15-count)
else:
    print("you are already very short of attendance")
'''