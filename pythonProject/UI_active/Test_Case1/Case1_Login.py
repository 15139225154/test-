import json
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from UI_active.BASE_PAGE.base_page import BasePage
from UI_active.common.common_date import Yaml_Case1


class Case_login_page(BasePage):


    click_page_senior = (By.XPATH, "//*[@id='details-button']")
    click_page_continue = (By.XPATH, "//*[@id='proceed-link']")
    username = (By.XPATH, "//input[@name='username']")
    password = (By.XPATH, "//input[@name='password']")
    click_login = (By.XPATH, "//button/span/span")
    click_select = (By.XPATH, "//ul[3]/li[1]/span")
    send_text = (By.XPATH, "//input[@placeholder='Search']")
    click_time = (By.XPATH, "//*[@id='QuickSelectPopover']/div/button")
    choice_time = (By.XPATH, "//button[@data-test-subj='superDatePickerCommonlyUsed_Last_30 days']")
    choice_chage = (By.XPATH, "//discover-index-pattern-select/div/div[2]/span/button/span/span")
    choice_chage1 = (By.XPATH, "//div/div/button[@role='option'][8]")
    refresh = (By.XPATH, "//span[@class ='euiButton__text euiSuperUpdateButton__text']")

    #登录
    def login(self):
        self.Locator(self.click_page_senior).click()
        self.Locator(self.click_page_continue).click()
        sleep(5)
        self.Locator(self.username).send_keys(Yaml_Case1()['账号'])
        self.Locator(self.password).send_keys(Yaml_Case1()['密码'])
        self.Locator(self.click_login).click()
        sleep(5)
    #进入查询页面
    def nyggqxj_page(self,text01):
        #判断元素是否存在截图
        res = self.isElementExist(self.click_select)
        self.JP(res,'登录失败')
        #查询
        self.Locator(self.click_select).click()
        sleep(3)
        self.Locator(self.choice_chage).click()
        self.Locator(self.choice_chage1).click()
        sleep(3)
        self.Locator(self.send_text).send_keys(text01)
        self.Locator(self.click_time).click()
        self.Locator(self.choice_time).click()
        self.Locator(self.refresh).click()
        sleep(5)
    #获取能源关岗url
    click_list = (By.XPATH, "//tr/td/button/icon/../../../td[3]/div/span/dl/dd[1]/span[1]")
    def nyggqxj_url(self):

        txs = self.Locators(self.click_list)
        for i in txs:
            ii = json.loads(i.text)
            print(ii)
            if ii['appName'] == '化小易':
                get_url = ii['pageUrl']
                self.driver.get(get_url)
                sleep(5)
                break
            else:
                pass
        self.JP(False,'能源关岗')

if __name__ == '__main__':
    lo = Case_login_page(Yaml_Case1()['浏览器'],Yaml_Case1()['url'])
    lo.login()
    lo.nyggqxj_page(Yaml_Case1()['查询条件'])
    lo.nyggqxj_url()
    sleep(3)
    lo.quit_browser()