"""
Design a Throttling management service which responds true until hits its limit
Extension- Restrict the throttle to 1 second
"""
from datetime import datetime
from time import sleep
from unittest import TestCase

THROTTLING_LIMIT = 10
THROTTLING_TIME = 1


class ThrottlerService(object):
    def __init__(self):
        self.start = datetime.now()
        self.end = None
        self.counter = 0

    def increase_counter(self, i):
        if self.counter < THROTTLING_LIMIT:
            self.counter += 1
        else:
            if self.throttle():
                self.reset_timer()
            else:
                raise Exception("Limit exceeded")
        return True

    def throttle(self) -> bool:
        self.end = datetime.now()
        if (self.end - self.start).seconds < THROTTLING_TIME:
            return False
        return True

    def reset_timer(self) -> None:
        self.counter = 1
        self.start = datetime.now()


class TestThrottlerService(TestCase):
    def setUp(self) -> None:
        pass

    def test_increase_counter(self) -> None:
        obj = ThrottlerService()
        for i in range(10):
            self.assertTrue(obj.increase_counter(i))

    def test_increase_counter_failed(self) -> None:
        obj = ThrottlerService()
        try:
            for i in range(15):
                obj.increase_counter(i)
        except Exception as e:
            print(e)

    def test_throttle(self) -> None:
        obj = ThrottlerService()
        for i in range(15):
            try:
                self.assertTrue(obj.increase_counter(i))
                print(i, " => ", obj.counter)
            except Exception as e:
                print("sleep to reset the counter", i, " => ", obj.counter)
                sleep(1)
