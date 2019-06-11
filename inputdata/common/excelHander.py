from xlrd import open_workbook


class ExcelHandler:

    def __init__(self, excel_name):
        self.excel_name = excel_name
        wb = open_workbook(self.excel_name)
        defalutSheet = wb.get_sheet(0)
        self.table_head = defalutSheet.row_values(0)

    def getColumnName(self):

     return self.table_head

    def get 