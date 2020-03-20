#-*- coding: utf-8 -*-
"""1. 录入学生信息，要创建一个文件存储学生信息
   2. 将录入的学生信息先整合到一个列表中
   3. 将列表存储到文件中中"""

filename = 'students_messages.txt'


def save(student):
    # 存储函数
    # 注意传过来的是存储着字典的列表
    try:
        students_txt = open(filename, 'a')  # 以追加模式打开文件
    except Exception as e:
        students_txt = open(filename, 'w')  # 文件不存在就创建文件
    print('\n', "\033[1;31m总的学生学生信息：\033[0m")
    for d in student:  # 取出列表中的字典
        print(d)
        students_txt.write(str(d) + '\n')  # 将字典按字符串形式写入文件
    students_txt.close()

# ==================================================================================


def insert():
    student_list = []  # 要插入的学生列表
    while True:

        ID = input("输入学生ID（例如1001）：")
        if ID == '':
            break

        name = input("输入学生姓名：")
        if name == '':
            break

        try:
            English = int(input("请输入英语成绩："))
            Python = int(input("请输入Python成绩："))
            C = int(input("输入C语言成绩："))
        except:
            print("\033[1;31m输入信息有误，需要输入整数!\033[0m")
            continue

        student = {'ID': ID, 'name': name,
                   'English': English, 'Python': Python, 'C': C}
        student_list.append(student)  # 学生字典信息添加到学生列表
        input_mark = input("\n是否继续添加？（y/n）：")
        if input_mark == 'y':
            print('\n')
            continue
        else:
            # -------------------学生信息保存到文件中-----------------------
            save(student_list)  # 此时的student_list是存储着字典的列表
            print('\n', "\033[1;31m学生信息录入完成!\033[0m")
            break


if __name__ == "__main__":
    pass
