# import random
# a=random.randint(1,10)
# # random.seed(1)
# # print(a)

# #需求: 用户被要求输入一个年份和一个月份。程序会根据输入的年份和月份判断该月份有多少天
# year=int(input('enter year'))
# month=int(input('enter month'))
# month_names = [
#     "", "January", "February", "March", "April", "May", "June",
#     "July", "August", "September", "October", "November", "December"
# ]
# if month==2:
#     if year%4==0 and year%100!=0 or year%400==0:
#         print(f'{month_names[month]} has 29 days')
#     else:
#         print(f'{month_names[month]} has 28 days')
# else:
#     if month==1 or  month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#         print(f'{month_names[month]} has 31 days')
#     elif  month==4 or month==6 or month==9 or month==11:
#         print(f'{month_names[month]} has 30 days')
# #     else:
# #         print('this is earth')

# n=i=input('enter an integer')
# s=1
# if i.isdigit():
#     n=int(n)
#     i=n
#     while i>0:
#         s=s*i
#         i=i-1
#     print(f'the factorial of {n} is {s}')
# else:
#     print('invalid input')

# i=1
# s=0
# while i<101:
#     s=s+i
#     i+=1
# print(s)

# even=sum(range(2,101,2))
# # odd=sum(range(1,101,2))
# # multiplesof3=sum(range(3,101,3))
# # print(even,odd,multiplesof3)

# i=0
# o=0
# e=0
# t=0
# while i<101:
#     if i%2==0:
#         e+=i
#     else:
#         o+=i
#     if i%3==0:
#         t+=i
#     i+=1
# print(o,e,t)

# i=0
# s=0
# while i<100:
#     i+=1
#     if i%2==0:
#         continue
#     s+=i
# print(s)

# i=0
# while i<100:
#     i+=1
#     if i%7==0 or '7' in str(i):
#         continue        
#     print(i)

# for i in range(100,1000,1):
#     a,b,c=str(i)
#     a=int(a)
#     b=int(b)
#     c=int(c)
#     if a**3+b**3+c**3==i:
#         print(i)

i = 12345
digits = str(i)  # 转为字符串"12345"

# # 从右往左取各位数字
# a = int(digits[-1])  # 个位：最后一位
# b = int(digits[-2]) if len(digits) >= 2 else 0  # 十位：倒数第二位
# c = int(digits[-3]) if len(digits) >= 3 else 0  # 百位：倒数第三位
# d = int(digits[-4]) if len(digits) >= 4 else 0  # 千位：倒数第四位
# e = int(digits[-5]) if len(digits) >= 5 else 0  # 万位：倒数第五位

# print(f"个位: {a}, 十位: {b}, 百位: {c}, 千位: {d}, 万位: {e}")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}',end='\t')
# print(' ')
# s=0
# for i in range(1,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             if i!=j and j!=k and k!=i:
#                 print(f'{i}{j}{k}')
#                 s+=1
# print(s)

for rooster in range(0,21):
    for hen in range(0,34):
        
            chick=100-rooster-hen
            if rooster*5+hen*3+chick/3==100:
                print(rooster,hen,chick)