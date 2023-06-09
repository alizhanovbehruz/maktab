from django.urls import path
from .views import *

app_name = "class"

urlpatterns = [
    path('class_list/', group_list, name="class_list"),
    path('class_details/<int:pk>/', group_details, name="group_details"),
]
