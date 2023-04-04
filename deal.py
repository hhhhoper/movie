import re
import pyperclip
import Chtml
def deal(string):
	pattern=re.compile("<a href.*ulink.*</a>")
	result=pattern.findall(string)
	return result
def html(string): #获取电影页地址
	string1=deal(string)
	html=[]
	pattern=re.compile("/html.*html")
	for i in string1:
		st=pattern.findall(i)
		st[0]="https://www.ygdy8.net/"+st[0]
		html.extend(st)
	return html
def name(string): #获取电影名字
	string1=deal(string)
	name=[]
	pattern=re.compile(">.*<")
	num=0
	for i in string1:
		num+=1
		st=pattern.findall(i)
		st[0]=re.sub(">|<","",st[0])
		st[0]="#"+str(num)+"	"+st[0]
		name.extend(st)
	return name
def choose(string):
	pattern=re.compile('''◎简　　介.*?target.*?">''')
	result=pattern.findall(string)
	result[0]=re.sub("&hellip;|&nbsp;|&middot;","",result[0])
	result[0]=re.sub("<br />","\n",result[0])
	result[0]=re.sub("&mdash;|<","",result[0])
	result[0]=re.sub('''a target="_blank" href="|br style.*href="''',"\n迅雷种子链接：",result[0])
	result[0]=re.sub('''">''',"",result[0])
	print(result[0])
	return result[0]
	
	
		
		