import os, sys;
import pandas as pd;
import urllib2 as u;
import csv, time, random;

def CSVread(f):
	r=[];
	cnt=0;
	with open(f,"rU") as csvfile:
		csvr=csv.reader(csvfile);
		for row in csvr:
			if cnt==0:
				cnt+=1;
				continue;
			t=[k for k in row]
			r+=[t];
	return r;

def getTckrs(fn):
	dx={};
	fc=CSVread(fn);
	for i in fc:
		if i[2]=="include":
			k=i[0];
			v=i[1];
			dx[k]=v;
	return dx,dx.keys();

tckrs=getTckrs("my_tickers.csv")[1];

for t in tckrs:
	print t,;
	sys.stdout.flush();
	try:
		response=u.urlopen("http://chart.finance.yahoo.com/table.csv?s="+t+"&a=8&b=29&c=2001&d=10&e=12&f=2016&g=d&ignore=.csv")
		time.sleep(random.random()*13);
	except u.HTTPError:
		print "*",
		continue;
	html=response.read();
	f=open(t.lower()+".csv","w");
	f.write(html);
	f.close();