from django.shortcuts import render
from . import models
import requests
import json
# Create your views here.

def home(request):
	joker=False
	if request.method=='POST':
		first_name=request.POST.get('first')
		last_name= request.POST.get('last')
		
		url= requests.get('http://api.icndb.com/jokes/random?firstName='+first_name+'&lastName='+last_name)
		json_data = json.loads(url.text )
		joke= json_data.get('value').get('joke')
		joker=True
		return render(request, 'index.html', {'joke':joke, 'joker':joker})

	else:
		return render(request, 'index.html')
	


def portfolio(request):
	return render(request,'portfolio.html')

def hire_me(request):
	submit=False
	
	if request.method=='POST':
		name= request.POST['Name']
		email= request.POST['Email']
		message= request.POST['Message']
		data= models.Contact.objects.get_or_create(name=name , email=email , message=message)
		submit=True
	

	return render(request,'hireme.html', {'submit':submit})

import  requests
import json
def dictionary(request):
	if request.method== 'POST':
		word= request.POST.get('word')

		# TODO: replace with your own app_id and app_key
		app_id = 'ea1d3229'
		app_key = '2d6779fdca0a286d67eb310ba86efc14'
		language = 'en'
		word_id = word
		url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word_id.lower()
		#url Normalized frequency
		urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()

		r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key}).json()
		p=r.keys()
		j=''
		status=False

		for i in p:
			j=i
		if j=='error':
			status=True
			return render(request, 'dictionary.html',{'status':status})
		else:
			syn=''
			etymologies=r['results'][0].get('lexicalEntries')[0].get('entries')[0].get('etymologies')
			if etymologies != None:
				for i in etymologies:
					syn=i
			
			mean=''
			meaning=r['results'][0].get('lexicalEntries')[0].get('entries')[0].get('senses')[0]['definitions']
			for i in meaning:
				mean=i
			
			
			try:
				new_word=''
				new=r['results'][0].get('lexicalEntries')[0].get('entries')[0].get('senses')[0].get('examples')[0]['text']
				new_word=new
				# print(new)
				# if new != None:
				# 	for i in new:
				# 		new_word=i
				# print(new_word)
			except TypeError:
				new_word='none'

			return render(request, 'dictionary.html', {'etymologies':syn , 'mean':mean , 'new_word':new_word , 'status':status, 'word':word})
	return render(request, 'dictionary.html')