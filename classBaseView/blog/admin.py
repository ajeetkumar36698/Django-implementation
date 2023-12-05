from django.contrib import admin
from .models import postModel
# Register your models here.
@admin.register(postModel)
class postAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','publish_date']