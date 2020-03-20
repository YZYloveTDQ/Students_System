#-*- coding: utf-8 -*-
"""查询文件的前提是文件存在，所以要先判断文件是否存在"""
import os


filename = 'students_messages.txt'


def search():
    # student_searched = []  # 保存已经查询过的学生
    while True:
        ID = ""
        name = ""
        if os.path.exists(filename):  # 检查保存的文件是否存在
            mode = input("按ID查询输入1，按姓名输入2：")  # 所以文件中的内容要按照字典存放
            if mode == '1':  # input输入的是字符
                ID = input("输入学生ID：")
            elif mode == '2':
                name = input("输入学生姓名：")
            else:
                print("\033[1;31m输入错误，请重新输入\033[0m")
                continue

            with open(filename, 'r') as file:  # 查询以读模式就可以
                student = file.readlines()  # 读取全部内容，按照行
                for alist in student:
                    d = eval(alist)  # 字符串转字典
                    if ID:
                        if d['ID'] == ID:
                            print("\n\033[1;33m查询结果\033[0m" + str(d))
                    elif name:
                        if d['name'] == name:
                            print("\n\033[1;33m查询结果\033[0m" + str(d))

                # show_student(student_searched) # 显示全部查询结果
                # student_searched.clear() # 清空查询结果

                # 循环结束条件
                input_mark = input("\n是否继续？（y/n）：")
                if input_mark == 'y':
                    continue
                else:
                    print('\n')
                    break
        else:
            print("\033[1;31m暂未保存数据\033[0m")
            break


if __name__ == "__main__":
    pass
