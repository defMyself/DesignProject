import requests
import re
from urllib.parse import quote, urlparse
import time
from pyquery import PyQuery as pq
import socket
import db
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
UA = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"


def http_req(url, method = 'get', **kwargs):
    kwargs.setdefault('verify', False)
    kwargs.setdefault('timeout', (10.1, 30.1))
    kwargs.setdefault('allow_redirects', False)

    headers = kwargs.get("headers", {})
    headers.setdefault("User-Agent", UA)
    kwargs["headers"] = headers
    conn = getattr(requests, method)(url, **kwargs)
    return conn


##############################################
# Baidu
class BaiduSearch():
    def __init__(self, keyword=None, page_num=6):
        self.search_url = "https://www.baidu.com/s?rn=100&pn={page}&wd={keyword}"
        self.num_pattern = re.compile(r'百度为您找到相关结果约([\d,]*)个')
        self.frist_html = ""
        self.keyword = keyword
        self.page_num = page_num
        self.pq_query = "#content_left h3.t a"
        self.search_result_num = 0
        self.default_interval = 0.2

    def result_num(self):
        url = self.search_url.format(page=0, keyword=quote(self.keyword))
        #logger.info("search url {}".format(url))
        html = http_req(url).text
        self.first_html = html
        result = re.findall(self.num_pattern, html)
        num = int("".join(result[0].split(",")))
        self.search_result_num = num
        return num

    def match_urls(self, html):
        dom = pq(html)
        result_items = dom(self.pq_query).items()
        urls_result = [item.attr("href") for item in result_items]
        urls = set()
        for u in urls_result:
            try:
                resp = http_req(u, "head")
                real_url = resp.headers.get('Location')
                if real_url:
                    urls.add(real_url)
            except Exception as e:
                #logger.exception(e)
                print("error")
        return list(urls)

    def run(self):
        self.result_num()
        #logger.info("baidu search {} results found for keyword {}".format(self.search_result_num, self.keyword))
        urls = []
        for page in range(1, min(int(self.search_result_num / 10) + 2, self.page_num + 1)):
            if page == 1:
                _urls = self.match_urls(self.first_html)
                #logger.info("baidu firsturl result {}".format(len(_urls)))
            else:
                time.sleep(self.default_interval)
                url = self.search_url.format(page=(page - 1) * 10, keyword=quote(self.keyword))
                html = http_req(url).text
                _urls = self.match_urls(html)
                #logger.info("baidu search url {}, result {}".format(url, len(_urls)))
                urls.extend(_urls)
        return urls


def baidu_search(domain, page_num=6):
    keyword = "site:{}".format(domain)
    b = BaiduSearch(keyword, page_num)
    urls = b.run()
    urls = [urlparse(u).netloc for u in urls if domain in urlparse(u).netloc]
    return set(urls)


def getdomainsfrombaidu(task_name):
    mydb = db.DB()
    domains = baidu_search(task_name)

    results = []

    for x in domains:
        data = (x, socket.gethostbyname(x))
        print(data)
        results.append(data)

    mydb.write(task_name, results)


if __name__ == "__main__":
    getdomainsfrombaidu("xisu.edu.cn")