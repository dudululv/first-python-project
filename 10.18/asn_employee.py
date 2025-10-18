import csv
import unicodedata

FILENAME = "employee.csv"

# ===================== 工具函数 =====================
def save_employees(employees):
    """保存员工数据到文件"""
    with open(FILENAME, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["编号", "姓名", "年龄", "地址"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)


def load_employees():
    """从文件加载员工数据；如果文件不存在则创建空文件"""
    employees = []
    try:
        with open(FILENAME, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        print("⚠️ 未检测到员工数据文件，正在创建新的 employee.csv ...")
        save_employees([])  # 创建空文件
    return employees

# ===================== 左对齐显示函数 =====================
col_widths = [10, 10, 8, 15]  # 显示列宽，可调整

def display_width(s: str) -> int:
    """计算字符串显示宽度（中文2列，英文/数字1列）"""
    width = 0
    for ch in s:
        if unicodedata.east_asian_width(ch) in ("F", "W"):
            width += 2
        else:
            width += 1
    return width

def left_align(s: str, width: int) -> str:
    """按显示宽度左对齐，填充空格"""
    w = display_width(s)
    if w >= width:
        return s
    return s + " " * (width - w)

def print_employee(e):
    """打印单个员工信息（左对齐按显示宽度）"""
    print("".join(left_align(e[k], w) for k, w in zip(["编号","姓名","年龄","地址"], col_widths)))

def show_all(employees):
    """显示所有员工"""
    if not employees:
        print("暂无员工信息！")
        return
    print("\n—— 员工信息 ——")
    headers = ["编号", "姓名", "年龄", "地址"]
    print("".join(left_align(h, w) for h, w in zip(headers, col_widths)))
    for e in employees:
        print_employee(e)
    print()

# ===================== 主功能 =====================
def add_employee(employees, auto_save):
    while True:
        emp_id = input("请输入员工编号（输入q结束）：").strip()
        if emp_id.lower() == "q":
            break
        name = input("请输入员工姓名：").strip()
        age = input("请输入员工年龄：").strip()
        address = input("请输入员工地址：").strip()

        # 检查重复编号
        for e in employees:
            if e["编号"] == emp_id:
                print("❌ 员工编号已存在，请重新输入。")
                break
        else:
            employees.append({"编号": emp_id, "姓名": name, "年龄": age, "地址": address})
            print(f"✅ 员工 {name} 添加成功！")
            if auto_save:
                save_employees(employees)
                print("💾 已自动保存。")

def modify_employee(employees, auto_save):
    emp_id = input("请输入要修改的员工编号：").strip()
    for e in employees:
        if e["编号"] == emp_id:
            print("当前信息：")
            print_employee(e)
            e["姓名"] = input(f"新姓名（留空不改）：") or e["姓名"]
            e["年龄"] = input(f"新年龄（留空不改）：") or e["年龄"]
            e["地址"] = input(f"新地址（留空不改）：") or e["地址"]
            print("✅ 修改成功！")
            if auto_save:
                save_employees(employees)
                print("💾 已自动保存。")
            return
    print("❌ 未找到该员工！")

def delete_employee(employees, auto_save):
    emp_id = input("请输入要删除的员工编号：").strip()
    for e in employees:
        if e["编号"] == emp_id:
            employees.remove(e)
            print("✅ 员工删除成功！")
            if auto_save:
                save_employees(employees)
                print("💾 已自动保存。")
            return
    print("❌ 未找到该员工！")

def search_employee(employees):
    while True:
        print("""
—— 查询员工信息 ——
1. 精确查找（按编号或姓名）
2. 模糊查找（部分匹配）
3. 查看全部员工
0. 返回上一级
""")
        choice = input("请选择操作：").strip()

        if choice == "1":
            key = input("请输入要查询的编号或姓名：").strip()
            found = False
            for e in employees:
                if e["编号"] == key or e["姓名"] == key:
                    print("\n✅ 查询结果：")
                    print("".join(left_align(h, w) for h, w in zip(["编号","姓名","年龄","地址"], col_widths)))
                    print_employee(e)
                    found = True
                    break
            if not found:
                print("❌ 未找到匹配的员工信息！")

        elif choice == "2":
            key = input("请输入部分编号或姓名关键字：").strip()
            results = [e for e in employees if key in e["编号"] or key in e["姓名"]]
            if results:
                print("\n✅ 模糊查询结果：")
                print("".join(left_align(h, w) for h, w in zip(["编号","姓名","年龄","地址"], col_widths)))
                for e in results:
                    print_employee(e)
            else:
                print("❌ 未找到匹配的员工信息！")

        elif choice == "3":
            show_all(employees)
        elif choice == "0":
            break
        else:
            print("❌ 无效的选择，请重新输入。")

# ===================== 主程序入口 =====================
def main():
    employees = load_employees()

    # 选择保存模式
    print("""
—— 员工管理系统启动 ——
请选择保存模式：
1. 实时保存模式（操作后立即写入文件）
2. 集中保存模式（退出时统一写入）
""")
    mode = input("请输入选择（1或2）：").strip()
    auto_save = (mode == "1")

    if auto_save:
        print("✅ 已启用【实时保存模式】")
    else:
        print("💾 已启用【集中保存模式】")

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
            add_employee(employees, auto_save)
        elif choice == "2":
            search_employee(employees)
        elif choice == "3":
            modify_employee(employees, auto_save)
        elif choice == "4":
            delete_employee(employees, auto_save)
        elif choice == "0":
            if not auto_save:
                save_employees(employees)
                print("💾 已保存数据。")
            print("系统退出，再见！👋")
            break
        else:
            print("❌ 无效的选择，请重新输入。")


if __name__ == "__main__":
    main()
