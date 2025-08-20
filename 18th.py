# positive negitive or zero
# def positive_negative_zero(num1):
#     print('zero') if num1==0 else print('positive') if num1>0 else print('negative') 
# positive_negative_zero(-2)
# positive_negative_zero(0)
# positive_negative_zero(345678)
# # o/p:
# # negative
# # zero
# # positive

# # odd or even
# def odd_even(num1):
#     print('even') if num1 % 2 ==0 else print('odd')
# odd_even(3)
# odd_even(24)
# o/p:
# odd
# even


# #calculate age
def vote(age):
    return True if age>=18 else False
print(vote(20))
print(vote(17))

# #check nu1 is positive or negitive
# def positive_negitive(num1):
#     print('true') if num1>0 else print('negative')    
# (positive_negitive(num1=40))

# #check num1 or num2 is greater
# def greater_less_equal(num1,num2):
#     print(num1) if num1>num2 else print(num2) if num2>num1 else print('equal')
    
# greater_less_equal(20,20)
# greater_less_equal(30,20)


# #check pass or fail
# def pass_fail(num1):
#     print('pass') if num1>40 else print('fail')
    
# pass_fail(39)
# pass_fail(45)


# #check days on numbers
# def days(num1):
#     if num1==1:
#         print('monday')
#     elif num1==2:
#         print('tuesday')
#     elif num1==3:
#         print('wednesday')
#     elif num1==4:
#         print('thursday')
#     elif num1==5:
#         print('friday')
#     elif num1==6:
#         print('saturday')
#     elif num1==7:
#         print('sunday')   
#     else:
#         print('invalid') 
        
# days(2)

# #operations upon giving operators
# def calculate(op,num1,num2):
#     if op == '+':
#         return num1+num2
#     elif op=='-':
#         return num1-num2
#     elif op=='*':
#         return num1*num2
#     elif op=='/':
#         return num1/num2 if num2>0 else 'Invalid'
#     else:
#         return 'invalid operator'
# op=input('enter the operator:')
# num1=float(input('enter num1:'))
# num2=float(input('enter num2:'))

# print(calculate(op,num1,num2))

# #display moths 
# def months(num1):
#     if num1==1:
#         print('january')
#     elif num1==2:
#         print('Febraury')
#     elif num1==3:
#         print('March')
#     elif num1==4:
#         print('April')
#     elif num1==5:
#         print('May')
#     elif num1==6:
#         print('June')
#     elif num1==7:
#         print('July')
#     elif num1==8:
#         print('August')
#     elif num1==9:
#         print('september')
#     elif num1==10:
#         print('october')
#     elif num1==11:
#         print('november')
#     elif num1==12:
#         print('December')
#     else:
#         print('invalid')
        
# months(2)

# greatest of 3 numbers
# def greatest_number(num1,num2,num3):
#     if num1 > num2 and num1 > num3 :
#         print(num1)
#     elif num2 > num3 and num2 > num1:
#         print(num2)
#     else:
#         print(num3)

# greatest_number(3,4,1)
# greatest_number(100,99,98)
# greatest_number(98,99,100)

# leap year
# def leap_year(num1):
#     if num1 % 400 == 0 or num1 % 100 != 0 and num1 % 4 ==0:
#         print('leap year')
#     else:
#         print('not a leap year')
        
#     print('leap') if num1 % 400 ==0 or num1 % 100 !=0 and num1 % 4 ==0 else print('not a leap')

# leap_year(2004)
# #student grade
# def grade(marks):
#     if marks>90:
#         print('Grade A')
#     elif marks > 80:
#         print('Grade B')
#     elif marks > 70:
#         print('Grade C')
#     else:
#         print('Fail')
        
# grade(98)
# grade(69)

# #traingle
# def triangle(side1,side2,side3):
#     if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
#         print('traiangle is possible')
#         if side1 == side2 or side1 == side3 or side2 == side3 or side2 == side1 :
#             print('isolated traingle')
#         elif side1 == side2== side3:
#             print('equlaterial triangle')
#         elif side1 != side2 != side3:
#             print('scalar traingle')
#     elif (side1**2 + side2**2 == side3**2) or (side2**2 + side3**2 == side1**2) or (side1**2 + side3**2 == side2**2):
#         print("right angled triangle")
#     else:
#         print('not possible')
    

# triangle(3,4,5)
# triangle(25,45,32)

# #1 to 100 numbers
# for i in range (1,101):
#     print(i,end=',')

# sum of natural numbers
# n=int(input('enter the number:'))
# summ=0
# for i in range(1,n):
#     summ=n*(n+1)/2
# print(summ)

# even numbers from 1 to 50
# for i in range(1,51):
#     while i % 2 ==0:
#         print(i,end=',')
#         i+=1

# table of a number
# num1=int(input('enter the number:'))
# for i in range(1,21):
#     print(num1,"x",i,"=",num1*i)