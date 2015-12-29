from django.conf.urls import patterns, url
from login import views


urlpatterns = patterns('',
    url(r'^$', views.login_view, name='login_view'),
    url(r'^sign$', views.sign_view, name='sign_view'),
)