import pymysql

connect = pymysql.connect(host='localhost', user='root', passwd='root', db='cobweb')
print(connect.query('show tables'))

connect.query('create table if not EXISTS mytb (title CHAR(20) not NULL , keywd CHAR (30))')
print(connect.query('show tables'))

# 插入
# connect.query('insert into mytb(title, keywd) VALUES ("first tile", "first keywd")')

# 提交
connect.commit()

# 获取游标
cursor = connect.cursor()
cursor.execute('select * from mytb')
for i in cursor:
    print('当前是第 {num} 行'.format(num=cursor.rownumber))
    print('标题是: {title}'.format(title=i[0]))
    print('关键词是: {keyword}'.format(keyword=i[1]))

connect.close()


# "select * from naclog_count_info where time = '" + real_time + "'"