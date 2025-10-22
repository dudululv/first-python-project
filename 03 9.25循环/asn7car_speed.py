# # 汽车里程表对称数问题求解

# # 初始里程表读数（对称数）
# start_mileage = 95859
# # 时间（小时）
# time_hours = 2

# # 定义函数检查一个数是否是对称数
# def is_symmetric(number):
#     # 将数字转换为字符串
#     str_number = str(number)
#     # 检查字符串是否与其反转后的字符串相同
#     return str_number == str_number[::-1]

# # 寻找下一个对称数
# next_mileage = start_mileage + 1
# found = False

# while not found:
#     if is_symmetric(next_mileage):
#         found = True
#     else:
#         next_mileage += 1

# # 计算行驶距离
# distance = next_mileage - start_mileage
# # 计算时速
# speed = distance / time_hours

# # 输出结果
# print(f"初始对称数: {start_mileage}")
# print(f"2小时后的新对称数: {next_mileage}")
# print(f"行驶距离: {distance} 公里")
# print(f"汽车时速: {speed} 公里/小时")
for i in range(95860,100000):
    a,b,c,d,e=str(i)
    if a==e and b==d:
        print((i-95859)/2)
        break
print("程序结束")