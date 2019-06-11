import pymysql

def createTableByExcel(sql, dburl, username, password, dbName, charset='utf8'):



    conn = pymysql.connect(dburl, username, password, dbName, charset)
    cur = conn.cursor()
    cur.execute(sql)


def genSQLbySheetName(tableName, sheets):

    startStr = 'create table '+tableName+'( uuid() int(30),'
    sqlList = []

    for value in sheets:
        sqlList.append(value+' varchar(400)')

    sqlStr = startStr + ' ,'.join(sqlList) + ')'  #拼接sql

    return sqlStr