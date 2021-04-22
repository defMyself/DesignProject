import nmap3

nm = nmap3.Nmap()
ret = nm.scan_top_ports("www.baidu.com")
print(ret)

