import xlsxwriter
import logging

#setting path in logger
logging.basicConfig(filename='status_update.log',filemode='w',level=logging.DEBUG)
'''class Question_2 is not commented'''
class Question_2:
'''method is not commented'''
    def get_column(self):
        return ["Employee no","Employee name","Department","Experience","Total compensation"]

     #function to find the Employee no,Employee name,Department name,Experience in months and compensation
    def solution(self,cursor):
        try :
            self.cursor = cursor
            self.cursor.execute("""select e.empno,e.ename,d.dname,jh.months,jh.compensation
            from dept as d
            inner join
    
            (select empno,deptno,ename from emp)as e on e.deptno=d.deptno
            inner join
    
            (select empno,sum(((DATE_PART('year', (case when enddate is not null then enddate else current_date end)::date)-
               DATE_PART('year',startdate ::date))* 12 +(DATE_PART('month',(case when enddate is not null then enddate 
               else current_date end)::date)-
               DATE_PART('month', startdate::date)))*
              (sal+(case when comm is not null then comm else 0 end))) as compensation,
               sum((DATE_PART('year', (case when enddate is not null then enddate else current_date end)::date)
             - DATE_PART('year',startdate ::date))* 12 +(DATE_PART('month',(case when enddate is not null then enddate 
               else current_date end)::date)
              -DATE_PART('month', startdate::date)))as months
              from jobhist
             group by empno)
             as jh
             on e.empno=jh.empno
            """)
            data= self.cursor.fetchall()

            #writing in .xlsx file
            with xlsxwriter.Workbook('Employee compensation.xlsx') as workbook:
                worksheet = workbook.add_worksheet()
                worksheet.write(0, 0, 'Employee no')
                worksheet.write(0, 1, 'Employee name')
                worksheet.write(0, 2, 'Department')
                worksheet.write(0, 3, 'Experience')
                worksheet.write(0, 4, 'Total compensation')
                for row_num, d in enumerate(data, start=1):#starting from index 1 as index 0 contains column names
                    worksheet.write_row(row_num, 0, list(d))
            logging.info("question 2 executed successfully")
        except Exception as e:
            logging.error('error in executing question 2')
            raise Exception(e)
