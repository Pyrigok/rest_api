from django.db import models

class Books_Model(models.Model):
	title = models.CharField(
		max_length=100,
		null=False,
		verbose_name = u'Book Title')

	author = models.CharField(
		max_length = 100,
		null = False,
		verbose_name = u'Book Author Name')

	description = models.CharField(
		max_length = 255,
		null = True,
		verbose_name = u'Short books description')

	def __str__(self):
		return '%s %s' %(self.title, self.author, self.description)
