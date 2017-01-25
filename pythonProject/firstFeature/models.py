from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
	def __str__(self):
		return self.question_text
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date of post')

class Choice(models.Model):
	def __str__(self):
		return self.choice_text
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=100)
	votes = models.IntegerField(default=0)

class Validify(models.Model):
	def __str__(self):
		return self.validity
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	validity = models.CharField(max_length=10)

