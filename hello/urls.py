from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.home, name="hello-home"),
    path('sample/', views.sampleApi.as_view()),
]
