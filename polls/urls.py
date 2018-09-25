from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^test/$', views.test_function)
]