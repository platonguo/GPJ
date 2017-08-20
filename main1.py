# coding=utf-8
#获取图片所在网页的地址，以及新建文件夹 9999988
import urllib
import urllib2
import re
import sys
 

def processMainUrl2(content,x): 
    pattern = r'<h3><a href="(htm_data/\d{1,2}/\d{1,4}/\d{1,7}\.html)" target="_blank" id="">(.{1,100})</a></h3>' 

    m = re.compile(pattern)
    urls = re.findall(m, content)
 
    f0=file("%s.txt"%x,"a+")
    for i, url in enumerate(urls):
        f0.writelines(url[0]+";"+url[1])
	f0.writelines('\n')





 
def processMainUrl(url,x):
  	send_headers = {
	'Host':'dz.m85.co',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Connection':'keep-alive'
	}
	req = urllib2.Request(url,headers=send_headers)
	r = urllib2.urlopen(req)
	mainHtml = r.read()
	processMainUrl2(mainHtml,x)
	f=file("%s.html"%x,"w")
	f.write(mainHtml)

file1 = open("main.txt")
line = file1.readline()
x=1
while line:
    if line.startswith('//'):
        line = file1.readline()
        continue
    print line
    #dosomething here
    processMainUrl(line,x)
    x+=1
    line = file1.readline()
    

    


