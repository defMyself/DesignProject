# 输入 main domain
# 1. 子域名爆破
# 2. IP 扫描
# 3. Web 扫描
# 4. 漏洞扫描
# 5. poc扫描
# 6. 三方工具

# 域名 IP 说明
# (domain : IP)

task = {
    "id" : "001",
    "keydomain" : "zzu.edu.cn",
    "subdomain" : {
        "mail.zzu.edu.cn" : "202.22.34.11",
        "live.zzu.edu.cn" : "222.21.22.21",
        "job.zzu.edu.cn" : "203.33.22.11"
    }
}

ip = {
    "ip" : "127.0.0.1",
    "ports" : {
        "80" : "http",
        "22" : "ssh",
        "25" : "telnet",
        "3389" : "rdp"
    }
}

# vulnerablities scan

def main():
    # 任务队列
    # 执行任务队列里面的任务
    #
