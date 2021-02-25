from django import forms
from .models import TaskModel
 
class TaskForm(forms.ModelForm):
	class Meta:
		model= TaskModel
		fields= ['task']
		widgets = {
          'task': forms.Textarea(attrs={'rows':7, 'cols':30,'required': True ,'style':'resize:none','style':'border-radius: 10px;','placeholder':'write ur task here','autofocus': 'autofocus'}),
        

	}