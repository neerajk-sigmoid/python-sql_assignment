import unittest
from src.main import Main
from question_1 import Question_1
from question_2 import Question_2
from question_3 import Question_3
from question_4 import Question_4
class MainTest(unittest.TestCase):
    def test_the_execution_of_main(self):
        self.solve=Main()
        self.assertEqual(self.solve.solution(),True)

    def test_question_1_columns(self):
        self.q1=Question_1()
        self.columns=self.q1.get_column()
        self.assertTrue("Employee name" in self.columns)
        self.assertTrue("Manager" in self.columns)
        self.assertTrue("Employee no" in self.columns)

    def test_question_2_columns(self):
        self.q2=Question_2()
        self.columns=self.q2.get_column()
        self.assertTrue("Employee no" in self.columns)
        self.assertTrue("Employee name" in self.columns)
        self.assertTrue("Department" in self.columns)
        self.assertTrue("Experience" in self.columns)
        self.assertTrue("Total compensation" in self.columns)

    def test_table_created_in_question_3(self):
        self.q3= Question_3()
        self.assertEqual(self.q3.flag,True)

    def test_table_created_in_question_4(self):
        self.q4 = Question_4()
        self.assertEqual(self.q4.flag, True)
