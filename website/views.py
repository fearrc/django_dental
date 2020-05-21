from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
import website.models

def home(request):
	return render(request,'home.html', {})

def about(request):
	return render(request,'about.html', {})

def blogdetails(request):
	return render(request,'blog-details.html', {})

def blog(request):
	website.models.test()
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

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_phone = str(your_phone[0:3])+'-'+str(your_phone[3:6])+'-'+str(your_phone[6:10])
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_day = request.POST['your-day']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']

		return render(request, 'appointment.html', {
			'your_name':your_name,
			'your_phone':your_phone,
			'your_email':your_email,
			'your_address':your_address,
			'your_day':your_day,
			'your_time':your_time,
			'your_message':your_message,
			})
	else:
		return render(request,'appointment.html', {})

def newsletter(request):
	if request.method == "POST":
		nl_email = request.POST['nl-email']

		return render(request, 'newsletter.html', {
			'nl_email':nl_email,
			})
	else:
		return render(request,'newsletter.html', {})

def calendar(request):
	print(website.models.test())
	return render(request,'home.html', {})