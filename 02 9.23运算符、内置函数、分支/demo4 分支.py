# score=int(input("enter your test score"))
# if score>=60:
#     print('pass')
# else:
#     print('fail')

# num=int(input("enter your number"))
# if num%2==0:
#     print('even')
# else:
#     print('odd number')

# year=int(input("enter year"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(year,"is a leap year")
# else:
#     print(year,"is a normal year")

# score=int(input('enter score '))
# if score==100:
#     print('full marks')
# elif 100>score>=90:
#     print(score,'is outstanding')
# elif 90>score>=80:
#     print(score,'is good')
# elif 80>score>=70:
#     print(score,'is fair')
# elif 70>score>=60:
#     print(score,'is pass')
# elif 60>score>=0:
#     print(score,'is fail')
# else:
#     print('this score is out of range')

# age=int(input('enter age \n'))
# if 0<=age<6:
#     print(age,'is infancy')
# elif 6<=age<20:
#     print(age,'is childhood')
# elif 20<=age<150:
#     print(age,'is adulthood')
# else :
#     print('maybe this creature is not human')

n = 1
# 编写循环代码
while n <= 10:
    # 循环体打印数字
    print(n , end=', ')
    # 循环变量改变
    n += 1
else:
    print(f'{n} 不在1～10之间')