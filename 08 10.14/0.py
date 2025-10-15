file = open('08 10.14/a.txt', mode='r', encoding='utf-8')
print(file.read())
file.close()
# file.readline(5)
# context_list = file.readlines()
# for e in context_list:
#     print(e, end='')
import os
print("当前工作目录:", os.getcwd())

file=open('08 10.14/d.txt', mode='w', encoding='utf-8')
file.write('hello world')
file.writelines(['hello world\n', 'hello world\n'])
file.close()

file=open('08 10.14/f.txt', mode='a', encoding='utf-8')
file.write('ip4\n')
file.writelines(['ip5\n', 'ip6\n'])
file.close()