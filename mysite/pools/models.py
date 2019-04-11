from django.db import models

# Create your models here.

class Question(object):
	def __init__(self,question_text='',pub_date=''):
		self.question_text = question_text
		self.pub_date = pub_date
		
		