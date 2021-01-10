from django.shortcuts import render, HttpResponse
import requests
import json
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")


def profile(request):
    jsonlist = []
    req = requests.get('https://api.github.com/users/kishorevbhosale')
    jsonlist.append(json.loads(req.content))
    parseData = []
    userData = {}
    for data in jsonlist:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    parseData.append(userData)
    return HttpResponse(parseData)