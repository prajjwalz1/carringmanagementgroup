from django.shortcuts import render
from .models import Blog,Our_team,Feature,testimony,about_us,Slide,Service,Project,Package
# Create your views here.
def home(request):
  slide=Slide.objects.all()
  try:
    about = about_us.objects.get(logo__isnull=False)
    logo = about.logo
  except about_us.DoesNotExist:
    logo = None
  about=about_us.objects.all()
  services=Service.objects.all()
  team=Our_team.objects.all()
  testimonies=testimony.objects.all()
  projects = Project.objects.all()


  Context={'slides':slide,'about':about,'services':services,'team':team,'testimonies':testimonies,'logo':logo,'projects':projects

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

  return HttpResponse('success')
  # messages.success(request, 'appointment fixed')

def about(request):
  try:
    about = about_us.objects.get(logo__isnull=False)
    logo = about.logo
  except about_us.DoesNotExist:
    logo = None
  slide = Slide.objects.get(id=2)
  abouts=about_us.objects.all()
  team = Our_team.objects.all()
  testimonies = testimony.objects.all()
  services=Service.objects.all()
  Context={
    'about':abouts,'team':team,'testimonies':testimonies,'services':services,'slides':slide,'logo':logo
  }
  return render(request,'about.html',Context)

def service_view(request):
  try:
    about =about_us.objects.get(logo__isnull=False)
    logo = about.logo
  except about_us.DoesNotExist:
    logo = None

  slide = Slide.objects.get(id=3)
  services = Service.objects.all()
  package = Package.objects.all()
  Context={
    'services':services,'package':package,'slides':slide,'logo':logo
  }
  return render(request,'services.html',Context)


def Portfolio_view(request):
  try:
    about = about_us.objects.get(logo__isnull=False)
    logo = about.logo
  except about_us.DoesNotExist:
    logo = None
  projects=Project.objects.all()
  slide = Slide.objects.get(id=3)


  Context={
    'projects':projects,'slides':slide,'logo':logo
  }
  return render(request,'portfolio.html',Context)

def Package_view(request):
  package=Package.objects.all()


  Context={
    'package':package
  }
  return render(request,'pricing.html',Context)

def blog_view(request):
  try:
    about = about_us.objects.get(logo__isnull=False)
    logo = about.logo
  except about_us.DoesNotExist:
    logo = None
  slide = Slide.objects.get(id=4)
  blogs=Blog.objects.all()

  Context={
   'blogs':blogs,'slides':slide,'logo':logo
  }
  return render(request,'blog.html',Context)

def contact_view(request):
  try:
    about = about_us.objects.get(logo__isnull=False)
    logo = about.logo
  except about_us.DoesNotExist:
    logo = None
  blogs=Blog.objects.all()
  slide = Slide.objects.get(id=3)


  Context={
   'blogs':blogs,'slides':slide,'logo':logo
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
      [settings.DEFAULT_FROM_EMAIL,'consignsolution@gmail.com','bpn.dahal36@gmail.com','sauravrauniyar111@gmail.com'],
      fail_silently=False,
    )
    messagesucces = "Message sent successfully"

    return render(request,'contact.html',{'message':messagesucces })
  return render(request, 'contact.html')

def enquiry(request):
  return render(request,'enquiryform.html')

import ast
import ast
import io
import pandas as pd
from django.http import HttpResponse
from django.views import View
from .models import FormSubmission
from django.core.files.base import ContentFile
import json
class FormSubmissionView(View):
  def post(self, request, *args, **kwargs):
    # Process the form data
    form_data = request.POST.dict()  # Convert POST data to a dictionary
    form_data = request.POST.dict()  # Convert POST data to a dictionary
    availability_data = json.loads(form_data['availability'])  # Convert availability string to a list of dictionaries

    del form_data['availability']  # Remove availability from form_data as it will be handled separately

    df = pd.DataFrame([form_data])
    print(df)# Create a DataFrame from the remaining form data

    # Retrieve the existing Excel file from the database
    form_submission = FormSubmission.objects.first()  # Example, you can retrieve the desired file based on your logic

    import os

    if form_submission is None:
      # Create a new Excel file if it doesn't exist
      excel_buffer = io.BytesIO()
      with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
      excel_file = ContentFile(excel_buffer.getvalue())
      form_submission = FormSubmission.objects.create(excel_file=excel_file)
    else:
      # Read the existing Excel file into a DataFrame
      existing_df = pd.read_excel(form_submission.excel_file)

      # Append the new form data to the existing DataFrame
      updated_df = pd.concat([existing_df, df], ignore_index=True)

      excel_buffer = io.BytesIO()
      with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        updated_df.to_excel(writer, index=False)
      excel_file = ContentFile(excel_buffer.getvalue())

      # Update the excel_file field in the database
      form_submission.excel_file.save(form_submission.excel_file.name, excel_file, save=False)
      form_submission.save()

    # Handle availability data and save to database or perform any desired operations
    for availability in availability_data:
      # Process each availability entry as desired
      day = availability['day']
      morning = availability['morning']
      noon = availability['noon']
      night = availability['night']
      customTimeSlot = availability['customTimeSlot']

      # Save the availability information to the database or perform any desired operations

    # Return a success response
    return HttpResponse('success')