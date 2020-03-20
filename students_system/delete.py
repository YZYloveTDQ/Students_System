#-*- coding: utf-8 -*-
"""删除学生信息：
   1. 读取全部学生信息到列表
   2. 将不删除的学生信息重新写入文件"""
import os


filename = 'students_messages.txt'


def delete():
    while True:
        student_new = []
        ID = ''
        name = ''
        if os.path.exists(filename):  # 判断文件是否存在
            with open(filename, 'r') as file:
                student_old = file.readlines()  # 读取文件全部信息到列表

                # 显示学生信息
                print("\033[1;31m学生信息：\033[0m")
                for alist in student_old:
                    print(alist, end='')

                # 输入选项
                mode = input(
                    "\033[1;33m\n依据学生ID则输入1，依据学生姓名则输入2, 退出输入0：\033[0m")
                if mode == '1':
                    ID = input("输入学生ID：")
                elif mode == '2':
                    name = input("输入学生姓名：")
                elif mode == '0':
                    break
                else:
                    print("\033[1;31m输入错误\033[0m")
                    break

                for alist1 in student_old:
                    d = eval(alist1)  # 字符串转化为字典
                    if ID:
                        if d['ID'] != ID:
                            student_new.append(d)
                        else:
                            print("删除学生信息为：" + str(d))  # 输出删除的信息
                    elif name:
                        if d['name'] != name:
                            student_new.append(d)
                        else:
                            print("删除的学生信息为："+ str(d))  # 输出删除的学生信息
                print('\033[1;33m\n删除完成！\033[0m')

                # 显示删除后的学生信息
                print("\033[1;31m\n删除后的学生信息：\033[0m")
                for alist2 in student_new:
                    print(str(alist2) + '\n')

                # 写入文件
                with open(filename, 'w') as file2:
                    for alist3 in student_new:
                        file2.write(str(alist3) + '\n')

                # 是否继续
                delete_mark = input("\n是否继续？（y/n）：")
                if delete_mark == 'y':
                    continue
                else:
                    break
        else:
            print("\033[1;31m文件不存\033[0m")
            break


if __name__ == "__main__":
    pass
