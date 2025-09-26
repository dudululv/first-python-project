amount = float(input("请输入消费金额："))

print("是否参加优惠换购活动：")
print("1. 满50元，加2元换购百事可乐饮料1瓶")
print("2. 满100元，加3元换购500ml可乐一瓶")
print("3. 满100元，加10元换购5公斤面粉")
print("4. 满200元，加10元可换购1个苏波尔炒菜锅")
print("5. 满200元，加20元可换购欧莱雅爽肤水一瓶")
print("0. 不换购")

choice = input("请选择：")

total_amount = amount
gift = ""

if choice == "1":
    if amount >= 50:
        total_amount = amount + 2
        gift = "百事可乐饮料1瓶"
    else:
        print("金额不足，无法换购此商品")
elif choice == "2":
    if amount >= 100:
        total_amount = amount + 3
        gift = "500ml可乐一瓶"
    else:
        print("金额不足，无法换购此商品")
elif choice == "3":
    if amount >= 100:
        total_amount = amount + 10
        gift = "5公斤面粉"
    else:
        print("金额不足，无法换购此商品")
elif choice == "4":
    if amount >= 200:
        total_amount = amount + 10
        gift = "1个苏波尔炒菜锅"
    else:
        print("金额不足，无法换购此商品")
elif choice == "5":
    if amount >= 200:
        total_amount = amount + 20
        gift = "欧莱雅爽肤水一瓶"
    else:
        print("金额不足，无法换购此商品")
elif choice == "0":
    print("您选择了不换购")
else:
    print("选择无效")

if gift: 
    print(f"本次消费总金额：{total_amount}")
    print(f"成功换购：{gift}")
else:
    print(f"本次消费总金额：{amount}")