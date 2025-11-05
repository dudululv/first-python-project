import importlib
import subprocess
import sys

def check_and_install(package_name, display_name=None):
    """检查并安装指定的包"""
    if display_name is None:
        display_name = package_name
    
    try:
        importlib.import_module(package_name)
        print(f"✅ '{display_name}' 已安装！")
        return True
    except ImportError:
        print(f"⚙️ 未检测到 '{display_name}'，正在安装...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"✅ '{display_name}' 安装完成！")
            return True
        except Exception as e:
            print(f"❌ '{display_name}' 安装失败: {e}")
            return False

print("=== Excel 处理库检测与安装 ===")

# 检测和安装三个库
packages = [
    ("openpyxl", "openpyxl (.xlsx 读写)"),
    ("xlwt", "xlwt (.xls 写入)"), 
    ("xlrd", "xlrd (.xls 读取)")
]

results = {}
for package, display_name in packages:
    results[package] = check_and_install(package, display_name)

print("\n" + "="*50)