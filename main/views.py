from django.shortcuts import render_to_response
import requests

# Create your views here.
from django.template import RequestContext

CLIENT_ID = 'ba8e87348d3b4d8aa124578e513c11b3'
CLIENT_SECRET = '584e2de24e2b4ad1b8f7c788107dc6f2'
REDIRECT_URI = 'http://ff.agulex.com'


instagram_login_gateway = 'https://api.instagram.com/oauth/authorize/?client_id=%s&redirect_uri=%s&response_type=code' % (CLIENT_ID, REDIRECT_URI)


def index(request):
    context = {}
    if request.GET.get('code') == None:
        context['instagram_login_gateway'] = instagram_login_gateway
    else:
        CODE = request.GET.get('code')
        post_url = 'https://api.instagram.com/oauth/access_token?client_secret=%s&grant_type=authorization_code&redirect_uri=%s&code=%s'% (CLIENT_SECRET, REDIRECT_URI, CODE)
<<<<<<< HEAD
=======
        # write response to file to view.
        f = open('response.txt', 'w')
        f.write(requests.POST(post_url))
        f.close()
>>>>>>> ebd4e35d6ed3a831323affe66da7d1932eb5cfaa

        context['response'] = requests.post(post_url)

    return render_to_response('base.html', context, context_instance=RequestContext(request))
