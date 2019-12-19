# __Author__: NOLA
# __Date__: 2019/12/19


import re
import requests
import urllib.request as urllib
import json
from bs4 import BeautifulSoup


def create_tag(src):
    return "<img src=" + src + ">"


def save_pic(url, sid):
    urllib.urlretrieve(url, "./vip_pic/{}.png".format(sid))


# r = re.compile(r"http://h2\S*.[png, jpg]", re.S)

def vip(url):
    html = requests.get(url, verify=False)
    content = html.text.replace('lightartDataCallback(', "", 1).replace(")", "", 1)
    ret = json.loads(content)
    resource_list = ret["data"]["page_list"][0]["floor_list"]
    count = 0
    for item in resource_list:
        rr = item["data"]["resourceGroupList"][0]["resourceList"]
        with open("vip.html", "a+", encoding="utf8") as f:
            for resource in rr:
                try:
                    count += 1
                    url = resource["lightArtImage"]["imageUrl"]
                    name = resource["lightArtImage"]["componentId"]
                    f.write(create_tag(url))
                    save_pic(url, name)

                except Exception as e:
                    print(e)

    print("total images:", count)


with open("url.json", "r") as f:
    url_list = json.loads(f.read())["url"]

if __name__ == "__main__":
    for url in url_list:
        vip(url)
