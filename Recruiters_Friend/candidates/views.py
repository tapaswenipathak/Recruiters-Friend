from django.shortcuts import render, render_to_response
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
	topic, users = followers.get_some_followers(data)
	#print topic, users 
	response_data={'topic':topic, 'names':users}
	print('From views', json.dumps(response_data))
	#return HttpResponse(json.dumps(response_data),content_type="application/json")
	return render_to_response('candidates_result.html', response_data, context_instance=RequestContext(request))
