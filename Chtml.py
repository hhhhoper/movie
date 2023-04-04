import requests
def getoumei(pages): #欧美电影
	url="https://www.ygdy8.net/html/gndy/oumei/list_7_"+str(pages)+".html"
	headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
	response=requests.get(url,headers=headers)
	response.encoding='gbk'
	string=response.text
	return string
def getext(url):#电影介绍页面
	headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
	response=requests.get(url,headers=headers)
	response.encoding='gbk'
	string=response.text
	return string