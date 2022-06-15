import os

import allure
import pytest
from UI_active.Logger import logger
from UI_active.search_page.conftest import login
from UI_active.TEST_CASE.te_a import asd
from UI_active.common.common_date import Yaml


@allure.feature('一级标签')
class Test_1():
    def setup(self):
        Yaml()
        self.y = asd(Yaml()['浏览器'],Yaml()['url'])
        self.y.login()
        self.y.obtain_text()

    def teardown(self):
        self.y.quit_browser()

    @allure.title('标题1')
    @allure.story('二级标签')
    @pytest.mark.dependency()
    def test_1(self,login):
        with allure.step("动作标记"):
            self.y.driver.get_screenshot_as_file('./Picture/t.png')
            allure.attach.file('./Picture/t.png',attachment_type=allure)


    #@pytest.mark.skip()
    @allure.title('标题2')
    @allure.story('二级标签')
    @pytest.mark.dependency()
    def test_2(self):
        print("pass2")

    #@pytest.mark.skip()
    @allure.title('标题3')
    @allure.story('二级标签')
    @pytest.mark.dependency(depends=['test_1','test_2'])
    def test_3(self):
        pass


if __name__ == '__main__':
    #pytest.main(['-v', 'test_b.py'])
    pytest.main(['-v','test_b.py','--alluredir','./report'])
    os.system('allure generate ./report -o ./ro --clean')

'''
-s： 显示程序中的 print/logging 输出
-v: 丰富信息模式, 输出更详细的用例执行信息
-k： 运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
-q: 简单输出模式, 不输出环境信息
-x: 出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
'''