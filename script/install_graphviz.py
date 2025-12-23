"""
install_graphviz.py
自动安装 Python graphviz 库，并测试是否可用
"""

import sys
import subprocess


def run(cmd):
    print(f"\n>>> 执行: {cmd}")
    subprocess.check_call(cmd, shell=True)


def install_python_graphviz():
    # 使用当前 Python 对应的 pip
    run(f'"{sys.executable}" -m pip install --upgrade pip')
    run(f'"{sys.executable}" -m pip install graphviz')


def test_graphviz():
    try:
        from graphviz import Digraph

        dot = Digraph(comment="Test")
        dot.node("A", "Hello")
        dot.node("B", "Graphviz")
        dot.edge("A", "B")

        print("\n✅ graphviz Python 库安装成功")
        print("Dot source:\n")
        print(dot.source)

    except Exception as e:
        print("\n❌ graphviz Python 库已安装，但系统 Graphviz 可能未安装")
        print("错误信息：")
        print(e)


if __name__ == "__main__":
    install_python_graphviz()
    test_graphviz()
