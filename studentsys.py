#-*- coding:utf-8 -*-
# Python学习
#时间：2022/7/19 15:36
#文件名：studentsys.py
import os
filename='student.txt'  #该文件是用来存储学生成绩
def main():
    while True:
        menu()
        choice=int(input('请选择你所想使用的功能'))
        if choice in[0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用!!!')
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
            else:
                show()
        else:
            print('系统中暂无此功能，请重新选择')
            continue
def menu():
    print('===============================学生管理系统===================================')
    print('---------------------------------功能菜单-------------------------------------')
    print('\t\t\t\t\t1、录入学生成绩')
    print('\t\t\t\t\t2、查找学生成绩')
    print('\t\t\t\t\t3、删除学生成绩')
    print('\t\t\t\t\t4、修改学生成绩')
    print('\t\t\t\t\t5、排序')
    print('\t\t\t\t\t6、统计学生总人数')
    print('\t\t\t\t\t7、显示所有学生的成绩信息')
    print('\t\t\t\t\t0、退出系统')
    print('------------------------------------------------------------------------------')
def insert():   #在选择了选项1的情况下调用insert函数
    students_list=[]  #需要有一个存放每个学生成绩的列表
    while True:
        id=input('请输入添加的学生id(如1001)')
        if not id:   #空字符串的布尔值是False，not Flase就是True，这里就意思是如果id是布尔值为True的值，则结束这个循环跳转回选择界面
            break
        name=input('请输入添加的学生姓名')
        if not name:  #同上
            break
        try:
            English=int(input('请输入学生的英语成绩'))
            Python=int(input('请输入学生的Python成绩'))
            Java=int(input('请输入学生的Java成绩'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        #将录入的学生成绩保存到字典中，以便后面存入到文件中
        students={'id':id,'name':name,'English':English,'Python':Python,'Java':Java}
        #将录入的学生成绩保存到列表中
        students_list.append(students)
        #录入完成绩后询问用户是否需要继续录入成绩
        answer=input('是否还要继续录入成绩')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    #调用save函数，将录入的成绩保存到文件studnet.txt中
    save(students_list)
    print('学生成绩录入完毕!!!')
def save(list):  #括号里得给参数，要不然存放数据的列表不能保存到文件里
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    '''这里使用try...except异常处理，因为这个文件一开始不一定存在，在a模式中如果文件不存在'''
    for item in list:    #将列表里的数据遍历写到文件中
        stu_txt.write(str(item)+'\n')    #每一个学生的成绩写入完后换行接着下一个
    stu_txt.close()
def search():   #在选择了选项2的情况下调用search函数
    student_query=[]   #有可能有同名的，定义一个列表放在这里面
    while True:
        id=''
        name=''
        #首先要判断txt文件是否存在，有这个文件才能进行下面的查询操作
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2')
            if mode == '1':
                id=input('请输入学生id')
            elif mode == '2':
                name=input('请输入学生的姓名')
            else:
                print('您的输入有误，请重新输入!!!')
                search()    #这里可以写break，也可以像这样写引用函数本身
            with open(filename,'r',encoding='utf-8') as rfile:   #判断完是通过id还是姓名后，就要开始修改数据了，第一步就是要把文件中的数据拿出来放到一个变量里
                student=rfile.readlines()
                for item in student:    #遍历列表，将列表中一个个字典变成字符串类型数据
                    d=dict(eval(item))   #字符串类型转换成字典
                    if id !='':   #id不是空值走这里输出内容，后面可以把这个列表通过show_student函数查看信息
                        if d['id'] == id:    #如果通过id查找到了该学生，就放到一开始定义的空列表中
                            student_query.append(d)   #括号里面得加上d
                    elif name != '':   #name不是空值走这里添加进列表里，后面可以把这个列表通过show_student函数查看信息
                        if d['name'] == name:
                            student_query.append(d)
                        else:
                            print('未查找到该学生的成绩信息!!')
                            break
                    else:
                        print('未查找到该学生的成绩信息!!')
                        break
            #显示查询数据
            show_student(student_query)
            #第二次查询时防止有数据干扰，需要清空列表
            student_query.clear()
            answer=input('您是否需要继续查询信息? y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息!!!')
            return
def show_student(list):
    #显示查询结果 是按照一定的格式显示的 所以这里要使用格式化字符串
    if len(list) == 0:
        print('没有查询到学生信息，无数据显示!!!')
        return
    #查到的话定义标题的显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('id','姓名','英语成绩','Python成绩','Java成绩','总成绩')) #数字格式化，可以参考第九章多分demo13，具体方法：https://www.runoob.com/python/att-string-format.html
    #定义信息内容的显示格式   大括号{}是表明被替换的字符串
    format_data='{:^6}\t{:^12}\t{:^10}\t{:^18}\t{:^12}\t{:^10}'    #这里是将字符串的格式设置好同一放在了一个变量里，下面再用format方法调用的话直接就可以写变量名.format(所要替换的字符串)  (括号里面的东西可以是中英文、数字等，多个参数的话中间用逗号隔开)
    for item in list:
        print(format_data.format(item.get('id'),        #.get()函数是Python字典用于返回键值的函数，用item[键]也行
                                 item.get('name'),
                                 item.get('English'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 int(item.get('English'))+int(item.get('Python'))+int(item.get('Java')
                                )))
def delete():   #在选择了选项3的情况下调用delete函数
#学生管理系统的删除是这样实现的，就是先将所有学生数据都提取出来，
#然后再将所有数据都写回到文件夹内(除了要删除的学生的信息)，这样就相当于把这个学生的信息删除了
    while True:
        student_id = input('请输入要删除的学生的id')
        if student_id != '':   #如果是空字符串返回while True继续循环
            if os.path.exists(filename):  # 如果存在则用上下文管理器打开文件并读取里面的所有信息
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()  # 每一行都作为独立的字符串对象，并将这些对象放在列表里返回
            else:
                student_old = []
            flag = False   #标识是否删除
            if student_old:  # 判断student_old这个列表是里面有东西还是以个空列表
                with open(filename, 'w', encoding='utf-8') as wfile:  # 如果文件存在就以只写模式打开student.txt
                    d = []
                    for item in student_old:  # for...in循环遍历出来的是字符串类型数据
                        d = dict(eval(item))  # 将字符串数据转成字典类型  '''eval()方法的作用是执行一个字符串表达式，并返回表达式的值 这里就是用eval方法把字典外面的引号去掉，加不加这个dict都可以，就是防止报错'''
                        if d['id']!=student_id:   #这里的意思是：如果我删除的学生id不是我遍历到的这个id，则就把这个学生的信息重新写回txt文件；如果我删除的学生id是我遍历到的这个id，就走
                                                   #else分支，就相当于我没有把这条数据重新写回txt文件里，就达到了删除效果
                            wfile.write(str(d)+'\n')  #执行了这句话则flag还是false
                        else:
                            flag=True    #代表着我删除的学生id是我遍历到的这个id就走这条分支，不会重新写回txt文件里，表示这条数据被删除了
                    if flag:   #这里是flag=True的情况
                        print(f'id为{student_id}的学生信息已经被删除')
                    else:      #这里是flag=False的情况
                        print(f'没有找到id为{student_id}的学生信息')
            else:    #列表student_old没有数据的情况
                print('没有该学生信息')
                break
            show()    #删除之后要显示现有的所有学生的信息
            answer=input('是否继续删除操作？y/n')
            if answer=='y' or answer=='Y':
                continue
            else:
                break
def modify():   #在选择了选项4的情况下调用modify函数
    show()  #先展示一下所有学生的信息
    if os.path.exists(filename):   #检查文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:
             student_old=rfile.readlines()   #原来的学员数据，列表形式呈现
    else:    #文件不存在直接结束，连文件都没有还怎么改具体的数据
        return
    student_id=input('请输入你想修改的学员的ID')
    if student_id !='':
        with open(filename,'w',encoding='utf-8') as wfile:
            for item in student_old:
                d=dict(eval(item))    #字符串类型数据转成字典类型
                if d['id'] == student_id:
                    print('已经找到该学生信息，可以修改他的相关信息了!!!')
                    while True:
                        try:
                            d['name'] = input('请输入姓名')
                            d['English'] = int(input('请输入该学员的英语成绩'))
                            d['Python'] = int(input('请输入该学员的Python成绩'))
                            d['Java'] = int(input('请输入该学员的Java成绩'))
                        except:
                            print('输入的成绩有误，请重新输入')   #只要有错误就返回到While True重新循环
                        else:
                            break
                    wfile.write(str(d) + '\n')
                    print('修改成功!!!')
                else:
                    wfile.write(str(d)+'\n')
            answer=input('还要继续修改其他学生信息吗y/n')
            if answer == 'y' or answer == 'Y':
                modify()
            else:
                return

def sort():     #在选择了选项5的情况下调用sort函数
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
            student_new=[]
            for item in student_list:
                d=dict(eval(item))
                student_new.append(d)
    else:
         return   #文件不存在没有排序的必要了
    asc_or_desc=input('请选择(0.升序  1.降序)')
    if asc_or_desc == '0':
        asc_or_desc_bool=False
    elif asc_or_desc == '1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()   #输入的不是0或1的话调用自己从头再来
    #判断完升序还是降序后 设置按照哪个科目进行排序
    mode=input('请选择排序方式(1.按英语成绩排序  2.按Python成绩排序  3.按Java成绩排序  0.按总成绩排序)')
    if mode =='1':
        student_new.sort(key=lambda x : int(x['English']),reverse=asc_or_desc_bool)  #sort()方法的作用就是排序，方法里有两个关键字，一个是key(排序的关键字)，一个是reverse(排序的方式，它的值是Ture(降序)或False(升序))
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['Python']), reverse=asc_or_desc_bool)   #这里使用了隐匿函数lambda，里面的x是一个参数(可以随便写)，这里代表的是字典，后面的x['English]是函数体 他是一个没有函数名的函数
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['Java']), reverse=asc_or_desc_bool)
    elif mode =='0':
        student_new.sort(key=lambda x: int(x['English'])+int(x['Python'])+int(x['Java']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入!!!')
        sort()
    show_student(student_new)
def total():    #在选择了选项6的情况下调用total函数
    #先判断文件是否存在
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
            if student_list !='':
                print('总共有{}名学生成绩'.format(len(student_list)))
            else:
                print('还没有录入学生信息!!!...')
    else:
        print('暂未保存学生数据信息!!!...')
def show():     #在选择了选项7的情况下调用show函数
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student=rfile.readlines()   #数据类型是列表
            for item in student:
                d=dict(eval(item))
                student_list.append(d)
            if student_list:          #这里的if不能写在for循环的下面，不然的话就是先读取列表student里的第一条数据，然后加到空列表里紧接着判断；进行一次输出；
                show_student(student_list) #再回到for循环读第二条数据，第一条数据会显示两遍   原因就是if循环被套在for循环里面了，刚写完第一条数据还没添加第二条数据呢就被拉去执行if语句了
    else:         #调用show_student函数显示信息
        print('暂未保存学生成绩信息!!!...')
if __name__ == '__main__':
    main()
