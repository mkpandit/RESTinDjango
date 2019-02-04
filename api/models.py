#models.py

from django.db import models

LANGUAGE_CHOICES = (
	("python", 'python'),
    ("java", 'java'),
	("PHP", "PHP")
)

STYLE_CHOICES = (
	('friendly', 'friendly'),
	('strict', 'strict')
)

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

class Snippets(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default="")
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

	class Meta:
		ordering = ('created', )