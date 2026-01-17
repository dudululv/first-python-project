import subprocess
import sys

def install_and_check():
    # 定义本项目需要的库清单
    # pandas, numpy, tensorflow: 基础模型库
    # scikit-learn: 数据处理
    # imbalanced-learn: 解决数据不平衡的 SMOTE 算法
    required_libraries = [
        'pandas', 
        'numpy', 
        'tensorflow', 
        'scikit-learn', 
        'imbalanced-learn'
    ]

    print("--- 正在开始环境自动检查 ---")
    
    for lib in required_libraries:
        try:
            # 尝试导入库
            # 注意：imbalanced-learn 在导入时通常使用 imblearn
            lib_import_name = 'imblearn' if lib == 'imbalanced-learn' else lib
            __import__(lib_import_name)
            print(f"[已安装] {lib}")
        except ImportError:
            # 如果导入失败，则调用 pip 安装
            print(f"[未安装] 正在为您安装 {lib}，请稍候...")
            try:
                # 使用当前 Python 解释器对应的 pip
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
                print(f"[成功] {lib} 安装完成。")
            except Exception as e:
                print(f"[错误] 安装 {lib} 失败，请检查网络或权限。错误信息: {e}")

    print("\n--- 所有库检查/安装流程结束 ---")
    print("现在你可以运行主程序了。")

if __name__ == "__main__":
    install_and_check()