import csv
import random
users = {}
def reader():
    with open('10.16 文件和项目/count.csv', 'r', encoding='utf-8') as file:
        reader= csv.reader(file)
        next(reader)
        for i in reader:
            users[i[0]] = [i[1],i[2]]
def writer():
    with open('10.16 文件和项目/count.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['姓名', '密码', '卡号'])
        for i in users.items():
            writer.writerow([i[0], i[1][0], i[1][1]])
def is_num(msg, start, end):
    while True:
        key = input(msg)
        if key.isdigit():
            key = int(key)
            if start <= key <= end:
                return key
            else:
                print(f'输入不合法，请输入 {start}-{end}')
        else:
            print(f'输入不合法，请输入 {start}-{end}')
flag = True
login=[]
while True:
    if flag:
        reader()
        print(users)
        flag = False

    msg = '''---------奖富翁系统---------
请选择你的操作：1注册 2登录 3抽奖 0退出: '''
    num = is_num(msg, 0, 3)
    if num == 0:
        print("退出系统")
        writer()
        break
    elif num == 1:
        while True:
            name = input('请输入姓名：')
            if name not in users:
                pwd = input('请输入密码：')
                while True:
                    card = random.randint(1000, 9999)
                    for i in users.values():
                        if i[1] == str(card):
                            break
                    else:
                        users[name] = [pwd, str(card)]
                        print(f'注册成功，您的卡号为：{card}')
                        break
                break
            else:
                print('姓名已存在')      
    elif num == 2:
        name = input('请输入姓名：')
        if name in users:
            pwd = input('请输入密码：')
            if pwd == users[name][0]:
                login.append([name, users[name][1]])  # 把用户名和卡号放在一个列表里
                print('登录成功')

            else:
                print('密码错误')
        else:
            print('姓名不存在')
    elif num == 3:
        if login:
            print('您已登录')
            n=random.randint(0,9)
            if str(n) == login[1][-1]:
                print('恭喜您抽中了奖')
            else:
                print('很遗憾您没有抽中奖')
        else:
            print('请先登录')


