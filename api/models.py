#models.py

from django.db import models


# Define the model
# First Name, Last Name, Phone Number, E-mail Address, Date of creation, Date of modification
class phoneContact(models.Model):
	first_name = models.CharField(max_length=255, blank=False)
	last_name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=255, blank=False)
	email = models.CharField(max_length=255, default='noname@mail.com')
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.first_name)