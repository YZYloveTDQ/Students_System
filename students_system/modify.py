#-*- coding: utf-8 -*-
# modify（）修改学生信息功能
"""函数功能：
   1. 先判断文件是否存在，显示全部学生信息
   2. 将学生信息都先读入到列表
   3. 修改后的学生信息重新写入文件"""
import os

filename = 'students_messages.txt'
def modify():
    # ---------先显示全部学生信息------------------
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            student_all = file.readlines()  # 全部读取到列表中
            print("\033[1;31m全部学生信息：\033[0m")
            for alist in student_all:
                print(str(alist), end='')  # 消除空行

            # --------找到要修改的学生信息----------------
            student_new = []
            student_ID = input("\033[1;33m输入修改学生的ID：\033[0m")
            for student in student_all:
                d = eval(student)  # 字符串转化为字典
                if d['ID'] != student_ID:
                    student_new.append(d)
                else:
                    print("\033[1;34m要修改的学生信息为：\033[0m{}".format(d))

                    # -------开始修改学生信息------------------
                    while True:  # 循环——害怕学生输入错误可以重新输入
                        try:
                            d['name'] = input("输入学生姓名：")
                            d['English'] = int(input("输入英语成绩："))
                            d['Python'] = int(input("输入Python成绩："))
                            d['C'] = int(input("输入C语言成绩："))
                            break
                        except:
                            print("输入有误，重新输入!")
                    student_new.append(d)

        # ------将新的学生信息写入文件--------------------------
        with open(filename, 'w') as file2:  # 以写模式打开文件
            print("\033[1;31m\n修改后的学生信息：\033[0m")
            for alist1 in student_new:
                file2.write(str(alist1) + '\n')
                print(str(alist1))
        print("\033[1;33m\n修改成功!\033[0m")

        # --------是否继续-----------------------------------
        modify_mark = input("\n是否继续修改？（y/n）：")
        if modify_mark == 'y':
            modify()

    else:
        print("为保存数据！")
        return  # 要结束这个函数


if __name__ == "__main__":
    pass
