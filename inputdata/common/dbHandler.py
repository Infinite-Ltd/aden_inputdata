import pymysql
import traceback

class DBHander:

    def __init__(self, dburl, username, password, dbName, charset='utf8', port=3306):
        self.conn = pymysql.connect(host=dburl, port=port,  user=username, password=password, database=dbName, charset=charset)
        self.curs = self.conn.cursor()
        self.sheets = []


    def createTableByExcel(self, sql):

        self.curs.execute(sql)

    def insert_datas_to_mysql(self, data_tuples, table_name):

        for data_tuple in data_tuples:
            try:
                sql = 'insert into '+table_name+'('+','.join(self.sheets) + ') values (' + ','.join(data_tuple)+')'
                print(sql)
                self.curs.execute(sql)
                return True
            except:
                print('**********************************insert data :'+ str(data_tuple)+'fail!')
                traceback.print_exc()
                return False


    def genSQLbySheetName(self, tableName, sheets):

        self.sheets = sheets
        startStr = 'create table '+tableName+'( id int(10) primary key auto_increment, '
        sqlList = []

        for value in sheets:
            sqlList.append(value+' varchar(400)')

        sqlStr = startStr + ' ,'.join(sqlList) + ', result varchar(20))'  #拼接sql
        print(sqlStr+'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        try:
            self.curs.execute(sqlStr)
            return True
        except:
            print('create table failed')
            traceback.print_exc()
            return False

