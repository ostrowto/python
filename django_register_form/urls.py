#urls.py

from django.conf.urls import url
from mysite.core import views as core_Views

urlpatterns = [url(r'^signup/$', core_Views.signup, name = 'signup'),]

