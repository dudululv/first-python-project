# # 用户登录验证程序
# # 最多允许3次验证尝试

# # 预设的用户名和密码（实际应用中应该加密存储）
# CORRECT_USERNAME = "admin"
# CORRECT_PASSWORD = "password123"

# # 初始化验证次数
# attempts = 0
# max_attempts = 3

# # 标记登录是否成功
# login_successful = False

# # 循环进行登录验证，最多3次
# while attempts < max_attempts and not login_successful:
#     # 获取用户输入
#     username = input("请输入用户名: ")
#     password = input("请输入密码: ")
    
#     # 增加尝试次数
#     attempts += 1
    
#     # 验证用户名和密码
#     if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
#         login_successful = True
#         print("登录成功！欢迎使用系统。")
#     else:
#         # 计算剩余尝试次数
#         remaining_attempts = max_attempts - attempts
#         if remaining_attempts > 0:
#             print(f"用户名或密码错误！您还有{remaining_attempts}次尝试机会。")
#         else:
#             print("验证失败次数过多，账户已被锁定！")

# # 登录成功后的操作（实际应用中可以添加更多功能）
# if login_successful:
#     print("您已成功登录到系统，可以开始使用各项功能。")
CORRECT_USERNAME = "123"
CORRECT_PASSWORD = "123"
for i in range(3,0,-1):
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:  
        print(f"登录成功！欢迎{username}使用系统。")
        break
    elif i!=1:
            print(f"用户名或密码错误！您还有{i-1}次尝试机会。")
    else:
            print("验证失败次数过多，账户已被锁定！")