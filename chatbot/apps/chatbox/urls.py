from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ChatboxListView.as_view()),
    path('<id>/', views.ChatboxDetail.as_view()),
    path('<id>/component-add/', views.ChatboxComponentAdd.as_view()),
    path('<id>/component/<component_id>/', views.ChatboxComponentUpdate.as_view()),
]