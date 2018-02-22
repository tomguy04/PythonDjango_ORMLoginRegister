from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^login$', views.login),  
  url(r'^logout$', views.logout),
  url(r'^dashboard$', views.dashboard),
  url(r'^doregister$', views.doregister),
  url(r'^$', views.index)     # This line has changed!
]
