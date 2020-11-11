# JSON logging logger formatter

### 说明
Python JSON 日志记录器对象和格式化器。

记录器处理了线程隔离，可以设置全局参数和线程局部参数。

### 链接
- [GitHub](https://github.com/ztj1993/py-json-logging)
- [PyPI](https://pypi.org/project/py-ztj-json-logging)

### 安装
```
pip install py-ztj-json-logging
```

### 使用
```
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


logger.info('主线程日志输出 Start')


def thread_1():
    logger.set('局部参数', '这是一个局部的参数，只在线程一日志中有效')
    logger.info('线程一日志输出')


def thread_2():
    time.sleep(1)
    logger.info('线程二日志输出')


logger.info('主线程日志输出 End')


t1 = threading.Thread(target=thread_1, args=())
t2 = threading.Thread(target=thread_2, args=())
t1.start()
t2.start()
```
