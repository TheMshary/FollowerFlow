import json
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import requests

# Create your views here.
from django.template import RequestContext

CLIENT_ID = 'ba8e87348d3b4d8aa124578e513c11b3'
CLIENT_SECRET = '584e2de24e2b4ad1b8f7c788107dc6f2'
REDIRECT_URI = 'http://ff.agulex.com'
access_token = 'https://instagram.com/oauth/authorize/?client_id=%s&redirect_uri=%s&response_type=token'% (CLIENT_SECRET, REDIRECT_URI)

instagram_login_gateway = 'https://api.instagram.com/oauth/authorize/?client_id=%s&redirect_uri=%s&response_type=code' % (CLIENT_ID, REDIRECT_URI)


def index(request):
    context = {}
    if request.GET.get('code') == None:
        context['instagram_login_gateway'] = instagram_login_gateway
    else:
        CODE = request.GET.get('code')
        params = {}
        params['client_id'] = CLIENT_ID
        params['client_secret'] = CLIENT_SECRET
        params['grant_type'] = 'authorization_code'
        params['redirect_uri'] = REDIRECT_URI
        params['code'] = CODE
        response = requests.post(access_token, params=params)
        context['response'] = response.text


    return render_to_response('base.html', context, context_instance=RequestContext(request))



