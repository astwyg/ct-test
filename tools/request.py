# -*- coding: utf-8 -*-
import requests, urllib, logging
import config
from exceptions import APIError

log = logging.getLogger(__file__)


def _format_ucore_body(body):
    for k,v in body.items():
        if v is None:
            del body[k]
    return urllib.urlencode(body)


def post(url, body, header, mode="ucore", contentType=None,  **kwargs):
    if "http" not in url:
        url = config.NGINX + url
    if mode == "normal":
        r = requests.post(
            url = url,
            **kwargs
        )
        return r
    elif mode == "ucore":
        headers = header or {}
        if contentType:
            headers["Content-Type"] = contentType
        else:
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        body = _format_ucore_body(body)
        r = requests.post(
            url = url,
            data = body,
            headers = header,
        )
        log.info("{} - {} - {} - {} - {} - {} - {}".format("POST", url, body, header, r.status_code ,r.text, r.elapsed))
        if r.status_code == 200:
            r = r.json()
            if r["statusCode"] != 800:
                raise APIError("StatusCode非800")
            else:
                return r
        else:
            raise APIError("服务器HTTP状态非200")
    else:
        raise Exception("传入未知mode:{}".format(mode))


def get(url, header, body, mode="ucore", contentType=None, **kwargs):
    if "http" not in url:
        url = config.NGINX + url
    if mode == "normal":
        r = requests.post(
            url = url,
            **kwargs
        )
        return r
    elif mode == "ucore":
        body = _format_ucore_body(body)
        r = requests.post(
            url = url,
            data = body,
            headers = header,
        )
        log.info("{}-{}-{}-{}-{}-{}-{}".format("GET", url, body, header, r.status_code ,r.text, r.elapsed))
        if 1: # FIXME using code
            r = r.json()
            if r["statusCode"] != 800:
                raise APIError("StatusCode非800")
            else:
                return r
        else:
            raise APIError("服务器HTTP状态非200")
    else:
        raise Exception("传入未知mode:{}".format(mode))
