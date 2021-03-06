import os

# 学生信息管理系统
filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择'))
        if choice in range(8):
            if choice == 0:
                answer = input('您确定要退出系统吗？Y/N')
                if answer == 'y' or answer == 'y':
                    print('谢谢使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def insert():
    student_list = []
    while True:
        id = input('请输入ID（1001）')
        if not id:
            break
        name = input('请输入姓名')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩'))
            math = int(input('请输入数学成绩'))
            python = int(input('请输入python成绩'))
        except:
            print('请输入整数')
            continue
        student = {'id': id, 'name': name, 'english': english, 'math': math, 'python': python}
        student_list.append(student)
        answer = input('continue:Y/N')
        if answer == 'Y' or answer == 'y':
            continue
        if answer == 'N' or answer == 'n':
            break
    save(student_list)
    print('information is saved successfully')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    stu_query = []
    while True:
        if os.path.exists(filename):
            mode = input('按id查找请输入1；按姓名查找请输入2')
            if mode == '1':
                stu_id = input('请输入学生id')
                with open(filename, 'r', encoding='utf-8') as rfile:
                    stu_table = rfile.readlines()
                    for item in stu_table:
                        d = dict(eval(item))
                        if d['id'] == stu_id:
                            stu_query.append(d)
            elif mode == '2':
                stu_name = input('请输入学生姓名')
                with open(filename, 'r', encoding='utf-8') as rfile:
                    stu_table = rfile.readlines()
                    for item in stu_table:
                        d = dict(eval(item))
                        if d['name'] == stu_name:
                            stu_query.append(d)
            else:
                print('输入有误')
                search()
            # 显示结果
            show_stu(stu_query)
            # 清空列表
            stu_query.clear()
            answer = input('是否继续？Y/N\n')
            if answer == 'Y' or answer == 'y':
                continue
            else:
                break
        else:
            print('暂无学生信息')
            return


def delete():
    while True:
        stu_id = input('请输入学生id')
        if stu_id != ' ':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8')as file:
                    stu_old = file.readlines()
            else:
                stu_old = []
            flag = False
            if stu_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in stu_old:
                        d = dict(eval(item))
                        if d['id'] != stu_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{stu_id}的学生信息已经被删除')
                    else:
                        print(f'没有找到id为{stu_id}的学生')
        else:
            print('五学生信息')
            break
        show()
        answer = input('是否继续删除：Y|N\n')
        if answer == 'Y' or answer == 'y':
            continue
        else:
            break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu_old = rfile.readlines()
    else:
        return
    stu_id = input('请输入修改id')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in stu_old:
            d = dict(eval(item))
            if d['id'] == stu_id:
                print('存在该学生，可以修改')
                while True:
                    try:
                        d['name'] = input('请输入姓名')
                        d['english'] = input('请输入英语成绩')
                        d['math'] = input('请输入数学成绩')
                        d['python'] = input('q请输入python成绩')
                    except:
                        print('输入信息有误')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功')
        print('不存在该学生')
        answer = input('是否继续修改Y/N')
        if answer == 'Y' or answer == 'y':
            modify()


def sort():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu = rfile.readlines()
        stu_dict = []
        for item in stu:
            stu_dict.append(dict(eval(item)))
    else:
        print('暂无学生信息')
        return
    mode_tag = False
    mode = input('升序排序输入1；降序排序输入2')
    if mode == '1':
        mode_tag = False
    elif mode == '2':
        mode_tag == True
    else:
        print('输入有误')
        sort()
    sort_tag = input('按英语成绩排序输入1；按数学成绩排序输入2；按python成绩排序输入3；按总成绩排序输入4')
    if sort_tag == '1':
        stu_dict.sort(key=lambda x: int(x['english']), reverse=mode_tag)
    elif sort_tag == '2':
        stu_dict.sort(key=lambda x: int(x['math']), reverse=mode_tag)
    elif sort_tag == '3':
        stu_dict.sort(key=lambda x: int(x['python']), reverse=mode_tag)
    elif sort_tag == '4':
        stu_dict.sort(key=lambda x: int(x['english']) + int(x['math']) + int(x['python']), reverse=mode_tag)
    else:
        print('输入有误。')
        sort()
    # 显示结果
    show_stu(stu_dict)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu = rfile.readlines()
            if stu:
                print('一共有{}学生'.format(len(stu)))
            else:
                print('暂无学生信息')
    else:
        print('暂无学生信息')


def show():
    stu_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu = rfile.readlines()
        for item in stu:
            stu_list.append(eval(item))
        if stu_list:
            show_stu(stu_list)
    else:
        print('暂无学生信息')


def show_stu(lst):
    if len(lst) == 0:
        print('无信息，无数据显示')
        return
    # 标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', '数学成绩', 'Python成绩', '总成绩', ))
    # 内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item['id'],
                                 item['name'],
                                 item['english'],
                                 item['math'],
                                 item['python'],
                                 int(item['english']) + int(item['math']) + int(item['python'])))


def menu():
    print('==============================学生信息管理系统============================')
    print('---------------------------------功能菜单--------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')


if __name__ == '__main__':
    main()
