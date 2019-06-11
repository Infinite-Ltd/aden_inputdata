from  inputdata.common.dbHandler import genSQLbySheetName, createTableByExcel



testdata = ['testcaseName', 'precase', 'teststep']

print(genSQLbySheetName('testcase', testdata))