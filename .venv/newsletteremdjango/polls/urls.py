from django.urls import path

from . import views
app_name = 'polls' 
urlpatterns = [
    path('', views.dados_email_view, name="dados_email_view"),
    path('', views.iterate_entries, name="iterate_entries"),
    path('', views.get_initial_time, name="get_initial_time"),
]