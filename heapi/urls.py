from django.conf.urls import url

from heapi import views

urlpatterns = [
    url(r"^test-api/$", views.MyApiView.as_view(), name="testapi")
    ]