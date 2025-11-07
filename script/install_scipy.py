import subprocess
import sys

def install(package):
    """安装指定包"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])

def main():
    try:
        import scipy
        print(f"✅ SciPy 已安装，版本：{scipy.__version__}")
    except ImportError:
        print("⚙️ 未检测到 SciPy，正在安装中...")
        install("scipy")
        import scipy
        print(f"🎉 安装完成！SciPy 版本：{scipy.__version__}")

if __name__ == "__main__":
    main()
