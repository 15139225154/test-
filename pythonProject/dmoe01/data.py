import os

import yaml,os
import random


# for i in range(0,5):
#     print(i)
#     h = random.randint(9999999, 100000000)
#     x = '153{}'.format(h)
#     x1 = '{}@.163.common'.format(h)
#     print('手机号:',x,'邮箱:',x1)

with open(r'data.yaml',encoding='utf8') as f:
    # d1 = yaml.dump()
    d = pyyaml.load(f, Loader=yaml.SafeLoader)
    print(d)
# print(d)
# # print(type(d))
# # Username = d[0]
# # print(type(Username))
# Password = d['账号']
# print(Password)
# print(type(Password))


import js as js
from selenium import webdriver
from time import sleep
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://dev.mobile.sinochem.com/cangqiong-admin/login")
# sleep(2)
# driver.find_element_by_xpath('//input[@id="normal_login_username"]').send_keys('admin@tenant1')
# driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('admin')
# driver.get('http://dev.mobile.sinochem.com/cangqiong-admin/system/login')
# driver.refresh()
# sleep(1)
# window = 'window.open("http://dev.mobile.sinochem.com/cangqiong-admin/login")'
# driver.execute_script(window)
# driver.switch_to_window(driver.window_handles[1])
# print(driver.window_handles)
# handle = driver.current_window_handle
# print(handle)
# sleep(1)

# driver.quit()

with open('123.txt','rt') as f1:
    print(f1.read())