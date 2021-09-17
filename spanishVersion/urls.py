from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("program/<str:program_title>", views.program, name="program"),
]
