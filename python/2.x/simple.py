#!/usr/bin/env python
import urllib2
import random
username = 'lum-customer-CUSTOMER-zone-YOURZONE'
password = 'YOURPASS'
port = 22225
session_id = random.random()
super_proxy_url = ('http://%s-session-%s:%s@zproxy.luminati.io:%d' %
    (username, session_id, password, port))
proxy_handler = urllib2.ProxyHandler({
    'http': super_proxy_url,
    'https': super_proxy_url,
})
opener = urllib2.build_opener(proxy_handler)
print('Performing request')
print(opener.open('http://lumtest.com/myip.json').read())