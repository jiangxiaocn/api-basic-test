import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import json

base_url='http://httpbin.org'

#cookie,timeout
'''
cookie={'user':'xiao'}
r=requests.get(base_url+'/cookies', cookies=cookie,timeout=3)
print(r.status_code)
print (r.text)
'''

#header,bodydata
'''
header={'user-agent':'Mozilla/5.0'}
form_data={'user':'xiao','password':'11111'}
re=requests.post(base_url+'/post',data=form_data,headers=header)
print (re.text)
print (re.json())
'''

#go through all cookies
'''
r=requests.get('http://www.baidu.com')
print (type(r.cookies))
print (r.cookies)
for key,value in r.cookies.items():
    print (key+':'+value)
'''


#file upload
'''
file ={'file':open('picture.png','rb')}
req=requests.post(base_url+'/post',files=file)
print (req.text)
'''


#create session
'''
se=requests.session()
r=se.get(base_url+'/cookies/set/user/jiang')
print (r.text)
re=se.get(base_url+'/cookies')
print (re.text)
'''  

#certificate verification
'''
r=requests.get('https://www.12306.cn',verify=False)
print (r.text)
'''

#proxies

'''
proxy={'http':'http://95.67.45.234:8080'}
r=requests.get(base_url+'/get',proxies=proxy)
print (r.text)
'''

#identity authentication
'''
r=requests.get(base_url+'/basic-auth/xiao/8888',auth=HTTPBasicAuth('xiao','8888'))
print(r.text)

re=requests.get(base_url+'/digest-auth/auth/xiao2/6666',auth=HTTPDigestAuth('xiao','6666'))
print (re.text)

'''
#stream request (respons with more than one result)
'''
r=requests.get(base_url+'/stream/10',stream=True)
print (r.text)

if r.encoding is None:
    r.encoding='utf-8'

for line in r.iter_lines(decode_unicode=True):
    if line:
        data = json.loads(line)
        print(data['id'])
'''




