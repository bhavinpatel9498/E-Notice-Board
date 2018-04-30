from django.shortcuts import render
from django.http import HttpResponse
import datetime

from myapp.officialview import *
# Create your views here.
from myapp.saveofficialpostview import *

def hello(request):
    return render(request, "hello.html", {})

def homepage(request):
	return render(request, "HomePage.html", {})


def createofficialpost(request):
    emailid = request.POST.get('emailid')
    user = request.POST.get('user')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')

    errmsg = request.POST.get('errormsg')

    print ('errmsg :'+str(errmsg))

    if str(errmsg) == 'None':
        errmsg = 'All fields are Mandatory'

    params = {'emailid': emailid, 'user': user, 'subject': subject, 'msg': msg, 'errormsg': errmsg}
    return render(request, "CreateNewPost.html", params)

def createsportspost(request):
    emailid = request.POST.get('emailid')
    user = request.POST.get('user')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')

    errmsg = request.POST.get('errormsg')

    print ('errmsg :'+str(errmsg))

    if str(errmsg) == 'None':
        errmsg = 'All fields are Mandatory'

    params = {'emailid': emailid, 'user': user, 'subject': subject, 'msg': msg, 'errormsg': errmsg}
    return render(request, "CreateNewSportsPost.html", params)

def createeventpost(request):
    emailid = request.POST.get('emailid')
    user = request.POST.get('user')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')

    errmsg = request.POST.get('errormsg')

    print ('errmsg :'+str(errmsg))

    if str(errmsg) == 'None':
        errmsg = 'All fields are Mandatory'

    params = {'emailid': emailid, 'user': user, 'subject': subject, 'msg': msg, 'errormsg': errmsg}
    return render(request, "CreateNewEventPost.html", params)

def createbuypost(request):
    emailid = request.POST.get('emailid')
    user = request.POST.get('user')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')

    errmsg = request.POST.get('errormsg')

    print ('errmsg :'+str(errmsg))

    if str(errmsg) == 'None':
        errmsg = 'All fields are Mandatory'

    params = {'emailid': emailid, 'user': user, 'subject': subject, 'msg': msg, 'errormsg': errmsg}
    return render(request, "CreateNewBuyPost.html", params)


   
#def hello(request):
   # now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)