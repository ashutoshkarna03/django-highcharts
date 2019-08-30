from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_html, name='show_table')
]
