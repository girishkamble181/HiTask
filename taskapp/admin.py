from django.contrib import admin
from .models import TaskModel
from django.contrib.auth.models import User

@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
	list_diplay=TaskModel.DisplayFields

#admin.site.register(TaskModel,TaskAdmin)

