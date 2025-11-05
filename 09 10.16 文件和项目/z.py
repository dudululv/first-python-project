import csv
import random

FILENAME = "lottery_users.csv"
users = {}  # username 为 key，value = [password, card_number]

# 读取 CSV 文件
def load_users():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # 跳过表头
            for row in reader:
                if len(row) < 3:
                    continue
                username, pwd, card = row
                users[username] = [pwd, card]
    except FileNotFoundError:
        pass  # 文件不存在时不报错

# 写入 CSV 文件（自动创建）
def save_users():
    with open(FILENAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["用户名", "密码", "卡号"])
        for username, data in users.items():
            writer.writerow([username] + data)

# 注册用户
def register():
    username = input("请输入用户名：").strip()
    if not username:
        print("用户名不能为空！")
        return
    if username in users:
        print("用户名已存在！")
        return
    password = input("请输入密码：").strip()
    # 生成唯一卡号
    while True:
        card = str(random.randint(1000, 9999))
        if card not in [u[1] for u in users.values()]:
            break
    users[username] = [password, card]
    save_users()
    print(f"✅ 注册成功！您的卡号是：{card}")

# 用户登录
def login(logged_in):
    username = input("请输入用户名：").strip()
    if username not in users:
        print("❌ 用户不存在！")
        return None
    password = input("请输入密码：").strip()
    if password != users[username][0]:
        print("❌ 密码错误！")
        return None
    print("✅ 登录成功！")
    logged_in[0] = username  # 使用列表保存登录状态
    return username

# 抽奖功能
def lottery(logged_in):
    if not logged_in[0]:
        print("❌ 请先登录！")
        return
    username = logged_in[0]
    card = users[username][1]
    n = random.randint(0, 9)
    if str(n) == card[-1]:  # 卡号最后一位
        print(f"🎉 恭喜 {username} 抽中奖品！")
    else:
        print(f"😔 很遗憾 {username} 没有中奖。")

# 主菜单
def main():
    load_users()
    logged_in = [None]  # 用列表保存登录状态，可修改
    print("🎰 欢迎使用奖富翁抽奖系统（CSV版，实时保存）")

    while True:
        print("""
----- 奖富翁系统 -----
1. 注册
2. 登录
3. 抽奖
0. 退出
""")
        choice = input("请输入选项：").strip()
        if choice == "1":
            register()
        elif choice == "2":
            login(logged_in)
        elif choice == "3":
            lottery(logged_in)
        elif choice == "0":
            save_users()
            print("📂 已保存并退出系统")
            break
        else:
            print("❌ 无效输入，请重新选择。")

if __name__ == "__main__":
    main()
