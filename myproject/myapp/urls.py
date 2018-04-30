from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
	url(r'^homepage/', views.homepage, name='homepage'),
	url(r'^officialpost/', views.officialpost, name='officialpost'),
	url(r'^createofficialpost/', views.createofficialpost, name='createofficialpost'),
	url(r'^saveofficialpost/', views.saveofficialpost, name='saveofficialpost'),

	url(r'^eventpost/', views.eventspost, name='eventpost'),
	url(r'^createeventpost/', views.createeventpost, name='createeventpost'),
	url(r'^saveeventpost/', views.saveeventpost, name='saveeventpost'),
	
	url(r'^buypost/', views.buypost, name='buypost'),
	url(r'^createbuypost/', views.createbuypost, name='createbuypost'),
	url(r'^savebuypost/', views.savebuypost, name='savebuypost'),
	
	url(r'^sportpost/', views.sportspost, name='sportpost'),
	url(r'^createsportspost/', views.createsportspost, name='createsportspost'),
	url(r'^savesportspost/', views.savesportspost, name='savesportspost'),
]