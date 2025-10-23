import math

# 从键盘输入a, b, c三个值
try:
    a = float(input("请输入三角形的第一条边a: "))
    b = float(input("请输入三角形的第二条边b: "))
    c = float(input("请输入三角形的第三条边c: "))
    
    # 检查输入是否为正数
    if a <= 0 or b <= 0 or c <= 0:
        print("错误：三角形的边长必须为正数！")
    else:
        # 检查能否构成三角形（任意两边之和大于第三边，任意两边之差小于第三边）
        if a + b > c and a + c > b and b + c > a:
            print(f"{a}, {b}, {c}可以构成三角形。")
            
            # 使用海伦公式计算三角形的面积
            s = (a + b + c) / 2  # 半周长
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # 海伦公式
            
            print(f"三角形的面积为: {area:.2f}")
        else:
            print(f"{a}, {b}, {c}不能构成三角形。")
except ValueError:
    print("错误：请输入有效的数字！")