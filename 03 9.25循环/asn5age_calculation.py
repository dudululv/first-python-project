# 计算小红父亲在几年后比她年龄大1倍的问题

# 初始化当前年龄
xiaohong_age = 12
father_age = xiaohong_age + 20  # 父亲比小红大20岁
years = 0

# 使用while循环计算需要的年数
while father_age != 2 * xiaohong_age:
    # 每过一年，两人年龄各加1
    xiaohong_age += 1
    father_age += 1
    years += 1

# 输出结果
print(f"需要{years}年后，父亲的年龄是小红的1倍。")
print(f"那时小红的年龄是：{xiaohong_age}岁")
print(f"那时父亲的年龄是：{father_age}岁")