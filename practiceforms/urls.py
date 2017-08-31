from django.conf.urls import url
from practiceforms import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
]