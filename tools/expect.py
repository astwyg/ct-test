# -*- coding: utf-8 -*-
from exceptions import ExpectError
import logging

log = logging.getLogger(__file__)


def expect(expect_value, actual_value):
    if type(expect_value) != type(actual_value):
        try:
            temp_actual_value = type(expect_value)(actual_value)
            if temp_actual_value == expect_value:
                log.warning("请注意, 测试变量{}, 服务器返回类型为{}, 而你的测试用例类型为{}, 测试系统默认你笔误了".format(
                    expect_value, type(actual_value), type(expect_value)
                ))
                return
            temp_expect_value = type(actual_value)(expect_value)
            if temp_expect_value == actual_value:
                log.warning("请注意, 测试变量{}, 服务器返回类型为{}, 而你的测试用例类型为{}, 测试系统默认你笔误了".format(
                    expect_value, type(actual_value), type(expect_value)
                ))
                return
        except TypeError,e:
            pass

    if expect_value != actual_value:
        raise ExpectError(expect_value, actual_value)
