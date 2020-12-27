from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='Home'),
    path('update/<int:pk>', views.update, name='Update'),
    path('delete/<int:pk>', views.delete, name='Delete')

]