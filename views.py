from django.shortcuts import render,render_to_response, RequestContext,HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.
from .forms import LoginForm
def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/ProjectEvaluation/loggedin')
    else:
        return HttpResponseRedirect('/ProjectEvaluation/invalid')
    
def loggedin(request):
    return render_to_response('loggedin.html',
                             {'username':request.user.username})

def invalid(request):
    return render_to_response('invalid.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
