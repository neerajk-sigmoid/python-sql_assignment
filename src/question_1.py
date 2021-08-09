import xlsxwriter
import logging

#setting path in logger
logging.basicConfig(filename='status_update.log',filemode='w',level=logging.DEBUG)

class Question_1:

    def get_column(self):
        return ["Employee no","Employee name","Manager"]

    #function to query the table to get Employee name,Employee no and Manager name
    def solution(self, cursor):
        try:
            self.cursor=cursor
            self.cursor.execute("select emp1.empno,emp1.ename,(select emp2.ename from emp as emp2 where emp1.mgr=emp2.empno) from emp as emp1")
            data= self.cursor.fetchall()

            #writing to xlsx file
            with xlsxwriter.Workbook('Employee detail.xlsx') as workbook:
                worksheet = workbook.add_worksheet()
                worksheet.write(0, 0, 'Employee no')
                worksheet.write(0, 1, 'Employee name')
                worksheet.write(0, 2, 'Manager')
                for row_num, d in enumerate(data,start=1): #starting from index 1 as index 0 contains column names
                    worksheet.write_row(row_num, 0, list(d))
            logging.info("question 1 executed successfully")
        except Exception as e:
            logging.error('error in executing question 1')
            raise Exception(e)