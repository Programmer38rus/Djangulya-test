from django.contrib import admin
from first_app.models import FirstModel, SecondModel


# Register your models here.


@admin.register(FirstModel)
class FirstAdmin(admin.ModelAdmin):
    pass

@admin.register(SecondModel)
class SecondAdmin(admin.ModelAdmin):
    pass