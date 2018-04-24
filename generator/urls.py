from django.urls import path
from generator import views


urlpatterns = [path('generate_csrf/', views.CSRFGeneratorView.as_view())]