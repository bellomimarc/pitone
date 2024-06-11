

import requests

url = 'http://www.baidu.com'
response = requests.get(url)
print(f"""-----------------RESPONSE-----------------
status code: {response.status_code}
text: {response.text[:20]}
content-type: {response.headers.get('content-type')}
""")

