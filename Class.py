import Chtml
import deal
import meiju
class Program:
	pages=0  #电影页数
	mpages=0 #美剧页数
	def next(self): #下一页操作
		Program.pages+=1
		print('页数:'+str(Program.pages))
		for i in deal.name(Chtml.getoumei(Program.pages)):
			print(i)
	def back(self):	#上一页操作
		if Program.pages>1:
			Program.pages-=1
		print('页数:'+str(Program.pages))
		for i in deal.name(Chtml.getoumei(Program.pages)):
			print(i)
	def html(self): #获取电影介绍的链接数组
		return deal.html(Chtml.getoumei(Program.pages))
	def mnext(self):
		Program.mpages+=1
		print('页数:'+str(Program.mpages))
		meiju.getName(Program.mpages)
	def mback(self):
		if Program.mpages>1:
			Program.mpages-=1
		print('页数:'+str(Program.mpages))
		meiju.getName(Program.mpages)
		

		