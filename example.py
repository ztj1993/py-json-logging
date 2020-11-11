import logging
import threading
import time

from ZtjJsonLogging import JsonFormatter
from ZtjJsonLogging import JsonLogger

# 定义格式化器
formatter = JsonFormatter()
formatter.set_ensure_ascii(False)
formatter.set_indent(4)

# 定义处理器
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

# 定义记录器
logger = JsonLogger(__name__)
logger.addHandler(handler)

# 全局参数
logger.glob('全局参数', '这是一个全局参数，在所有的线程中有效')

logger.info('主线程日志输出开始')


def thread_1():
    logger.set('局部参数', '这是一个局部的参数，只在线程日志中有效')
    logger.info('线程一日志输出')


def thread_2():
    time.sleep(1)
    logger.info('线程二日志输出')


t1 = threading.Thread(target=thread_1, args=())
t2 = threading.Thread(target=thread_2, args=())
t1.start()
t2.start()

time.sleep(2)

logger.info('主线程日志输出结束')
