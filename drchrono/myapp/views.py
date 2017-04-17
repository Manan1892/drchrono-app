from django.shortcuts import render,redirect, render_to_response
from django.contrib.auth.decorators import login_required
import requests
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth import login, logout as my_logout
from django.views.generic import View
from django.http import JsonResponse
from datetime import datetime
from django.core import serializers
from myapp.models import *
from myapp.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from datetime import datetime 



class IndexView(View):
	def get(self, request, *args, **kwargs):
		return render(request,'index.html')
	
def data_url(request,url, filter={}):
    data = []
    headers = {'Authorization': 'Bearer %s' %request.session['access_token'],}
    while url:
        page = requests.get(url, filter, headers=headers).json()
        data.extend(page['results'])
        url = page['next']
    return data

	
class HomeView(APIView):
	def get(self, request, *args, **kwargs):
		if (request.user.is_anonymous() == True or request.user.is_authenticated() == False) :
			return Response({'status':'Failed'})
		else:
			instance = request.user.social_auth.get(provider='drchrono')
			user_name = str(instance)
			request.session['un'] = user_name
			request.session['access_token'] = instance.extra_data['access_token']
			data = data_url(request,'https://drchrono.com/api/users')
			patients = data_url(request,'https://drchrono.com/api/patients')

			for da in data:
				if da['username'] == user_name:
					if da['is_doctor'] == True:
						request.session['doc_id'] = da['doctor']
			today = datetime.today()
			mon = today.month
			day = today.day
			if int(day) < 10:
			  day = '0'+str(day)

			if int(mon) < 10:
			  mon = '0'+str(mon)

			date = str(mon)+"-"+str(day)
			return Response({'status':'Success','username':user_name,'patients':patients,'date':date})


class SendmailView(APIView):
    #send email using the email id
    def get(self, request):
	    if request.method == "GET":
			patients = data_url(request,'https://drchrono.com/api/patients')
			today = datetime.today()
			mon = today.month
			day = today.day
			if int(day) < 10:
			  day = '0'+str(day),

			if int(mon) < 10:
			  mon = '0'+str(mon)

			date = str(mon)+"-"+str(day)
			for p in patients:
				if p['date_of_birth'] and p['email']:
					try:
						Patients.objects.get(date=today.date(),patient_id=p['id'])
					except:
						if date in p['date_of_birth']:
							email = p['email']
							mesage = 'Wishing you all the great things in life, hope this day will bring you an extra share of all that makes you happiest. Happy Birthday.'
							email = EmailMessage('Happy Birthday!', mesage, to=[email])
							email.send()
							inst = Patients(date=today.date(),flag='True',patient_id=p['id'],
											first_name = p['first_name'],
											last_name=p['last_name'],
											email=p['email'])
							inst.save()
			return Response({'message':'Mesage Sent Successfully!'})

		
def logout(request):
	my_logout(request)
	return redirect('/')

