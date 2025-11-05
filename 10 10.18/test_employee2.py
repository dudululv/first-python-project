import csv
FILENAME = "employee.csv"
def save_employees(employees):
    with open(FILENAME, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["编号", "姓名", "年龄", "地址"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)

def load_employees():
    employees = []
    try:
        with open(FILENAME, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        print("未检测到员工数据文件，正在创建新的 employee.csv ...")
        save_employees([])  
    return employees

def add_employee(employees):
    while True:
        emp_id = input("请输入员工编号（输入q结束）：").strip()
        if emp_id.lower() == "q":
            break
        name = input("请输入员工姓名：").strip()
        age = input("请输入员工年龄：").strip()
        address = input("请输入员工地址：").strip()
        for e in employees:
            if e["编号"] == emp_id:
                print("员工编号已存在，请重新输入。")
                break
        else:
            employees.append({"编号": emp_id, "姓名": name, "年龄": age, "地址": address})
            print(f"员工 {name} 添加成功！")


def show_all(employees):
    if not employees:
        print("暂无员工信息！")
        return
    print("\n—— 员工信息 ——")
    print(f"{'编号':<10}{'姓名':<10}{'年龄':<8}{'地址':<15}")
    for e in employees:
        print(f"{e['编号']:<10}{e['姓名']:<10}{e['年龄']:<8}{e['地址']:<15}")
    print()

def search_employee(employees):
    while True:
        print("""
—— 查询员工信息 ——
1. 按编号或姓名精确查询
2. 查看全部员工
0. 返回上一级
""")
        choice = input("请选择操作：").strip()
        if choice == "1":
            key = input("请输入要查询的编号或姓名：").strip()
            found = False
            for e in employees:
                if e["编号"] == key or e["姓名"] == key:
                    print("\n查询结果：")
                    print(f"{'编号':<10}{'姓名':<10}{'年龄':<8}{'地址':<15}")
                    print(f"{e['编号']:<10}{e['姓名']:<10}{e['年龄']:<8}{e['地址']:<15}")
                    found = True
                    break
            if not found:
                print("未找到匹配的员工信息！")
        elif choice == "2":
            show_all(employees)
        elif choice == "0":
            break
        else:
            print("无效的选择，请重新输入。")

def modify_employee(employees):
    emp_id = input("请输入要修改的员工编号：").strip()
    for e in employees:
        if e["编号"] == emp_id:
            print(f"当前信息：{e}")
            e["姓名"] = input(f"新姓名（留空不改）：") or e["姓名"]
            e["年龄"] = input(f"新年龄（留空不改）：") or e["年龄"]
            e["地址"] = input(f"新地址（留空不改）：") or e["地址"]
            print("修改成功！")
            return
    print("未找到该员工！")

def delete_employee(employees):
    """删除员工"""
    emp_id = input("请输入要删除的员工编号：").strip()
    for e in employees:
        if e["编号"] == emp_id:
            employees.remove(e)
            print("员工删除成功！")
            return
    print("未找到该员工！")

def main():
    employees = load_employees()
    while True:
        print("""
——— 员工管理系统 ———
1. 添加新员工
2. 查询员工信息
3. 修改员工信息
4. 删除员工信息
0. 退出系统
""")
        choice = input("请选择操作：").strip()
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            search_employee(employees)
        elif choice == "3":
            modify_employee(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "0":
            save_employees(employees)
            print("已保存数据，系统退出。")
            break
        else:
            print("无效的选择，请重新输入。")
main()