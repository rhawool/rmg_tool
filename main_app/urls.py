from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),



    path('associate_list/', views.associate_list, name='associate_list'),
    path('associate_list/export_associate_data', views.export_associate_data, name='export_associate_data'),

    path('add_associate_home/', views.add_associate_home, name='add_associate_home'),
    path('add_associate_home/download_sample_format/', views.download_sample_format, name='download_sample_format'),
    path('add_associate_home/bulk_import_associates/', views.bulk_import_associates, name='bulk_import_associates'),

    path('about_page/', views.about_page, name='about_page'),
]
