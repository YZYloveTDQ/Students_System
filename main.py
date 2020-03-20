# _*_ coding:utf-8   _*_
"""运行程序后，首先进入功能菜单
   1. menu()函数使用print（）输出功能菜单
   2. 用户输入功能对应的序号
   3. 程序根据序号调用不同的函数"""
from students_system.menu import menu
from students_system.insert import insert, save
from students_system.search import search
from students_system.delete import delete
from students_system.modify import modify
from students_system.sort import sort
from students_system.total import total
from students_system.show import show


def main():
    mark = True  # 标记是否退出程序
    function_number = [1, 2, 3, 4, 5, 6, 7, 0]
    while mark:
        menu()  # menu（）函数显示功能菜单
        option_number = int(input("\033[1;33m输入序号：\033[0m"))
        if option_number in function_number:

            if option_number == 0:
                print("\033[1;31m\n退出管理系统!\033[0m")
                break

            elif option_number == 1:
                insert()  # 调用插入函数

            elif option_number == 2:
                search()  # 查询函数

            elif option_number == 3:
                delete()  # 调用删除函数

            elif option_number == 4:
                modify()  # 调用修改函数

            elif option_number == 5:
                sort()  # 排序函数

            elif option_number == 6:
                total()  # 统计函数

            elif option_number == 7:
                show()  # 显示所有学生信息


if __name__ == "__main__":
    main()
