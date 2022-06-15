import unittest,os
from HTMLTestRunner import HTMLTestRunner


class HTR():
    #a=[TestCase('test_3'),TestCase('test_2')]
    def Suite1(self,a):
        self.suite = unittest.TestSuite()
        self.suite.addTests(a)
    #b=TestCase
    def Suite2(self,b):
        self.suite = unittest.TestSuite()
        self.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(b))
    #c='test_cases.TestCase'
    def Suite3(self,c):
        self.suite = unittest.TestSuite()
        self.suite.addTests(unittest.TestLoader().loadTestsFromName(c))

    def Html_Test_Runner(self):
        repotr_name = '测试报告名称'
        report_title = '测试报告标题'
        report_desc = '测试报告描述'
        report_path = './report/'
        report_file = report_path+'report.html'

        if not os.path.exists(report_path):
            os.mkdir(report_path)
        else:
            pass

        #HTMLTestRunner使用
        with open(report_file,'wb') as report:
            runner = HTMLTestRunner(
                stream=report,title=report_title,description=report_desc)
            runner.run(self.suite)
