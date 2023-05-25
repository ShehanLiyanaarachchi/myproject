# myapp/urls.py

from django.urls import path, include
from myapp import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]
