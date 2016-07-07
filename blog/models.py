from django.db import models
from django.utils import timezone

class Publication(models.Model):

	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 150)
	contet = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	published_type = models.CharField(max_length = 20, default = 1)

	def publish (self):
		self.published_date = timezone.now()
		self.save()

	def __str__ (self):
		return self.title

class Contact(models.Model):

	subject = models.CharField(max_length = 200)
	message = models.TextField()
	from_email = models.CharField(max_length = 200)

	def __str__ (self):
		return self.title