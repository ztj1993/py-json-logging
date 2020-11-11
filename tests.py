import unittest
import threading
import time

from ZtjJsonLogging import JsonLogger
import threading
import time
import unittest

from ZtjJsonLogging import JsonLogger


class TestLogging(unittest.TestCase):
    def test_json_logger(self):
        """测试初始化"""
        logger = JsonLogger(__name__)
        logger.glob('glob', 'glob')
        logger.set('main', 'main')

        def thread(cls):
            logger.set('thread', 'thread')
            cls.assertEqual(logger.get('glob'), 'glob')
            cls.assertEqual(logger.get('main'), None)
            cls.assertEqual(logger.get('thread'), 'thread')

        time.sleep(1)

        self.assertEqual(logger.get('glob'), 'glob')
        self.assertEqual(logger.get('main'), 'main')
        self.assertEqual(logger.get('thread'), None)

        threading.Thread(target=thread, args=(self,)).start()


if __name__ == '__main__':
    unittest.main()
