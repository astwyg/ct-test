# -*- coding: utf-8 -*-


class ExpectError(Exception):

    def __init__(self, expect_value, actual_value):
        self.expect_value = expect_value
        self.actual_value = actual_value

    def __str__(self):
        print self #TODO 断点调试
        return "期望获得<{}>, 但是实际是<{}>".format(self.expect_value, self.actual_value)

class APIError(Exception):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "接口发生错误:{}".format(self.text)