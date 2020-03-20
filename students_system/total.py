#-*- coding: utf-8 -*-
"""统计学生信息中的学生人数
   1. 文件以字典形式存储着
   2. 读出到列表后是字符串形式
   3. 直接统计字符串个数即可
"""
import os


filename = 'students_messages.txt'
def total():
    # ----------判断文件是否存在--------------------
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            student_all = file.readlines() # 字符串形式读取
            print("\n学生总人数为：" + str(len(student_all)))
    else:
        print("\033[1;31m数据未存储!\033[0m")

if __name__ == "__main__":
    pass