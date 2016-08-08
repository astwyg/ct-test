# -*- coding: utf-8 -*-

import config
from tools.request import post, get
from tools.exceptions import ExpectError
from tools.expect import expect
import json


def listHandingForm(params):
    return post("/cmbe/handingForm/listHandingForm/", params)

if __name__ == "__main__":
    resp = listHandingForm({
        "id":41
    })
    assert len(resp["returnObj"]["result"])>0
    resp = listHandingForm({
        "status":3
    })
    assert len(resp["returnObj"]["result"])>0
    resp = listHandingForm({
        "orderNo":"123"
    })
    assert len(resp["returnObj"]["result"])==0
