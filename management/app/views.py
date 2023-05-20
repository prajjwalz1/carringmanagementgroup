from django.shortcuts import render
from .models import Blog,Our_team,Feature,testimony,about_us,Slide,Service,Project,Package
# Create your views here.
def home(request):
  slide=Slide.objects.all()
  about=about_us.objects.all()
  services=Service.objects.all()
  team=Our_team.objects.all()
  testimonies=testimony.objects.all()
  projects=Project.objects.all()
  Blogs=Blog.objects.all()
  package=Package.objects.all()
  Context={'slides':slide,'about':about,'services':services,'team':team,'testimonies':testimonies,'projects':projects,'blogs':Blogs,'package':package

  }
  return render(request,'index.html',Context)


def recent_blogs(request):
  blogs = Blog.objects.filter(is_published=True).order_by('-publication_date')[:3]
  return render(request, 'blog/recent_blogs.html', {'blogs': blogs})


from .models import Appointment
from django.http import HttpResponse

def make_appointment(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    services = request.POST.get('services')
    email = request.POST.get('email')
    appointment = Appointment(name=name, phone=phone, services=services, email=email)
    appointment.save()


  return HttpResponse('successs')
  # messages.success(request, 'appointment fixed')

def about(request):
  abouts=about_us.objects.all()
  team = Our_team.objects.all()
  testimonies = testimony.objects.all()
  services=Service.objects.all()
  Context={
    'about':abouts,'team':team,'testimonies':testimonies,'services':services
  }
  return render(request,'about.html',Context)

def service_view(request):
  services = Service.objects.all()
  package = Package.objects.all()
  Context={
    'services':services,'package':package
  }
  return render(request,'services.html',Context)


def Portfolio_view(request):
  projects=Project.objects.all()

  Context={
    'projects':projects
  }
  return render(request,'portfolio.html',Context)

def Package_view(request):
  package=Package.objects.all()

  Context={
    'package':package
  }
  return render(request,'pricing.html',Context)

def blog_view(request):
  blogs=Blog.objects.all()

  Context={
   'blogs':blogs
  }
  return render(request,'blog.html',Context)

def contact_view(request):
  blogs=Blog.objects.all()


  Context={
   'blogs':blogs
  }
  return render(request,'contact.html',Context)

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse
import time
def contact_form(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    print(name)
    print(email)
    print(message)

    # Send email
    send_mail(
      'Contact Form Submission',
      f'Name: {name}\nEmail: {email}\nMessage: {message}',
      settings.DEFAULT_FROM_EMAIL,
      [settings.DEFAULT_FROM_EMAIL,'consignsolution@gmail.com','bpn.dahal36@gmail.com'],
      fail_silently=False,
    )
    messagesucces = "Message sent successfully"

    return render(request,'contact.html',{'message':messagesucces })
  return render(request, 'contact.html')

def enquiry(request):
  return render(request,'enquiryform.html')