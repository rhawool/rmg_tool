from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('associate_list/', views.associate_list, name='associate_list'),
    path('bulk_import_associates/', views.bulk_import_associates, name='bulk_import_associates'),
]
