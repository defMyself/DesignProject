import socket


def isAlive(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(ip)
    except:
        print("this domain 2 ip ERROR")


def parse(domain):
    with open("wordlist.txt") as f:
        s = f.read()
        result = s.split('\n')
        for i in result:
            print(i + '.' + domain)


with open("domains.txt") as f:
    s = f.read()
    print(s)

domain = "www.zzu.edu.cn"
parse(domain)
isAlive(domain)


