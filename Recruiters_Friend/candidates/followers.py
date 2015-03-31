import requests
from pattern import web



####################################################################
# API
####################################################################

def  get_some_followers (topic) :
	url = "http://www.quora.com/" + topic + "/followers"
	users = get_user_details(url)
	#print "from get_some_followers ", topic, users
	return topic, users

def get_user_details(url):
	print(url)
	r = requests.get(url)
	html = r.text
	dom = web.Element(html)
	users = {}
	for a in dom.by_class("user"):
		if a.attrs.has_key(u'href'):
			#print(a.attrs[u'href'])
			users["http://www.quora.com"+a.attrs[u'href']] = a.content
	return users