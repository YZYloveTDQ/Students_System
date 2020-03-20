#-*- coding: utf-8 -*-
"""显示学生信息"""
import os


filename = 'students_messages.txt'
def show():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            student_all = file.readlines()
        print("\033[1;315m学生信息：\033[0m")
        for alist in student_all:
            print(alist, end='')
    else:
        print("\033[1;31m数据未保存！\033[0m")

if __name__ == "__main__":
    pass