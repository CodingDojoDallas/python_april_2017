from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
import datetime
import pytz 
from django.db.models import Count


def index(request):
	print ('INDEX')

	client = Client.objects.all()
	context = {'clients': client}
	return render(request, 'first_app/index.html', context)

def Showaddclient(request):
	print ('Showaddclient')
	#loads form
	return render(request, 'first_app/addclient.html')

def addclient(request):
	print('addclient')
	if request.method != 'POST':
		return redirect('/')
	else:
		check = Client.objects.validateClient(request.POST)
		if check[0] == False:
			for errors in check[1]:
				messages.error(request, errors)
			return redirect('/Showaddclient')
		else:
			client = Client.objects.filter(name=request.POST['business_name']).first()
			print client
			if client is not None:
				messages.error(request,'client already exists')
				return redirect('/Showaddclient')
			else:
				client = Client.objects.create(name=request.POST['business_name'], email=request.POST['email'], phone=request.POST['phone'])
				return redirect('/client/{}'.format(client.id))



def client(request,clientid):
	print('client')
	client = Client.objects.filter(id=clientid).first()
	context = {'client': client}

	return render(request, 'first_app/client.html', context)

def showaddproject(request, clientid):
	print ('showaddproject')

	context = {'clientid': clientid}

	return render(request, 'first_app/addproject.html',context)

def addproject(request, clientid):
	print ('addproject')
	if request.method != 'POST':
		return redirect('/')
	else:
		check = Project.objects.validateProject(request.POST)
		if check[0] == False:
			for errors in check[1]:
				messages.error(request, errors)
			return redirect('/showaddproject/{}'.format(clientid))
		else:
			client = Client.objects.filter(id=clientid).first()
			project = Project.objects.create(title=request.POST['project_name'], client=client)
			note = Note.objects.create(content=request.POST['notes'], project=project)

	return redirect('/project/{}'.format(project.id))


def project(request, projectid):
	print('project')

	project = Project.objects.get(id=projectid)
	context = {'project':project}


	return render(request, 'first_app/project.html', context)

def addnote(request, projectid):
	print('addnote')
	if request.method != 'POST':
		return redirect('/')
	else:
		check = Note.objects.validateNote(request.POST)
		if check[0] == False:
			for errors in check[1]:
				messages.error(request, errors)
			return redirect('/project/{}'.format(projectid))
		else:
			project = Project.objects.filter(id=projectid).first()
	
			note = Note.objects.create(content=request.POST['add_note'], project=project)
	


	return redirect('/project/{}'.format(projectid))

def deleteNote(request, noteid):
	print ('deleteNote')
	

	note = Note.objects.filter(id=noteid).first()
	projectid = note.project.id
	note.delete()


	return redirect('/project/{}'.format(projectid))



