import json,logging
import time

#创建一个日志器，实例化对象
logger = logging.getLogger('test')
#输出所有大于DEBUG级别的
logger.setLevel(logging.DEBUG)
#创建一个创建处理器，用于写入日志文件
fh = logging.FileHandler(filename='Log/{}_log'.format(time.strftime('%Y年%m月%d日 %H_%M_%S',time.localtime())),
                         encoding='utf8')
fh.setLevel(logging.DEBUG)
#创建一个创建处理器
stream_hdl = logging.StreamHandler()
stream_hdl.setLevel(logging.DEBUG)
#创建一个格式器
fmt = logging.Formatter(fmt='[%(filename)s] [%(asctime)s] [%(levelname)s] %(message)s',
                        datefmt='%Y/%m/%d/%X')
#处理器设置一个格式器
stream_hdl.setFormatter(fmt)
fh.setFormatter(fmt)
#日志器可以添加多个格式器
logger.addHandler(stream_hdl)
logger.addHandler(fh)

if __name__ == '__main__':
    logger.debug('debug信息')
    logger.info('日志：')
    logger.warning('warning信息')
    logger.error('error信息')
    logger.critical('critical信息')