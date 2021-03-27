from python_console_menu import AbstractMenu, MenuItem
import subprocess
import sys


def run(cmd):
    file = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return file


def student():
    print('请输入要统计的班级名称')
    classname = sys.stdin.readline().strip()
    command = 'csvgrep -c 班级 -r ' + classname + ' data.csv | csvstat --count'
    csv = run(command)
    print(csv.stdout.read())


def search():
    print("请输入要查询的学生姓名：")
    name = sys.stdin.readline().strip()
    command = "csvgrep -c 姓名 -r " + name + " data.csv"
    csv = run(command)
    line = csv.stdout.readline().strip()
    sys.stdout.flush()
    line = csv.stdout.readline().strip()
    if line is not '':
        print("已找到")
        return True
    else:
        print("未找到")
        return False


def status():
    print('请输入要统计的班级')
    classname = sys.stdin.readline().strip()
    print('请输入要统计的课程')
    course = sys.stdin.readline().strip()
    command = 'csvgrep -c 班级 -r ' + classname + ' data.csv | csvgrep -c 选课 -r ' + course
    csv = run(command)
    print(csv.stdout.read())


class MainMenu(AbstractMenu):
    def __init__(self):
        super().__init__("欢迎使用Csv集成操作系统")

    def initialise(self):
        self.add_menu_item(MenuItem(100, "退出").set_as_exit_option())
        self.add_menu_item(MenuItem(101, "查询学生", lambda: search()))
        self.add_menu_item(MenuItem(102, "统计班级学生数", lambda: student()))
        self.add_menu_item(MenuItem(103, "查询班级中选课情况", lambda: status()))


if __name__ == '__main__':
    mainMenu = MainMenu()
    mainMenu.display()
