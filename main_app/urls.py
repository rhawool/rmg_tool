from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),



    path('emp_list/', views.emp_list, name='emp_list'),
    path('emp_list/export_associate_data', views.export_associate_data, name='export_associate_data'),

    path('add_emp_home/', views.add_emp_home, name='add_emp_home'),
    path('add_emp_home/download_sample_format/', views.download_sample_format, name='download_sample_format'),
    path('add_emp_home/bulk_import_associates/', views.bulk_import_associates, name='bulk_import_associates'),

    path('about_page/', views.about_page, name='about_page'),

    path('login_page/', views.login_page, name='login_page'),
    path('signup_page/', views.signup_page, name='signup_page'),


]
