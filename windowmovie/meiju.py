from urllib.request import quote, unquote
import requests
import re
import pyperclip
def getString(url):
	headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
	response=requests.get(url,headers=headers)
	response.encoding='gbk'
	string=response.text
	return string
def getName(page):
	url ="https://www.dydytt.net/html/tv/oumeitv/list_9_"+str(page)+".html"
	string=getString(url)
	pattern=re.compile('''class="ulink">.*?</a>''')
	name=pattern.findall(string)
	num=0
	for i in name:
		num+=1
		movie=re.sub('''class="ulink">|</a>''', "", i)
		print("#"+str(num)+"        "+movie)
def getHtml(page):
	url ="https://www.dydytt.net/html/tv/oumeitv/list_9_"+str(page)+".html"
	string=getString(url)
	pattern=re.compile("/html/tv/oumeitv/[0-9]*/[0-9]*.html")#预编译
	html=pattern.findall(string) #返回数组
	return html
def downloadUrl(num,html):
	url="https://www.dydytt.net"+html[num-1]
	string=getString(url)
	titlepat='<div class="title_all"><h1><font color=#07519a>.*</div>'
	result1=re.search(titlepat,string)
	title=result1.group()
	title=re.sub('<div class="title_all"><h1><font color=#07519a>|</font></h1></div>',"",title)
	print(title)
	try:
		contentpat='◎译　　名.*<br /><br />'
		result2=re.search(contentpat,string)
		content=result2.group()
		content=re.sub('<br />',"\n",content)
		content=re.sub('&middot;','.',content)
		content=re.sub('&mdash;','-',content,5)
		content=re.sub('&nbsp;'," ",content,100)
		content=re.sub('&hellip;',"",content,10)
		content=re.sub('<img border="0".*alt="" />','',content,1)
		content=re.sub('<strong><font.*下载地址.*</font></strong>','',content,1)
		content=re.sub('<a.*</a>','',content,1)
		print(content)
	except:
		print("简介:有bug懒得修了(●'◡'●)，可以正常下载！")
	magnetpattern=re.compile('''href="magnet.*?fannounce|href="ftp.*?mkv|href="ftp.*?rmvb''')
	magnet=magnetpattern.findall(string) #下载链接
	num=0
	for i in magnet:
		i=re.sub('''href="''','',i,5)
		num+=1
		print("第"+str(num)+"集:\n"+i+"\n")
	return magnet
