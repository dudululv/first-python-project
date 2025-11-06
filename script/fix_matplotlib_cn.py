import os
import matplotlib
from matplotlib.font_manager import findSystemFonts

# 常见中文字体（按优先级）
chinese_fonts = [
    "SimHei", "Microsoft YaHei", "SimSun",       # Windows 常见字体
    "STHeiti", "Heiti TC", "PingFang SC",        # macOS 常见字体
    "Noto Sans CJK SC", "Source Han Sans CN"     # Linux 常见字体
]

# 检查系统中已安装的字体
installed_fonts = [os.path.basename(f).split(".")[0] for f in findSystemFonts()]

# 找到第一个匹配的中文字体
chosen_font = None
for font in chinese_fonts:
    if any(font.lower() in f.lower() for f in installed_fonts):
        chosen_font = font
        break

if not chosen_font:
    print("⚠️ 未找到中文字体，请手动安装黑体或微软雅黑。")
else:
    print(f"✅ 检测到中文字体：{chosen_font}")

    # 获取用户配置目录
    config_dir = matplotlib.get_configdir()
    rc_path = os.path.join(config_dir, "matplotlibrc")

    # 写入配置
    with open(rc_path, "w", encoding="utf-8") as f:
        f.write(f"font.sans-serif : {chosen_font}\n")
        f.write("axes.unicode_minus : False\n")

    print(f"✅ 已在 {rc_path} 写入永久配置")
    print("🎉 现在重新启动 Python 或 Jupyter 后，中文绘图将自动显示正常！")
