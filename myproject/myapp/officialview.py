
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.db import connection
from myapp.models import *


def officialpost(request):
    now = datetime.datetime.now()
    #cursor = connection.cursor()
    #cursor.execute("SELECT * FROM accounts_account where id=%s", [self.id])
    #cursor.execute("select * from test")
    #row = cursor.fetchall()

    all_posts = officialpoststbl.objects.raw("Select * from myapp_officialpoststbl order by messagedate desc, id desc");

    #all_posts = your_model_class_name.objects.all()

    params = {'current_date': str(now), 'current_date1': str(now), 'all_posts': all_posts}

    return render(request, "OfficialPosts.html", params)


def eventspost(request):
    now = datetime.datetime.now()
    #cursor = connection.cursor()
    #cursor.execute("SELECT * FROM accounts_account where id=%s", [self.id])
    #cursor.execute("select * from test")
    #row = cursor.fetchall()

    all_posts = officialpoststbl.objects.raw("Select * from myapp_eventspoststbl order by messagedate desc, id desc");

    #all_posts = your_model_class_name.objects.all()

    params = {'current_date': str(now), 'current_date1': str(now), 'all_posts': all_posts}

    return render(request, "EventPosts.html", params)

def sportspost(request):
    now = datetime.datetime.now()
    #cursor = connection.cursor()
    #cursor.execute("SELECT * FROM accounts_account where id=%s", [self.id])
    #cursor.execute("select * from test")
    #row = cursor.fetchall()

    all_posts = officialpoststbl.objects.raw("Select * from myapp_sportspoststbl order by messagedate desc, id desc");

    #all_posts = your_model_class_name.objects.all()

    params = {'current_date': str(now), 'current_date1': str(now), 'all_posts': all_posts}

    return render(request, "SportsPosts.html", params)

def buypost(request):
    now = datetime.datetime.now()
    #cursor = connection.cursor()
    #cursor.execute("SELECT * FROM accounts_account where id=%s", [self.id])
    #cursor.execute("select * from test")
    #row = cursor.fetchall()

    all_posts = officialpoststbl.objects.raw("Select * from myapp_buysellpoststbl order by messagedate desc, id desc");

    #all_posts = your_model_class_name.objects.all()

    params = {'current_date': str(now), 'current_date1': str(now), 'all_posts': all_posts}

    return render(request, "BuyPosts.html", params)
