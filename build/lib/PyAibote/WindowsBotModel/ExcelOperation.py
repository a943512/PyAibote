import re
import json

class ExcelOperation:
    """
        EXCEL操作
        EXCEL operation
    """

    def open_excel(self, excel_path: str) -> dict:
        """
            获取Excel对象
            Get Excel objects

            excel_path: excle路径
            return: excel对象或者None

            excel_path: excle path
            return: excel object or None
        """
        response = self.SendData("openExcel", excel_path)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return json.loads(response)

    def open_excel_sheet(self, excel_object: object, sheet_name: str) -> str:
        """
            打开excel表格
            Open excel table

            excel_object: excel对象
            sheet_name: 表名
            return: 成功返回sheet对象，失败返回None

            Excel_object: excel object
            Sheet_name: table name
            Return: the sheet object is returned successfully, and None is returned on failure
        """
        response = self.SendData("openExcelSheet", excel_object['book'], excel_object['path'], sheet_name)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return response

    def save_excel(self, excel_object: object) -> bool:
        """
            保存excel文档
            Save excel document

            excel_object: excel对象
            return: True或者False

            excel_object: excel object
            return: True or False
        """
        return "true" in self.SendData("saveExcel", excel_object['book'], excel_object['path']) 

    def write_excel_num(self, excel_object: object, row: int, col: int, value: int) -> bool:
        """
            写入数字到excel表格
            Write numbers to excel tables

            excel_object: excel对象
            row: 行
            col: 列
            value: 写入的值
            return: True或者False

            excel_object: excel object
            row: row
            col: column
            value: the value written
            return: True or Fals
        """
        return "true" in self.SendData("writeExcelNum", excel_object, col, row, value) 

    def write_excel_str(self, excel_object: object, row: int, col: int, str_value: str) -> bool:
        """
            写入字符串到excel表格
            Write a string to an excel table

            excel_object: excel对象
            row: 行
            col: 列
            str_value: 写入的值
            return: True或者False

            excel_object: Excel object
            row: row
            col: col
            str_value: Written value
            return: True or False
        """
        return "true" in self.SendData("writeExcelStr", excel_object, row, col, str_value)

    def read_excel_num(self, excel_object: object, row: int, col: int) -> float:
        """
            读取excel表格数字
            Read excel table numbers

            excel_object: Excel object
            row: row
            col: col
            return: The number read
        """
        response = self.SendData("readExcelNum", excel_object, col, row)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return float(response)

    def read_excel_str(self, excel_object: object, row: int, col: int) -> str:
        """
            读取excel表格字符串
            Read excel table string

            excel_object: Excel object
            row: row
            col: col
            return: Read character
        """
        response = self.SendData("readExcelStr", excel_object, row, col)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def remove_excel_row(self, excel_object: object, row_first: int, row_last: int) -> bool:
        """
            删除excel表格行
            Delete excel table rows

            excel_object: excel对象
            row_first: 起始行
            row_last: 结束行
            return: True或者False

            excel_object: Excel object
            row_first: Starting line
            row_last: End line
            return: True or False
        """
        return "true" in self.SendData("removeExcelRow", excel_object, row_first, row_last)

    def remove_excel_col(self, excel_object: object, col_first: int, col_last: int) -> bool:
        """
            删除excel表格列
            Delete excel table columns

            excel_object: excel对象
            col_first: 起始列
            col_last: 结束列
            return: True或者False

            excel_object: Excel object
            col_first: Starting column
            col_last: End column
            return: True or False 
        """
        return "true" in self.SendData("removeExcelCol", excel_object, col_first, col_last) 

