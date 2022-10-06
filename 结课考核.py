# -*- coding:utf-8 -*-
def conn():
    import cx_Oracle as cx;
    conn = cx.connect('bbbb/123456@localhost:1521/ORCL', encoding='UTF-8', nencoding='UTF-8');
    return conn;

def car_insert():
    while True:
        conn1 = conn();
        cur_car_1 = conn1.cursor();
        sql_car_1 = 'select * from car';
        cur_car_1.execute(sql_car_1);
        row_car_1 = cur_car_1.fetchall();
        print(row_car_1)
        brand_1 = input("请输入汽车品牌：");
        if brand_1 == "":
            break;
        else:
            model_1 = input("请输入汽车型号：");
            price_1 = input("请输入汽车单价：");
            fld_1 = input("请输入厂商编号：");
            if fld_1 != "":
                cur_car_2 = conn1.cursor();
                sql_car_2 = 'insert into car(id,brand,model,price,fld) values(:id,:brand,:model,:price,:fld)';
                cur_car_2.execute(sql_car_2, (0, brand_1, model_1, price_1, fld_1));
                conn1.commit();
                cur_car_1.close();
                cur_car_2.close();
                break;
            else:
                print("请重新输入！");


def car_select():
    while True:
        conn2 = conn();
        print("请输入汽车品牌，"
              "如果输入为空则可观看所有汽车，"
              "输入ESC为退出");
        brand_2 = input("请输入要查询的汽车品牌：");
        if brand_2 == "":
            cur_car_3 = conn2.cursor();
            sql_car_3 = 'select * from car';
            cur_car_3.execute(sql_car_3);
            row_car_2 = cur_car_3.fetchall();
            print(row_car_2);
            cur_car_3.close;
        elif brand_2 == "ESC":
            break;
        elif brand_2 != "":
            cur_car_4 = conn2.cursor();
            sql_car_4 = 'select * from car where brand = :brand';
            cur_car_4.execute(sql_car_4, (brand_2));
            row_car_3 = cur_car_4.fetchall();
            print(row_car_3);
            cur_car_4.close;



def car_delete():
    while True:
        conn3 = conn();
        print("请输入要删除的汽车的品牌以及型号");
        brand_3 = input("请输入汽车品牌：");
        if brand_3 == "":
            break;
        elif brand_3 != "":
            model_3 = input("请输入汽车型号：");
            cur_car_5 = conn3.cursor();
            sql_car_5 = 'select * from car where brand = :brand and model = :model';
            cur_car_5.execute(sql_car_5, (brand_3, model_3));
            row_car_3 = cur_car_5.fetchall();
            cur_car_5.close();
            if row_car_3 != []:
                cur_car_6 = conn3.cursor();
                sql_car_6 = 'delete from car where brand = :brand and model = :model'
                cur_car_6.execute(sql_car_6, (brand_3, model_3));
                print("删除成功");
                conn3.commit();
                cur_car_6.close();
                break;
            else:
                print("数据库中没有此数据");
                break;

def user_insert():
    while True:
        conn4 = conn();
        cur_user_0  =conn4.cursor();
        sql_user_0 = 'select * from firm';
        cur_user_0.execute(sql_user_0);
        row_user_0 = cur_user_0.fetchall();
        print(row_user_0);
        print("请输入厂商名称(名称不可重复)、是否是国内公司以及简介");
        name_1 = input("请输入厂商名称：");
        if name_1 == "":
            break;
        else:
            domestic_1 = input("请输入是或否：");
            summary_1 = input("请输入简介：");
            cur_user_1 = conn4.cursor();
            sql_user_1 = 'insert into firm(id,name,domestic,summary) values(0,:name,:domestic,:summary)';
            cur_user_1.execute(sql_user_1,(name_1,domestic_1,summary_1));
            conn4.commit();
            cur_user_1.close;
            break;

def user_select():
    while True:
        conn5 = conn();
        print("请输入厂商名称，"
              "如果输入为空则可观看所有厂商，"
              "输入ESC为退出");
        name_2 = input("请输入厂商名称：");
        if name_2 == "":
            cur_user_2 = conn5.cursor();
            sql_user_2 = 'select * from firm';
            cur_user_2.execute(sql_user_2);
            row_user_1 = cur_user_2.fetchall();
            print(row_user_1);
            cur_user_2.close;
        elif name_2 == "ESC":
            break;
        else:
            cur_user_3 = conn5.cursor();
            sql_user_3 = 'select * from firm where name = :name';
            cur_user_3.execute(sql_user_3,(name_2));
            row_user_2 = cur_user_3.fetchall();
            print(row_user_2);
            cur_user_3.close;

def user_delete():
    while True:
        conn6 = conn();
        print("请输入要删除的厂商名称")
        name_3 = input("请输入厂商名称：");
        if name_3 == "":
            break;
        else:
            cur_user_4 = conn6.cursor();
            sql_user_4 = 'select * from firm where name = :name';
            cur_user_4.execute(sql_user_4,(name_3));
            row_user_3 = cur_user_4.fetchall();
            cur_user_4.close();
            if row_user_3 == []:
                print("没有该厂商相关信息");
            else:
                cur_user_5 = conn6.cursor();
                sql_user_5 = 'delete from firm where name = :name';
                cur_user_5.execute(sql_user_5,(name_3));
                print("删除成功");
                conn6.commit();
                cur_user_5.close();
                break;

def Information_maintenance_car():
    while True:
        print("     1.新增汽车     ");
        print("     2.查询汽车     ");
        print("     3.删除汽车     ");
        print("      4.退出        ");
        car_choice = input("请输入操作序号：");
        if car_choice == "1":
            car_insert();
        elif car_choice == "2":
            car_select();
        elif car_choice == "3":
            car_delete();
        elif car_choice =="4":
            print("成功退出");
            break;
        else:
            print("无效选项");

def Information_maintenance_user():
    while True:
        print("     1.新增厂商     ");
        print("     2.查询厂商     ");
        print("     3.删除厂商     ");
        print("      4.退出        ");
        user_choice = input("请输入操作序号：");
        if user_choice == "1":
            user_insert();
        elif user_choice == "2":
            user_select();
        elif user_choice == "3":
            user_delete();
        elif user_choice =="4":
            print("成功退出");
            break;
        else:
            print("无效选项");

while True:
    print("     主界面     ");
    print(" 1.汽车信息维护 ");
    print(" 2.厂商信息维护 ");
    print("     3.退出     ");
    choice = input("请输入操作序号：");
    if choice == "1":
        Information_maintenance_car();
    elif choice == "2":
        Information_maintenance_user();
    elif choice == "3":
        print("成功退出");
        break;
    else:
        print("无效选项");

