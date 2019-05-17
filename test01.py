import pymysql
#创建一个数据库连接对象
db = pymysql.connect("127.0.0.1","root","123456","woniuatm_test",charset="utf8")
#创建游标对象
cur = db.cursor()
#执行sql语句
#创建数据库
#sql = "create database woniuatm_test"
#创建表格
# sql ="""create table user_info1(
# id int PRIMARY KEY,
# username VARCHAR(10),
# passwd VARCHAR(20),
# phone_num CHAR(11)
# )engine = Innodb DEFAULT charset = "utf8"
# """
#插入数据  增加数据
# sql = """ insert into user_info values(1,'张三','123456','13478452541'),(2,'李四','123478','13698452541'),
# (3,'李流','125678','13678452541')
# """
#查询数据 查询结果需要重新获取
#sql ="select * from user_info where username='张三'"
sql ="select * from user_info "
#删除表格数据
# sql = "drop table user_info1 "
#修改数据
# sql ="update user_info set passwd = '111111' where username = '李四'"
# 增加表格的列
#sql = "alter table user_info add balance FLOAT"
cur.execute(sql)
#提交事务(手动)
# db.commit()
#获取一条数据  结果为元组
# result = cur.fetchone()
#获取全部数据 结果为元组
result = cur.fetchall()
#获取多条数据  获取指定数量的元组个数  括号里面是查询记录条数
# result = cur.fetchmany(3)
cur.close()
db.close()
print(result)

#初级版数据类函数
#增删改查都行  函数化
def db_operation(sql):
    db = pymysql.connect("127.0.0.1","root","123456","woniuatm_test",charset="utf8")
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()

#针对查询一条语句
def db_queryone(sql):
    db = pymysql.connect("127.0.0.1","root","123456","woniuatm_test",charset="utf8")
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    result = cur.fetchone()
    cur.close()
    db.close()
    return result
#result= db_queryone(sql)


#针对查询多条语句
def db_querymany(sql,num):
    db = pymysql.connect("127.0.0.1","root","123456","woniuatm_test",charset="utf8")
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    result = cur.fetchmany(num)
    cur.close()
    db.close()
    return result
#result = db_querymany(sql,num)

#修改版1
#连接数据库
def create_obj():
    db = pymysql.connect("127.0.0.1","root","123456","woniuatm_test",charset="utf8")
    cur = db.cursor()
    return db,cur

#关闭数据库
def close_obj():
    db,cur = create_obj()
    cur.close()
    db.close()

#增删改查都行  函数化
def db_operation(sql):
    db,cur = create_obj()
    cur.execute(sql)
    db.commit()
    close_obj()

#针对查询一条语句
def db_queryone(sql):
    db,cur = create_obj()
    cur.execute(sql)
    db.commit()
    result = cur.fetchone()
    close_obj()
    return result
#result= db_queryone(sql)


#针对查询多条语句
def db_querymany(sql,num):
    db,cur = create_obj()
    cur.execute(sql)
    db.commit()
    result = cur.fetchmany(num)
    close_obj()
    return result
#result = db_querymany(sql,num)



