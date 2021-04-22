import nmap3


def callback_result(host, scan_result):
    print('--------------------')
    print(host, scan_result)


nm = nmap3.Nmap()
result = nm.nmap_version_detection("aov.zzu.edu.cn")
print(result)
