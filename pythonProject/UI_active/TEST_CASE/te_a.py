import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# //tr[@class='ant-table-row ant-table-row-level-0']/td[3]
from UI_active.BASE_PAGE.base_page import BasePage
from UI_active.Logger.logger import logger
from UI_active.common.common_date import Yaml


class  asd(BasePage):
    input_1 = (By.XPATH, '//input[@id="normal_login_username"]')
    input_2 = (By.XPATH, '//input[@placeholder="请输入密码"]')
    click_1 = (By.XPATH, '//button[@type="submit"]/span')
    input_img = (By.XPATH,'//div[@class="ant-form-item-control-input-content"]/img')
    yzm = (By.XPATH, '//input[@placeholder="请输入验证码"]')

    def login(self):

        self.Locator(self.input_1).send_keys(Yaml()['账号'])
        self.Locator(self.input_2).send_keys(Yaml()['密码'])
        logger.info('日志：开始登录')
        for n in range(1,5):
            print('输入验证码第{}次'.format(n))
            self.get_screenshot_img(self.input_img,self.yzm)
            self.Locator(self.click_1).click()
            time.sleep(2)
            im = self.img_text()
            print(im)
            if im == False:
                print('验证码错误')
                for m in range(1, 5):
                    self.driver.find_element_by_xpath('//input[@placeholder="请输入验证码"]').send_keys(Keys.BACK_SPACE)
            else:
                break
    def obtain_text(self):
        try:
            a = self.driver.find_element_by_xpath('//div[@id="logo"]/a/h1')
            logger.info('日志：登录成功  title:{}'.format(self.driver.title))
        except:
            logger.info('日志：登录失败  title:{}'.format(self.driver.title))
        # action_chains = ActionChains(self.driver)
        # action_chains.move_to_element(a).perform()
        message = a.text
        print(message)

    def img_text(self):
        try:
            self.driver.find_element_by_xpath('//div[@class="messageTip___3xP-_"][3]')
            return False
        except NoSuchElementException as e:
            #print('except:', e)
            return True

if __name__ == '__main__':
    y = asd(Yaml()['浏览器'],Yaml()['url'])
    y.login()
    y.obtain_text()
    y.quit_browser()






