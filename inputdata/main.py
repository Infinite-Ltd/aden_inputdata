from inputdata.common.dbHandler import DBHander
from inputdata.common.excelHander import ExcelHandler

dbName = 'testcase'
dbhandler = DBHander('127.0.0.1', 'root', '1234', dbName)
excelHandler = ExcelHandler('c.xlsx')


dbhandler.genSQLbySheetName('performance3',excelHandler.getColumnName())
dbhandler.insert_datas_to_mysql(excelHandler.get_all_data_of_excel(), 'performance')