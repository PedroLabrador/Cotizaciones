# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from models import *

# Create your views here.

def home(request):
	texto = "banana"
	template = "index.html"

	return render_to_response(template, locals())

def user_request(request):
	data_users = quotes.objects.all()
	to_json = []
	for user in data_users:
		line = {
			"id_number": user.id_number,
			"name": user.name,
			"phone": user.phone,
			"email": user.email,
			"type_info": user.type_info,
			"details": user.details
		}
		to_json.append(line)
	return JsonResponse(to_json, safe=False)