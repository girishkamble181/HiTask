from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from random import randrange
from taskproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .forms import TaskForm
from .models import TaskModel
import requests
import bs4

def delete(request, id):
	name= request.user
	#TaskModel.objects.filter(id=id)
	d= get_object_or_404(TaskModel, id=id )
	d.delete()	
	return redirect('home')		

def logo(request):
	return redirect('home')					
	
def home(request):
	name=request.user
	if request.user.is_authenticated:
		cn="india"
		web_add= "https://www.worldometers.info/coronavirus/country/" + cn +"/"
		ress= requests.get(web_add)
		#print(res)
	
		dataa= bs4.BeautifulSoup(ress.text,"html.parser")		#html tree
		#print(data)
	
		info= dataa.find_all("div",{"class":"maincounter-number"})
		#print(info)

		# find and display on sep lines : total cases, deaths and recovered cases
	
		total_cases=info[0].find('span').text

		print("total cases",total_cases)
		#return render(request,'home.html',{'total_cases':total_cases})




		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + "mumbai"
		a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
		wa = a1 + a2 + a3 

		res= requests.get(wa)	
		data= res.json()
		temp= data['main']['temp']			
		desc= data['weather'][0]['description']
		degree_sign= u'\N{DEGREE SIGN}'

		icon= "http://api.openweathermap.org/img/w/" + data['weather'][0]['icon'] + ".png"
		msg1= "Temperature :  " + str(temp)+ str(degree_sign) + " Condition : " + str(desc)
		print(msg1)
		#return render(request,'ulogin.html',{'msg1':msg1,'icon':icon})
		 
		data= TaskModel.objects.filter(user=name)
		return render(request,'home.html',{'data':data,'msg1':msg1,'icon':icon,'total_cases':total_cases})
	else:
		return redirect('ulogin')

"""
def cases(request):
	if request.user.is_authenticated:
		
	else:
		return redirect('home')		

"""	

def usignup(request):
	if request.method=="POST":
		un= request.POST.get('un')
		em= request.POST.get('em')
		try:
			usr= User.objects.get(username=un)
			return render(request,'usignup.html',{'msg':'username already registered'})
		except User.DoesNotExist:
			try:
				usr= User.objects.get(email=em)
				return render(request,'usignup.html',{'msg':'email already registered'})
			except User.DoesNotExist:
				pw=""
				text="0123456789"
				for i in range(5):
					pw= pw + text[randrange(len(text))]
				print(pw)
				subject= " System Generated Email "
				msg= "Your password is "+str(pw)
				send_mail(subject,msg,EMAIL_HOST_USER,[em])
				usr= User.objects.create_user(username=un, password=pw, email=em)
				usr.save()
				return redirect('ulogin')	


	else:
		return render(request,'usignup.html')

def ulogin(request):
	if request.method == "POST":
		un= request.POST.get('un')
		pw= request.POST.get('pw')
		usr= authenticate(username=un, password=pw)
		if usr is None:
			return render(request,'ulogin.html',{'msg':'invalid credentials'})
		else:
			login(request,usr)
			return redirect('home')
	else:
		return render(request,'ulogin.html')


def ulogout(request):
	logout(request)
	return redirect('ulogin')


def uresetpass(request):
	if request.method=="POST":
		un = request.POST.get('un')
		em = request.POST.get('em')

		try:
			usr= User.objects.get(username=un) and User.objects.get(email=em)			
			pw=""
			text= "1234567890"
			for i in range(5):
				pw= pw + text[randrange(len(text))]
			print(pw)
			subject= " System Generated Email "
			msg= "Your new password is "+ str(pw)
			send_mail(subject,msg, EMAIL_HOST_USER, [em])
			usr= User.objects.get(username=un)
			usr.set_password(pw)
			usr.save()
			return redirect('ulogin')

		except User.DoesNotExist:
			return render(request,'uresetpass.html',{'msg':'username/email does not exist'})
		
	else:
		return render(request,'uresetpass.html')



def create(request):
	if request.method=="POST":
		t= TaskForm(request.POST)
		if t.is_valid():
			task= request.POST['task']
			tm= TaskModel(task=task, user=request.user)
			tm.save()			
			tm= TaskForm()
			return render(request,'create.html',{'tm':tm,'msg':'Task Created'})
		else:
			tm= TaskForm()
			return render(request,'create.html',{'tm':t,'msg':'check errors'})

	else:
		tm= TaskForm()
		return render(request,'create.html',{'tm':tm})
		






