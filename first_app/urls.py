from django.urls import path
from .views import first_model_list

app_name = 'first_app'

urlpatterns = [
    path('', first_model_list)
]