import csv

FILENAME = "students.csv"
students = {}  # 学号为 key，value = [姓名, 年龄, 家庭住址]

# 读取 CSV 文件
def load_students():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # 跳过表头
            for row in reader:
                if len(row) < 4:
                    continue
                sid, name, age, address = row
                students[sid] = [name, age, address]
    except FileNotFoundError:
        pass  # 文件不存在就先不做任何操作，保存时会自动创建

# 写入 CSV 文件（自动创建）
def save_students():
    with open(FILENAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["学号", "姓名", "年龄", "家庭住址"])
        for sid, data in students.items():
            writer.writerow([sid] + data)

# 添加学生
def add_student():
    sid = input("请输入学号：").strip()
    if not sid:
        print("学号不能为空！")
        return
    if sid in students:
        print("学号已存在！")
        return
    name = input("请输入姓名：").strip()
    age = input("请输入年龄：").strip()
    address = input("请输入家庭住址：").strip()
    students[sid] = [name, age, address]
    save_students()
    print(f"✅ 已添加学生：{name}")

# 查询学生
def query_student():
    sid = input("请输入要查询的学号（留空显示所有学生）：").strip()
    if sid:
        if sid in students:
            name, age, address = students[sid]
            print(f"学号:{sid}, 姓名:{name}, 年龄:{age}, 家庭住址:{address}")
        else:
            print("❌ 未找到该学生信息。")
    else:
        if not students:
            print("学生列表为空。")
        else:
            print("📒 所有学生信息：")
            for sid, data in students.items():
                print(f"学号:{sid}, 姓名:{data[0]}, 年龄:{data[1]}, 家庭住址:{data[2]}")

# 修改学生
def modify_student():
    sid = input("请输入要修改的学号：").strip()
    if sid in students:
        name = input(f"请输入新姓名（留空不改，原：{students[sid][0]}）：").strip() or students[sid][0]
        age = input(f"请输入新年龄（留空不改，原：{students[sid][1]}）：").strip() or students[sid][1]
        address = input(f"请输入新家庭住址（留空不改，原：{students[sid][2]}）：").strip() or students[sid][2]
        students[sid] = [name, age, address]
        save_students()
        print("✅ 学生信息已更新。")
    else:
        print("❌ 未找到该学生信息。")

# 删除学生
def delete_student():
    sid = input("请输入要删除的学号：").strip()
    if sid in students:
        confirm = input(f"确认删除 {students[sid][0]} 吗？(y/n)：").lower()
        if confirm == "y":
            del students[sid]
            save_students()
            print(f"✅ 已删除学生：{sid}")
        else:
            print("取消删除。")
    else:
        print("❌ 未找到该学生信息。")

# 主菜单
def main():
    load_students()
    print("🎓 欢迎使用学生管理系统（CSV版，实时保存）")
    while True:
        print("""
----- 学生管理系统 -----
1. 添加学生
2. 查询学生
3. 修改学生
4. 删除学生
0. 退出
""")
        choice = input("请输入选项：").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            query_student()
        elif choice == "3":
            modify_student()
        elif choice == "4":
            delete_student()
        elif choice == "0":
            save_students()
            print("📂 已保存并退出系统")
            break
        else:
            print("❌ 无效输入，请重新选择。")

if __name__ == "__main__":
    main()
