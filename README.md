# luminati.io API

To get CUSTOMER, YOURZONE and YOURPASS, sign up on http://luminati.io

## How to Use Luminati API
### Terms

- Client: Your machine running the scraping code. It connects to the Super Proxy to request URLs you wish to scrape.
- Super Proxy: Luminati Super Proxy that distributes your requests through the Luminati network to the Luminati Exit Nodes.
- Exit Node: The final PC that sends your URL request to to the target website. This is the IP that the website sees, it is a PC that is part of the huge Luminati P2P network. It is a regular home PC, mobile phone or tablet, typically behind DSL, Cable Modem, or WiFi.

### Using the system — Overview

- You send your requests to the Super Proxy, and the Super Proxy relays them through an Exit Node on our network.
- You can specify to the Super Proxy which country the Exit Node should be in, when to force a switch to a different IP address within the country, and set other parameters.
- The control is done by -country-CODE suffixes after username.
Example for Brasil: lum-customer-CUSTOMER-zone-YOURZONE-country-br

### Obtaining adresses of Super Proxies

- Super Proxies are available under zproxy.luminati.io. This DNS name resolves to the set of currently fastest Super Proxies.

### Additional options for obtaining Super Proxies

- To improve latency from your servers to Super Proxies you can use servercountry-nl.zproxy.luminati.io for example to select super proxies in Netherlands. You may select us, uk or nl. Note that it does not restrict your Exit Node countries, only the proxy location.
- To refresh the set of Super Proxies use session-12345.zproxy.luminati.io, where 12345 is a new unique number every time. You can combine servercountry and session: servercountry-gb-session-12345.zproxy.luminati.io

### Session: Exit Node IP persistence

- In many cases you may want to run several parallel sessions from the same Client, use different Exit Nodes per session, and be able to change them when needed.
This can be done by adding the session to the proxy username: lum-customer-CUSTOMER-zone-YOURZONE-session-rand39484
Generate the random number on thread startup, and change it when you want to change the Exit Node assigned for the thread's connection.
- Session ID can be any random string/counter: requests with same session string will use the same Exit Node (as long as possible); requests with different session strings will be assigned different Exit Nodes.
- To force an IP change, just modify the session ID.
- If an assigned Exit Node becomes unavailable, the Super Proxy will change it automatically, even if you do not change the session ID.
- The Session IP is kept persistent up to 1 minute of idle time. After a minute with no requests, the IP is released back to the pool.
To keep this Session/IP for longer, send a tiny keep-alive request every 30 seconds, to prevent this session from becoming idle for over a minute.
This request may be anything small, such as /favicon.ico or even a request that returns 404 (as long as the web server does not disconnect the socket due to this request).

### Super Proxy status

- To “ping” the Super Proxy status:
curl "$SUPER_PROXY:22225/ping"
You will receive its version number, IP, country where it's located, and whether it is “connected” to the Luminati network.

### Increasing performance

- Reduce round-trip/latency:
Choose Exit Node IP via lum-customer-CUSTOMER-zone-YOURZONE-country-br (Brazil for example) matching the destination site you connect to.
Use Super Proxies close to your location by using full name servercountry-us.zproxy.luminati.io (Super Proxies located in United States for example, see Additional options for obtaining Super Proxies).
- Increase throughput: Run multiple parallel sessions with unique session IDs, from the same Client, where each session will be assigned a unique Exit Node using distinct session IDs.

### Controlling where DNS resolution is performed

- If you use lum-customer-CUSTOMER-zone-YOURZONE-dns-local, domain names will be resolved and cached by the Super Proxy.
- If you wish to perform the DNS resolution at the Exit Node, use lum-customer-CUSTOMER-zone-YOURZONE-dns-remote. This is slower, but will give you the same IP as users in your chosen country receive.

### Changing Exit Node IP when using a browser or browser automation

- Changing an Exit Node IP in Luminati is done by changing the -session-rand93849 part in the proxy username to a new random number.
There are two problems with browsers: they cache the proxy username, and sites may use cookies or local storage in your browser to identify the same user even after an IP change.
- To solve the proxy username caching problem, open this URL in the browser:
http://trigger.domain/hola_trigger?disconnect_sockets=1&all=1&reject=lum-customer-CUSTOMER-zone-YOURZONE-session-rand39484 
Make sure to keep http:// prefix, also if you are accessing an https site!
trigger.domain should not be modified to your domain name (its not a template). Its a special domain name that is handled by the super-proxy.
- To solve the cookies and local storage problem, use the commands in the browser's options menu to clear cookies and local storage, or install a browser extension for cleaning those in one click. Some browsers also have a Private or Incognito mode which makes sure that cookies and local storage are purged when the window is closed.

### Statistics API

- Get the bandwidth stats for a zone: /api/get_zone_bw

```curl -H "X-Hola-Auth: $USERNAME-key-$PASSWORD" "http://luminati.io/api/get_zone_bw?zone=YOURZONE&details=1"```
- Get the bandwidth stats for all your zones: /api/get_customer_bw

```curl -H "X-Hola-Auth: $USERNAME-key-$PASSWORD" "http://luminati.io/api/get_customer_bw?details=1"```
