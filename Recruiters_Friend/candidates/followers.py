import urllib2
from bs4 import BeautifulSoup
import feedparser
import re



####################################################################
# API
####################################################################

def  get_some_followers (topic) :
	url = "http://www.quora.com/" + topic + "/followers"
	html_doc = urllib2.urlopen (url)
	soup = BeautifulSoup (html_doc.read ())
	raw_data = str (soup.find_all ('a',class_='user'))
	soup = BeautifulSoup (raw_data)
	name = soup.get_text ()
	print type (name)
	return topic, name
	
