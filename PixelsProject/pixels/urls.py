from django.urls import path
from . import views

app_name = 'pixels'

urlpatterns = [
    path('', views.image_list, name='image_list'), #Root path
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('image/<int:pk>/', views.image_details, name='image_details'),
    path('image/<int:pk>/delete/', views.delete_image, name='delete_image'),
]