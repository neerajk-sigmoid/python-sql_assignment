import logging
from question_1 import Question_1
from question_2 import Question_2
from question_3 import Question_3
from question_4 import Question_4
import psycopg2

#setting path in logger
logging.basicConfig(filename='status_update.log',filemode='w',level=logging.DEBUG)

# Establishing connection with database
class Config_database:
    #function to connect the database
    def connect(self):
        try:
            self.connection = psycopg2.connect("dbname=postgres user=postgres password=sigmoid")
            self.cursor=self.connection.cursor()
            logging.info("connected to database")
            return self.cursor
        except Exception as e:
            logging.error("error in connecting to database")
            raise Exception(e)

    #function to commit the operations
    def commit(self):
        self.connection.commit()
        logging.info("Operations commited")
        self.connection.close()

#Main class to carry out all the given tasks
class Main:
    def __init__(self):
        self.db=Config_database()

     #function to run all the solution function of every task
    def solution(self):
        try:
            self.cursor = self.db.connect()
            self.q1 = Question_1()
            self.q1.solution(self.cursor)
            self.q2 = Question_2()
            self.q2.solution(self.cursor)
            self.q3 = Question_3()
            self.q3.solution(self.cursor)
            self.q4 = Question_4()
            self.q4.solution(self.cursor)
            self.db.commit()
        except Exception as e:
            logging.error(e)
            return False
        else:
            logging.info("all operations run successfully")
            return True
solve=Main()
solve.solution()