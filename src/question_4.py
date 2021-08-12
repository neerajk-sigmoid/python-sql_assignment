import xlsxwriter
import logging

#setting path in logger
logging.basicConfig(filename='status_update.log',filemode='w',level=logging.DEBUG)
'''class Question_4 is not commented'''
class Question_4:
    flag=True
    #function to find the Department name,Department no and compensation department wise
    def solution(self, cursor):
        try:
            self.cursor=cursor
            #joining the table created from Employee compensation.xlsx file(backup_table) and dept table
            self.cursor.execute(""" select a.deptno,b.department,b.compensation from dept as a
                                    inner join
                                    (select department,sum(total_compensation)as compensation from backup_table
                                      group by department)as b
                                      on b.department=a.dname""")
            data= self.cursor.fetchall()

            #writing to Department detail.xlsx file
            with xlsxwriter.Workbook('Department Detail.xlsx') as workbook:
                worksheet = workbook.add_worksheet()
                worksheet.write(0, 0, 'Department no')
                worksheet.write(0, 1, 'Department name')
                worksheet.write(0, 2, 'Compensation')
                for row_num, d in enumerate(data,start=1): #starting from index 1 as index 0 contains column names
                    worksheet.write_row(row_num, 0, list(d))
            logging.info("question 4 executed successfully")
        except Exception as e:
            self.flag=False
            logging.error('error in executing question 4')
            raise Exception(e)
