from xlrd import open_workbook


class ExcelHandler:

    def __init__(self, excel_name):
        self.excel_name = excel_name
        self.wb = open_workbook(self.excel_name)
        defalutSheet = self.wb.sheets()[0]
        self.table_head = defalutSheet.row_values(0)
        self.datas = []

    def getColumnName(self):

     return self.table_head

    def get_all_data_of_excel(self):

        for sheetname in self.wb.sheets():
            nrows = sheetname.nrows
            print(str(nrows)+'^^^^^^^^^^^^^^^^^^^^^^^^^')
            for i in range(1,nrows):
                self.datas.append(sheetname.row_values(i))
                print(sheetname.row_values(i))
        print(self.datas)
        return self.datas
