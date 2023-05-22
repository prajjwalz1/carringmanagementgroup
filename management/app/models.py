from django.db import models
from PIL import Image
import io
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.base import ContentFile

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to='projects',null=True)
    flaticon_icon_class = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    def save(self, *args, **kwargs):
        # Open the image using Pillow
        image = Image.open(self.image)

        # Get the dimensions of the original image
        width, height = image.size

        # Determine the desired size for cropping
        crop_size = min(width, height)

        # Calculate the coordinates for cropping the image
        left = (width - crop_size) // 2
        top = (height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Resize the cropped image to a desired size
        desired_size = (350, 350)
        cropped_image.thumbnail(desired_size, Image.ANTIALIAS)

        # Optimize the image to reduce file size
        optimized_image = ImageOps.exif_transpose(cropped_image)
        optimized_image.save(self.image.path, optimize=True)

        # Save the rest of the model
        super().save(*args, **kwargs)

    # Other fields for company information

    def __str__(self):
        return self.name

from PIL import Image,ImageOps
class Our_team(models.Model):
    Name = models.CharField(max_length=100)
    Role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects')
    fb = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Open the image using Pillow
        image = Image.open(self.image)

        # Get the dimensions of the original image
        width, height = image.size

        # Determine the desired size for cropping
        crop_size = min(width, height)

        # Calculate the coordinates for cropping the image
        left = (width - crop_size) // 2
        top = (height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Resize the cropped image to a desired size
        desired_size = (350, 350)
        cropped_image.thumbnail(desired_size, Image.ANTIALIAS)

        # Optimize the image to reduce file size
        optimized_image = ImageOps.exif_transpose(cropped_image)
        optimized_image.save(self.image.path, optimize=True)

        # Save the rest of the model
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Name;


class testimony(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects')
    comments = models.TextField(max_length=1000)

    def save(self, *args, **kwargs):
        # Open the image using Pillow
        image = Image.open(self.image)

        # resize the image to the desired dimensions
        image = image.resize((607, 607))

        # Save the cropped image to a buffer
        buffer = io.BytesIO()
        image.save(buffer, 'JPEG')
        buffer.seek(0)

        # Save the buffer to the ImageField
        self.image.save(self.image.name, buffer, save=False)

        # Save the rest of the model
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name;


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects')
    project_location = models.CharField(max_length=100)
    project_Description = models.TextField(max_length=100)
    project_cost = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name;


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='projects', null=True)
    is_published = models.BooleanField(default=False)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Publisher_image = models.ImageField(upload_to='projects', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date']


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=100)
    package_flaticon_icon_class = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.name


class Slide(models.Model):
    image_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel')
    def save(self, *args, **kwargs):
        # Open the original image using Pillow
        original_image = Image.open(self.image)

        # Optimize the image to reduce file size
        optimized_image = ImageOps.exif_transpose(original_image)

        # Create an in-memory file-like object to save the optimized image
        image_io = BytesIO()
        optimized_image.save(image_io, format='JPEG', optimize=True)

        # Create an InMemoryUploadedFile from the optimized image
        optimized_image_file = InMemoryUploadedFile(
            image_io,
            None,
            self.image.name,
            'image/jpeg',
            optimized_image.tell,
            None
        )

        # Save the optimized image to the image field
        self.image = optimized_image_file

        super().save(*args, **kwargs)

    def __str__(self):
        return self.image_title
from django.core.exceptions import ValidationError
def validate_svg(value):
    if value.file.content_type != 'image/svg+xml':
        raise ValidationError("Only SVG files are allowed.")

class SVGField(models.FileField):
    def __init__(self, *args, **kwargs):
        kwargs['upload_to'] = 'logo'  # Set the upload directory as per your requirements
        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super().clean(*args, **kwargs)
        validate_svg(data)
        return data
import io
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
class about_us(models.Model):
    image = models.ImageField(upload_to='projects/carousel/', max_length=255, null=True)
    Company_name = models.CharField(max_length=100, null=True)
    logo = SVGField(null=True)
    Title = models.CharField(max_length=100, null=True)
    years_of_experience = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True)
    Total_projects = models.CharField(max_length=20, null=True)
    image_thumbnail = models.ImageField(upload_to='projects/thumbnails/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Open the original image using Pillow
        original_image = Image.open(self.image)

        # Optimize the image to reduce file size
        optimized_image = ImageOps.exif_transpose(original_image)

        # Create an in-memory file-like object to save the optimized image
        image_io = BytesIO()
        optimized_image.save(image_io, format='JPEG', optimize=True)

        # Create an InMemoryUploadedFile from the optimized image
        optimized_image_file = InMemoryUploadedFile(
            image_io,
            None,
            self.image.name,
            'image/jpeg',
            optimized_image.tell,
            None
        )

        # Save the optimized image to the image field
        self.image = optimized_image_file

        super().save(*args, **kwargs)


    def __str__(self):
        return self.Company_name



class Appointment(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20)
    services = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class Availability(models.Model):
#     day = models.CharField(max_length=20)
#     morning = models.BooleanField(default=False)
#     noon = models.BooleanField(default=False)
#     night = models.BooleanField(default=False)
#     custom_time_slot = models.CharField(max_length=100, blank=True)
#
# class FormSubmission(models.Model):
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     contact = models.CharField(max_length=50)
#     email = models.EmailField()
#     country = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     birthdate = models.DateField(blank=True, null=True)
#     passportnumber = models.CharField(max_length=50)
#     TFN = models.CharField(max_length=50)
#     policeChecks = models.CharField(max_length=10)
#     wwcc = models.CharField(max_length=10)
#     covidVaccination = models.CharField(max_length=20, choices=[("firstDose", "First Dose"), ("secondDose", "Second Dose")], blank=True)
#     account_holder_name = models.CharField(max_length=50)
#     bsbnumber = models.CharField(max_length=20)
#     accountnumber = models.CharField(max_length=50)
#     emergency_contact_person = models.CharField(max_length=50)
#     emergency_contact_number = models.CharField(max_length=50)
#     availability = models.ManyToManyField(Availability)
#
#     def __str__(self):
#         return f"{self.firstname} {self.lastname}"

from django.db import models
from django.core.files.base import ContentFile
import pandas as pd


import io

class FormSubmission(models.Model):
    excel_file = models.FileField(upload_to='projects/form_submissions/')

    @classmethod
    def create_from_dataframe(cls, df):
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        excel_file = ContentFile(excel_buffer.getvalue())
        form_submission = cls.objects.create(excel_file=excel_file)
        return form_submission

    def update_from_dataframe(self, df):
        existing_df = pd.read_excel(self.excel_file)
        updated_df = pd.concat([existing_df, df], ignore_index=True)

        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            updated_df.to_excel(writer, index=False)
        updated_excel_file = ContentFile(excel_buffer.getvalue())

        self.excel_file.save(self.excel_file.name, updated_excel_file, save=False)
        self.save()
