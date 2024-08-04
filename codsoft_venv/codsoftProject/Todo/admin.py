from django.contrib import admin

# Register your models here.

from Todo.models import Todos

class TodosAdmin(admin.ModelAdmin):
    list_display = ['id','content','date']

admin.site.register(Todos,TodosAdmin)