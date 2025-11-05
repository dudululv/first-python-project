import csv
peoples={}
title={}
def readerpeople():
  with open('day1018项目\员工信息.csv','r',encoding='utf-8') as f:
      f= csv.reader(f)
      global title
      title=next(f)
      for i in f: 
          peoples[i[0]]=[i[1],i[2],i[3]] 
  print(f'读取成功{peoples}')
def writerpeople():
    with open('day1018项目\员工信息.csv','w',encoding='utf-8',newline='') as f:
        f=csv.writer(f)
        f.writerow(title)
        for key,value in peoples.items():
            f.writerow([key,value[0],value[1],value[2]])
            print(f'写入成功{peoples}')
def input_num(m, start, end):
    while True:
        key = input(m)
        if key.isdigit():
            key = int(key)
            if start <= key <= end:
                return key
            else:
                print(f'请输入{start}-{end}')
        else:
            print(f'请输入{start}-{end}')
def addpeople():
    id=input('请输入员工编号:')
    if id not in peoples:
        name=input('请输入员工姓名:')
        age=input('请输入员工年龄:')
        address=input('请输入住址:')
        peoples[id]=[name,age,address]
        print(f'{id},{name}添加成功')
    else:
        print('员工编号已存在')
def  searchpeople():
    k=input('1.查询全部\n2.查询学号请选择:',1,2)
    if k==1:
        print('编号\t姓名\t年龄\t家庭住址')
        for key,value in peoples.items():
            print(f'{key}\t{value[0]}\t{value[1]}\t{value[2]}')
    elif k==2:
        id=input('请输入编号:')
        if id in peoples:
            print('编号\t姓名\t年龄\t家庭住址')
            print(f'{id}\t{peoples[id][0]}\t{peoples[id][1]}\t{peoples[id][2]}')
        else:
            print('编号不存在')
def modify_people():
        name=input('请输入姓名:')
        names=[i[0] for i in peoples.values()]
        if name in names:
            print('编号\t姓名\t年龄\t家庭住址')
            for key,value in peoples.items():
                if name==value[0]:
                    print(f'{key}\t{value[0]}\t{value[1]}\t{value[2]}')
        else:
            print('姓名不存在')
def delpeople():
    id=input('请输入编号:')
if id in peoples:
    if id in peoples:
        id.pop(peoples)
        print(f'{id}删除成功')
    else:
        print('编号不存在')

msg = '''1.添加新员工
允许用户循环输入员工编号,员工姓名,年龄,地址（输入 “q” 结束输入）；
2.查询员工信息
3.修改员工信息
4.删除员工信息
0.退出系统'''
info = readerpeople("day1018项目\员工信息.csv")
while True:
        key = input_num(msg, 0, 4)
        if key == 0:
            writerpeople()
            print("已退出系统，数据已保存")
            break
        elif key == 1:
            addpeople()
        elif key == 2:
            searchpeople()
        elif key == 3:
            modify_people()
        elif key == 4:
            delpeople()