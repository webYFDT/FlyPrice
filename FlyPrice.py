# -*- coding:utf-8 -*-
import requests
import re
import time
from twilio.rest import Client
import datetime
def SMS(low_price,date,number):
	acc='ACe09235d42c71d4f82bb2e95bdc0de140'
	aut='e6bf813bbe8aa2aed9be351bad53b93a'
	client=Client(acc,aut)
	body_text="(东方)1-25~1-27最低太原到重庆机票的价格为: "+str(low_price)+" 日期为: "+date
	message=client.messages.create(
	    to=number,
	    from_="+12562864849 ",
	    body=body_text
	    )
url='http://www.ceair.com/otabooking/flight-lowpricesearch!doLowpriceSearch.shtml'
key={'lowpriceCond':'{"tripType":"OW","adtCount":1,"chdCount":0,"infCount":0,"currency":"CNY","sortType":"a","segmentList":[{"deptCd":"TYN","arrCd":"CKG","deptDt":"2018-01-27","deptAirport":"","arrAirport":"","deptCdTxt":"太原","arrCdTxt":"重庆","deptCityCode":"TYN","arrCityCode":"CKG"}],"sortExec":"a","page":"0"}'}
low_price=500
n=1
while True:
	print datetime.datetime.now()
	print '运行次数: '+str(n)
	r=requests.post(url,data=key)
	data=r.json()
	print data
	price_list=[]
	for i in [1,2,3,4]:
		p=int(data[u'lowPriceDto'][0][u'lowPriceItem'][i])
		if p==-1:
			p=9000
		price_list.append()
	price=min(price_list)
	print price_list
	price_addr=price_list.index(price)#位置
	#print price
	#print price_addr
	date='2017-1-'+str(price_addr+25)
	if low_price>price:
		low_price=price
		'''短信或者微信接口，当有更低价格时给我发短信或者微信'''
		numberliu='+8615735640998'
		numberWu='+8618181392015'
		SMS(low_price,date,numberliu)
		SMS(low_price,date,numberWu)
	time.sleep(1800)
	n=n+1
