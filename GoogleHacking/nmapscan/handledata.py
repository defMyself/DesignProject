import json

data = {'202.196.64.190': {'osmatch': {}, 'ports': [{'protocol': 'tcp', 'portid': '80', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '124', 'service': {'name': 'http', 'product': 'Microsoft IIS httpd', 'version': '7.5', 'ostype': 'Windows', 'method': 'probed', 'conf': '10'}, 'cpe': [{'cpe': 'cpe:/o:microsoft:windows'}], 'scripts': []}, {'protocol': 'tcp', 'portid': '49153', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '124', 'service': {'name': 'msrpc', 'product': 'Microsoft Windows RPC', 'ostype': 'Windows', 'method': 'probed', 'conf': '10'}, 'cpe': [{'cpe': 'cpe:/o:microsoft:windows'}], 'scripts': []}, {'protocol': 'tcp', 'portid': '49154', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '124', 'service': {'name': 'msrpc', 'product': 'Microsoft Windows RPC', 'ostype': 'Windows', 'method': 'probed', 'conf': '10'}, 'cpe': [{'cpe': 'cpe:/o:microsoft:windows'}], 'scripts': []}], 'hostname': [{'name': 'aov.zzu.edu.cn', 'type': 'user'}, {'name': 'aov.zzu.edu.cn', 'type': 'PTR'}], 'macaddress': None, 'state': {'state': 'up', 'reason': 'echo-reply', 'reason_ttl': '124'}}, 'stats': {'scanner': 'nmap', 'args': '"C:/Program Files (x86)/Nmap/nmap.exe" -oX - -sV aov.zzu.edu.cn', 'start': '1618305784', 'startstr': 'Tue Apr 13 17:23:04 2021', 'version': '7.91', 'xmloutputversion': '1.05'}, 'runtime': {'time': '1618305860', 'timestr': 'Tue Apr 13 17:24:20 2021', 'summary': 'Nmap done at Tue Apr 13 17:24:20 2021; 1 IP address (1 host up) scanned in 77.61 seconds', 'elapsed': '77.61', 'exit': 'success'}}

# print(json.dumps(data, indent=4))
# print(data['202.196.64.190']['ports'][0])

for i in data['202.196.64.190']['ports']:
    # print(i['service']['name'])
    print(i['service']['product'])

