# # 从用户输入的5个数中找出最小值

# numbers = []
# count = 0

# print("请输入5个数字：")

# while count < 5:
#     try:
#         # 获取用户输入并转换为浮点数
#         num = float(input(f"请输入第{count+1}个数字: "))
#         numbers.append(num)
#         count += 1
#     except ValueError:
#         print("错误：请输入有效的数字！")

# # 使用min()函数找出最小值
# minimum = min(numbers)

# # 也可以通过循环比较找出最小值（注释掉的代码）
# # minimum = numbers[0]
# # for num in numbers[1:]:
# #     if num < minimum:
# #         minimum = num

# print(f"输入的5个数是: {numbers}")
# print(f"其中的最小值是: {minimum}")
for i in range(5):
    num = float(input(f"请输入第{i+1}个数字: "))
    if i == 0:
        minimum = num
    else:
        if num < minimum:
            minimum = num
print(f"当前最小值是: {minimum}")