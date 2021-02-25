from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	task= models.CharField(max_length=300)	
	timestamp= models.DateTimeField(auto_now_add=True, auto_now=False)
	DisplayFields=['user','timestamp']	
	
	def __str__(self):
		return str(self.user)
		

	
	class Meta:
		verbose_name_plural='tasks'