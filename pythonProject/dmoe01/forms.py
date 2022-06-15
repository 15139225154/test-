import os
from time import sleep
from selenium import webdriver
class Case_1():

    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms1.html'
        self.driver.get(file_path)
    def test_checkbox(self):
        swimming = self.driver.find_element_by_name('swimming')
        reading = self.driver.find_element_by_name('reading')
        sleep(1)
        if not  swimming.is_selected():
            swimming.click()
        sleep(1)
        if not reading.is_selected():
            reading.click()
        sleep(1)
        self.driver.quit()
    def Js(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id('kw').send_keys('国邦医药')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.execute_script('window.scrollTo(100,500)')
        #self.driver.execute_script('window.scrollTo({top:100,behavior:"smooth"})')
        #self.driver.execute_script("document.getElementById('kw')")
        sleep(5)
        self.driver.quit()
    #时间空间操作
    def JS_time(self):
        self.driver.get('https://www.12306.cn/index/')
        ls = self.driver.current_window_handle
        sleep(1)
        js = 'window.open("https://www.cnblogs.com/miki-peng/")'
        self.driver.execute_script(js)
        js1 = self.driver.window_handles
        sleep(1)
        self.driver.switch_to_window(js1[0])
        #给出发元素
        sleep(1)
        time_element =  'document.getElementById("train_date")'
        #打印修改前日期
        print(self.driver.execute_script(f"return {time_element}.value"))
        #移除元素的readonly属性
        self.driver.execute_script(f'{time_element}.removeAttribute("readonly")')
        # j = 'document.getElementById("train_date").readOnly=false;'
        # self.driver.execute_script(j)
        #修改元素的值
        self.driver.execute_script(f'{time_element}.value="2020-12-30"')
        # 打印修改的日期
        print(self.driver.execute_script(f"return {time_element}.value"))
        self.driver.quit()

if __name__ == '__main__':
    case = Case_1()
    case.JS_time()




'''
window.scrollTo()

语法1: 
window.scrollTo(x-coord,y-coord)
x-coord 是文档中的横轴坐标。
y-coord 是文档中的纵轴坐标。
例子：
　　window.scrollTo(0,1000); // 垂直滚动到1000的位置

语法2：
window.scrollTo(options)
top 等同于  y-coord
left 等同于  x-coord
behavior  类型String,表示滚动行为,支持参数 smooth(平滑滚动),instant(瞬间滚动),默认值auto,实测效果等同于instant
例子：
    window.scrollTo({top:100,behavior:"smooth"})
如果某个元素滚动到某个位置，也可以用以上方法：

　　document.querySelector('.className').scrollTo()
'''


