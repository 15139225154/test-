#基本页
import ddddocr
from PIL import Image
from selenium import webdriver
import time,os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage(object):
    #初始化
    def __init__(self,browser_tepy,url):
        self.driver = self.Open_Browser(browser_tepy)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.Visit(url)
        time.sleep(3)

    def Visit(self,url):
        self.driver.get(url)

    # 取消黄页 option:选择 argument：论点 diaable：可折叠 infobars：信号棒
    def Option(self):
        option = webdriver.ChromeOptions()
        # 取消黄页
        option.add_argument('diaable-infobars')
        # 无头模式
        option.add_argument('headless')

    #调用浏览器
    def Open_Browser(self,browser_tepy):
        if browser_tepy == 'chrome':
            self.driver = webdriver.Chrome()
            return self.driver
        elif browser_tepy == 'firefox':
            self.driver = webdriver.Firefox()
            return self.driver
        else:
            print('browser_tepy  error')

    #定位元素  *locator：读取元组
    def Locator(self,locator):
        return self.driver.find_element(*locator)
    def Locators(self,locator):
        return self.driver.find_elements(*locator)


    #该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    #flag=旗帜
    def isElementExist(self,locator):
        try:
            self.Locator(locator)
            return True
        except NoSuchElementException as e:
            print('except:',e)
            return False

    #关闭  browser=浏览器
    def quit_browser(self):
        self.driver.quit()

    #页面截图   screenshot =屏幕截图
    def JP(self,res,name):
        if  res == False:
            # if not os.path.exists('./'):
            #     os.mkdir('./Picture')
            self.driver.get_screenshot_as_file(filename='Picture/'+name+'{}.png'.format(time.strftime('%Y年%m月%d日 %H_%M_%S',time.localtime())))
        else:
            pass

    #获取验证码
    def get_screenshot_img(self,input_img,yzm):

        #截图
        self.driver.get_screenshot_as_file(r"./p/a.png")
        #定位验证码
        imgelement = self.Locator(input_img)
        #获取验证码坐标，获取验证码宽和高
        locatinon = imgelement.location
        #print(locatinon)
        size= imgelement.size
        #print(size)
        #获取验证码左顶点坐标
        left = locatinon['x']+255
        top = locatinon['y']+93
        right = left + size['width']+26
        bottm = top + size['height']+12
        #打开截图
        look = Image.open(r'./p/a.png')
        #截取验证码区域
        im = look.crop((left,top,right,bottm))
        #保存图片
        im.save('./p/b.png')

        #读取验证码
        ocr = ddddocr.DdddOcr()
        with open(r'.\p\b.png','rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        print(res)
        self.Locator(yzm).send_keys(res)
        time.sleep(1)
        return res








