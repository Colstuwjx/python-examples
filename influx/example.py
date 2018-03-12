# coding=utf-8

import requests
import urllib


def make_influx_query(uri, db, q):
    data = {
        "db": db, "q": q, "pretty": True
    }
    return requests.post("http://{0}?{1}".format(uri, urllib.urlencode(data)))


print make_influx_query(
    "127.0.0.1:8086/query", "monitordb", "show series"
).json()
