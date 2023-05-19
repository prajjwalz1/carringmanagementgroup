from django.db import models
from PIL import Image
import io
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    flaticon_icon_class = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

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
    project_challenges = models.TextField(max_length=100)
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
    image = models.ImageField(upload_to='carousel_images')

    def __str__(self):
        return self.image_title

import io
from io import BytesIO
class about_us(models.Model):
    image = models.ImageField(upload_to='carousel_images/', null=True)
    Company_name = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='logo', null=True)
    Title = models.CharField(max_length=100, null=True)
    years_of_experience = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True)
    Total_projects = models.CharField(max_length=20, null=True)
    image_thumbnail = models.ImageField(upload_to='projects/thumbnails/', null=True, blank=True)

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
