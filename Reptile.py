import requests

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
params = {"pq":"python"}
url = "http://www.baidu.com"
response = requests.get(url,headers = headers, params = params)
print(response.status_code)
print(response.request.url)
print(response.content)