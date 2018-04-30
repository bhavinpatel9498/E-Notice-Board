from django.shortcuts import render
from myapp.models import *


def saveofficialpost(request):
    emailid = request.POST.get('emailid')
    user = request.POST.get('user')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')

    print('Bhavin *****************'+str(msg))

    print('Bhavin Before save')

    errmsg = ''

    try:
        post = officialpoststbl(username=user, emailid=emailid, subject=subject, message=msg)
        post.save()
        errmsg = 'Post Saved Successfully'
    except:
        errmsg = 'Error Occurred! Try Again.'

    print('Bhavin after save')

    params = {'emailid': emailid, 'user': user, 'subject': subject, 'msg': msg, 'errormsg': errmsg}

    return render(request, "CreateNewPost.html", params)


def saveeventpost(request):
    emailid = request.POST.get('emailid')
    user = request.POST.get('user')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')

    print('Bhavin *****************'+str(msg))

    print('Bhavin Before save')

    errmsg = ''

    try:
        post = eventspoststbl(username=user, emailid=emailid, subject=subject, message=msg)
        post.save()
        errmsg = 'Post Saved Successfully'
    except:
        errmsg = 'Error Occurred! Try Again.'

    print('Bhavin after save')

    params = {'emailid': emailid, 'user': user, 'subject': subject, 'msg': msg, 'errormsg': errmsg}

    return render(request, "CreateNewEventPost.html", params)



def savesportspost(request):
    emailid = request.POST.get('emailid')
    user = request.POST.get('user')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')

    print('Bhavin *****************'+str(msg))

    print('Bhavin Before save')

    errmsg = ''

    try:
        post = sportspoststbl(username=user, emailid=emailid, subject=subject, message=msg)
        post.save()
        errmsg = 'Post Saved Successfully'
    except:
        errmsg = 'Error Occurred! Try Again.'

    print('Bhavin after save')

    params = {'emailid': emailid, 'user': user, 'subject': subject, 'msg': msg, 'errormsg': errmsg}

    return render(request, "CreateNewSportsPost.html", params)


def savebuypost(request):
    emailid = request.POST.get('emailid')
    user = request.POST.get('user')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')

    print('Bhavin *****************'+str(msg))

    print('Bhavin Before save')

    errmsg = ''

    try:
        post = buysellpoststbl(username=user, emailid=emailid, subject=subject, message=msg)
        post.save()
        errmsg = 'Post Saved Successfully'
    except:
        errmsg = 'Error Occurred! Try Again.'

    print('Bhavin after save')

    params = {'emailid': emailid, 'user': user, 'subject': subject, 'msg': msg, 'errormsg': errmsg}

    return render(request, "CreateNewBuyPost.html", params)