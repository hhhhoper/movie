##电影搜索
from urllib.request import quote, unquote
import requests
import re
import pyperclip
def search(mname):
    url = "http://s.ygdy8.com/plus/so.php?typeid=1&keyword="+mname
    gbk_url = quote(url, safe=";/?:@&=+$,", encoding="gbk")
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    print('加载中...')
    response=requests.get(gbk_url,headers=headers)
    response.encoding='gbk'
    string=response.text
    npattern=re.compile("<td width='55%'>.*</td>")
    mname=npattern.findall(string)
    hpattern=re.compile("<a.*'>")
    num=0
    ahtml=[]
    for i in mname:
        i=re.sub("<td width='55%'><b>|<font color='red'>|</font>|</a></b></td>","",i)
        html="https://m.ygdy8.com/"+re.sub("<a href='|'>","",hpattern.findall(i)[0],2)
        ahtml.append(html) 
        i=re.sub("<a.*'>","",i)
        num+=1
        print("#"+str(num)+"    "+i+'\n')
    return ahtml
def info(string):
    try:
        titlepat='<div class="title_all"><h1><font color=#07519a>.*</div>'
        result1=re.search(titlepat,string)
        title=result1.group()
        title=re.sub('<div class="title_all"><h1><font color=#07519a>|</font></h1></div>',"",title)
        print(title)
        contentpat='◎译　　名.*<br /><br />'
        result2=re.search(contentpat,string)
        content=result2.group()
        content=re.sub('<br />',"\n",content)
        content=re.sub('&middot;','.',content)
        content=re.sub('&mdash;','-',content,5)
        content=re.sub('&nbsp;'," ",content,1000)
        content=re.sub('<img border="0".*alt="" />','',content,1)
        content=re.sub('<strong><font.*下载地址.*</font></strong>','',content,1)
        print(content)
        magnetpat='magnet.*fannounce'
        result3=re.search(magnetpat,string)
        magnet="迅雷下载链接:   "+result3.group()
        print(magnet)
        return magnet
    except:
        print("对不起，电影无版权！")

