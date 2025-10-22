import importlib

packages = ["numpy", "pandas", "matplotlib", "seaborn"]

for pkg in packages:
    try:
        m = importlib.import_module(pkg)
        print(f"{pkg} 已安装，版本：{m.__version__}")
    except ImportError:
        print(f"{pkg} 未安装")
