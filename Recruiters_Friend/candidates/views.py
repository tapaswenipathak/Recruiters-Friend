from django.shortcuts import render
from django.http import HttpResponse
import sys
import followers
import json

# Create your views here.
def base1(request):
	return render(request,'candidates.html')

def api_call(request):
	data=request.GET.get('candidates')
	print data
	topic, names = followers.get_some_followers(data)
	print topic, names 
	response_data={'topic':topic, 'names':names}
	return HttpResponse(json.dumps(response_data),content_type="application/json")

