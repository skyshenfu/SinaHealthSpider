# coding=utf-8
import urllib2
import json
import data as Data

namelist = []
sourcelist = []
page = 1
starturl = ""


def getUrls(number):
    backup = number
    while number >= 1:
        global starturl, page
        starturl = 'http://feed.mix.sina.com.cn/api/roll/get?pageid=39&lid=561&num=20&versionNumber=1.2.8&page=' + str(backup - number + 1) + '&encode=utf-8&callback=feedCardJsonpCallback&_=1496306569345'
        print str(backup - number + 1)
        request = urllib2.Request(starturl)
        request.add_header("User-Agent",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36c")
        response = urllib2.urlopen(request)
        str1 = response.read()[26:-14]
        json1 = json.loads(str1)
        json1 = json.loads(json.dumps(json1["result"]["data"][3:], ensure_ascii=False))
        for item in json1:
            if str(item["url"]).startswith('''http://slide.'''):
                print'-start----------违法------------------'
                print item["url"]
                print'------------违法-------------end---'
                continue
            else:
                print item["url"]
                namelist.append(item["title"])
                sourcelist.append(item["url"])
        number -= 1
    print "完事了"
    Data.set_urlSourceValue(sourcelist)
    Data.set_nameSourceValue(namelist)
