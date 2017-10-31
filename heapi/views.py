# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from models import HeUser

import datetime

class MyApiView(APIView):
    """
    Test API
    """
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
    	request_id = request.data.get("request_id")
    	user = request.data.get("username")
    	user = HeUser.objects.filter(username="TestUser1")[0]
    	if user:	
	        diff = datetime.datetime.now() - user.tmin.replace(tzinfo=None)
	        if user.hit_count < settings.MAX_THRESHOLD and diff.seconds <=settings.USER_LEVEL_TIME_WINDOW :
	            user.hit_count = user.hit_count + 1
	            print "Current count limit :"+str(user.hit_count)
	            user.save()
	        elif diff.seconds > settings.USER_LEVEL_TIME_WINDOW:
	                print "Before resetting count limit : "+str(user.hit_count)
	                print "Seconds : "+ str(diff.seconds)
	                user.tmin = datetime.datetime.now()
	                user.hit_count = 0
	                user.save()
	                print "Current count limit :"+str(user.hit_count)
	        else:
	            print "Throwttled"
	            return HttpResponseForbidden()
        else:
        	return Response({"message": "User does not exists"},
                        content_type="application/json")
        return Response({"message": "API called successfully!"},
                        content_type="application/json")

