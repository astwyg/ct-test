# -*- coding: utf-8 -*-

import config
from tools.request import post, get
from tools.exceptions import ExpectError
from tools.expect import expect
import json


# part1: 接口定义
def submitNewOrder(accountId, userId, accountType, orderDetail):
    return post("/order/SubmitNewOrderCtrl",{"orderDetail":json.dumps(orderDetail)},{
        "accountId":accountId,
        "userId":userId,
        "accountType":accountType,
    })

# part2: 测试用例数据
RAW_DATA = '''
{
    "orderType":"1",
    "customPrice":"",
    "payType":"1",
    "remark":"",
    "description":"",
    "isVirtualOrder":"false",
    "orders":[
        {
            "instanceCnt":"1",
            "cycleCnt":"1",
            "cycleType":"1",
            "orderConfig":{
                "payPattern":"日"
            },
            "serviceTag":"VMS",
            "items":[
                {
                    "sale":{
                        "pricePlanId":"",
                        "saleEntryId":"9375f5f8407b11e68072ac162d757e00",
                        "description":""
                    },
                    "master":"true",
                    "resourceType":"VM",
                    "serviceTag":"VMS",
                    "itemConfig":{
                        "memSize":"16",
                        "workOrderCount":"1",
                        "cpuNum":"8",
                        "sysVolume":"40",
                        "vpcNet":"",
                        "hasVPCIP":"",
                        "InternetMaxBandwidthIn":"",
                        "osType":"win0864-bj-zcj-20160703",
                        "vlanId":"",
                        "zoneId":"d15ff6c8f92011e4a2fbe2ad47403cef",
                        "templateId":"",
                        "InternetMaxBandwidthOut":"",
                        "publicIpAddress":"",
                        "vpcVlanId":"",
                        "year":"2016"
                    },
                    "itemValue":1
                },
                {
                    "sale":{
                        "pricePlanId":"",
                        "saleEntryId":"5d60d88c3dd511e68072ac162d757e00",
                        "description":""
                    },
                    "master":"false",
                    "resourceType":"VM",
                    "serviceTag":"VMS",
                    "itemConfig":{
                        "workOrderCount":"1",
                        "value":"",
                        "year":"2016",
                        "volumeType":"SATA",
                        "volumeName":"",
                        "zoneId":"7b119b2a08ba11e3a674ac162d757d14"
                    },
                    "itemValue":1
                }
            ]
        }
    ],
    "chargingStatus":"1",
    "requestTicketId":""
}
'''

GOOD_DATA = '''
{
    "orderType":1,
    "payType":1,
    "remark":"",
    "description":"",
    "isVirtualOrder":false,
    "orders":[
        {
            "instanceCnt":1,
            "cycleCnt":1,
            "cycleType":1,
            "orderConfig":{
                "payPattern":"日"
            },
            "serviceTag":"VMS",
            "items":[
                {
                    "sale":{
                        "pricePlanId":"",
                        "saleEntryId":"9375f5f8407b11e68072ac162d757e00",
                        "description":""
                    },
                    "master":"true",
                    "resourceType":"VM",
                    "serviceTag":"VMS",
                    "itemConfig":{
                        "memSize":16,
                        "workOrderCount":1,
                        "cpuNum":8,
                        "sysVolume":40,
                        "vpcNet":"",
                        "hasVPCIP":"",
                        "InternetMaxBandwidthIn":"",
                        "osType":"win0864-bj-zcj-20160703",
                        "vlanId":"",
                        "zoneId":"d15ff6c8f92011e4a2fbe2ad47403cef",
                        "templateId":"",
                        "InternetMaxBandwidthOut":"",
                        "publicIpAddress":"",
                        "vpcVlanId":"",
                        "year":"2016"
                    },
                    "itemValue":1
                },
                {
                    "sale":{
                        "pricePlanId":"",
                        "saleEntryId":"5d60d88c3dd511e68072ac162d757e00",
                        "description":""
                    },
                    "master":"false",
                    "resourceType":"VM",
                    "serviceTag":"VMS",
                    "itemConfig":{
                        "workOrderCount":1,
                        "value":"",
                        "year":"2016",
                        "volumeType":"SATA",
                        "volumeName":"",
                        "zoneId":"7b119b2a08ba11e3a674ac162d757d14"
                    },
                    "itemValue":1
                }
            ]
        }
    ],
    "chargingStatus":"1",
    "requestTicketId":""
}
'''

if __name__ == "__main__":
    # part3: 测试过程
    resp = submitNewOrder("1", "1", "dummy", RAW_DATA)
    expect(resp["FIXME"], "FIXME")
    resp = submitNewOrder("1", "1", "dummy", GOOD_DATA)
    expect(resp["FIXME"], "FIXME")
    # TIPS: 如果测试数据很多, 请这样组织
    for data in (RAW_DATA, GOOD_DATA,):
        resp = submitNewOrder("1", "1", "dummy", data)
        expect(resp["FIXME"], "FIXME")