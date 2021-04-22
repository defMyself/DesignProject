from googlesearch import search
import socket

class Google:

    def getgoogleresult(self, query, number):
        """
        :param query: google 查询参数(inurl,insite...)
        :param number: 查询结果数目
        :return: url列表
        """
        result = []
        for url in search(query, tld='com', lang='cn', stop=number):
            result.append(url)

        for u in result:
            print(u)


def domain_to_ip(domain):
    return socket.gethostbyname(domain)


def test_domain_to_ip():
    domain = 'www.baidu.com'
    ip = domain_to_ip(domain)
    print(ip)


def test_google():
    g = Google()
    g.getgoogleresult('inurl:zzu.edu.cn', 10)


test_google()