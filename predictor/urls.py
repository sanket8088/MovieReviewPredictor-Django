from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="hom_page"),
    path('prediction/', views.predictor, name="prediction"),
]
