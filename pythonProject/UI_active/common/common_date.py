from string import Template

import yaml

def Yaml():
    with open(r'C:\Users\亿利和\PycharmProjects\pythonProject\UI_active\common\data.yaml', encoding='utf8') as f:
        lo_ad = yaml.load(f, Loader=yaml.SafeLoader)
    return lo_ad

def Yaml_Case1():
    with open(r'C:\Users\亿利和\PycharmProjects\pythonProject\UI_active\common\date_Case1.yaml', encoding='utf8') as f:
        lo_ad1 = yaml.load(f, Loader=yaml.SafeLoader)
    return lo_ad1
def Yaml_template(date:dict):
    with open(r'C:\Users\亿利和\PycharmProjects\pythonProject\UI_active\common\date_Case1.yaml', encoding='utf8') as f:
        lo_ad2 = Template(f.read()).substitute(date)
        return yaml.safe_load(lo_ad2)

print(Yaml_Case1())
# date= {
#     'value1':'test1',
#     'value2':'test2'
# }
# print(Yaml_template(date=date))
