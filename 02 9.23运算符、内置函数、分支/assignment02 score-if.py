score = float(input("请输入赵本山的考试成绩："))

if score == 100:
    print("爸爸给他买辆车")
elif 100>score >= 90:
    print("妈妈给他买MP4")
elif 90>score >= 60:
    print("妈妈给他买本参考书")
elif 60>score>=0:
    print("什么都不买")
else:
    print('Invalid input! Please try again.')