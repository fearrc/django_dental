from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

def home(request):
	return render(request,'home.html', {})

def about(request):
	return render(request,'about.html', {})

def blogdetails(request):
	return render(request,'blog-details.html', {})

def blog(request):
	return render(request,'blog.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		try:
			send_mail(
				message_name, #subject
				message, #message
				message_email, #from email
				['camfearrington@gmail.com'], #to email
				fail_silently=False,
				) 
		except BadHeaderError:
			return HttpResponse('Invalid Header Found.')
		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request,'contact.html', {})

def pricing(request):
	return render(request,'pricing.html', {})

def service(request):
	return render(request,'service.html', {})
