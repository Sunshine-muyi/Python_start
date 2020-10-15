import os

#学生信息管理系统
filename='student.txt'
def main():
    while True:
        menm()
        choice=int(input('请选择'))
        if choice in range(8):
            if choice==0:
                answer = input('您确定要退出系统吗？Y/N')
                if answer == 'y' or answer == 'y':
                    print('谢谢使用！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
def insert():
    student_list=[]
    while True:
        id=input('请输入ID（1001）')
        if not id:
            break
        name=input('请输入姓名')
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
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    pass
def delete():
    while True:
        stu_id=input('请输入学生id')
        if stu_id!=' ':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8')as file:
                    stu_old=file.readlines()
            else:
                stu_old=[]
            flag=False
            if stu_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in stu_old:
                        d=dict(eval(item))
                        if d['id']!=stu_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{stu_id}的学生信息已经被删除')
                    else:
                        print(f'没有找到id为{stu_id}的学生')
        else:
            print('五学生信息')
            break
        show()
        answer=input('是否继续删除：Y|N\n')
        if answer=='Y' or answer=='y':
            continue
        else:
            break

def modify():

def sort():
    pass
def total():
    pass
def show():
    pass



def menm():
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