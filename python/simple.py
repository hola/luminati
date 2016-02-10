
#!/usr/bin/env python
import requests
import base64
import random
username = 'lum-customer-CUSTOMER-zone-YOURZONE'
password = 'YOURPASS'
port = 22225
session_id = random.random()
super_proxy_url = ('http://%s-session-%s:%s@zproxy.luminati.io:%d' %
    (username, session_id, password, port))
proxies = {
    'http': super_proxy_url,
    'https': super_proxy_url,
}
auth = base64.b64encode((username+':'+password).encode('utf-8')).decode('utf-8')
headers = {'Proxy-Authorization': 'Basic '+auth}
print('Performing request')
print(requests.get('http://lumtest.com/myip.json', proxies = proxies, headers = headers).text)
