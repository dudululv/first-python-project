import csv
cars = {}
def readerCar():
    with open('10.18/cars.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)  # 修正：使用不同的变量名
        next(reader)  # 跳过表头
        for i in reader:  # ['轿车','宝马X6(京NY28588)','800']
            if i[0] in cars:
                cars[i[0]].append(i[1:])
            else:
                cars[i[0]] = [i[1:]]  # {'轿车': [[],[],[]]} 第一次创建，后续append
    print(f'读取成功{cars}')  # 修正：缩进和字符串格式化

def zuJiaoChe():  # 租轿车函数
    print(f'编号\t具体信息\t\t日租金')
    index = 1
    for car in cars['轿车']:  # [[],[],[]]  ['宝马X6(京NY28588)', '800']
        print(f'{index}\t{car[0]}\t{car[1]}')
        index += 1
    # 选择车
    choice = is_num('请选择车型编号:', 1, len(cars['轿车'])) - 1
    car = cars['轿车'][choice]  # ['宝马X6(京NY28588)', '800']
    # 输入天数
    days = int(input('请输入租车的天数:'))
    # 计算租金
    sum_ = days * int(car[-1])
    # 计算折扣
    if 7 < days <= 30:
        sum_ *= 0.9
    elif 30 < days <= 150:
        sum_ *= 0.8
    elif days > 150:
        sum_ *= 0.7
    print(f'您租的车是{car[0]}，天数是:{days}，总金额:{sum_}')

def zuKeChe():
    print(f'编号\t具体信息\t\t日租金')
    index = 1  # 编号
    for can in cars['客车']:  # [[],[],[]]  ['宝马X6(京NY28588)', '800']
        print(f'{index}\t{can[0]}\t{can[1]}')
        index += 1
    # 选择车
    index = is_num('请选择车型编号:', 1, 4) - 1
    car = cars['客车'][index]  # 修正：应该是[index]而不是['index]
    # 输入天数
    days = int(input('请输入租车的天数:'))
    # 计算租金
    sum_ = days * int(car[-1])  # 修正：应该是car而不是ca
    # 计算折扣
    if 3 <= days < 7:
        sum_x = 0.9
    elif 7 <= days < 30:
        sum_x = 0.8
    elif 30 <= days < 150:
        sum_x = 0.7
    elif days >= 150:
        sum_x = 0.6
    else:
        sum_x = 1.0  # 添加默认情况，天数小于3天不打折
    # 应用折扣
    sum_ = sum_ * sum_x  # 应用折扣计算最终金额
    print(f'您租的车是{car[0]}，天数是:{days}，总金额:{sum_}')

def is_num(msg, start, end):
    while True:
        key = input(msg)
        if key.isdigit():
            key = int(key)
            if start <= key <= end:
                return key
            else:
                print(f'输入有误,请输入{start}-{end}')
        else:
            print(f'输入有误,请输入{start}-{end}')

# 读取文件一次标识
flag = True
msg = '1.轿车 2.客车 0.退出\n请选择:'

while True:
    if flag:
        readerCar()  # 首次运行读取文件
        flag = False
        
    num = is_num(msg, 0, 2)
    
    if num == 0:
        print('退出系统')
        break
    elif num == 1:
        zuJiaoChe()  # 调用租轿车功能
    elif num == 2:
        zukeChe()    # 调用租客车功能