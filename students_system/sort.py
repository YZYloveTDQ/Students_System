#-*- coding: utf-8 -*-
"""学生信息排序：
   1. 先显示全部学生信息
   2. 选择排序升序还是降序
   3. 选择排序参量
   排序只是显示的界面"""
import os


filename = 'students_messages.txt'
def sort():
    # -------------显示全部学生信息----------------------
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            student_all = file.readlines()  # 读取全部信息到列表
        student_new = []
        for alist in student_all:
            student_new.append(eval(alist))  # 将字典存入到新的列表中
    else:
        print("\033[1;31\n文件不存在\033[0m")
        return

    # ------------选择升序还是降序-------------------------------
    asc_or_desc = input("\033[1;33m升序输入0，降序输入1：\033[0m")
    if asc_or_desc == '0':
        reverse_mark = False
    elif asc_or_desc == '1':
        reverse_mark = True
    else:
        print("\033[1;31m\n输入有误，请输入数字0/1！\033[0m")
        sort()

    # ----------选择排序的参量------------------------------------
    mode = input(
        "\033[1;33m输入排序参考参量（1代表英语成绩，2代表Python成绩，3代表C语言成绩，4代表总成绩）：\033[0m")
    if mode == '1':
        student_new.sort(key=lambda x: x['English'], reverse=reverse_mark)
    elif mode == '2':
        student_new.sort(key=lambda x: x['Python'], reverse=reverse_mark)
    elif mode == '3':
        student_new.append(key=lambda x: x['C'], reverse=reverse_mark)
    elif mode == '4':
        student_new.sort(
            key=lambda x: x['English']+x['Python']+x['C'], reverse=reverse_mark)
    else:
        print("\033[1;31m输入有误，请输入1/2/3/4！\033[0m")
        sort()

    # ----------显示学生信息------------------------------------------
    print("\033[1;31m学生信息：\033[0m")
    for alist1 in student_new:
        print(alist1)


if __name__ == "__main__":
    pass
