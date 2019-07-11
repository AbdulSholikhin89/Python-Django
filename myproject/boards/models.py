from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
	name = models.CharField(max_length = 30,unique = True)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=225)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board, models.CASCADE, related_name ='topics')
	starter = models.ForeignKey(User, models.CASCADE, related_name ='topics')
	

class Post(models.Model):
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic, models.CASCADE,related_name ='post')
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, models.CASCADE, related_name ='post')
	update_by = models.ForeignKey(User, models.CASCADE, null=True,related_name ='+')

# Create your models here.
