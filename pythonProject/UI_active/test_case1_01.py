import os
from time import sleep
import allure
import pytest
from UI_active.Test_Case1.Case1_Login import Case_login_page
from UI_active.common.common_date import Yaml_Case1


@allure.feature('一级标签1')
class Test_Case1_01():

    def setup(self):
        self.lo = Case_login_page(Yaml_Case1()['浏览器'], Yaml_Case1()['url'])
        self.lo.login()
    def teardown(self):
        self.lo.quit_browser()

    @allure.story('二级标签1')
    @allure.title('查询能源关岗请休假')
    def test_01(self):
        self.lo.nyggqxj_page(Yaml_Case1()['查询条件'])
        self.lo.nyggqxj_url()
        sleep(3)

if __name__ == '__main__':
    #pytest.main(['-v', 'test_b.py'])
    pytest.main(['-v','test_b.py','--alluredir','./report'])
    os.system('allure generate ./report -o ./ro --clean')