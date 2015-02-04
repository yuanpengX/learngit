import feedparser
import re

def getwordcounts(url):
	d = feedparser.parse(url);
	wc ={};
	
	for e in d.entries:
		if 'summary' in e:summary = e.summary;
		else: summary = e.description;
		worlds=getwords(e.title+' '+summary);
		for word in words:
			wc.setdefault(word,0);
			wc[word]+=1;
	
	return d.feed.title,wc

def getwords(html):
	txt = re.compile(r'<[^>]+>').sub('',html);#clean html tag
	words = re.compile(r'[^A-Z^a-z]+').split(txt);#split into word
	return [word.lower() for word in words if word!=''];#convert into lower words
